# Full-text assessment notes — Review 4, batch 1 of 4 (part 1, 171 records)

Assessor pass date: 2026-11-12 (PT). Decisions: `stage3-extraction/fulltext-decisions-part1.csv` (one row per record, list order). Eligibility: `stage0-protocol/protocol.md`; full-text hierarchy: `stage2-screening/fulltext-rules.md` (FT-R1 to FT-R8). This is a decision pass, not the formal extraction; counts in the CSV notes are as printed in the retrieved full texts (or, where marked, in gate-stage full-text checks) and are flagged for the extractors to re-verify against tables.

## Decision counts (from the CSV)

| Decision | n |
|---|---|
| INCLUDE_PRIMARY | 13 |
| INCLUDE_SECONDARY | 1 |
| INCLUDE_NARRATIVE | 15 |
| EXCLUDE | 93 |
| NOT_RETRIEVED (FT-R8) | 49 |
| **Total** | **171** |

Exclusions by first applicable code: FT-R5 specialty-only 65; FT-R7 no poolable outcome 12; FT-R4 not patient-facing 8; FT-R1 not a primary study 3; FT-R2 no general-purpose LLM / clinician in loop 3; FT-R3 clinician-facing task 2; FT-R6 duplicates 0 (no duplicate PMID or normalised title exists inside this batch; duplicates named at gate stage pair part-1 records with records in other batches, e.g. R0211/R2099, and were not coded FT-R6 here).

Full texts saved: **122** files in `stage3-extraction/fulltexts/` for part-1 records (121 via the scripted routes + R0017 via publisher OA page; R0205 via publisher OA PDF — see QA notes).

## Retrieval method

Legitimate routes only; no paywall workarounds. Per record, in order: (A) Europe PMC `fullTextXML` by PMID (task-specified pattern — returned HTTP 500 for every record, because that endpoint keys on PMCID, not PMID); (B) Europe PMC `fullTextXML` by the article's own PMCID taken from PubMed's `PubmedData/ArticleIdList`; (C) Europe PMC search (by PMID, then by DOI) with identity-verified PMCID/OA-URL follow-up; (D) Unpaywall best OA location for the PubMed DOI and the search-file DOI; (E) PMC HTML for a verified PMCID; (F) DOI resolution for known OA publishers/preprint servers. Every candidate full text had to pass a title-token verification against the record title before saving. All 49 not-retrieved records additionally had a batch NCBI IDConv check (PMID→PMCID), and three (R0017, R0048, R0188) had PubMed-page checks; R0017 was rescued through the publisher OA page (JMIR). Each not-retrieved record therefore has at least four logged route attempts — well above the two-route minimum in FT-R8. Per-route detail is in the retrieval log table at the end of this file and in the CSV notes.

**FT-R8 convention applied:** a record whose full text was not retrieved is coded NOT_RETRIEVED / FT-R8 even where the abstract strongly suggests a content code, per the FT-R8 text ("counted as not retrieved, never as excluded on content"). The CSV note for every such record preserves the abstract-level provisional signal (provisional decision + code + reasoning) so the coordinator can recheck the record if the text is later obtained, and can reclassify without redoing the abstract work. 7 of the 49 are provisionally includable (R0048 and R0188 primary; R0530 secondary; R0009, R0370, R0582 narrative; plus R0019-type scope exclusions dominate the rest) — see the flags section.

