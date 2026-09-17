
## 2026-09-15 (Claude)
- Positioning line is now "Where the skill of craft meets the precision of technology." (hero, Vision, meta description) — Bennett rejected the Brand Guide line, then "hand", then "art"; chose "skill".
- Also today: partner marks, Technology rewrite, product click-throughs, USMC additive photo, Evening Mist hero loop, Powered-by lockup artwork, clean URLs, WRKS caption "software and services".
- gh-pages = main 7ee0e21; artifact 2cfc39f8 v36.
- Next: nothing open on this site; Bennett to read the Technology wording once.

## 2026-09-17 (Claude)
- Discoverability layer mirrored from mwacoustic.com: per-page meta descriptions, Open Graph + Twitter cards, Organization/ItemList/Person/ContactPage JSON-LD, robots.txt + sitemap.xml generated from the pages dict, gstatic preconnect, and an empty MEASURE dict (GA4 / Meta Pixel / GSC / Bing) that emits nothing until it is filled.
- Invariant 1 held: no new copy. Approved sentences were hoisted into named constants and reused verbatim; page bodies are byte-identical to the previous build apart from five jpg→webp filenames. Mapping table appended to COPY-SOURCES.md.
- Images: five rasters over 150 KB re-encoded to WebP (cwebp -q 82); JPEG originals moved to assets-src/. Published folder 6.7 MB → 6.4 MB (images 1.5 MB → 1.2 MB; the 4.7 MB hero video is untouched).
- Verified: build runs clean, zero broken relative refs on all 11 built pages, title/description/canonical/og:image/twitter:card present on all seven real pages, og:image files exist, every ld+json parses, local http.server returns 200 for / and every new asset. Redirect stubs (/principles, /privacy, /terms, /support) are deliberately absent from the sitemap. Not committed — tree left dirty for review.
- Next: Bennett's calls — (a) og:image is a .webp (LinkedIn/X render WebP unreliably; a JPEG OG card would need a decision, and the same applies to mwacoustic.com), (b) team-diane-meier is still 305 KB at 1424 px and would benefit from a resize, (c) MEASURE needs real GA4 / Search Console / Bing IDs before any of it reports.
