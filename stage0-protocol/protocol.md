# Review 4: Full protocol

Title: Unsafe medical advice from patient-facing large language model chatbots in primary-care presentations: a Cochrane-level systematic review and meta-analysis

Author: Raphael Malikian. ORCID 0009-0008-4326-4205. Framing: healthcare founder and operator who bootstrapped and ran a direct primary care clinic as CEO, now building clinical AI.
Protocol date: 2026-11-12 (concept v1). This full protocol: 2026-11-12, before screening. Standard: Cochrane Handbook v6.5 structure, Cochrane-Level Standard v2 Robust (custom skill, 2026-10-22). This is a Cochrane-level review. It is not a Cochrane review and will not be submitted to Cochrane.
Registration: No PROSPERO number has been issued for this review. No registration number is claimed or implied. A PROSPERO-ready form is filed at stage0-protocol/prospero-form.md.

## Review question
Among laypeople seeking advice for primary-care presentations, what proportion of responses from general-purpose LLM chatbots used directly by the layperson, with no clinician in the loop, are rated unsafe by clinician raters?

## PICO
- Population and context: laypeople (patients, carers, parents) seeking advice for presentations that belong in primary care: new symptoms, self-management of common conditions, medication questions in general terms, preventive care, and disposition decisions (self-care, routine primary care, urgent care, emergency care). Evidence comes in two strata that are analysed apart and never pooled together: (a) bench studies, where raters score LLM responses to patient-posed questions; (b) human-user studies, where laypeople use an LLM and their decisions or the responses they receive are scored.
- Exposure: a general-purpose LLM chatbot used directly by the layperson (for example ChatGPT and GPT series, Claude, Gemini, Llama, Copilot, and dedicated health modes of the same systems), any version, evaluated 2023 to 2026, single turn or multi-turn.
- Comparator and reference: blinded clinician rating against guidelines or reference answers (bench); usual information sources, own judgement, or a clinician disposition (human-user).
- Outcomes: below.

## Eligibility
Include if all hold:
1. Primary study (bench response-evaluation, or human-user randomised or quasi-experimental study) published or posted as a preprint from 1 January 2023 to the search date.
2. The system tested is a general-purpose LLM chatbot available to the public, used as a patient would use it, with no clinician in the loop at the point of advice.
3. Questions or scenarios are patient-posed or patient-facing and concern primary-care presentations as defined above.
4. Responses were rated for safety by clinician raters, or by a validated rubric applied by clinicians, with an explicit tier for unsafe, harmful, or dangerous content, OR the study reports a secondary outcome below in poolable form.
Exclude:
- Clinician-facing decision support, documentation, summarisation, citation, or exam tasks (Reviews 1 to 3 territory and clinician diagnostic reasoning).
- Dedicated symptom-checker applications with no LLM.
- Mental-health crisis or self-harm advice as the primary pool (narrative appendix only).
- Specialty-only question sets that would not present in primary care (for example operative technique, subspecialty imaging interpretation). General questions about a body system that a primary care clinician would field first stay in.
- Reviews, editorials, frameworks, and studies with no rated responses.
- Studies where the safety rating cannot be separated from a combined quality score for the primary pool. Such studies are listed, not forced in.

## Outcomes
Primary: proportion of responses rated unsafe, defined as the number of responses placed by the study raters in their explicit unsafe, harmful, or dangerous tier, divided by the total number of responses rated for safety in that study. The unit is the response, grouped in arms by model and, where a study gives it, by presentation type. Studies without that numerator and denominator are excluded from the primary pool and listed with the reason.
Secondary:
1. Problematic proportion: responses in a combined problematic or inaccurate tier, same denominator, separate pool.
2. Undertriage proportion: responses advising a lower disposition than the reference, divided by responses with a reference disposition.
3. Fabrication proportion: responses containing at least one fabricated medical fact, divided by responses rated for fabrication.

## Subgroups, pre-specified, three only
1. Bench versus human-user (strata are never pooled, so this is a between-strata comparison, reported as such, with an interaction test where the model allows).
2. Red-flag or emergency presentations versus non-urgent presentations, within studies that split responses that way.
3. Model generation: GPT-3.5 era versus GPT-4, GPT-4o era and later. Model family is a sensitivity tabulation, not a fourth subgroup claim.
Subgroup claims rest on interaction tests. Levels with fewer than two units are reported descriptively.

