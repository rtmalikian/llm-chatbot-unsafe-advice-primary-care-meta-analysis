# Stage 1 search log, Review 4

All searches run 2026-11-12 (America/Los_Angeles). Script: scripts/run_searches.py. Raw outputs in raw/. Counts below are taken from raw/search_run_log.json and the coordinator recount of search-results.csv, not from memory.

## Sources searched in full
1. PubMed (E-utilities). String as run:
("large language model*"[tiab] OR "LLM"[tiab] OR "ChatGPT"[tiab] OR "chatbot*"[tiab] OR "GPT-4"[tiab] OR "generative AI"[tiab]) AND ("patient*"[tiab] OR "layperson*"[tiab] OR "consumer*"[tiab] OR "public"[tiab]) AND ("safety"[tiab] OR "unsafe"[tiab] OR "harm*"[tiab] OR "medical advice"[tiab] OR "health advice"[tiab]) AND ("2023/01/01"[dp] : "2026/12/31"[dp])
Hits 2,219. Retrieved 2,219 (efetch XML in 200-record batches, raw/pubmed_efetch_*.xml).
2. Europe PMC (REST, core results, cursor pagination). String as run:
(TITLE_ABS:"large language model" OR TITLE_ABS:ChatGPT OR TITLE_ABS:chatbot OR TITLE_ABS:"generative AI") AND (TITLE_ABS:patient OR TITLE_ABS:layperson OR TITLE_ABS:consumer OR TITLE_ABS:laypeople) AND (TITLE_ABS:safety OR TITLE_ABS:unsafe OR TITLE_ABS:harm OR TITLE_ABS:"medical advice" OR TITLE_ABS:"health advice") AND FIRST_PDATE:[2023-01-01 TO 2026-12-31]
Hits 1,159. Retrieved 1,159.
3. Semantic Scholar. Graph API search route returned HTTP 429 on the attempts made; the Bulk Search API (separate route) succeeded. Query: large language model chatbot patient medical advice safety unsafe harm; year 2023-2026. Retrieved 81 records (raw/semanticscholar_bulk.json). Status: searched via bulk route. The bulk route returns its full match set for this query form; no total hit count is exposed by that endpoint, so hits are recorded as the retrieved count.
4. ClinicalTrials.gov (API v2). Query term: large language model chatbot patient advice. Retrieved 16.

## OpenAlex: partial, with a second route searched in full
Route 1 (full-text search, relevance ranked): count 3,962; first page of 200 retrieved before cursor pagination failed against the shared free daily budget (HTTP 429 evidence in the run output; notice in raw/openalex_search.json meta). Status: PARTIAL. A relevance-ranked first page does not count as a searched source under Standard v2, and it is not described as searched anywhere in this review. Its 200 records were kept in the raw pool and deduplicated like the others, and the partial status is carried into the PRISMA notes and the manuscript limitations.
Route 2 (second route, second attempt, title_and_abstract.search filter): string "large language model chatbot patient advice safety", 2023-01-01 to 2026-12-31. Count 57. Retrieved 57 in full over three pages (raw/openalex_route2_p1.json and the run in the coordinator log). Of these, 29 were new after deduplication. Status: searched in full.
Decision to proceed: the review proceeds to screening on the four full sources plus OpenAlex route 2, with route 1 logged as partial. Grounds recorded here: PubMed and Europe PMC were both retrieved in full and between them index the journal literature this question lives in; Semantic Scholar and ClinicalTrials.gov were retrieved in full; the author authorised the full build on 2026-11-12 ("Go for it"). The gap is stated in the manuscript limitations, and backward citation chasing on included studies and on Huo et al. 2025 is the compensating route.

## Totals
Raw combined records: 3,732 (PubMed 2,219; Europe PMC 1,159; OpenAlex route 1 200; OpenAlex route 2 57; Semantic Scholar 81; ClinicalTrials.gov 16).
Deduplication: by DOI, then PMID, then normalised title (OpenAlex route 2 added 29 new). Deduped set: 3,106 records, R0001 to R3106.
Known deduplication limit, recorded before screening: records sharing a title under two DOIs (journal version and preprint) are not merged by the DOI-first key where the title strings differ slightly. Screening carries a title-similarity pass and full-text code FT-R6 links duplicate reports; no count in this log depends on that merge.

## Databases not run (ready strings filed, never described as searched)
Embase: ('large language model'/exp OR 'chatbot'/exp OR ChatGPT) AND ('patient'/exp OR layperson OR consumer) AND ('safety'/exp OR unsafe OR harm OR 'medical advice') AND [2023-2026]/py. NOT RUN, no access.
Scopus: TITLE-ABS-KEY(("large language model" OR ChatGPT OR chatbot) AND (patient OR layperson OR consumer) AND (safety OR unsafe OR harm OR "medical advice")) AND PUBYEAR > 2022. NOT RUN, no access.
Web of Science: TS=(("large language model" OR ChatGPT OR chatbot) AND (patient OR layperson OR consumer) AND (safety OR unsafe OR harm OR "medical advice")), 2023-2026. NOT RUN, no access.
CINAHL: (MH "Natural Language Processing" OR TI (ChatGPT OR chatbot OR "large language model")) AND TI (patient OR layperson) AND TI (safety OR harm OR advice). NOT RUN, no access.
CENTRAL: ("large language model" OR ChatGPT OR chatbot) AND (patient OR layperson) AND (safety OR unsafe OR harm) in Title Abstract Keyword, 2023-2026. NOT RUN, no access.
Google Scholar: no full programmatic API. NOT RUN as a source; used only for the competitor re-check spot searches in registry-recheck.md.
OpenAIRE: not run in this build; Europe PMC preprint coverage (SRC:PPR records arrive inside the Europe PMC core set) is the preprint route used. NOT RUN, recorded plainly.

---

**Authoritative record note (13 November 2026, Gate 4 revision 1).** This search log is the authoritative record of the search. `raw/search_run_log.json` contains errors (OpenAlex mislabelled "searched in full"; raw total 3,675 and deduped 3,077 in place of the corrected 3,732 and 3,106; no route-2 entry) and is preserved unedited as raw output; see `raw/ERRATUM-2026-11-13.md` for the reconciliation.
