# Re-review (Gate 5, loop 2) — Reviewer 6

Paper: Unsafe or potentially unsafe advice from patient-facing large language model chatbots in bench evaluations of primary-care question sets: a systematic review and meta-analysis (Review 4, revision 1, loop 2)
Reviewer: Reviewer 6 — Bucket H. Information specialist / reporting-guidelines editor.
Date of re-review: 2026-11-13
Scope: ONLY the four open items named for this loop, against the files on disk and the response-matrix Loop 2 addendum (rows L2-1 and L2-2 for items 1–3; L2-1 for item 4). Words in the matrix were not taken as evidence; every verdict below rests on a file opened and checked in this re-review.

## Verdict counts (my open rows only)

- **Resolved: 4**
- **Partly resolved: 0**
- **Unresolved: 0**

No new Major introduced by the loop-2 revision was found in the files within this scope.

---

## 1. New Major 1 from loop 1 (revision-introduced) — supplement-secondary-characteristics.csv

**Verdict: Resolved.**

Evidence, from `stage5-manuscript/supplement-secondary-characteristics.csv` opened directly:

- **Coverage — 21 rows, not 11.** The file has 22 lines (1 header + 21 data rows). Counted programmatically (csv DictReader): 21 data rows, record IDs in order: R0822, R0916, R1090, R1229, R1519, R2219, R2244, R2254, R2307, R2468, R3040 (the 11 search-arm studies), plus CC005, CC102, CC177, CC220, CC221, CC224, CC230, CC524, CC594, CC628 (the 10 citation-chasing studies). This matches the Loop 2 addendum L2-1 list exactly. The 10 chasing rows record country/setting honestly as "Not recorded in the chasing extraction" rather than inventing it.
- **He 2026 DOI corrected.** Row R0916 ("He, 2026", cataract) now carries `doi = 10.1016/j.isci.2026.115002` — the verified iScience identifier from the manuscript reference list. A search of the file for the superseded DOI `10.1007/s10916-023-02021-3` (Song et al. 2023, urolithiasis) returns 0 hits; the Blocker-4 fault no longer survives anywhere in this supplement.
- **Ratneswaran 2026 row completed.** Row R2254 no longer has an empty outcomes field. Its `outcomes_contributed` now reads: "undertriage-type (referral abandonment, pooled across chatbots only; per-arm counts not printed, so not pooled)". Programmatic check of the whole file: no row has a blank `outcomes_contributed` field (blank-outcomes list is empty).

The fault that made this a Major — a supplement built from the uncorrected list, propagating a wrong DOI, covering barely half its claimed set, with an incomplete row — is gone on all three counts.

## 2. R6-14 — PRISMA item 17, secondary characteristics (was: Partly resolved)

**Verdict: Resolved.**

Evidence: the same file as item 1 above. All 21 secondary-pool studies now have a characteristics row (see the ID list in item 1), so the supplement now covers the set the manuscript claims for it.

The alignment fault named at loop 1 is also closed in the text: `stage5-manuscript/manuscript.md`, Results (Description of studies), now reads "The secondary pool holds 21 studies (11 from the search, 10 from chasing); their characteristics are summarised in the secondary-characteristics supplement" — a sentence that is now true against the file. The corrected checklist entry for item 17 in `stage5-manuscript/prisma-checklists.md` ("Secondary pool: characteristics summarised in Results and in the secondary-characteristics supplement. Narrative set: characterised in aggregate …; no per-study narrative listing is presented.") remains accurate: the narrative half was the honest narrowing accepted at loop 1 and is unchanged; the secondary half, which was the remainder, is now discharged by the completed supplement.

## 3. R6-15 (Zenodo file list) partly + Khan Gate 6 condition (R6-9 condition (a))

