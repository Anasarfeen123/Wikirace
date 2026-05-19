"""
wiki_api.py — Wikipedia API wrapper with in-memory caching.
"""

import re
import time
import requests
from bs4 import BeautifulSoup
from typing import Optional

# ─── Constants ────────────────────────────────────────────────────────────────
API_URL   = "https://en.wikipedia.org/w/api.php"
REST_URL  = "https://en.wikipedia.org/api/rest_v1"
HEADERS   = {"User-Agent": "WikiRaceGame/1.0 (educational project)"}
TIMEOUT   = 10

# Namespaces that are NOT valid game targets (main namespace = 0 is valid)
_NS_PATTERN = re.compile(
    r"^/wiki/(Talk|User|Wikipedia|WP|File|Image|MediaWiki|Template|"
    r"Help|Category|Portal|Book|Draft|Special|MOS|T):",
    re.IGNORECASE,
)

# Simple LRU-style cache: {title_lower: (timestamp, data)}
_cache: dict = {}
_CACHE_TTL = 300  # seconds


def _cache_get(key: str):
    entry = _cache.get(key)
    if entry and (time.time() - entry[0]) < _CACHE_TTL:
        return entry[1]
    return None


def _cache_set(key: str, value):
    _cache[key] = (time.time(), value)
    # Trim cache if too large
    if len(_cache) > 200:
        oldest = sorted(_cache, key=lambda k: _cache[k][0])
        for k in oldest[:50]:
            del _cache[k]


# ─── Public API ───────────────────────────────────────────────────────────────

def normalize_title(title: str) -> str:
    """Canonical form: spaces, stripped, first-letter capitalised."""
    title = title.replace("_", " ").strip()
    return title[0].upper() + title[1:] if title else title


def titles_match(a: str, b: str) -> bool:
    return normalize_title(a).lower() == normalize_title(b).lower()


def get_random_article() -> dict:
    """Return {'title': str, 'pageid': int} for a random main-namespace article."""
    params = {
        "action": "query", "format": "json",
        "list": "random", "rnnamespace": 0, "rnlimit": 1,
    }
    r = requests.get(API_URL, params=params, headers=HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    page = r.json()["query"]["random"][0]
    return {"title": page["title"], "pageid": page["id"]}


def get_random_pair() -> tuple[dict, dict]:
    """Return two distinct random articles (start, target)."""
    a = get_random_article()
    b = get_random_article()
    while titles_match(a["title"], b["title"]):
        b = get_random_article()
    return a, b


def get_article(title: str) -> Optional[dict]:
    """
    Fetch and return article data:
      {title, display_title, html (cleaned), links (list[str])}
    Returns None if article not found.
    """
    key = normalize_title(title).lower()
    cached = _cache_get(key)
    if cached:
        return cached

    params = {
        "action": "parse", "format": "json",
        "page": normalize_title(title),
        "prop": "text|displaytitle|links",
        "disableeditsection": True,
        "disabletoc": True,
        "mobileformat": False,
    }
    r = requests.get(API_URL, params=params, headers=HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    data = r.json()

    if "error" in data:
        return None

    parse = data["parse"]
    raw_html = parse["text"]["*"]
    links = [
        lk["*"] for lk in parse.get("links", [])
        if lk.get("ns", -1) == 0
    ]

    result = {
        "title": parse["title"],
        "display_title": parse.get("displaytitle", parse["title"]),
        "html": _clean_html(raw_html),
        "links": links,
    }
    _cache_set(key, result)
    return result


def get_article_links(title: str) -> list[str]:
    """Return list of main-namespace link titles from an article (for bots)."""
    article = get_article(title)
    if not article:
        return []
    return article["links"]


def article_exists(title: str) -> bool:
    """Check if a main-namespace article exists."""
    params = {
        "action": "query", "format": "json",
        "titles": normalize_title(title),
        "redirects": True,
    }
    r = requests.get(API_URL, params=params, headers=HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    pages = r.json()["query"]["pages"]
    return "-1" not in pages


# ─── HTML Cleaning ────────────────────────────────────────────────────────────

def _is_game_link(href: str) -> bool:
    return href.startswith("/wiki/") and not _NS_PATTERN.match(href)


def _clean_html(raw: str) -> str:
    """
    Transform raw Wikipedia API HTML so it is suitable for in-game display:
    - Strip edit-section controls, TOC, nav boxes, ref lists, coord badges
    - Convert internal /wiki/ hrefs to /navigate/<title>
    - Mark external / special links so they don't navigate the game
    """
    soup = BeautifulSoup(raw, "lxml")

    # ── Remove unwanted elements ──────────────────────────────────────────────
    selectors = [
        ".mw-editsection",        # [edit] buttons
        "#toc",                   # table of contents
        ".toc",
        ".navbox",                # navigation boxes
        ".navbox-styles",
        ".reflist",               # references section
        ".references",
        ".mw-references-wrap",
        ".sistersitebox",
        ".noprint",               # print-only / hatnote extras
        ".metadata",
        ".geo-nondefault",
        ".geo-multi-punct",
        ".coordinates",
        "#coordinates",
        ".mw-empty-elt",
        ".hatnote img",           # icons inside hatnotes
        ".mbox-image",
        "style",                  # inline <style> tags
        "link",                   # inline <link> tags
    ]
    for sel in selectors:
        for tag in soup.select(sel):
            tag.decompose()

    # ── Rewrite links ─────────────────────────────────────────────────────────
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if _is_game_link(href):
            article_name = href[len("/wiki/"):]
            a["href"] = f"/navigate/{article_name}"
            a["class"] = (a.get("class") or []) + ["wikirace-link"]
            a["data-article"] = article_name.replace("_", " ")
        elif href.startswith("#"):
            pass  # in-page anchor — fine
        else:
            # External / namespace link — disable game navigation
            a["href"] = "#"
            a["class"] = (a.get("class") or []) + ["wikirace-external"]
            a["tabindex"] = "-1"

    # ── Fix image src paths ───────────────────────────────────────────────────
    for img in soup.find_all("img", src=True):
        src = img["src"]
        if src.startswith("//"):
            img["src"] = "https:" + src
        if img.get("srcset"):
            img["srcset"] = re.sub(
                r"//", "https://", img["srcset"]
            )

    return str(soup)
