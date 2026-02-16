# SESSION PROMPT: v2.4 Validation — Part B: Cross-Document Consistency

## Instructions

Follow CLAUDE.md session protocol. Load spine (`substrate_spine.md`) first. For each check, load ONLY the specific sections referenced — do not read entire documents.

READ-ONLY. Report format: PASS/CONCERN/FAIL per item, under 1500 words total.

## Checks

### 1. Terminology Sweep
Search (grep) all .md files in repo root for:
- "siloxane" (should be "silazane" everywhere except petrification chemistry where Si-O-Si forms)
- "laminar" in context of dark-side boundary layer (should be "aerodynamically smooth turbulent")
- "parasite" referring to tower symbiotes (should be "mutualist"; "parasite" OK for actual parasites)
Report any incorrect usages with file and line number.

### 2. Atmospheric Parameters
Verify these values are consistent across spine, bible §2.1, geology hub §1:
- 8 bar, N₂ 55%, H₂ 15%, NH₃ 12.5%, CH₄ 10%, SiH₄ 0.3%
- T_term = 240K, T_sub = 265K, T_anti = 215K
- Wind 9.5 m/s at terminator, scale height 5.5 km
- Air density: 7.4 (sub), 8.2 (term), 9.2 (anti) kg/m³

### 3. Tower-Dependent Seas
Check: spine §SURFACE GEOMORPHOLOGY, bible §3.4, geology hub §8 (Surface Geomorphology subsection).
- Do all three describe seas as tower-dependent in the modern era?
- Do all three describe the sediment trap problem consistently?
- Is shore deposition described consistently?

### 4. Genesis Environment
Check: spine §SURFACE GEOMORPHOLOGY, bible §4.7, pool genesis hub §2.5, geology hub §8.
- Proto-tower shelter model consistent across all four?
- Million-pools model mentioned in all relevant docs?
- One-way door (ecosystem erased genesis conditions) consistent?

### 5. Network Wars
Check: spine §PLANETARY NETWORK, bible §10.5 and §10.7.
- Primordial wars (independent colonies) described consistently?
- Post-unification wars (fragmentation + drift) described consistently?
- Dark-side plume breakthrough timing (~500 Myr-1 Gyr) consistent between bible §2 and §10.7?

### 6. Colonization Mechanism
Check: spine §DEEP-ROCK, bible §10.6, and bible balloon fauna "same recruitment pathway" cross-ref.
- Root budding + symbiote migration described consistently?
- Schottky coupling mentioned in both spine and bible?
- Balloon fauna cross-reference (bible §9 balloon section) points to §10.6?

### 7. Speciation Axes
Check: spine §MOLECULAR LIBRARY, bible §6, fauna hub.
- Two axes for amorphs (cognitive protocol + library addressing)?
- Four axes for middle kingdom (+hook-lattice pore geometry + chelation badge)?
- Consistent across all three documents?

## Output

Table format: Check | Verdict | Discrepancies found (if any) | File:line references
