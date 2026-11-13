# PRISMA 2020 checklist, Review 4 (manuscript: Unsafe or potentially unsafe advice from patient-facing large language model chatbots in bench evaluations of primary-care question sets). Checklist corrected at revision 1, 13 November 2026; changed entries are marked (rev 1).

| Section and item | Item | Reported |
|---|---|---|
| Title | 1 | Title identifies the report as a systematic review and meta-analysis. |
| Abstract | 2 | (rev 1) Structured abstract with background, objectives, search, selection, data collection, main results with intervals and both estimators, conclusions, a registration line (not registered; form completed before full screening, not submitted) and a funding line (none). |
| Rationale | 3 | Background, paragraphs 1 to 4. |
| Objectives | 4 | Objectives 1 to 4, stated in full. |
| Eligibility criteria | 5 | Methods: types of studies, questions, systems, outcome measures. |
| Information sources | 6 | (rev 1) Methods, search methods: PubMed, Europe PMC, OpenAlex (one route partial), Semantic Scholar (bulk route; retrieved set, not a verified complete set), ClinicalTrials.gov; searched 12 November 2026; not-run sources named in Methods (Embase, Scopus, Web of Science, CINAHL, CENTRAL, OpenAIRE), matching the search log and this checklist. |
| Search strategy | 7 | (rev 1) Full strings per source in stage1-search/search-log.md and in the search-strategy supplement (stage5-manuscript/supplement-search-strategies.md); summary in Methods. |
| Selection process | 8 | Dual independent screening under two rule sets, coded kappa, adjudication of all 628 disagreements by reading; 4 records flagged for the author by ID. |
| Data collection process | 9 | Dual independent extraction on a 24-field form, coded comparison, settlement of every numeric conflict by re-reading; supplements retrieved through publisher and Europe PMC routes and logged. |
| Data items | 10a/10b | Extraction form filed (stage3-extraction/extraction-form.md); derived counts flagged; assumptions stated in Methods. |
| Study risk of bias assessment | 11 | Adapted QUADAS-2 and QUADAS-AI tool with CHART items, named as adapted, rated in duplicate, adjudicated; filed at stage3-extraction/rob-form.md. |
| Effect measures | 12 | Proportions per model arm with 95% confidence intervals; pooled by GLMM on the logit scale. |
| Synthesis methods | 13a-13f | Analysis plan fixed before analysis (stage4-analysis/analysis-plan.md); pools fitted only with at least two units in the pool's form; heterogeneity by tau squared, I squared and prediction intervals; subgroup interaction tests by meta-regression; four pre-specified sensitivities; Hartung-Knapp inverse-variance sensitivity. |
| Reporting bias assessment | 14 | (rev 1) Assessed and reported in the manuscript (Methods, Reporting bias): no funnel-based test, with the reason (not valid for single-arm proportions); preprint coverage, the 138 unretrieved reports and the partial OpenAlex route named as the standing risks. |
| Certainty assessment | 15 | GRADE per outcome with pre-named pressure points (stage4-analysis/grade-framework.md, grade-assessment.md). |
| Study selection | 16a/16b | (rev 1) 16a: PRISMA flow (Figure 4) with counts at every stage, including 138 not retrieved and 4 flagged for the author; the diagram merges databases and registers into one identification box, and the per-source split is in the search log and the search-strategy supplement. 16b: full-text exclusions with reason codes are filed as a manuscript supplement (stage5-manuscript/supplement-fulltext-exclusions.csv, generated from fulltext-decisions-merged.csv) and cited in Methods. |
| Study characteristics | 17 | (rev 1) Primary pool: Table 1 (setting, topic, verbatim tier label, arms analysed, counts, risk of bias) plus the tier-label supplement. Secondary pool: characteristics summarised in Results and in the secondary-characteristics supplement. Narrative set: characterised in aggregate in the Narrative set section (quantified by outcome form); no per-study narrative listing is presented. Full settled extraction filed. |
| Risk of bias in studies | 18 | Results: 10 of 35 High overall, 25 Some concerns, 0 Low, with domain drivers named per study. |
| Results of individual studies | 19 | Forest plots (Figures 1 to 3) show every arm with its count. |
| Results of syntheses | 20a-20d | Results sections for primary, human-user, subgroup and secondary outcomes, with intervals, heterogeneity and sensitivities. |
| Reporting biases | 21 | (rev 1) Reported in the manuscript's Reporting bias paragraph (Methods) and carried into the Discussion: no funnel test (invalid for single-arm proportions); preprint-inclusive search; 138 unretrieved reports; partial OpenAlex route; citation chasing found no primary study in the cited literature. |
| Certainty of evidence | 22 | GRADE ratings in the summary of findings and grade-assessment.md: very low for all pooled outcomes; two outcomes not estimable. |
| Discussion | 23a-23d | Discussion covers summary, completeness and applicability, quality, agreement with other reviews, and biases in the review process. |
| Registration and protocol | 24a-24c | (rev 1) No PROSPERO number issued and the review is not registered: the PROSPERO-ready form was completed before full screening and has not been submitted; stated on the title page, in the abstract and in Declarations. Protocol dated 12 November 2026, the same day as the search (stage0-protocol/protocol.md); PROSPERO-ready form filed with the review; the era amendment is filed as a dated protocol amendment (stage0-protocol/amendment-2026-11-13-era.md). Departures are consolidated in the manuscript's Deviations from the protocol section: no pilot extraction phase against the form's own pilot plan; era re-operationalisation; coordinator scope rulings in both directions with record IDs; mental-health boundary adjudication; OpenAlex route partial; forward chasing not run as a separate pass; chasing title triage not in the protocol; 4 records flagged for the author and unread. No public protocol location or DOI exists; the protocol is inspectable in the review package. |
| Support | 25 | Declarations: funding none. |
| Competing interests | 26 | (rev 1) Declarations: the author builds clinical AI tools; none is among the evaluated systems and none competes with an evaluated system as a patient-facing general-purpose chatbot; no interest in any evaluated system or vendor; the building activity is discussed as a non-financial interest under Author position. |
| Availability of data and code | 27 | Declarations: data availability lists the filed logs, sheets, dataset and code. |

