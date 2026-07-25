#!/usr/bin/env python3
"""Generate the contribution-velocity stat cards used by the profile README.

Third-party README widgets rot: visitor-badge.glitch.me is 410, github-profile-trophy
is 402, and github-readme-stats sits at 503 for long stretches. This renders the same
information locally and commits it, so the profile can never render broken.

Usage:
    GITHUB_TOKEN=<pat> python3 scripts/generate_stats.py
    # or, locally, with the gh CLI already authenticated:
    python3 scripts/generate_stats.py

The token must belong to USER to include private contributions; see
.github/workflows/refresh-stats.yml for how CI supplies one.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

USER = "chrispmonkey"
FIRST_YEAR = 2019
OUT_DIR = Path(__file__).resolve().parent.parent / "assets"

# Refuse to overwrite good data with a token that cannot see private contributions.
MIN_CREDIBLE_TOTAL = 500

GRAPHQL = "https://api.github.com/graphql"


# --------------------------------------------------------------------------- data


def _post(token: str, query: str) -> dict:
    req = urllib.request.Request(
        GRAPHQL,
        data=json.dumps({"query": query}).encode(),
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": f"{USER}-profile-stats",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.load(resp)
    if "errors" in payload:
        raise RuntimeError(payload["errors"])
    return payload["data"]


def _gh_cli(query: str) -> dict:
    out = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={query}"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    payload = json.loads(out)
    if "errors" in payload:
        raise RuntimeError(payload["errors"])
    return payload["data"]


def query(q: str) -> dict:
    """Run a GraphQL query via token if present, else fall back to the gh CLI."""
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        return _post(token, q)
    return _gh_cli(q)


def collect() -> dict:
    now = datetime.now(timezone.utc)
    totals = query(
        "{user(login:\"%s\"){"
        "followers{totalCount} "
        "pullRequests{totalCount} "
        "repositories(ownerAffiliations:OWNER){totalCount} "
        "repositoriesContributedTo(contributionTypes:[COMMIT,PULL_REQUEST,REPOSITORY]){totalCount}"
        "}}" % USER
    )["user"]

    years: list[tuple[int, int]] = []
    for year in range(FIRST_YEAR, now.year + 1):
        data = query(
            "{user(login:\"%s\"){contributionsCollection"
            "(from:\"%d-01-01T00:00:00Z\",to:\"%d-12-31T23:59:59Z\")"
            "{contributionCalendar{totalContributions}}}}" % (USER, year, year)
        )
        years.append(
            (year, data["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"])
        )

    return {
        "years": years,
        "lifetime": sum(v for _, v in years),
        "current_year": years[-1][1],
        "prs": totals["pullRequests"]["totalCount"],
        "repos": totals["repositories"]["totalCount"],
        "contributed_to": totals["repositoriesContributedTo"]["totalCount"],
        "followers": totals["followers"]["totalCount"],
        "generated": now,
    }


# -------------------------------------------------------------------------- render

THEMES = {
    "dark": {
        "bg": "#0D1117",
        "border": "#21262D",
        "fg": "#F0F6FC",
        "muted": "#8B949E",
        "faint": "#6E7681",
        "track": "#161B22",
        "c1": "#22D3EE",
        "c2": "#818CF8",
        "c3": "#A78BFA",
    },
    "light": {
        "bg": "#FFFFFF",
        "border": "#D1D9E0",
        "fg": "#0D1117",
        "muted": "#59636E",
        "faint": "#6E7781",
        "track": "#F0F3F6",
        "c1": "#0891B2",
        "c2": "#6366F1",
        "c3": "#7C3AED",
    },
}

W, H = 900, 340
CHART_LEFT, CHART_RIGHT = 42, 566
BASELINE, CHART_TOP = 286, 172
MIN_BAR = 2.5


def render(d: dict, t: dict) -> str:
    years = d["years"]
    peak = max(v for _, v in years) or 1
    n = len(years)
    slot = (CHART_RIGHT - CHART_LEFT) / n
    bar_w = min(44.0, slot * 0.60)
    span = BASELINE - CHART_TOP

    # Square-root scale: on a linear axis the pre-2025 years collapse to invisible
    # slivers and the chart reads as broken. Every bar is labelled with its true
    # value so the compressed axis cannot mislead.
    def height(value: int) -> float:
        return max(MIN_BAR, ((value / peak) ** 0.5) * span)

    bars: list[str] = []
    for i, (year, value) in enumerate(years):
        h = height(value)
        x = CHART_LEFT + slot * i + (slot - bar_w) / 2
        y = BASELINE - h
        mid = x + bar_w / 2
        is_last = i == n - 1
        fill = "url(#barHot)" if is_last else "url(#barCool)"
        delay = i * 0.07

        bars.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{h:.1f}" rx="3" fill="{fill}">'
            f'<animate attributeName="height" from="0" to="{h:.1f}" dur="0.9s" '
            f'begin="{delay:.2f}s" fill="freeze"/>'
            f'<animate attributeName="y" from="{BASELINE}" to="{y:.1f}" dur="0.9s" '
            f'begin="{delay:.2f}s" fill="freeze"/></rect>'
        )
        bars.append(
            f'<text x="{mid:.1f}" y="{y - 8:.1f}" font-size="{11 if is_last else 9.5}" '
            f'fill="{t["c1"] if is_last else t["faint"]}" font-weight="{700 if is_last else 500}" '
            f'text-anchor="middle" font-family="ui-monospace,\'SF Mono\',Menlo,Consolas,monospace">'
            f"{value:,}</text>"
        )
        bars.append(
            f'<text x="{mid:.1f}" y="{BASELINE + 21}" font-size="11.5" '
            f'fill="{t["fg"] if is_last else t["faint"]}" font-weight="{700 if is_last else 500}" '
            f'text-anchor="middle" font-family="ui-monospace,\'SF Mono\',Menlo,Consolas,monospace">'
            f"&#39;{str(year)[2:]}</text>"
        )

    def stat(y: int, value: str, label: str) -> str:
        return (
            f'<text x="628" y="{y}" font-size="30" font-weight="700" fill="{t["fg"]}">{value}</text>'
            f'<text x="628" y="{y + 21}" font-size="10.5" letter-spacing="1.6" fill="{t["faint"]}" '
            f'font-family="ui-monospace,\'SF Mono\',Menlo,Consolas,monospace">{label}</text>'
        )

    cy = d["years"][-1][0]
    stamp = d["generated"].strftime("%d %b %Y").upper()

    prev = d["years"][-2][1] if len(d["years"]) > 1 else 0
    growth = (
        f'<tspan fill="{t["c1"]}" font-weight="600">&#215;{d["current_year"] / prev:.1f} vs {d["years"][-2][0]}</tspan>'
        if prev
        else ""
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Contribution velocity for {USER}: {d['current_year']:,} contributions in {cy}, {d['lifetime']:,} lifetime, {d['prs']:,} pull requests">
  <defs>
    <linearGradient id="barHot" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0" stop-color="{t['c1']}"/><stop offset="1" stop-color="{t['c3']}"/>
    </linearGradient>
    <linearGradient id="barCool" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0" stop-color="{t['c2']}" stop-opacity="0.30"/>
      <stop offset="1" stop-color="{t['c2']}" stop-opacity="0.60"/>
    </linearGradient>
    <linearGradient id="hr" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t['c1']}"/><stop offset="1" stop-color="{t['c3']}" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14" fill="{t['bg']}" stroke="{t['border']}"/>

  <text x="42" y="48" font-size="11.5" letter-spacing="2.4" fill="{t['muted']}" font-weight="600"
        font-family="ui-monospace,'SF Mono',Menlo,Consolas,monospace">CONTRIBUTION VELOCITY</text>
  <rect x="42" y="60" width="132" height="2" rx="1" fill="url(#hr)"/>

  <g font-family="'Helvetica Neue',Helvetica,Arial,sans-serif">
    <text x="42" y="124" font-size="56" font-weight="700" fill="{t['fg']}" letter-spacing="-1.5">{d['current_year']:,}</text>
    <text x="42" y="150" font-size="13.5" fill="{t['muted']}">contributions in {cy} &#183; {d['lifetime']:,} lifetime &#183; {growth}</text>

    <text x="42" y="{H - 18}" font-size="9" letter-spacing="0.8" fill="{t['faint']}"
          font-family="ui-monospace,'SF Mono',Menlo,Consolas,monospace">&#8730; SCALE &#183; EVERY BAR LABELLED WITH ITS TRUE VALUE</text>

    <line x1="598" y1="42" x2="598" y2="298" stroke="{t['border']}"/>
    {stat(104, f"{d['prs']:,}", "PULL REQUESTS")}
    {stat(180, f"{d['repos']:,}", "REPOSITORIES")}
    {stat(256, f"{d['contributed_to']:,}", "ORGS CONTRIBUTED TO")}

    <line x1="42" y1="{BASELINE}" x2="{CHART_RIGHT}" y2="{BASELINE}" stroke="{t['border']}"/>
    {"".join(bars)}
  </g>

  <text x="{W - 42}" y="{H - 18}" font-size="9.5" letter-spacing="1.2" fill="{t['faint']}" text-anchor="end"
        font-family="ui-monospace,'SF Mono',Menlo,Consolas,monospace">SELF-HOSTED &#183; UPDATED {stamp}</text>
</svg>
"""


def main() -> int:
    try:
        data = collect()
    except (urllib.error.URLError, subprocess.CalledProcessError, RuntimeError) as exc:
        print(f"error: could not fetch stats: {exc}", file=sys.stderr)
        return 1

    if data["lifetime"] < MIN_CREDIBLE_TOTAL:
        print(
            f"error: lifetime total {data['lifetime']} is below the {MIN_CREDIBLE_TOTAL} sanity "
            "floor — the token likely cannot see private contributions. Refusing to overwrite.",
            file=sys.stderr,
        )
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, theme in THEMES.items():
        path = OUT_DIR / f"stats-{name}.svg"
        path.write_text(render(data, theme), encoding="utf-8")
        print(f"wrote {path.relative_to(OUT_DIR.parent)}")

    print(
        f"  {data['current_year']:,} in {data['years'][-1][0]} | "
        f"{data['lifetime']:,} lifetime | {data['prs']:,} PRs | {data['repos']:,} repos"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