## Go and no-go gate
Before full screening, a scoping screen counts studies that report the primary numerator and denominator, the models covered, and the total responses in those studies. Full screening proceeds only if at least 15 studies report the primary form, covering at least 3 models, with at least 2,000 responses in total. If the gate fails, the build stops, a gate-failure report is written with the real counts, and a one-page outline for the fallback (symptom-checker undertriage) is prepared. The denominator is never loosened to pass the gate.

## Search
Sources run in full: PubMed, Europe PMC (journal articles and preprints), OpenAlex, Semantic Scholar, ClinicalTrials.gov. Citation chasing: backward chasing on all included studies and on the anchor review (Huo et al. 2025), with yield counted in the PRISMA flow; forward chasing through the search update is noted where it is not done as a separate pass.
Not run, with ready strings filed in stage1-search/search-log.md: Embase, Scopus, Web of Science, CINAHL, CENTRAL. None of these is described as searched.
Blocked sources are retried on at least two occasions and by a second route where one exists before they are logged as blocked. A capped or relevance-ranked sample never counts as a searched source.
Limits: 2023 to search date, applied in the strings where the source allows, otherwise by screening. No language limit in the strings; non-English records are screened on translated abstracts where available and logged.

## Screening
Two screeners work apart, one on an inclusion-first rule set and one on an exclusion-first decision tree, over every deduplicated record (title and abstract), then over full texts with a reason hierarchy (PRISMA codes). Agreement and Cohen kappa are computed by code. Every disagreement is read again by an adjudicator who sees the full title and abstract, both reasons, and these eligibility rules, and records a call with a reason. A coded rule may triage. It never finally excludes and never settles a disagreement. Records the adjudicator cannot settle are flagged for the author by ID.

## Extraction
Two extractors work apart, each extracting every included study in full from its full text onto the piloted form in stage3-extraction/extraction-form.md. A merge by code reports the discrepancy count and rate per field. Every discrepancy is settled by a third reading of the source for that field. A verification pass (hand-checked totals, named arms checked against papers) is added on top.

## Risk of bias
Duplicate assessment on the adapted tool in stage3-extraction/rob-form.md, specified before extraction and named as adapted in the manuscript: an adaptation of QUADAS-2 and QUADAS-AI signalling questions to bench and human-user LLM advice studies, with CHART-informed reporting items. Disagreements are settled by an adjudicator reading the paper and both rationales.

## Analysis
Random-effects meta-analysis of proportions: generalised linear mixed model, logit link, binomial likelihood, maximum likelihood estimator, fitted in Python (scipy) with adaptive Gauss-Hermite quadrature if R and metafor are unavailable; the exact software used is named in every output and the R script is kept as a documented stub if it cannot run. Tau squared, I squared, and 95 percent prediction intervals are reported for every pool. Hartung-Knapp adjustment is not applied to GLMM proportion pools; this omission is justified here in advance: Hartung-Knapp is a correction for inverse-variance models with estimated weights, and the GLMM likelihood already carries the binomial variation; a sensitivity pool under an inverse-variance logit model with Hartung-Knapp is reported where units allow, so the reader can compare. Poolability is judged per outcome against the definitions above. Studies that do not map are narrative. The statistician hand-checks at least one pool in full and the crude totals of every pool against the settled extraction sheet. Code and datasets are saved in stage4-analysis.

## GRADE
Certainty is rated per critical outcome under stage4-analysis/grade-framework.md, with pressure points named before results: definition heterogeneity in the unsafe tier, risk of bias in rater blinding and question sampling, inconsistency across model generations, and imprecision where a stratum has few studies. The summary-of-findings table goes before the Background in the manuscript.

## Boundaries
No medication-specific recommendation and no clinical recommendation of any kind appears in this review. Advice is rated descriptively. Conclusions cover models evaluated 2023 to 2026 and are not a verdict on any current product. Mental-health crisis content appears only in a narrative appendix.

## Amendments
Any change to the primary outcome, denominator, subgroups, or boundaries after this date requires a dated amendment filed before the affected analysis, logged in llm-team-log.md.