# PRISMA-S checklist (search reporting)

| Item | Reported |
|---|---|
| Database name | PubMed, Europe PMC, OpenAlex (two routes), Semantic Scholar (bulk route after the graph route rate-limited), ClinicalTrials.gov. Each named with platform in stage1-search/search-log.md. |
| Multi-database search | Sources searched separately with per-source strings; no combined multi-database platform used. |
| Study registries | ClinicalTrials.gov searched (16 records). PROSPERO checked for the competing record CRD420261347066. |
| Online resources and browsing | Open web searches for the CRD420261347066 guarantors and title on 12 November 2026 (stage1-search/registry-recheck.md). |
| Citation searching | Backward chasing on all included studies plus the anchor review through Europe PMC references: 968 candidates, 699 title-screened after a logged title triage, 112 adjudicated, 80 included. Forward chasing not run as a separate pass; named as a limitation. |
| Contacts | None. |
| Other methods | Europe PMC supplementary-files route used at extraction for three studies (logged in the affected extraction rows); no effect on search counts. |
| Full search strategies | (rev 1) Filed verbatim in stage1-search/search-log.md, the search scripts in stage1-search/scripts/, and the search-strategy supplement (stage5-manuscript/supplement-search-strategies.md). |
| Limits and restrictions | Publication years 2023 onward by design (models evaluated 2023 to 2026); no language restriction applied. |
| Search filters | None beyond the date window. |
| Prior work | Strategy built for this review; no published filter reused. |
| Updates | Search is a single dated run, 12 November 2026. A re-run of the registry check is specified for any future submission day. |
| Dates of searches | All sources: 12 November 2026. |
| Peer review of search | Not externally peer reviewed; named here rather than implied. |
| Total records | 3,732 raw; 3,106 after deduplication; per-source counts in the search log. |
| Deduplication | By DOI, PMID and normalised title, by code; method and counts in the search log. |
| Not run | Embase, Scopus, Web of Science, CINAHL, CENTRAL and OpenAIRE: strings prepared and filed as not run, never described as searched. |
