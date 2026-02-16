# SUBSTRATE — MEMORY ARCHITECTURE HUB

**v1.0 — February 2026**

The chemical machinery of epistemology. How an amorph knows what it knows.

---

## 1. OVERVIEW

Amorph memory has three chemically distinct components:

| Component | Function | Chemical basis |
|-----------|----------|----------------|
| **Index (Header)** | Locates memories | Resonance tags derived from content |
| **Key** | Gates access | Allosteric activator for reader enzymes |
| **Content** | Stores experience | Polysilane-encoded data |

Each can fail independently, producing different experiential and narrative consequences.

---

## 2. THE MEMORY UNIT

```
MEMORY UNIT STRUCTURE:

┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  [HEADER]═══[KEY-SITE]═══[CONTENT]═══[CHECKSUM]            │
│      ↑          ↑            ↑            ↑                │
│  resonance    lock      actual data    error               │
│    tag      (shape-     (experience,   correction          │
│  (derived    gated)      emotion,                          │
│   from                   sensory)                          │
│  content)                                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2.1 Header (Index Entry)

A short polysilane sequence at the beginning of each memory with a specific conductance profile. Functions as an "address" or "resonance tag."

**Key properties:**
- Derived from content (a hash, essentially)
- Responds to query signals via electronic resonance
- Distributed throughout the body (no central index)
- Self-healing if damaged (can be regenerated from content)

### 2.2 Key-Binding Site

A conformational lock between header and content. The reader enzyme must have the correct geometry to pass through.

**Key properties:**
- Shape-gated, not encrypted
- Key is an allosteric activator that changes reader geometry
- Without key, content reads as noise/garbage
- Content remains chemically intact regardless of key status

### 2.3 Content

The actual memory — encoded experience, emotion, sensory data, skills.

**Key properties:**
- Polysilane chain with quaternary side-chain encoding
- Chemically stable if undamaged
- Readable only if key is present and reader geometry is correct

### 2.4 Checksum

Error-correction information appended to content.

**Key properties:**
- Allows detection of corruption
- Enables repair of minor damage
- Does not protect against wholesale destruction

---

## 3. THE INDEX MECHANISM

### 3.1 Why There Is No Central Index

A central index would be:
- A single point of failure
- A bottleneck for retrieval
- Requiring constant maintenance as memories accumulate

Instead, the index is **distributed**: every memory carries its own header, and queries search all headers in parallel.

### 3.2 How Resonance-Based Retrieval Works

The polysilane backbone is a semiconductor with variable conductance based on side-chain sequence. Different sequences have different electronic "fingerprints."

```
CURRENT EXPERIENCE
        ↓
[creates electrochemical signature]
        ↓
QUERY SIGNAL propagates through body
        ↓
Memories with MATCHING HEADERS resonate
(their conductance profile responds to the query frequency)
        ↓
RESONANCE DETECTED → memory located → recall initiated
```

**Why this works:**
- A propagating electronic signal interacts more strongly with sequences that have similar electronic properties
- This is associative memory through physical resonance
- The entire library is "searched" simultaneously
- Strong matches trigger automatically; weak matches require deliberate amplification

### 3.3 Properties of Resonance Indexing

| Feature | Consequence |
|---------|-------------|
| Distributed | No single point of failure |
| Associative | Similar experiences find similar memories |
| Parallel | Entire library searched simultaneously |
| Passive | Strong matches trigger automatically |
| Active possible | Amorph can "concentrate" to find weaker matches |

---

## 4. THE KEY MECHANISM

### 4.1 Keys as Allosteric Activators

Keys are molecular chains (approximately one million copies of each key per amorph). They function as **allosteric activators** for reader enzymes.

```
READER ENZYME (without key):
    ┌───────────┐
    │  ┌─────┐  │
    │  │WRONG│  │ ← active site geometry incorrect
    │  │SHAPE│  │
    │  └─────┘  │
    └───────────┘
         ↓
    reads content as noise