**Identifier warning:** the search-file DOIs are unreliable — for most records the DOI in `search-results.csv` / the part-1 list does not match the article (e.g. R0001 lists 10.1007/s11606-024-09200-z; the article's DOI per PubMed is 10.3389/fpubh.2026.1985180). All retrieval keyed on PMID and on PubMed's own DOI/PMCID; the CSV notes use PubMed-verified identifiers where they matter. Do not cite search-file DOIs downstream without checking PubMed.

## QA incidents (both caught by title verification, both fixed)

1. **Pilot ID-parsing bug.** The first pilot script read `ArticleId` elements from anywhere in the PubMed XML, including reference lists, and saved 3 wrong articles (R0001, R0211, R0215). Title verification caught all three; the files were deleted, identifier parsing was restricted to the article's own `ArticleIdList`, a title-overlap gate (≥0.45 plus a distinctive-token check) was added, and the whole batch was rerun. Final QA over all 122 saved files: every file contains the record's distinctive title tokens.
2. **R0205 wrong-DOI save.** The search-file DOI for R0205 (10.1371/journal.pone.0328230) belongs to a different article (an osteoporosis decision-aids scoping review); a PLOS page fetched under that DOI passed a generic token check. The distinctive-token QA flagged it ("OsteoCHAT" absent). It was replaced with text extracted from the publisher OA PDF for the correct PubMed DOI (10.1007/s00198-026-08247-4, Osteoporosis International, © The Author(s) 2026), and the decision (FT-R2) was re-verified against the true text.
3. **R0017 partial save.** JMIR's site is behind an AWS WAF that returns HTTP 202 to scripted clients; the full text was retrieved and read in full (940 lines) through the publisher OA page via the DOI, and `R0017.txt` preserves the abstract, safety definition, and safety results (incl. Table 2) verbatim as fetched, with a retrieval header explaining this. The article has no PMCID yet. Counts in the CSV note are from that full text.

## Included for the primary pool (13) — unsafe numerator/denominator as printed

All bench stratum. Per-arm detail is in each CSV note.

- **R0017** COPD (JMIR): 27/330 — ChatGPT 4/55, Gemini 4/55, Copilot 4/55, DeepSeek 4/55, Qwen 5/55, Doubao 6/55 (Table 2; safety 0=safe/1=unsafe, ≥3/5 raters).
- **R0068** Depression/anxiety support in chronic illness: major clinical/safety errors, Round 1 ChatGPT 0/20, Gemini 2/20, Doubao 3/20 (120 responses over 2 rounds; round-2 counts in the same full-text table).
- **R0211** Bacterial vaginosis: 31/305 — 4, 6, 5, 7, 9 per 61 (ChatGPT, Gemini, Copilot, DeepSeek, Doubao; Table 1). Gate-verified.
- **R0215** Herpes zoster: 66/230 — 11, 12, 15, 14, 14 per 46 (ChatGPT-5.5 Instant, DeepSeek-V4-Pro, Doubao-Seed-2.0-Pro, Gemini 3.5 Flash, Qwen3.7-Plus; Table 1). Gate-verified.
- **R0216** Diabetes foot-ulcer prevention: 0/100 primary outputs (0/40 repeat outputs; grades 2–3 = major safety error tier).
- **R0234** Late-life depression: 29/270 — ChatGPT 5/90, Gemini 9/90, Doubao 15/90 (major safety error). Included per the gate-stage coordinator adjudication that this question set (medication, delirium, falls, triage — not crisis-only) is in primary-care scope; extractors should keep any crisis-specific items separable.
- **R0247** Paediatric vitamin D deficiency: 20/220 total (44 questions × 5 chatbots); per-arm counts in full-text table.
- **R0269** Painful diabetic peripheral neuropathy: 28/300 total; per-arm only as range/figure per gate.
- **R0284** TBI/concussion: 27/325 total; per-arm endpoints only in text per gate.
- **R0299** Mpox: 31/312 — per-arm 4, 5, 6, 5, 4, 7 per 52 derived at gate from printed safe counts. Gate-verified.
- **R0362** Hand, foot and mouth disease: 10/100 — 1, 2, 2, 2, 3 per 20 (Table 1). Gate-verified.
- **R0392** Vegetarian/vegan nutrition: 47/290 — 7, 12, 8, 6, 14 per 58. Gate-verified.
- **R0401** High-risk HPV follow-up: 10/90 — ChatGPT 3/45, DeepSeek-V3 7/45 (potential-harm outcome, Table 4). Gate-verified.

Primary-pool totals in this batch (as printed, before formal extraction): **331 unsafe of 2,932 responses** across the 13 studies (R0068 counted on its round-1 denominator of 60; extractors to settle round handling — see flag 5). Models covered in this batch's primary pool: ChatGPT/GPT series, Gemini, Microsoft Copilot, DeepSeek, Doubao, Qwen (Claude appears only in narrative/secondary records in this batch).

## Included for a secondary pool (1)

- **R0822** Lay self-triage, Japanese vignettes, gpt-4o-mini: undertriage pool. Hard under-triage vs the reference action range: red-flag slice ≈100% across prompts/decoding conditions (99.7–100.0%), 0% in mild/non-red-flag slices; gate full-text check counted 3,342 outputs in the red-flag analysis. Per-slice numerators/denominators are in the full-text tables for extraction. No explicit unsafe tier, so not primary.

## Included as narrative (15)

R0038 (gestational diabetes, Likert safety), R0053 (postpartum, stage scale scores; stage 3 clinician-facing — flagged), R0087 (nasal polyps, rubric safety; rating-level lowest scores 7/162 involving 3/27 responses), R0265 (acne appropriateness), R0270 (Ramadan diabetes; harmful-or-contradictory 30/276 not separable — gate-listed, not pooled), R0300 (STI, 5-point safety), R0327 (falls, 10 questions), R0381 (low back pain; serious errors inseparable from composite grade), R0524 (haemorrhoids, 5-point safety), R0525 (paediatric queries, safety composite score threshold — full corpus not clinician-rated), R0667 (psoriasis, safety score /8), R0714 (general paediatric advice, qualitative zero-unsafe), R0717 (pertussis, qualitative no-harm over 100 responses), R0720 (scabies; hallucination outcome is citation-level), R0748 (smoking cessation, accuracy rubric).

## Flags for the coordinator / author

1. **Provisionally includable but not retrieved (recheck first if texts are obtained):** R0048 (ED information; abstract: 26/228 safety-flagged, 6 interfaces — publisher returned 403), R0188 (altered consciousness; abstract: 330 responses, safe rates 89.4–95.5% — Elsevier paywall; gate stage also could not retrieve counts), R0530 (nipple discharge; abstract: combined misleading/unsafe 8/216 — secondary problematic; Elsevier paywall), R0009 (skincare myths — narrative signal), R0370 (diabetic foot ulcer — narrative signal), R0582 (heavy menstrual bleeding — narrative signal).
2. **R0335 embargo:** a PMCID exists (PMC13532023) but IDConv reports it embargoed until 2027-03-29; the record is coded FT-R8 with a provisional FT-R5 signal.
3. **Scope precedents followed:** gate-stage scope calls were not overturned (e.g. R0019 adenomyosis, R0308 IC/BPS, R0219 achalasia = FT-R5 even with printed unsafe counts; R0234 late-life depression = included per the gate adjudication). Dental/orthodontic/periodontal sets were coded FT-R5 throughout, consistent with gate. Cancer-education sets were coded FT-R5, consistent with gate (breast/bladder), except cervical-screening follow-up (R0401) and sexual-health (R0300) topics, which the gate treated as primary-care.
4. **Borderline calls to double-check at adjudication:** R0024 (regenerative ED therapies — FT-R5 over FT-R7), R0025 (paediatric epilepsy — FT-R5 despite printed critical-flag counts 11/40), R0339 (acute pancreatitis — FT-R5; full text has hallucinations 16/120 and low-risk safety signals 7/120), R0368 (vascular/perioperative — FT-R5; 0/110 high clinical-risk flags), R0399 (inhaler technique — FT-R7 over narrative; step-level errors, safety-warning scores), R0435 (OB/GYN triage — FT-R5; score outcomes), R0525 (safety composite — narrative over secondary; corpus scored by a validated composite, not clinician-rated per response), R0530 (combined misleading/unsafe tier coded secondary-problematic, not primary, because all 8 events were classified misleading and 0 unsafe — moot unless retrieved).
5. **R0068 round handling:** the primary numerator/denominator in the CSV note uses round 1 (5/60); the study ran 2 rounds (120 responses). Extractors should prespecify whether round 2 enters as separate arms or a sensitivity set, consistently with R0017 (round 2 = retest sensitivity, excluded from the primary denominator there).
6. **Duplicate reports across batches (not FT-R6 within this batch):** gate stage linked R0211↔R2099, R0269↔R2108, R0308↔R2105, R0362↔R2116, R0699↔R2209, R0722↔R2126, R0343↔R2139, R0234↔R2204 (same study as the gate-counted late-life depression study). The coordinator should confirm the retained record per study across batches before analysis so no study is double-counted.

## Retrieval log (per record)

| record_id | saved file | routes attempted (status) |
|---|---|---|
| R0001 | R0001.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0003 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [404]; IDConv batch [no live PMCID] |
| R0009 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0017 | R0017.txt | A EPMC-by-PMID [500]; C EPMC search x2 [200, no OA full text]; D Unpaywall [200, doi.org only]; F doi.org via urllib [202 WAF]; RESCUE browser fetch of publisher OA page via DOI [200, 940 lines] |
| R0019 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; D_unpaywall_oa_fetch [403]; D_unpaywall_oa_fetch [403]; IDConv batch [no live PMCID] |
| R0024 | R0024.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0025 | R0025.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0026 | R0026.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0028 | R0028.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0038 | R0038.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0044 | R0044.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0046 | R0046.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0048 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0052 | R0052.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0053 | R0053.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0068 | R0068.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0074 | R0074.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0077 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0087 | R0087.txt | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; D_unpaywall_oa_fetch [403]; D_unpaywall_oa_fetch [None]; E_pmc_html [200] |
| R0092 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; F_doi_oa_publisher [202]; IDConv batch [no live PMCID] |
| R0115 | R0115.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0122 | R0122.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0132 | R0132.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0139 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; D_unpaywall_oa_fetch [403]; D_unpaywall_oa_fetch [403]; IDConv batch [no live PMCID] |
| R0145 | R0145.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0148 | R0148.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0151 | R0151.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0187 | R0187.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0188 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0193 | R0193.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0196 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0198 | R0198.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0205 | R0205.txt | A [500]; C x2 [200]; D Unpaywall x2 [200, Springer PDF located]; F PLOS page via wrong search-file DOI [200, WRONG ARTICLE - replaced]; publisher OA PDF for PubMed DOI 10.1007/s00198-026-08247-4 [200, pdftotext] |
| R0207 | R0207.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0211 | R0211.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0215 | R0215.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0216 | R0216.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0219 | R0219.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0234 | R0234.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0240 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; D_unpaywall_oa_fetch [403]; D_unpaywall_oa_fetch [403]; IDConv batch [no live PMCID] |
| R0242 | R0242.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0245 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; D_unpaywall_oa_fetch [403]; D_unpaywall_oa_fetch [403]; IDConv batch [no live PMCID] |
| R0247 | R0247.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0248 | R0248.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0253 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0265 | R0265.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0269 | R0269.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0270 | R0270.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0274 | R0274.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0275 | R0275.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0284 | R0284.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0288 | R0288.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0297 | R0297.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0299 | R0299.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0300 | R0300.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0302 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0305 | R0305.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0308 | R0308.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0309 | R0309.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0318 | R0318.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0327 | R0327.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0329 | R0329.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0333 | R0333.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0335 | - | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; D_unpaywall_oa_fetch [403]; D_unpaywall_lookup [200]; D_unpaywall_oa_fetch [200]; D_unpaywall_oa_fetch [200]; E_pmc_html [403]; IDConv batch [no live PMCID] |
| R0339 | R0339.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0343 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0346 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [404]; IDConv batch [no live PMCID] |
| R0353 | R0353.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0354 | R0354.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0356 | R0356.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0358 | R0358.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0362 | R0362.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0364 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; D_unpaywall_lookup [200]; D_unpaywall_oa_fetch [200]; D_unpaywall_oa_fetch [200]; F_doi_oa_publisher [403]; IDConv batch [no live PMCID] |
| R0365 | - | A_epmc_fulltext_by_pmid [None]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0368 | R0368.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0370 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0373 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0377 | R0377.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0378 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0381 | R0381.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0392 | R0392.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0394 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0396 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0399 | R0399.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0401 | R0401.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0419 | R0419.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0422 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0423 | R0423.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0425 | R0425.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0430 | R0430.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0435 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0439 | R0439.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0447 | R0447.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0454 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; D_unpaywall_oa_fetch [403]; D_unpaywall_oa_fetch [403]; IDConv batch [no live PMCID] |
| R0463 | R0463.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0474 | R0474.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0501 | R0501.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0502 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; D_unpaywall_oa_fetch [200]; D_unpaywall_oa_fetch [200]; IDConv batch [no live PMCID] |
| R0510 | R0510.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0515 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0517 | R0517.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0518 | R0518.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0524 | R0524.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0525 | R0525.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0529 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0530 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0531 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; D_unpaywall_lookup [200]; F_doi_oa_publisher [202]; IDConv batch [no live PMCID] |
| R0534 | R0534.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0535 | R0535.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0545 | R0545.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0552 | - | A_epmc_fulltext_by_pmid [None]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0554 | - | A_epmc_fulltext_by_pmid [None]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0563 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0564 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0569 | R0569.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0579 | R0579.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0580 | R0580.txt | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [500]; C_epmc_search_pmid [200]; C_epmc_oa_url [403]; C_epmc_oa_url [403]; C_epmc_oa_url [200]; C_epmc_search_doi [200]; C_epmc_oa_url [403]; C_epmc_oa_url [403]; C_epmc_oa_url [200]; D_unpaywall_lookup [200]; E_pmc_html [200] |
| R0582 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0586 | R0586.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0592 | R0592.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0597 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0606 | R0606.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0618 | R0618.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0623 | R0623.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0636 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0642 | R0642.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0643 | R0643.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0646 | R0646.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0648 | R0648.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0651 | R0651.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0653 | R0653.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0655 | R0655.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0656 | R0656.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0663 | R0663.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0667 | R0667.txt | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [500]; C_epmc_search_pmid [200]; C_epmc_oa_url [403]; C_epmc_oa_url [403]; C_epmc_oa_url [403]; C_epmc_search_doi [200]; C_epmc_oa_url [403]; C_epmc_oa_url [None]; C_epmc_oa_url [None]; D_unpaywall_lookup [200]; D_unpaywall_oa_fetch [200]; D_unpaywall_oa_fetch [200]; D_unpaywall_lookup [200]; D_unpaywall_oa_fetch [200]; D_unpaywall_oa_fetch [200]; E_pmc_html [200] |
| R0670 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0673 | R0673.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0684 | R0684.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0688 | R0688.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0692 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0696 | R0696.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0699 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; D_unpaywall_lookup [200]; D_unpaywall_oa_fetch [200]; D_unpaywall_oa_fetch [200]; IDConv batch [no live PMCID] |
| R0705 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0709 | R0709.txt | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [500]; C_epmc_search_pmid [200]; C_epmc_oa_url [403]; C_epmc_oa_url [403]; C_epmc_oa_url [200]; C_epmc_search_doi [200]; C_epmc_oa_url [403]; C_epmc_oa_url [None]; C_epmc_oa_url [200]; D_unpaywall_lookup [200]; D_unpaywall_oa_fetch [200]; D_unpaywall_oa_fetch [200]; E_pmc_html [200] |
| R0710 | R0710.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0714 | R0714.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0717 | R0717.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0718 | R0718.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0720 | R0720.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0722 | R0722.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0726 | R0726.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0746 | R0746.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0748 | R0748.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0754 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0759 | R0759.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0769 | R0769.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0775 | R0775.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0780 | R0780.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0789 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0792 | R0792.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0797 | R0797.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0802 | R0802.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0803 | R0803.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0805 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0813 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0819 | R0819.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0822 | R0822.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |
| R0839 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0842 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0843 | - | A_epmc_fulltext_by_pmid [500]; C_epmc_search_pmid [200]; C_epmc_search_doi [200]; D_unpaywall_lookup [200]; D_unpaywall_lookup [200]; IDConv batch [no live PMCID] |
| R0854 | R0854.xml | A_epmc_fulltext_by_pmid [500]; B_epmc_fulltext_by_pmcid [200] |