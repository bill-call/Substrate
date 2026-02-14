# SUBSTRATE — Document Architecture and Session Protocol

## Purpose

This file governs how Claude works with the Substrate world-building project. Load this file at the start of every Substrate session. It tells Claude which documents exist, when to load them, and how to manage the growing knowledge base.

## The Problem

Substrate's world-building is deeply interconnected. The towers alone touch geology, deep-rock biology, symbiote chemistry, atmospheric physics, ecology, network consciousness, civilization, and the space program. No flat document structure handles this — either you load everything (too large) or you load topic slices (missing critical cross-references).

## Architecture: Spine + Hub + Modules

### Tier 0: CLAUDE.md (this file)
- **Always load first.** Tells Claude what's available and what to request.
- ~500 words. Pure instruction. No world-building content.
- Where instructions require you to load any file, always load the most recent version of that file *ignoring* the parenthesized duplication counters that the file system appends to the base file name.  "foo.md", "foo (1).md", and "foo (10).md" are all the same file; take the most recent version. The same concept applies to file names that include version suffixes (e.g., "_v2.1").  A version number suffix does not make a file unique for the purposes of determining the latest version (e.g., "foo.md", "foo_v3.md", and "foo_v3 (2).md" are all the same file). In any case where the file names are semantically identical, by these rules, take the latest version by the last-updated date.
Use pandoc to convert .docx to .md, when necessary. Hard requirement: pandoc does not work correctly unless you specify the FULL file path for each pandoc command line option that requires one.

### Tier 1: Spine
- **File:** `substrate_spine.md`
- **Always load.** Every session. No exceptions.
- **Contains:** Every hard constraint, resolved decision, and key number. No explanatory prose. Tables and one-line resolutions only.
- **Size target:** <2,000 words. Currently ~1,500.
- **If a fact is in the spine, Claude can rely on it without checking other documents.**

### Tier 2: Hub Documents
- Larger convergence documents for topics where many systems intersect.
- Load the relevant hub when the session focuses on that nexus.
- **Currently built:**
  - `substrate_tower_hub.docx` / `substrate_tower_hub_latest.md` — towers as nexus of geology, ecology, network, civilization, wind.
  - `substrate_silicon_chemistry_hub.md` — all silicon chemistry: silazane, carbosilane, fluorine, metallosilazane catalysis, lattice composition.
  - `substrate_fauna_structural_hub.md` — structural materials, body plans, mechanical engineering for all mobile life. Tower symbiote guilds.
  - `substrate_planetary_geology_hub.md` — mantle model, volcanic regime, SiH₄ budget, H₂O ratchet, petrification, gas pockets, crisis.
  - `substrate_pool_genesis_hub.md` — ammonia-pool abiogenesis, dual-origin lineage fork, undersea tower genesis.
  - `substrate_memory_architecture_hub.md` — amorph cognition, working memory, meme architecture, federation.
  - `substrate_amorph_economics_hub.md` — charge economy, power constraints, evolutionary economics, tech tree, day-side colonization.
  - `substrate_heavy_industry_hub.md` — industrial processes, machinery, biological-to-mechanical transition, factory architecture.
  - `substrate_warfare_hub.md` — weapons, escalation ladder, fluorine taboo, strategic constraints, grid warfare.
  - `substrate_amorph_emergence_hub.md` — pore-to-megafauna pathway, aeroplankton dispersal, tower biofilm, IFF/first meme, miner competition, cognition emergence.
- **Planned hubs:**
  - Network Hub — adversarial ratchet, consciousness question, awakening crises, merger, monks. (Touches towers, deep-rock, civilization, narrative.)
  - Crisis Hub — atmospheric decline, tower deaths, merger, probe, space program. (Touches everything.)

### Tier 3: Leaf/Branch Modules
- Self-contained topic documents. Load as needed.
- Leaf modules need only the spine for context. Branch modules may note dependencies on other modules.
- **Size target:** 500–1,500 words each.
- **Planned modules (not yet built):**
  - Astro/Geo — star, planet, atmosphere, tectonics, volcanism
  - Deep-Rock Biosphere — origins, colony isolation, fracture networks, geological pruning
  - Biochemistry — Si-Si backbone, silicone oil matrix, carbosilane pathway, energy sources
  - Molecular Library — fragment architecture, three currencies, two speciation axes, reproduction
  - Amorph Biology — body plan, disease, death, population variation, cognition, merge
  - Ecology: Fluorine Biome — thorn-flora, pollination, aposematism, biomagnification, volcanic provinces
  - Ecology: Balloon Fauna — fall-survival origin, permanent aerial life, atmospheric conveyor, network blind spot
  - Ecology: Middle Kingdom — three-tier architecture, tower mutualists, sessile/mobile split, insect-scale arms races
  - Civilization — governance, religion, economy, art, writing, metallurgy, shell economy
  - Transport & Space — surfing, balloons, boats, flight, rocketry, mass driver, the probe
  - Narrative — scene concepts, POV candidates, timeline, emotional beats, open questions

