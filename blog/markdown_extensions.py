"""Markdown extensions for rendering post bodies."""

from urllib.parse import urlparse

from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

# Links to these hosts are treated as internal and open in the same tab.
INTERNAL_HOSTS = {"mattambrogi.com", "www.mattambrogi.com"}


def is_external(href):
    """True if `href` points off-site.

    Relative paths, anchors and mailto: links are all internal, so only
    absolute http(s) URLs to another host qualify.
    """
    if not href:
        return False
    parsed = urlparse(href)
    if parsed.scheme not in ("http", "https"):
        return False
    return (parsed.hostname or "").lower() not in INTERNAL_HOSTS


class ExternalLinkTreeprocessor(Treeprocessor):
    def run(self, root):
        for anchor in root.iter("a"):
            if is_external(anchor.get("href", "")):
                anchor.set("target", "_blank")
                # noopener closes the reverse-tabnabbing hole that bare
                # target="_blank" opens up.
                anchor.set("rel", "noopener noreferrer")
        return root


class ExternalLinkExtension(Extension):
    """Open off-site links in a new tab, as the hand-written templates do."""

    def extendMarkdown(self, md):
        # Priority 15 runs after the inline processor (20) has built the
        # <a> elements, but before prettify (5).
        md.treeprocessors.register(
            ExternalLinkTreeprocessor(md), "external_links", 15
        )