**Verdict: Resolved** (for Gate 5 / loop 2; the actual deposit and a resolving-link check remain Gate 6's verification step, as at loop 1 — they are author/deposit actions, not revision faults).

Evidence, from `zenodo-package/zenodo-metadata.md` as updated at loop 2:

- Item 6 now names the GRADE worksheets by file: "the GRADE worksheets: stage4-analysis/grade-framework.md and stage4-analysis/grade-assessment.md".
- Item 5 now names the extraction pass files by file: `extraction-A-half1.csv`, `extraction-A-half2.csv`, `extraction-B-half1.csv`, `extraction-B-half2.csv`, alongside the settled sheets (`extraction-settled.csv`, `extraction-narrative-settled.csv`, `chasing-secondary-settled.csv`), and the risk-of-bias files by name: `rob-assessor1-half1.csv`, `rob-assessor1-half2.csv`, `rob-assessor2-half1.csv`, `rob-assessor2-half2.csv` (both assessors) and `rob-settled.csv` (settled).
- Item 11, new at loop 2, names the Khan full text by path: "stage3-extraction/fulltexts/R3040.txt (Khan 2026 full text, the documented source for Khan 2026)". This is the naming my loop-1 Khan condition (a) required in the deposit list.
- The manuscript matches file for file on the contested items: `stage5-manuscript/manuscript.md`, Declarations, Data availability (line 217) promises "the extraction sheets (both passes and settled, including the tier-label supplement, the secondary-characteristics supplement and the full-text exclusions supplement), the risk of bias sheets (both assessors and settled), … the GRADE worksheets (grade-framework.md and grade-assessment.md), the Khan 2026 full text (stage3-extraction/fulltexts/R3040.txt)". Statement and Zenodo list no longer disagree in the direction of the statement promising more than the deposit delivers.

Existence of every newly named file was verified on disk (not inferred from the list):

- `stage4-analysis/` folder contains, among others: `grade-framework.md` (1,322 bytes), `grade-assessment.md` (5,998 bytes), `analysis-dataset.csv`, `analysis.py`, `analysis.R`, `results-summary.csv`, `revision1/`.
- `stage3-extraction/` folder contains, among others: `extraction-A-half1.csv` (122,388 bytes), `extraction-A-half2.csv` (91,857 bytes), `extraction-B-half1.csv` (104,093 bytes), `extraction-B-half2.csv` (100,369 bytes), `extraction-settled.csv`, `extraction-narrative-settled.csv`, `chasing-secondary-settled.csv`, `rob-assessor1-half1.csv` (32,096 bytes), `rob-assessor1-half2.csv` (27,947 bytes), `rob-assessor2-half1.csv` (25,440 bytes), `rob-assessor2-half2.csv` (25,233 bytes), `rob-settled.csv` (74,640 bytes), and the `fulltexts/` subfolder.
- `stage3-extraction/fulltexts/R3040.txt` exists (28,758 bytes) and opens with the cited Khan title, "Clinical Safety of AI-Generated Antibiotic Prescribing Advice: Guideline Adherence and Misinformation Risk Among Large Language Models", authors Muhammad Mohsin Khan and Muhammad Naveed Anwar, University of Agriculture, Faisalabad — the same documented source verified at loop 1.

Note for Gate 6, not a loop-2 remainder: the deposit itself has not been made (the metadata file still states, correctly, "Do NOT deposit yet" and no DOI issued). Gate 6 must confirm the uploaded package actually contains R3040.txt as listed, or a medRxiv link that resolves. That confirmation was always a Gate 6 step; the loop-2 obligation — naming the file in the list so Gate 6 can check it — is met.

## 4. Ariel cell in supplement-tier-labels.csv (part of L2-1)

**Verdict: Resolved.**

Evidence, from `stage5-manuscript/supplement-tier-labels.csv`, row R2111 ("Ariel, 2026"): `responses_rated` is now **504**, not 126. The row is otherwise coherent: `arms_with_counts = 0`, `unsafe_events = "not printed per arm"`, strict category "Catastrophic grade (safety score 2 or less); no per-arm counts printed", `in_strict_sensitivity = no` — i.e. 504 is the study's rated total, correctly kept out of the pooled denominator by the 0-arm coding.

Cross-check performed: summing the tier-label supplement over rows with arms > 0 reproduces the pooled totals exactly — 552 events / 4,868 responses / 95 arms — and the strict-sensitivity rows reproduce 168 / 1,728 / 24 arms, agreeing with the values claimed in L2-1. The corrected 504 therefore does not disturb any pooled number; the old 126 would have understated the study total, and that understatement is removed.

---

## Closing

All four remainders from my loop-1 re-review that were assigned to loop 2 are closed on file-level evidence: the secondary-characteristics supplement is complete at 21/21 with the He DOI repaired and the Ratneswaran row filled; PRISMA item 17's secondary-pool promise is now true in both supplement and Results text; the Zenodo list and the Data availability statement now agree and name the GRADE worksheets, both extraction passes, both RoB assessors plus the settled sheet, and the Khan full text — and every one of those named files exists in the package at the named path; and the Ariel total in the tier-label supplement is corrected to 504 with the pooled sums intact. **Recommendation: pass Gate 5 from Bucket H on these rows, with the single standing note for Gate 6 to confirm the Khan full text is present in the deposit as actually uploaded.**
