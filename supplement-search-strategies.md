# Supplement: full search strategies, Review 4 (revision 1, 2026-11-13)

All searches were run on 12 November 2026. Strings are reproduced exactly as
run, from stage1-search/search-log.md, which remains the authoritative log.
The raw run output is in stage1-search/raw/, with an erratum note
(ERRATUM-2026-11-13.md) reconciling the raw totals and the OpenAlex status
label. The search script is stage1-search/scripts/run_searches.py.

## Sources searched, with strings as run

1. PubMed (E-utilities). Hits 2,219, retrieved 2,219.
("large language model*"[tiab] OR "LLM"[tiab] OR "ChatGPT"[tiab] OR "chatbot*"[tiab] OR "GPT-4"[tiab] OR "generative AI"[tiab]) AND ("patient*"[tiab] OR "layperson*"[tiab] OR "consumer*"[tiab] OR "public"[tiab]) AND ("safety"[tiab] OR "unsafe"[tiab] OR "harm*"[tiab] OR "medical advice"[tiab] OR "health advice"[tiab]) AND ("2023/01/01"[dp] : "2026/12/31"[dp])

2. Europe PMC (REST, core results, cursor pagination). Hits 1,159, retrieved 1,159.
(TITLE_ABS:"large language model" OR TITLE_ABS:ChatGPT OR TITLE_ABS:chatbot OR TITLE_ABS:"generative AI") AND (TITLE_ABS:patient OR TITLE_ABS:layperson OR TITLE_ABS:consumer OR TITLE_ABS:laypeople) AND (TITLE_ABS:safety OR TITLE_ABS:unsafe OR TITLE_ABS:harm OR TITLE_ABS:"medical advice" OR TITLE_ABS:"health advice") AND FIRST_PDATE:[2023-01-01 TO 2026-12-31]

3. Semantic Scholar (Bulk Search API; the Graph API route returned HTTP 429).
Query: large language model chatbot patient medical advice safety unsafe harm; years 2023 to 2026. Retrieved 81 records. The bulk endpoint reports no total hit count, so the 81 records are the retrieved set, not a verified complete set.

4. ClinicalTrials.gov (API v2). Query term: large language model chatbot patient advice. Retrieved 16.

5. OpenAlex route 1 (full-text search, relevance ranked). Count 3,962; 200 retrieved before a rate limit stopped the route. PARTIAL: not counted as a searched source.

6. OpenAlex route 2 (title_and_abstract.search filter). String: "large language model chatbot patient advice safety", 2023-01-01 to 2026-12-31. Count 57, retrieved 57 in full; 29 new after deduplication.

Totals: 3,732 raw records; 626 duplicates removed; 3,106 deduplicated records screened.

## Citation searching

Backward citation chasing ran on the reference lists of all included studies
and of one anchor review (Huo et al. 2025) through the Europe PMC references
service: 968 candidate records from 2023 onward that were not in the search
set. A title triage by the review team removed 269 candidates before dual
screening (see the manuscript Methods for the rule, its limits and the
revision 1 re-screen of a sample of 50). The remaining 699 were title-screened
in duplicate; 112 passed at least one screener and were adjudicated against
abstracts or full texts; 80 were included (0 primary, 10 secondary, 70
narrative), 23 were excluded and 9 were not retrieved. Forward chasing was
not run as a separate pass.

## Sources not run (ready strings, never described as searched)

Embase: ('large language model'/exp OR 'chatbot'/exp OR ChatGPT) AND ('patient'/exp OR layperson OR consumer) AND ('safety'/exp OR unsafe OR harm OR 'medical advice') AND [2023-2026]/py. NOT RUN, no access.
Scopus: TITLE-ABS-KEY(("large language model" OR ChatGPT OR chatbot) AND (patient OR layperson OR consumer) AND (safety OR unsafe OR harm OR "medical advice")) AND PUBYEAR > 2022. NOT RUN, no access.
Web of Science: TS=(("large language model" OR ChatGPT OR chatbot) AND (patient OR layperson OR consumer) AND (safety OR unsafe OR harm OR "medical advice")), 2023-2026. NOT RUN, no access.
CINAHL: (MH "Natural Language Processing" OR TI (ChatGPT OR chatbot OR "large language model")) AND TI (patient OR layperson) AND TI (safety OR harm OR advice). NOT RUN, no access.
CENTRAL: ("large language model" OR ChatGPT OR chatbot) AND (patient OR layperson) AND (safety OR unsafe OR harm) in Title Abstract Keyword, 2023-2026. NOT RUN, no access.
Google Scholar: no full programmatic API. NOT RUN as a source.
OpenAIRE: NOT RUN; Europe PMC preprint coverage was the preprint route used.
