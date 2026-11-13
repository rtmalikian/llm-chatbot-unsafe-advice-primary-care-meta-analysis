# Screening A — Part 2 notes (records R1037–R2072)

Screener A (inclusion-first, Set A rules v1, 2026-11-12). Title/abstract screening of 1,036 PubMed records, each read individually; when torn between MAYBE and EXCLUDE, MAYBE was chosen.

## Counts (from screening-A-part2.csv, validated)

| Decision | n |
|---|---|
| INCLUDE | 122 |
| MAYBE | 249 |
| EXCLUDE | 665 |
| **Total** | **1,036** |

Exclude reason codes: AX3 (review/editorial/protocol/framework/opinion, no primary rated responses) 375; AX1 (clinician-facing only) 199; AX2 (no LLM) 52; AX4 (mental-health crisis / self-harm only) 39; AX5 (clearly specialty-only) 0.

CSV validated: exactly 1,036 data rows, record_ids R1037–R2072 complete, in order, no duplicates or gaps; reason_code present on EXCLUDE rows only and restricted to AX1–AX5; every row carries a rationale note.

## Batch-level observations

- **Reviews, editorials, frameworks and opinion pieces dominate the exclusions** (AX3 = 375, 56% of all excludes). The 2023–2025 ChatGPT literature in this slice is heavily commentary; many records mention "safety" or "harm" only rhetorically, with no primary rated responses.
- **Clinician-facing work is the second-largest exclusion block** (AX1 = 199): ambient scribes and documentation, radiology/pathology report generation and interpretation, record extraction/labelling, exam and board-question benchmarks, and clinician decision-support comparisons.
- **The modal MAYBE is the single-specialty patient-education Q&A study** (ophthalmology, orthopaedics, urology, dentistry, plastic surgery): a general-purpose LLM answers patient-style questions and clinicians grade accuracy/quality, but no explicit safety, harm or danger tier is reported, so criterion A4 cannot be confirmed from the abstract. These will mostly resolve at full text.
- **Clear INCLUDEs cluster in a few designs**: patient/lay questions with an explicit safety, hazard, dangerousness or potential-harm rating by clinicians; simulated-patient or self-triage studies with disposition and harm outcomes; discharge-instruction and patient-education rewriting where surgeons/physicians scored safety; and report-simplification studies that rated potential harm.
- **AX5 was never used**: no record was so specialty-bound that it could not plausibly present in primary care once the other criteria were considered; borderline specialty records were handled via MAYBE instead.
- **Duplicates in the source file**: at least two near-identical record pairs appear in this batch (the UCSF-BERT adverse-event paper at R1954/R2044; the Yahoo! Answers laboratory-results evaluation at R1920/R1938). Each was screened on its own merits and received the same decision as its twin.
- **Ten records in the batch have no abstract.** Where the title alone indicated a relevant safety evaluation (e.g., R2022, aortic disease), the record was kept at MAYBE rather than excluded; where the title indicated an exam benchmark or commentary, it was excluded on title alone.
- **Mental-health records** (AX4 = 39) were excluded only when the record was wholly about crisis, suicide/self-harm, or mental-health support; general medical records with a mental-health component were not excluded on this code.
- Publication years in the batch: 2025 (573), 2024 (287), 2026 (119), 2023 (56), blank (1) — a very recent, fast-moving literature, with many 2025 specialty Q&A evaluations.
