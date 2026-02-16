# SESSION PROMPT: v2.4 Comprehensive Validation (Agent-Dispatched)

## Instructions

You are a COORDINATOR. Do not load or read any Substrate documents yourself. Your job is to dispatch validation agents, collect their reports, and compile a unified assessment.

Follow CLAUDE.md session protocol only to the extent of understanding the project structure. Do NOT load the spine or bible into your own context.

## Step 1: Dispatch Three Agents in Parallel

Launch three Task agents simultaneously (subagent_type: "general-purpose"). Each agent gets one of the prompts below. Run all three in the background.

### Agent A: Physical Plausibility

```
You are validating the physical plausibility of a world-building project. Load `substrate_spine.md` from the repo root. For each check below, load ONLY the spine sections referenced — do not read entire documents.

Produce a PASS/CONCERN/FAIL verdict for each item with 1-2 sentence justification.

1. ATMOSPHERIC CONVEYOR (spine §SURFACE GEOMORPHOLOGY): Does the grain-size filter argument hold? Chimney lofts only particles light enough for updraft; katabatic wind re-entrains everything chimney admitted. Closed loop. Anti-stellar stagnation cap claimed "self-limiting, geologically insignificant." Would atmospheric scientists accept?

2. SiC ABRASION: SiC (Mohs 9.5) abrading silicate bedrock (Mohs 6-7) over Gyr. Mirror-smooth peneplain. Estimate erosion rate order-of-magnitude. Physically reasonable?

3. BOUNDARY LAYER: Re ~10¹² claimed. Check with: air density 8.2 kg/m³, wind 5-8 m/s, length scale ~planetary radius 8600 km, dynamic viscosity of N₂/H₂/NH₃ mix at 220K. Is Re ~10¹² correct? Viscous sublayer ~50 μm reasonable? Is "aerodynamically smooth turbulent" the correct term?

4. MARINE PHYSICS (spine §AMMONIA SEA ECOLOGY): H₂O at 50 ppm in seas — consistent with trace atmospheric H₂O + concentration? Medusa-fish Tesla valve manufactured by controlled petrification — physically feasible? Involuntary EM broadcast in NH₃ (dielectric constant ~22) coupling to electronic neural processing — does high dielectric enhance or attenuate EM from semiconductor junctions?

5. BALLOON AERODYNAMICS (spine balloon entries): Venturi body plan — estimate Re for 1m organism in 8.2 kg/m³ air at 5-10 m/s. Viable? Drifter cycle ~24-35 days for full planetary circuit — check against planet circumference ~54,000 km, superstream 50-100 m/s, surface transit 2-8 m/s. Does the timing work?

6. THERMAL KILL ZONE: Silazane biology at ~240K. Polysilazanes pyrolyze to SiCN at ~800-1000°C. Is there a biologically relevant thermal ceiling well below pyrolysis? SiC survives to ~2700K. Is "1200K+ kills biology, lattice survives" sound?

Output: table with columns [Item | Verdict | Key reasoning | Fix needed if any]. Keep under 1500 words.
```

### Agent B: Cross-Document Consistency

