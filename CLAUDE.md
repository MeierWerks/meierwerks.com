# AGENTS.md — meierwerks.com (parent / ownership-brand website) (single source; CLAUDE.md + GEMINI.md are symlinks to this file)

## Invariants (hand-written, tiny — the only prose to trust; change rarely)
1. NO NEW COPY. Every sentence traces to COPY-SOURCES.md (Diane Meier's Brand Guide / Architecture sheet / live site). Adding or rewriting copy needs Bennett's approval.
2. Brand system is the Brand Guide Working Edition 02 (kit: ~/Desktop/MeierWerks/business/website/assets/07-brand-guides). Palette, type and marks are not to be reinterpreted.
3. Pages are GENERATED: edit build.py + site/assets/styles.css, then `python3 build.py`. Never hand-edit site/*.html.
4. Parent site carries no product or service detail — divisions, philosophy, team, contact, legal only.
5. Publishing (DNS, hosting, Squarespace) is human-gated.

## Working discipline
- Dispatch source = the human in chat. `git status` first every session.
- Read `docs/STATE.md` (machine-written, always current) before working.
- Commit only your own work via pathspec; never `git add -A` on a shared tree.
- End every session: dated 5-line handoff appended to `docs/session-notes.md`.
- Authority: this file > newest HUMAN decision in `DECISIONS.md` > specs > chat.
  Automation-written entries are NOT decisions.

## Doc hygiene (why this project won't rot)
- Three tiers: THIS file (invariants) · `docs/STATE.md` (generated) · everything
  else gets a `> ⚠️ SUPERSEDED` banner the day it stops being true.
- When direction changes: update the spec, banner the old doc, log DECISIONS —
  same turn.

## Codebase knowledge graph (optional but recommended)
Install once: `uv tool install graphifyy --python 3.12` → then `graphify init .`
in the repo. Rules: architecture/relationship questions → `graphify query`;
known symbols → grep; after edits → `graphify update .` (wire into post-commit
next to generate-state.sh).
