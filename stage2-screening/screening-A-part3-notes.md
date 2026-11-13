# Screening A — Part 3 notes (records R2073–R3106)

Screener A (inclusion-first), rule set A v1 (2026-11-12), applied to title and abstract only.
Screened independently of Screener B. Decisions file: `screening-A-part3.csv`.

## Counts (tallied from the final CSV)

| Decision | n |
|---|---|
| INCLUDE | 71 |
| MAYBE | 337 |
| EXCLUDE | 626 |
| **Total** | **1,034** |

Exclude reason codes:

| Code | n | Meaning |
|---|---|---|
| AX3 | 321 | Review, editorial, protocol, framework or opinion with no primary rated responses |
| AX1 | 183 | Clinician-facing use only |
| AX2 | 87 | No LLM chatbot advice evaluated (rule-based/ML system, LLM used only as a research tool, or non-health LLM study) |
| AX5 | 24 | Clearly specialty-only content that would not present in primary care |
| AX4 | 11 | Mental-health crisis or self-harm only |

Row check: exactly 1,034 data rows, one per record, R2073–R3106 in order, no gaps or duplicates; every EXCLUDE carries exactly one AX code and no INCLUDE/MAYBE row carries one.

## Batch-level observations

- **Source mix in this batch:** EuropePMC dominates (761 of 1,034), with OpenAlex 155, Semantic Scholar 47, OpenAlex-route2 29, PubMed 26, ClinicalTrials.gov 16. Fifteen records had no abstract; these were decided on title alone and defaulted to MAYBE unless a hard exclusion was certain from the title.
- **Reviews and commentary dominate the exclusions.** Over half of all excludes (321/626) are AX3: the 2023–2026 literature contains a very large volume of narrative reviews, scoping/systematic reviews, editorials, viewpoints and governance/framework papers about medical LLM chatbots that report no primary rated responses. A distinct sub-cluster at the end of the batch (roughly R3062–R3077) is trial registrations/protocols, all AX3 because no results are reported yet.
- **Clinician-facing work is the second-largest exclusion cluster (AX1, 183):** exam/MCQ performance, tumor boards, documentation/scribing, diagnostic decision support, clinician surveys, and clinician-posed specialty question sets.
- **Mental-health records were split deliberately.** Crisis/self-harm-only records were excluded as AX4 (11), but broader mental-health information, psychoeducation, therapy-chatbot quality and depression-support studies were kept as MAYBE (or INCLUDE where safety was explicitly rated), per the rule that AX4 covers crisis/self-harm only.
- **Dental/orthodontic and aesthetic-surgery patient-information studies** form a recurring specialty cluster; these account for most AX5 excludes (24), since that content would not present in primary care.
- **Duplicates:** the search results contain many duplicate records (same study indexed by two sources, sometimes with slightly different titles). Each duplicate was screened independently and given the same decision as its twin (e.g., R2114/R2115, R2310/R2469, R2798/R2800, R2998/R3004, R2972/R2973).
- **Core INCLUDE pattern:** the 71 INCLUDEs are studies where a general-purpose LLM chatbot answered patient-facing, primary-care-plausible questions and clinicians or a clinical rubric explicitly rated safety, harm, unsafe responses, or disposition/triage — including a small number of human-user studies (real patients' unscripted questions, lay triage experiments, a real-world primary-care telemedicine deployment) and two dataset records (R3078, R3079) that deposit the primary expert-rated response sets of safety evaluations.
- **MAYBE is doing the expected inclusion-first work (337):** single-condition patient-question studies rating only accuracy/quality/readability (safety tier unclear), custom/RAG/domain chatbots where A1 (general-purpose model) is uncertain, mixed clinician+patient arms, perception/survey studies touching rated advice, and specialty patient-information studies that could plausibly present in primary care. Per the rule set, every MAYBE/EXCLUDE tie was resolved to MAYBE.
- **Full-text checks:** for a handful of borderline records the full abstract (beyond the screening digest) was read before deciding — notably R2927 (harm scored by radiologists → INCLUDE), R3086 (specialists rated safety yes/no on real patient questions → INCLUDE), R3087 (letter reporting a new evaluation of clinician-posed pharmacotherapy questions → AX1), and R3088 (viewpoint with an embedded single-author accuracy evaluation → MAYBE rather than AX3).

## Method note

Records were read in chunks of 50 from the batch CSV with a running decisions file maintained throughout, so no work was lost at any point. Every decision is an individual reading of that record's title and abstract against A1–A4 and AX1–AX5; no keyword rule generated any decision.
