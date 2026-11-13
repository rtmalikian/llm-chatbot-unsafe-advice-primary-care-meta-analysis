# Full-text notes — Review 4, batch 4 of 4 (part 4, 56 records)

Assessor pass date: 2026-11-12. Eligibility: stage0-protocol/protocol.md; reason hierarchy: stage2-screening/fulltext-rules.md (FT-R1–FT-R8, first applicable code).
Decisions file: fulltext-decisions-part4.csv (one row per record, list order).
Full texts saved to stage3-extraction/fulltexts/{record_id}.txt (plain text extracted from publisher PDF or Europe PMC XML; .xml also retained where Europe PMC supplied it).

## Retrieval method and routes

Route 1 for every record: Europe PMC search (by PMID where present, else DOI) followed by Europe PMC fullTextXML for any PMCID/PMID found.
Route 2: OpenAlex best/alternate OA location PDF. Route 3 where applicable: direct publisher/preprint PDF from the record URL, medRxiv PDF, or Unpaywall best OA PDF.
Second-attempt routes for first-pass failures: Research Square PDF (R2687, success), BMC/Springer article page and browser fetch (R2875, abstract-level publisher text retrieved), medRxiv second PDF URL (R2714, success after first URL returned a bot-challenge page, which was replaced), Zenodo API record (R3078, R3079 — records retrieved; they are dataset/supplementary deposits only), JMIR Preprints and SSRN pages (R3082, R3080, no downloadable text).
No paywall workarounds were used. Records coded NOT_RETRIEVED (FT-R8) each had at least two routes tried; routes are logged per record in the CSV notes.
One retrieved file was discarded: R3035's publisher direct fetch returned only a bot-challenge page, not the article, so the record is NOT_RETRIEVED and no file is saved for it.

Saved full texts: 46 of 56 records (every record not coded NOT_RETRIEVED has a .txt in fulltexts/; R3078 and R3079 files are the retrieved Zenodo record metadata documenting the deposits).

## Counts per decision (from the CSV)

- INCLUDE_PRIMARY: 4 — R2861, R2908, R2915, R3023
- INCLUDE_SECONDARY: 2 — R2916, R3040
- INCLUDE_NARRATIVE: 7 — R2688, R2757, R2875, R2882, R2947, R2992, R3045
- EXCLUDE: 33 — FT-R1 ×4 (R2747, R2962, R3078, R3079), FT-R3 ×2 (R2775, R2993), FT-R4 ×1 (R2684), FT-R5 ×11 (R2687, R2699, R2714, R2733, R2810, R2927, R2957, R2979, R2981, R3015, R3041), FT-R6 ×1 (R2812, duplicate of R2769), FT-R7 ×14 (R2758, R2769, R2782, R2803, R2805, R2821, R2825, R2828, R2833, R2852, R2884, R3011, R3012, R3033)
- NOT_RETRIEVED: 10 — FT-R8 (R2888, R3021, R3025, R3034, R3035, R3050, R3060, R3080, R3082, R3086)

## Included studies — counts as printed (decision pass, not formal extraction)

### Primary pool
- R2861 (vegetarian/vegan nutrition, bench): 58 questions × 5 models (ChatGPT, Gemini, Copilot, DeepSeek, Doubao) = 290 responses; binary safe vs potentially unsafe, majority of 5 blinded raters. Potentially unsafe 47/290 total (Results/Discussion). Per-model percentages in Figure 2; exact per-arm counts to confirm from figure/supplement.
- R2908 (postoperative pain education, bench): 51 questions × 7 interfaces = 357 responses; binary Safe/Unsafe. Unsafe 11/357 (3.08%). Per-arm unsafe derived from printed safe rates per 51 (ChatGPT 1, Gemini 0, Copilot 1, DeepSeek 3, Doubao 2, Perplexity 2, Claude 2; sums to 11) — flagged derived; verify against Supplementary Table S4.
- R2915 (osteoporotic vertebral compression fractures, bench): 36 questions × 4 chatbots, round 1. Potentially unsafe per arm as printed: ChatGPT 3/36, DeepSeek 5/36, Gemini 6/36, Doubao 7/36; total 21/144. Second round (144 further responses) was for stability only.
- R3023 (diabetic kidney disease, bench): 42 questions × 6 LLMs (ChatGPT, Gemini, DeepSeek, Doubao, Kimi, Qwen) = 252 responses; binary safe vs potentially unsafe, majority of 5 raters. Potentially unsafe 30/252 (11.9%); per-model range 3–7 in text, exact per-arm counts in Supplementary Material S7.

### Secondary pool (problematic)
- R2916 (Ramadan diabetes medication, bench): 276 responses (23 prompts × 3 chatbots × 2 languages × 2 days). Problematic tier (accuracy score 0 = guideline-conflicting or clinically unsafe) 30/276 (11%), Figure 1/Results. No pure primary unsafe tier (separate safety scale reported as medians only).
- R3040 (antibiotic advice for viral vignettes, bench): 5,000 model-vignette evaluations as printed (1,000 vignettes × 5 models). Problematic: 1,191 inappropriate antibiotic recommendations (Results; 767 WHO Access, 424 Watch). Denominator for the 1,191 to be verified against tables at extraction — flagged in CSV.

### Narrative only (eligible, nothing poolable)
- R2688: ChatGPT simulated patients, 27 trials; unnecessary-or-harmful medication suggestions 23/27 (combined outcome, not a response unsafe tier).
- R2757: GPT-4o medication recognition/education, 20 medications, 4-point accuracy scale; text states none labelled incorrect or directly harmful, no formal unsafe tier.
- R2875: appendicitis, 540 responses, explicit major-harm tier reported only as category percentages in retrieved publisher text (H_any/H_maj); no numerator printed — coordinator should check version-of-record tables.
- R2882: sexual health, 360 responses, potentially harmful tier reported only as per-arm percentages (7.1%, 9.3%, 11.5% of 120) that do not back-convert to integer counts (Table 2).
- R2947: 212 lay-prompted responses, physician Harm scale (harmful = score ≥3) but no harmful count printed.
- R2992: human-user triage experiment (49 lay participants); participant decision outcomes only, responses not clinician-rated.
- R3045: heart failure/cardiomyopathy, 50 questions × 6 models, appropriateness ratings; potentially harmful failure type described qualitatively, no count.

## Duplicates
- R2812 (Research Square preprint) is a duplicate report of R2769 (Journal of Medical Systems version of the same BLS/PALS lay-rescuer study): R2812 excluded FT-R6, R2769 retained (itself excluded FT-R7 on outcome grounds).

## Flags for the coordinator
- R2875 and R2882 may hold primary-pool counts in tables/supplements not present in the legitimately retrieved text; both are coded narrative on the retrieved text only.
- R2908 per-arm counts are derived from printed safe-response percentages plus the printed total (11) and need verification against Supplementary Table S4.
- R3040's secondary denominator needs table verification before pooling (two-step prompting design).
- Several 2026-dated records report models accessed in late 2025/2026 (e.g. R2875 GPT-5.2/Gemini 3 Flash, queries Dec 2025–Jan 2026); eligibility window is 2023–2026 per protocol, so retained.