```
You are checking cross-document consistency for a world-building project. For each check, load ONLY the specific files and sections referenced.

Produce PASS/CONCERN/FAIL per item. Report discrepancies with file:line references.

1. TERMINOLOGY SWEEP: Grep all .md files in repo root for: (a) "siloxane" — should be "silazane" everywhere except petrification chemistry where Si-O-Si forms; (b) "laminar" in context of dark-side boundary layer — should be "aerodynamically smooth turbulent"; (c) "parasite" referring to tower symbiotes — should be "mutualist." Report incorrect usages.

2. ATMOSPHERIC PARAMETERS: Verify consistent across `substrate_spine.md`, `substrate_bible.md` §2.1, `substrate_planetary_geology_hub.md` §1: 8 bar, N₂ 55%, H₂ 15%, NH₃ 12.5%, CH₄ 10%, SiH₄ 0.3%; T_term=240K, T_sub=265K, T_anti=215K; wind 9.5 m/s at terminator; scale height 5.5 km; density 7.4/8.2/9.2 kg/m³.

3. TOWER-DEPENDENT SEAS: Check spine §SURFACE GEOMORPHOLOGY, bible §3.4, geology hub §8. All describe seas as tower-dependent? Sediment trap problem consistent? Shore deposition consistent?

4. GENESIS ENVIRONMENT: Check spine §SURFACE GEOMORPHOLOGY, bible §4.7, `substrate_pool_genesis_hub.md` §2.5, geology hub §8. Proto-tower shelter, million-pools, one-way door — all consistent?

5. NETWORK WARS: Check spine §PLANETARY NETWORK, bible §10.5 and §10.7. Primordial wars + post-unification fragmentation + drift — consistent? Dark-side plume timing (~500 Myr-1 Gyr) matches between bible §2 and §10.7?

6. COLONIZATION MECHANISM: Check spine §DEEP-ROCK, bible §10.6, bible balloon fauna "same recruitment pathway" cross-ref. Root budding + Schottky-coupled symbiote migration consistent? Cross-ref target exists?

7. SPECIATION AXES: Check spine §MOLECULAR LIBRARY, bible §6, `substrate_fauna_structural_hub.md`. Two axes (amorphs) + four axes (middle kingdom) consistent across all three?

Output: table with columns [Check | Verdict | Discrepancies | File:line refs]. Keep under 1500 words.
```

### Agent C: Gap Analysis

```
You are analyzing gaps in a world-building project. Load `substrate_spine.md` first. For each gap, load ONLY the sections needed to assess it.

Produce DOCUMENTED / PARTIAL / MISSING for each. Note what exists and what's missing.

1. GAS INTAKE SCALING: How does atmospheric SiH₄ intake scale with organism size? Check spine §AMORPH BIOLOGY (metabolic rate ~M^0.85) and `substrate_bible.md` §8. Is there a consistent intake model or just an assertion?

2. MERGE DATA TRANSFER: What happens to molecular libraries during merge? Check spine §AMORPH BIOLOGY + §MOLECULAR LIBRARY, bible §8. Mechanism beyond "combined meme pool"?

3. ENERGY BUDGET: 300W rest / 750W active / 5000W peak for 100 kg. SiH₄ at 0.3%. Can atmospheric metabolism sustain 300W? Is there a documented calculation?

4. SOCIAL PREREQUISITES: What structures exist before awakening? Check spine §CIVILIZATION, bible §11-12. Prerequisites for shell economy, governance?

5. WARFARE SUPPLY CHAIN: Check spine §CIVILIZATION — iodine laser, biological railgun, fluorine weapons. Full supply chain documented for each? Logistics gaps?

6. SHORE ECOLOGY: Spine says shore is "richest marine zone." Check bible §9. Supporting detail beyond nutrient delivery? Species, food web?

7. THORN-FLORA ENERGY: Dual-source (geothermal thermoelectric + solar heliostat). Check spine ecology entries. Mechanisms physically described or just named?

8. SKYWHALE METABOLISM: Three-phase cycle. Check spine skywhale entry. Energy budget closed? Sea-dip cost in 1.82g?

9. MIDDLE KINGDOM TAXONOMY: Beyond Healers/Miners/Guards, what tower organisms exist? Check bible §7, `substrate_fauna_structural_hub.md`. Developed beyond mentions?

10. WORKING MEMORY CEILING: Federation bypasses single-network collapse. Check spine §MONKS, bible §8. Collapse mechanism physically described?

Output: table with columns [Gap | Status | What exists | What's missing | Priority (narrative-blocking / nice-to-have)]. Keep under 1500 words.
```

## Step 2: Collect and Compile

When all three agents complete, read their outputs and compile a unified report:

1. **Executive summary** (3-5 sentences)
2. **Critical issues** (any FAIL verdicts from Agent A, or MISSING gaps from Agent C that are narrative-blocking)
3. **Concerns** (CONCERN verdicts, PARTIAL gaps)
4. **Passes** (brief list of what checked out)
5. **Recommended next sessions** (prioritized, max 5 items)

Keep the compiled report under 1000 words. Write it to `v2.4_validation_report.md` in the repo root.
