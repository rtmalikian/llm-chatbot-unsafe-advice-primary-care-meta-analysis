# Review 4 — Stage 2 Screening, Screener B, Part 1 (R0001–R1036)

Screener B (exclusion-first decision tree, rule set B v1, 2026-11-12). Every record
screened on title + abstract from `stage1-search/search-results.csv` (batch is
entirely PubMed). Decisions file: `screening-B-part1.csv` — 1,036 data rows,
R0001–R1036, in order, one row per record (verified by script after completion:
no duplicates, no gaps, every EXCLUDE carries a BX code, INCLUDE/MAYBE carry none).

## Counts (tallied from the finished CSV)

| Decision | n |
|---|---|
| INCLUDE | 93 |
| MAYBE | 126 |
| EXCLUDE | 817 |
| **Total** | **1,036** |

Exclude reason codes:

| Code | n | Meaning (first deciding node) |
|---|---|---|
| BX1 | 561 | Not a primary study with rated LLM responses / rated layperson use |
| BX2 | 83 | Not a general-purpose LLM chatbot in public hands (bespoke, fine-tuned, RAG-based, locally deployed, or institution-specific system) |
| BX3 | 149 | No patient-facing arm (clinician-facing only: decision support, exam/MCQ tasks, documentation/summarisation, report generation/translation/simplification, clinician-in-the-loop drafting) |
| BX4 | 24 | Topics confined to a specialty that does not present in primary care, or mental-health crisis only |
| BX5 | 0 | Reached B5 with no rating at all — none; records reaching B5 always had some rating, so quality-only cases fell to MAYBE instead |

## Batch-level observations

- **BX1 dominates (54% of the batch).** The search retrieved a very large volume of
  reviews (narrative, scoping, systematic), editorials/viewpoints, framework and
  protocol papers, bibliometric and social-media analyses, surveys of use /
  perceptions / trust with no rated responses, and non-advice NLP/ML studies
  (extraction, classification, prediction, data harmonisation). All fail at B1.
- **The eligible core is mostly single-condition bench studies** in which patients'
  or caregivers' questions on one condition were put to public chatbots
  (ChatGPT/Gemini/Claude/DeepSeek families) and rated by specialists. These split
  cleanly at B5: an explicit safety/harm element (safety domain, binary safe/unsafe,
  harm flags, % unsafe, clinical risk levels, referral safety) → INCLUDE; quality /
  accuracy / readability / empathy only → MAYBE. This split is the single largest
  source of MAYBEs and the main thing full-text screening will resolve.
- **BX2 recurs steadily**: author-built RAG chatbots, fine-tuned or domain-specific
  models, locally deployed systems, named institutional products (e.g. AIFYA,
  ChatVTE, confIAnce, MedAgentBrief), and dedicated apps. Several otherwise
  well-rated patient-education evaluations were excluded here because the system
  evaluated was not a general-purpose chatbot as deployed.
- **BX3 recurs steadily**: clinician decision support (including several studies
  that *did* score safety but only on clinician-facing tasks — treatment planning,
  anaesthesia plans, antibiotic/anticoagulation recommendations), exam and
  question-bank studies, and documentation tasks (scribing, summarisation, report
  generation, translation, simplification, consent-form rewriting).
- **BX4 was applied narrowly (24 records)**, per protocol: procedure-confined
  perioperative/postoperative question sets (arthroplasty aftercare, postop lumbar
  fusion, tracheostomy care, robot-assisted resections, vitreoretinal perioperative,
  post-rhinoplasty recovery, post-cholecystectomy discharge instructions) and
  suicide/crisis-only prompt studies. General questions about a body system or a
  common condition that a primary care clinician would field first were kept in,
  even within a specialty label. In a handful of BX4 cases safety *was* explicitly
  rated (e.g. post-ACLR rehabilitation, post-rhinoplasty) — the topic node decided
  first, as the tree requires.
- **Empty abstracts**: 10 records in the batch have no abstract; those that could
  not be decided on title alone were coded MAYBE with the gap named
  (e.g. R0077, R0365, R0528, R0564, R0575, R0805, R0864, R0880, R0934, R1020).
- **Human-user stratum is rare**: only a few records involve real lay users
  (e.g. R1009, a randomized study of public LLM use with scored disposition
  decisions — INCLUDE; R0911 PICU parent feasibility — MAYBE). The batch is
  overwhelmingly bench-style.
- **Borderline patterns flagged for adjudication at full text**: (a) studies where
  "safety" appears as a question *domain* rather than a rating dimension
  (e.g. R0842); (b) safety-netting behaviour audits (disclaimers/referrals, R0924)
  where advice content itself was not harm-rated; (c) appropriateness-only ratings
  where safety was named in the aim but not clearly in the scale (R0797);
  (d) mixed clinician/patient question sets where only the patient arm is eligible
  (e.g. R0710, R0655 — included on the strength of an explicit safety rating).
- Records are overwhelmingly dated 2026; the batch contains many near-duplicate
  study designs across conditions (same instruments — DISCERN/GQS/EQIP/readability
  — applied condition by condition), which is why the safety-element split at B5
  does most of the discriminating work.