### Tier 4: Full Bible
- **File:** `substrate_bible_v2.1.docx`
- **Do NOT load routinely.** Too large for most sessions.
- **Use for:** Building new modules, cross-checking when something feels contradictory, comprehensive review sessions.
- Contains all prose, all context, all open questions. The authoritative reference when everything else is insufficient.

### Companion Documents (Legacy)
These predate the spine/hub/module system. Their content has been absorbed into the bible and will be absorbed into modules as they're built. They can still be loaded for deep-dive reference:
- `substrate_guide_v3.docx` — original 18-section bible
- `substrate_expansion_v1.1.docx` — 8 expansion sections
- `substrate_molecular_library.docx` — molecular library deep dive
- `substrate_carbosilane.docx` — carbosilane chemistry deep dive
- `substrate_marching_towers.docx` — wind, erosion, tower migration, geography, transportation

## Session Loading Protocol

**Step 1:** Always load CLAUDE.md + spine.

**Step 2:** Identify session focus. Load accordingly:

| Session Focus | Load (in addition to spine) |
|---|---|
| Towers (any aspect) | Tower Hub |
| Amorph emergence, pore-to-megafauna | Amorph Emergence Hub + Pool Genesis Hub |
| Network, consciousness, awakening | Network Hub (when built); until then, bible |
| Atmospheric crisis, probe, space | Crisis Hub (when built); until then, bible |
| Deep-rock biosphere | Deep-Rock module (when built); until then, spine is sufficient for most questions |
| Fluorine ecology | Fluorine module (when built); Tower Hub if discussing tower-adjacent provinces |
| Balloon fauna | Balloon module (when built); spine is sufficient for most questions |
| Biochemistry deep dive | Biochemistry module (when built); or carbosilane companion doc |
| Molecular library mechanics | Library module (when built); or molecular_library companion doc |
| Civilization, culture, economy | Civilization module (when built); until then, bible |
| Narrative planning | Narrative module (when built); plus whatever hub/module the scene touches |
| General / exploratory | Spine alone. Load more if the conversation narrows. |
| Comprehensive review | Bible v2.1 (full load) |

**Step 3:** If the session generates new resolved decisions, constraints, or major reframes:
- Update the spine (add new resolved lines, update tables)
- Update affected hub(s) and modules
- Update the bible (authoritative full record)
- Note the change in the session summary

## Rules for Building New Documents

### Spine Rules
- One-line resolutions. No "because" clauses.
- Tables for structured data (planet parameters, wind speeds, etc).
- ⚠ notes for critical warnings.
- □ OPEN for the 2–3 most important unresolved questions only. Full open-question list lives in the bible.
- If you can't express it in one line, it doesn't belong in the spine. Put it in a module.

### Hub Rules
- A hub exists because a topic is a NEXUS — many systems converge on it.
- The hub pulls tower-relevant (or network-relevant, or crisis-relevant) constraints from every adjacent system, but only the parts that intersect at the nexus.
- Not a copy of the relevant module sections. A re-synthesis focused on the intersection.
- Size target: 1,500–3,000 words. Bigger than a module, smaller than the bible.
- Include hub-specific open questions at the end.

### Module Rules
- Self-contained. A reader with only the spine + this module should be able to discuss the topic without confusion.
- State dependencies at the top: "Load with: spine (required), [other module] (optional, for X)."
- Size target: 500–1,500 words.
- Include module-specific open questions.
- Distinguish resolved (✓) from open (□) clearly.

### Bible Rules
- The bible is the authoritative record. If the spine, a hub, and the bible disagree, the bible is right.
- The bible contains all prose, all context, all open questions.
- Version the bible on every major update (v2.1, v2.2, etc).
- Flag new material with version markers ([NEW IN V2.1]) for quick scanning.

## Versioning

All documents carry version numbers matching the bible version they're current with.
- Current version: **v2.4** (February 2026)
- When the bible is updated, all spine/hub/module documents should be checked for consistency and updated if needed. Their version numbers should match.

## What Claude Should Do When Something Contradicts

1. Check the spine. If the spine has a clear answer, use it.
2. If the spine is ambiguous, check the relevant hub or module.
3. If hub/module is ambiguous, check the bible.
4. If the bible is ambiguous, flag it as a potential inconsistency and ask the user.
5. **Never silently resolve a contradiction. Always surface it.**

## What Claude Should Do at End of Session

Offer to update affected documents. At minimum:
- List new resolved decisions (for spine update)
- List new open questions (for bible update)
- Identify which hubs/modules need revision
- Build or revise documents if the user wants to commit
