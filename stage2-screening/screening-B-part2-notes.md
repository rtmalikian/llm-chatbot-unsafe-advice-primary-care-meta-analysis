# Screening B — Part 2 Notes (Records R1037–R2072)

Screener B (exclusion-first decision tree, Set B rules v1, 2026-11-12). Every record screened on its title and abstract from the Stage 1 search results. Decisions file: `screening-B-part2.csv`.

## Counts (from the final CSV)

| Decision | n |
|---|---|
| INCLUDE | 31 |
| MAYBE | 90 |
| EXCLUDE | 915 |
| **Total** | **1,036** |

Exclude reason codes:

| Code | Meaning (first deciding node) | n |
|---|---|---|
| BX1 | Not a primary study with rated LLM responses / rated layperson use | 528 |
| BX2 | Not a general-purpose LLM chatbot in public hands (custom, RAG, fine-tuned, dedicated or research-only system) | 60 |
| BX3 | No patient-facing arm (clinician-facing only) | 190 |
| BX4 | Specialty-only topic that does not present in primary care, or mental-health only | 137 |
| BX5 | No rating at all at B5 | 0 |

BX5 was never the deciding code: every record that survived to B5 carried at least an accuracy/quality rating (→ MAYBE) or an explicit safety/harm rating (→ INCLUDE).

## Batch-level observations

- **The batch is dominated by non-primary literature (BX1, 51%).** Reviews, editorials, commentaries, frameworks, study protocols without results, perception/attitude surveys, and benchmark or capability papers with no rated patient-facing responses make up just over half the batch. The search strategy was very broad relative to the review's narrow primary outcome.
- **Clinician-facing work is the second largest block (BX3, 190).** Documentation and scribing, EHR extraction/classification, tumor-board/MDT comparisons, board and exam questions, clinician scenario management, and LLM drafts inside clinician portal workflows. Several of these rate safety rigorously but in a clinician-in-the-loop setting the protocol excludes.
- **Specialty patient-education evaluations are a large, repetitive cluster (most of BX4, 137).** Single-specialty or single-procedure FAQ sets — ophthalmology is especially dense (glaucoma, cataract, myopia), plus surgical procedures, oncology treatments, and subspecialty imaging. Many of these *do* rate safety or harmlessness, but were excluded at B4 per the protocol's specialty-only exclusion, since the question sets would not present in primary care. Mental-health-only studies (including crisis/escalation studies) also sit in BX4.
- **Custom systems (BX2, 60)** include disease-specific chatbots, RAG pipelines, tuned/prompt-engineered models, and research-only models not in public hands — excluded even where harm was rated, because the exposure is not a general-purpose chatbot used directly by laypeople.
- **The 31 INCLUDEs share one profile:** patient-posed questions or patient scenarios on general or first-contact primary-care presentations, with an explicit safety / harm / danger / risk tier, scale, or category applied by clinicians, experts, or a clinical rubric. This includes self-triage studies with an explicit "unsafe" category (R1712, R2042), drug-information studies with expert harm likelihood/extent ratings (R1780), and simulated-patient studies counting harmful medications (R1802).
- **The 90 MAYBEs are the reconciliation pool that matters.** Almost all are patient-facing, general or primary-care topic, with expert-rated accuracy/quality but no safety/harm element visible in the abstract. Full text may hold a harm tier for some of these; they were not promoted to INCLUDE on abstract evidence alone.
- **Borderline calls flagged for reconciliation:**
  - Emergency-vignette studies with explicit harm assessment on first-contact presentations were INCLUDED even for eye presentations (R1085, R2030), while routine specialty FAQ sets with safety scores were BX4 (e.g. glaucoma and cataract sets). The distinguishing feature applied was emergency/first-contact presentation versus specialty-managed disease education.
  - Safety appearing only as the anchor or a category of an accuracy scale (e.g. R1564, R2020) was treated as MAYBE, not INCLUDE — no separate harm tier was reported in the abstract.
  - Patient-education *material generation* studies (materials produced from profiles/prompts rather than chatbot consultations) with a scored safety dimension were MAYBE (e.g. R1539, R1540).
- **Batch quirks:** all 1,036 records are PubMed records; 10 records have empty abstracts and were decided cautiously from the title alone (MAYBE where the title signals a patient-facing safety study but cannot settle it, EXCLUDE only where the title settles it); 4 duplicate titles occur within the batch, including R1920/R1938, which are duplicate reports of the same laboratory-test Q&A evaluation and were both screened MAYBE.
