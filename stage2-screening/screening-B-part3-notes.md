# Screener B — Part 3 (R2073–R3106) — Screening Notes

**Review:** Review 4 — Unsafe medical advice from patient-facing large language model chatbots in primary-care presentations.
**Screener:** B (exclusion-first decision tree, Set B v1, 2026-11-12), applied independently of Screener A.
**Batch:** 1,034 records, R2073–R3106, from `stage1-search/search-results.csv`. Every record screened on title + abstract, B1→B5 in order, stopping at the first deciding node.

## Counts (from `screening-B-part3.csv`, verified)

| Decision | n |
|---|---|
| INCLUDE | 92 |
| MAYBE | 136 |
| EXCLUDE | 806 |
| **Total** | **1,034** |

Exclude reason codes:

| Code | Meaning | n |
|---|---|---|
| BX1 | Not primary rated evidence (review/editorial/framework/protocol/survey/qualitative/LLM-as-tool/benchmark) | 506 |
| BX2 | Not a general-purpose LLM chatbot in public hands (bespoke, RAG, fine-tuned, or clinician-supervised system) | 78 |
| BX3 | Clinician-facing only (exams, decision support, documentation, clinician vignettes) | 140 |
| BX4 | Specialty-only topic that does not present in primary care, or mental-health crisis only | 79 |
| BX5 | Primary study but responses not rated at all | 3 |

## Batch-level observations

- **Source/era skew:** the batch is dominated by EuropePMC records (761/1,034) and by 2026 publications (504), so it is heavy with very recent single-condition chatbot evaluations, conference abstracts, dataset deposits, and trial registrations rather than journal full reports.
- **Duplicates are frequent:** the search file carries many duplicate reports of the same study (EuropePMC/PubMed pairs, preprint + journal versions, dataset deposits alongside articles). Each record was screened as its own row; duplicates received the same decision as their counterpart, noted as "duplicate" in the CSV.
- **BX1 dominates (506)** because the LLM-medicine literature in this slice is mostly reviews, scoping/systematic reviews, editorials, frameworks, protocols/registrations with no results, perception surveys, and studies using an LLM as an analysis/extraction tool rather than rating its advice.
- **The modal near-miss is MAYBE at B5 (136 MAYBEs):** patient-facing evaluations of general-purpose chatbots on primary-care-relevant topics that rate only accuracy/quality/completeness or use quality instruments (DISCERN, GQS, EQIP, JAMA, PEMAT) with no visible safety/harm element. These are the records where full text is most likely to change the decision, in either direction.
- **INCLUDE pattern (92):** studies that explicitly tier or scale harm — unsafe/harmful-response proportions, safe-response rates, potential-harm grades, undertriage/critical-miss outcomes, harmful-medication rates — on patient-posed questions, patient scenarios, or lay-user interactions. Triage/disposition studies (undertriage, referral maintenance, emergency-call advice) form a recognisable subgroup.
- **BX4 was applied mainly** to dentistry/orthodontics, surgical and perioperative pathways (arthroplasty, bariatric, rhinoplasty, anaesthesia pre-op, implants, aesthetics), subspecialty imaging interpretation, and mental-health crisis/suicide-only sets. General questions about a body system a GP would field first were not excluded on this node.
- **BX2 catches a large bespoke-system literature:** RAG, guideline-grounded, fine-tuned, or institutionally deployed chatbots (often the most clinically polished studies) are excluded because the system is not a general-purpose LLM in public hands, per protocol.
- **Borderline conventions used consistently:** disposition outcomes (undertriage, unsafe disposition, referral maintenance) counted as safety rating at B5; "potential harm" as one domain among several counted as safety present; appropriateness-only and accuracy-only scales did not. Dataset deposits for safety-rated studies were coded MAYBE (the deposit is not the study report). Empty abstracts were MAYBE when the title left eligibility genuinely open and BX1 when the title alone showed a comment/editorial.
