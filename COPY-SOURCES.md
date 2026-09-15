# Copy provenance — meierwerks.com build (2026-09-14)
Rule for this build: no new copy. Every sentence on the site comes from one of these sources.

| Page / element | Source |
|---|---|
| Positioning line "Where the craft of work meets advanced technology." | Brand Guide Working Edition 02, p.3; Brand Architecture sheet (Diane, Aug 2026) |
| Foundation statement (two paragraphs) | Brand Guide p.3 |
| "One ownership brand. Distinct divisions. Products with a clear home." | Brand Guide p.5 |
| "Every product belongs to one division. Only software carries the WRKS endorsement." | Brand Guide p.6 rule; Architecture sheet |
| Division one-line descriptors (six) | Brand Architecture sheet, sections 3–4 |
| Division colours | Brand Guide p.10 |
| Four governing principles (titles + text) | Brand Guide p.4 |
| WRKS strip: "Powered by WRKS." lockup + "WRKS is a collection of proprietary physics and simulation engines, built into all of our software." | Bennett, in chat 2026-09-15 ("WRKS is a collection of proprietary physics and simulation engines, made available in all softwares that we offer" — second half tightened at his request); supersedes the 2026-09-14 wording |
| Division headlines + paragraphs (FOCuS, SONIFoRM, THNSeT, FoAM, BRiDG, ISo-TL) | live meierwerks.com/divisions, verbatim |
| NEO • ONE / SDS / MetaGraph names, taglines, blurbs, "Powered by WRKS" | Brand Guide p.11 + Brand Architecture sheet, section 3 |
| Mission and proof (Principles page, teal band) | Diane, "For Bennett's deck. Proposal - Mission.docx" (Aug 2026) — written for the deck; easy to remove |
| Team bios (four) + portraits | live meierwerks.com/team, verbatim |
| Contact: Kent, CT USA · info@meierwerks.com · (714) 440-5526 | live meierwerks.com/contact + footer |
| Privacy Policy | live meierwerks.com/privacy, verbatim (it is the SDS app policy; no website Terms exist yet) |

Not used anywhere: Diane's MW Acoustics Website doc, Set List, Parts Express copy (all belong to the MW Acoustics site), Deck Copy (investment terms).
Fonts: DIN Condensed Bold + Futura Medium load from the local Mac (Brand Guide p.14). Web licences (Adobe Fonts: DIN Condensed / Futura PT) are needed before public launch; Barlow Condensed + Jost are the Google-Fonts fallbacks.

- 2026-09-14: Privacy Policy page REMOVED from meierwerks.com and moved to MW Acoustics (mwacoustic.com/privacy.html) — MW Acoustics owns SDS, so customers read the policy there. Bennett, chat, 2026-09-14.

- 2026-09-14: division colours reassigned per Bennett (chat): Acoustics green #0F492B · Heavy yellow #D38912 · Deep Learning light green #80843E · Magnetics red #9D3F2C · Composites tan #9D8974 · Additive blue #145868. Tiles = delivered marks with the accent fill swapped.

- 2026-09-14: WRKS strip = delivered WRKS colour logo (WRKS logos/wrks-color) + delivered "POWERED BY WRKS" KO lockup (poweredbywerks-blk+ko/poweredbywerks-ko.pdf → SVG) in place of typed text. Bennett, chat.

- 2026-09-14: Divisions page — MeierWerks ident reel (MW-ident-reel-v1_white.mp4, Bennett, chat) integrated as a scroll-scrubbed band between the page title and the division sections: the reel advances as you scroll down and rewinds as you scroll up; reduced-motion users get a looping autoplay instead.

- 2026-09-14 (later): Divisions page reel re-done per Bennett: the reel sits sticky beside the division sections; as each section reaches mid-screen the reel plays that division's tile segment (Additive 0.85–1.7 s teal · Acoustics 1.7–2.5 green · Composites 2.5–3.5 tan · Magnetics 3.45–4.3 red · Heavy 4.45–5.3 gold · Deep Learning 5.3–7.1 olive); at the page bottom the logo transformation (7.1–10.9 s) plays. Frames drawn to a canvas from the hidden video.

