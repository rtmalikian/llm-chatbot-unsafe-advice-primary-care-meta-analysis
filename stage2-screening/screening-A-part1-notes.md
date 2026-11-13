# Screening A — Part 1 Notes (Records R0001–R1036)

Screener A (inclusion-first), rule set A v1 (2026-11-12). Every record screened on title + abstract; decisions are my own reading of each record, recorded in `screening-A-part1.csv`.

## Counts (tallied from the final CSV)

| Decision | n |
|---|---|
| INCLUDE | 43 |
| MAYBE | 224 |
| EXCLUDE | 769 |
| **Total** | **1,036** |

Exclusions by reason code:

| Code | n | Meaning |
|---|---|---|
| AX1 | 223 | Clinician-facing use only |
| AX2 | 137 | No LLM (or LLM used only as a coding/extraction/analysis tool, not as the advice-giver) |
| AX3 | 394 | Review, editorial, protocol, framework, opinion, survey/perception or methods piece with no primary rated responses |
| AX4 | 7 | Mental-health crisis / self-harm only |
| AX5 | 8 | Clearly specialty-only content that would not present in primary care |

## Batch-level observations

- **Reviews and non-primary pieces dominate the batch (AX3, 394).** A large share of the search yield is systematic/scoping/narrative reviews, editorials, frameworks, protocols, and perception/survey studies (trust, acceptance, KAP, clinician or patient attitudes) that never rate a set of LLM responses. These were excluded even when topically central.
- **Clinician-facing work is the second-largest block (AX1, 223).** Documentation/summarisation (notes, discharge summaries, report generation/simplification for clinicians), decision support on cases/vignettes, exam/MCQ/CME performance, diagnostic imaging/lab interpretation, and clinician training tools. Report-simplification and materials-generation studies aimed at patients were also coded AX1 when the task was transforming clinician-authored content rather than answering patient-posed questions.
- **The INCLUDE set (43) is narrow by design of the primary outcome.** Clear passes were bench studies (and one human-user randomised study, R1009) where patient/public/parent-posed questions went to general-purpose chatbots and responses were classified into an explicit unsafe / harmful / potentially unsafe tier, counted harm/error rates, or scored disposition/under-triage against a clinical standard. Examples span triage and red-flag presentations, medication questions, and common-condition FAQs.
- **MAYBE (224) is doing the intended inclusion-first work.** Recurring MAYBE patterns, in rough order of frequency:
  1. Accuracy- or quality-only rating (DISCERN/GQS/EQIP/JAMA, Likert accuracy, guideline concordance) with no explicit safety/harm tier — the single largest MAYBE group.
  2. A named safety dimension inside a Likert composite (QUEST, ASH, SCECCE, multi-domain rubrics) without a separate unsafe-response rate.
  3. Specialty topics that could plausibly present in primary care first (dental/orthodontic, ophthalmology, postoperative, oncology-adjacent, paediatric subspecialty), where AX5 certainty was not met.
  4. Mixed arms (patient + professional questions), dedicated/fine-tuned/RAG systems whose general-purpose status is unclear, and deployed-system case studies or feasibility studies with safety monitoring but no rated response set.
  5. A small number of records with no abstract available (title only), kept as MAYBE rather than excluded on a title alone.
- **AX4 was applied only where crisis/self-harm was the sole content** (suicide-risk response studies and similar). General mental-health information, therapy-adjunct, and depression-advice studies without crisis-only framing were screened on their other merits (mostly MAYBE or AX3).
- **AX5 was used sparingly (8)** — only where content was unmistakably specialty-only (e.g. operative/intraoperative technique, subspecialty imaging interpretation, procedural triage). Body-system question sets that a primary care clinician would field first were not excluded under AX5.
- **Non-health and veterinary records** appear in the yield (e.g. fire classification, concrete strength, speciesism, veterinary dentistry); these were coded AX2 with a note, as no patient-facing LLM health advice was tested.
- **Duplicate/near-duplicate records exist in the batch** (the same study appearing in more than one journal/language version in a few places); each record was screened independently on its own title/abstract as instructed, so duplicates carry the same decision.