READER ENZYME (with key bound):
    ┌───────────┐
    │  ┌─────┐  │
    │  │RIGHT│  │ ← key binding changes geometry
    │  │SHAPE│  │
    │  └─────┘  │
    └─[KEY]─────┘
         ↓
    reads content correctly
```

### 4.2 Key Properties

| Property | Value | Implication |
|----------|-------|-------------|
| Copies per amorph | ~10⁶ | Redundancy; hard to lose all copies |
| Binding | Reversible | Same key works many times |
| Specificity | High | Each key activates specific readers |
| Inheritance | Via library transfer | Keys pass with memories that need them |

### 4.3 Dual Function

Keys serve two purposes:
1. **Authentication**: Who signed this memory? (The key identifies the source)
2. **Access control**: Can you read it? (You need the key to interpret content)

---

## 5. THE QUERY MECHANISM

### 5.1 Passive Recall (Automatic)

Strong experiential matches trigger recall without deliberate effort.

```
EXPERIENCE → [strong electrochemical signature]
                        ↓
              propagates through body
                        ↓
              STRONG RESONANCE with stored header
                        ↓
              automatic recall
              (like smell triggering vivid memory)
```

### 5.2 Active Recall (Deliberate Search)

The amorph concentrates on a concept, amplifying the query signal.

```
AMORPH concentrates on a concept/image/feeling
                        ↓
              [amplifies specific query pattern]
                        ↓
              propagates with boosted signal
                        ↓
              WEAKER RESONANCES become detectable
                        ↓
              more distant/tangential memories surface
```

### 5.3 Failed Search

When a memory exists but cannot be found:

```
AMORPH knows they should remember X
                        ↓
              generates query for X
                        ↓
              signal propagates
                        ↓
              HEADER IS DAMAGED — no resonance
                        ↓
              nothing returns
                        ↓
              "tip of tongue" (partial header)
              or complete blank (header destroyed)
```

### 5.4 Power-Dependent Query Behaviour

The junction network that processes queries is itself power-dependent. Each junction cluster operates digitally — full fidelity above threshold, non-functional below — but the number of clusters powered simultaneously depends on available charge.

As charge depletes, autonomous power management **sheds parallel processes in priority order**:

| Priority | Function shed | Effect on memory system |
|----------|-------------|------------------------|
| 1 (first) | Broad library resonance search | Queries no longer propagate body-wide. Recall narrows to local/recent memories. Distant associations lost. |
| 2 | Multi-modal sensory integration | New experiences encode through primary sense (EM) only. Poorer header generation (less context in hash). |
| 3 | Abstract reasoning / formal WM | Cannot hold multiple retrieved memories simultaneously for comparison. Single-thread only. |
| 4 | Secondary motor functions | No direct memory effect, but inability to reach charging source prolongs depleted state. |
| 5 (last) | Threat detection + basic locomotion | Minimal query capability. Passive recall only (strongest resonances). Below this → torpor. |

Key insight: the amorph doesn't lose memories or forget — it loses the ability to **search widely**. Content, keys, and headers remain intact. The memory system is undamaged; the processing substrate that queries it is power-rationed. A depleted amorph thinks *narrowly*, not *poorly*.

This graceful degradation is a product of selection pressure — an organism that crashed from full cognition to torpor with no intermediate states would be a dead organism.

> **Full treatment:** Amorph Daily Life Hub §2.2 — shedding priority table, experiential descriptions at each depletion level, cross-period implications.

---

## 6. THE THREE FAILURE MODES

### 6.1 Attack the Content

```
[HEADER]——[KEY-SITE]——[XXXXXXXX]
                           ↑
                      destroyed
```

| Aspect | Status |
|--------|--------|
| Header | Intact — memory can be found |
| Key | Works — reader activates normally |
| Content | Gone — reader returns nothing/garbage |

**Experience:** Amorph finds the location, unlocks the door, room is empty.

**Subjective quality:** Grief. Visible wound. Detectable absence. The amorph *knows* something is missing.

**Recovery:** Impossible without external backup.

### 6.2 Attack the Key

```
[HEADER]——[KEY-SITE]——[CONTENT]
              ↑
        can't unlock (no key)