- 2026-09-14 (night): Divisions reel v3 per Bennett — scroll-driven: the reel graphic's vertical midpoint is the trigger; crossing a divider line scrubs the reel through that colour transition (midpoint of the transition exactly on the line), colour holds while inside a section, scrolling back rewinds, the logo transformation scrubs over the runway below the last division. Divisions page ordered in the reel's sequence (Additive, Acoustics, Composites, Magnetics, Heavy, Deep Learning) so the reel plays linearly. Stylesheet URL now carries a content hash (cache-busting) on both sites.

- 2026-09-14 (night, v4): Divisions reel — per Bennett, the big sticky reel is removed; each division's own mark animates in place: the reel's plain→colour wipe (0.80–1.20 s, teal) is scrubbed by scroll as the mark enters the viewport (85% → ~47% of the viewport height) and recoloured to that division's colour on a canvas; reverses on scroll-up; the parent-logo transformation is dropped. Divisions back in brand order.

- 2026-09-14 (night, v5): division marks now animate with a vector wipe built from the delivered tile SVGs (plain variant generated at build time; the coloured band sweeps in bottom-left → top-right with a feathered edge) instead of video frames — smooth at any frame rate. Trigger: progress 0 when the mark is fully on screen at the bottom edge, 1 a third of the viewport higher; forced complete at the page bottom; reverses on scroll-up. The ident reel video is no longer used on the site.

- 2026-09-14 (night, v6): division-mark wipe now eases toward its scroll target every animation frame (decoupled from stepped wheel/trackpad scroll events) with the SVG tiles pre-rasterised at device pixel ratio — smooth motion regardless of input device.

## 2026-09-14 — Technology + Partners pages, Principles → Vision (Bennett, chat)
- Nav "Principles" renamed "Vision"; page file `vision.html`; `principles.html` kept as a redirect. Body copy unchanged (Brand Guide p.4 + deck Mission).
- **Technology page** (`TECH` in build.py): every trademark and claim comes from the live-site division copy (`LIVE_DIV`, `_incoming-2026-09-14/live-site-text/home.txt`), re-cut by technology. NEW connective copy (needs Diane's voice pass): the page lead ("Each division exists because a technology our first product needed did not yet exist…", a paraphrase of the live copy's "had not been invented / So, we created it"), the short glosses on "Variable field-coil systems", "High-energy permanent magnets", "Thermoset / thermoplastic matrices", "Legacy-compatible", and the MW Heavy sentence (from the Brand Architecture descriptor). SDS and MetaGraph lines = PRODUCTS blurbs (Brand Architecture sheet).
- Technology photos, Pexels licence (free for commercial use, no attribution): acoustics = OUR OWN Neo One render (4adf0233… horn close-up; the Pexels driver photo 6530797 was removed 2026-09-14 — Bennett: it showed another manufacturer's speaker), magnetics = 38032287 (Nicola Narracci), composites = 596815 (creapattern), additive = 20877032 (Bertelli Fotografia), deeplearning = 17483871 (Google DeepMind), heavy = 6804258 (Bence Szemerey). Stored at `site/assets/img/tech/*.jpg`, 1600 px.
- **Partners page** (`PARTNERS`): NVIDIA Inception — member mail from inceptionprogram@nvidia.com / "Exclusive for Inception Members" (Aug 2026). FORGE — member mail from accounts@forgeimpact.org addressed to the "FORGE Startup Community" (May–Sep 2026). Connecticut Innovations — Bennett's statement in chat; NO mail/kit record found — CONFIRM wording. Apple App Store — apps.apple.com/us/app/id6788087317 (SDS / Speaker Design Suite, seller MW-Acoustics Inc.). EMM Labs — MW-Business Deck-2.pdf p.8, verbatim sentence. No third-party logos used.

- 2026-09-14: EMM Labs removed from the Partners page at Bennett's request.
- 2026-09-15: Partners page cards carry official marks instead of text — NVIDIA horizontal logo (nvidia.com brand assets, used as a program member), FORGE logo (forgeimpact.org site header), Connecticut Innovations circular mark (ctinnovations.com header SVG; wordmark set in site type because no wordmark file was available), Apple "Download on the App Store" badge (tools.applemediaservices.com, Apple marketing guidelines). Files in site/assets/logos/partners/. Bennett, chat.
- 2026-09-15: powered-by-wrks lockup SVGs cropped to ink (viewBox 7.03 4.05 103.2 12.89) so the lockup sits flush left with the copy beneath it. Bennett, chat.