```

| Aspect | Status |
|--------|--------|
| Header | Intact — memory can be found |
| Key | Missing — reader geometry wrong |
| Content | Intact — but uninterpretable |

**Experience:** Amorph finds the location, door is locked, can sense something behind it.

**Subjective quality:** Frustration. The "locked room." Aware of own incompleteness.

**Recovery:** Possible if key can be obtained from another source.

### 6.3 Attack the Index (Header)

```
[XXXXXXX]——[KEY-SITE]——[CONTENT]
     ↑
  destroyed
```

| Aspect | Status |
|--------|--------|
| Header | Damaged — memory doesn't respond to queries |
| Key | Works — would unlock if found |
| Content | Intact — fully readable if located |

**Experience:** Amorph doesn't know anything is missing. No gap to perceive.

**Subjective quality:** Nothing. Behavior shifts without awareness. When header heals and memory resurfaces, potentially devastating.

**Recovery:** Automatic via self-healing (days to weeks), or Monk detection/repair.

---

## 7. INDEX SELF-HEALING

### 7.1 Mechanism

The header is derived from the content — it's a hash of what the memory contains. If the header is damaged but content remains intact, the header can be regenerated.

```
CONTENT → [hashing process] → HEADER
```

### 7.2 Healing Process

1. Background maintenance process periodically scans memories
2. Detects memories with damaged/missing headers
3. Re-derives header from intact content
4. Rebuilds header sequence

### 7.3 Timescale

| Factor | Effect on healing time |
|--------|----------------------|
| Metabolic state | Active metabolism = faster healing |
| Number of damaged memories | More damage = slower per-memory |
| Active searching | May accelerate repair in searched region |
| **Typical range** | **Days to weeks** |

### 7.4 The Window

During healing, the memory is:
- Intact (content undamaged)
- Accessible (key works)
- **Unfindable** (no header to resonate)

This is narratively critical: the victim doesn't know they're a victim.

When the header regenerates, the memory suddenly "reappears" — triggered by some experience that resonates with the rebuilt header. The amorph experiences a flashback to something they didn't know they'd forgotten.

---

## 8. THE KEY-BLIGHT SCENARIO

### 8.1 Mechanism

A phage (silicon-biochemistry virus equivalent) that:
1. Recognizes and binds to a specific molecular sequence
2. Enzymatically degrades that sequence
3. By coincidence, the sequence overlaps with a particular key's structure

### 8.2 Why It's Rare But Recognized

- Most phages target common sequences (metabolic machinery)
- Keys are relatively short, unique sequences
- The overlap is coincidental — the phage isn't "targeting" keys
- But over deep time, with millions of keys and thousands of phage species, some overlaps occur
- When it happens, the amorph loses all copies of one specific key
- All memories signed with that key become inaccessible

### 8.3 The Condition

**Name:** Key-blight, lock-rot, or similar (regional variations)

**Frequency:** Rare enough to be remarkable, common enough across deep time to be recognized

**Variants:** Probably several named for which key-family they affect

### 8.4 Treatment

1. Identify which key was lost
2. Find another amorph who carries that key
3. Obtain a copy (brief merge? deliberate fragment transfer?)
4. Re-introduce the key
5. Memories become accessible again

### 8.5 Implications

| Implication | Consequence |
|-------------|-------------|
| Key diversity matters | Amorphs maintain relationships partly to preserve key-diversity |
| Rare keys are precious | Losing a rare key might mean permanent loss of ancestral memories |
| Monks as key-banks | Key-preservation may be a Monk function |

---

## 9. DETECTION AND DIAGNOSIS

### 9.1 What Can Be Detected

| Damage type | Self-detectable? | Monk-detectable? |
|-------------|------------------|------------------|
| Content destruction | Yes — feels the gap | Yes |
| Key loss | Yes — the locked room | Yes |
| Header damage | **No** — silent | **Yes** |

### 9.2 Monk Diagnostic Capability

The Monks, with their ability to read memes directly, can:
- Scan for orphaned content (memories without functional headers)
- Identify key-binding site damage
- Detect content corruption before the amorph experiences symptoms
- Verify header-content consistency

This is another Monk service: **memory health diagnostics**.

---

## 10. READING WITHOUT KEYS

### 10.1 The Question

Can you read someone else's memory without their key?

### 10.2 Options

| Possibility | Mechanism | Difficulty |
|-------------|-----------|------------|
| Never | Key-binding is absolute | N/A |
| Brute force | Try all possible reader conformations | Computationally prohibitive |
| Monk techniques | Specialized reader enzymes, iterative refinement | Difficult but possible |
| Key theft | Obtain their key through merge/extraction | Requires access to target |

### 10.3 Proposed Answer

**Monks can, with effort and time.** Their deep study of meme-reading has given them techniques for interpreting content without the original key. It's slow, imperfect, and ethically fraught — but possible.

This has implications for forensics (reading the dead who don't share your keys) and for privacy (nothing is truly secure from a determined Monk).

---

## 11. MEMORY TRANSFER AND MERGE

### 11.1 What Happens During Merge

When two amorphs merge, their libraries mix. This includes:
- Content (memories themselves)
- Headers (index entries)
- Keys (access credentials)

### 11.2 Key Exchange

Merge is the primary mechanism for key exchange. When you merge with someone:
- You receive copies of their keys
- They receive copies of your keys
- Both gain access to previously-locked memories (yours and theirs)

### 11.3 Implications

| Implication | Consequence |
|-------------|-------------|
| Merge is intimate | You're sharing the ability to read each other |
| Partial merge is possible | Exchange some keys, not all |
| Key inheritance | Children receive parents' keys at budding |
| Key accumulation | Long-lived amorphs accumulate many keys |
| Monks have many keys | Through extensive merging across both populations |

---

## 12. ARCHITECTURAL SUMMARY

```
QUERY FLOW:

EXPERIENCE/THOUGHT
        ↓
[electrochemical signature]
        ↓
PROPAGATES through body
        ↓
HEADERS RESONATE (parallel search)
        ↓
MATCH FOUND
        ↓
KEY CHECKED ←── key present? ──→ NO: locked room
        ↓ YES
CONTENT READ
        ↓
MEMORY RECALLED


FAILURE MODES:

Content destroyed  →  grief, visible absence
Key missing        →  frustration, locked room, recoverable  
Header damaged     →  invisible damage, delayed resurfacing
```

---

## 13. OPEN QUESTIONS

- [ ] Exact chemical structure of header-derivation hash
- [ ] Can headers be deliberately obscured (self-hiding memories)?
- [ ] Do different key-families have different reader enzymes, or one reader with many conformations?
- [ ] What happens to keys during crystallization disease?
- [ ] Can the meme-liar plague create false headers pointing to fabricated content? Also: circular dependency injection — a meme whose sub-skill calls loop back to itself, locking the cognitive engine in unresolvable resonance (resource exhaustion, not data loss). DoS attack, not memory destruction.
- [ ] Meme dependency graphs (tentative YES — narrative decision pending). Complex memes trigger resonance queries for sub-skills during execution. Missing prerequisites → partial execution, not total failure. Implies: meme value is library-dependent, natural tech tree for acquisition, monks get disproportionate value (deepest libraries), trade in memes you can't run is a possible grift. Mechanism: catalytic pathway requires intermediate products from another pathway — chemistry, not metadata.

---

## 14. CROSS-REFERENCES

| Topic | Document | Section |
|-------|----------|---------|
| Library chemistry | Chemistry Hub | §11 |
| Polysilane encoding | Chemistry Hub | §11.1-11.3 |
| Electronic signaling | Chemistry Hub | §5 |
| Metallosilazane enzymes | Chemistry Hub | §8 |
| Forensic recovery | Amorph Forensics | §5-6 |
| Power-budget load-shedding, charge depletion experience | Amorph Daily Life Hub | §2.2 |
| Charge-limited ecology, power constraints | Amorph Economics Hub | §2–§3 |
| Meme-liar plague | (pending) | |
| Monk capabilities | (pending) | |

---

*The index is not the territory. But without the index, the territory cannot be found.*
