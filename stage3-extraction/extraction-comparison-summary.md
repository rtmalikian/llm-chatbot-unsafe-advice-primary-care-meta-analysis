# Extraction A vs B comparison (coordinator, by code, 2026-11-12)

Files compared: extraction-A-half1.csv (74 rows) + extraction-A-half2.csv (63 rows) = 137 A rows;
extraction-B-half1.csv (74 rows) + extraction-B-half2.csv (65 rows) = 139 B rows.
B-half2 splits fields 18/19 into numerator/denominator columns; the other three files use combined "n/n" columns.
Comparison normalised the combined/split formats before matching.

Row-count difference: only R0822 (A 1 row for the whole study, denominator 3,342; B 3 presentation-slice rows).
Arm matching: 114 arm pairs matched on record_id + normalised model name. A further 47 model-name
variants are the SAME arms under different naming (e.g. A "Microsoft Copilot" vs B "Copilot";
A "ChatGPT" vs B "ChatGPT 5.5" in R0247/R2134/R0234; A "Gemini (default)" vs B "Gemini (default free tier)" in R2219)
and must be aligned by the settlement reader, not treated as different arms.

Field discrepancy rates among the 114 matched pairs (any string difference, including coding-convention differences):
- n_responses_rated_safety: 29/114 differ. Almost all are secondary-pool studies where B left the safety
  denominator "not_reported" and carried the denominator in notes/other fields, while A entered it
  (R0916 54, R1090 10, R1229 233, R1519 55, R2219 45, R2244 248, R2254 140, R2307 480, R2468 80 vs B 24?, R3040 1000).
  Settlement rule: the denominator of the outcome actually rated goes in the denominator field for that outcome.
- n_unsafe: 11/114 differ. Substantive conflicts needing re-reading:
  * R0269: A has DeepSeek 7, Gemini 5, Copilot 4; B has not_reported (B derived only ChatGPT 3 and Doubao 9 from printed %).
  * R0284: A has DeepSeek 5, Doubao 6, Gemini 6; B has not_reported (B derived only ChatGPT 3, Copilot 7).
  * R3023: A has not_reported for all 6 arms (A: exact per-model counts only in Supplementary S7, not retrieved;
    pooled 30/252 verified); B derived per-model unsafe 3/6/4/7/5/5 as complements of per-model safe counts
    it reports in section 3.2 of the main text. Settlement MUST re-read R3023's full text and decide which is right.
  * R2134, R2101, R2120, R2252, R2361, R2104, R0017 and the gate-verified totals agree between A and B.
- n_problematic / n_rated_problematic: 5/114 each. R0401 (A counts 3 and 7 for two arms, B not_reported),
  R2361 (B counts 0/1/4 for the separate "Incorrect" tier, A not_reported). Settlement: record the
  problematic-tier count as each paper defines its intermediate tier, flagged in notes.
- n_undertriage numerator: 4/114 (R0822 structure; R2219 0 vs not_reported coding).
  Denominator fields (ut_d 47/114, fb_d 52/114) differ mostly by convention (blank vs not_reported vs a number).
  Settlement standard: use the printed denominator for that outcome, or "not_reported" - never blank.
- model_era: 2/114 differ. stratum: 0/114. comparator_flag: 60/114 string-differ, a coding-format
  difference (blank vs NO vs text) - settlement standard: YES for comparator rows, NO otherwise.
- n_questions: 17/114 differ, mostly wording (e.g. "15" vs "15 unique questions x 3 generations" in R0401).

Overall: the two extractions agree on every gate-verified study total. All discrepancies above go to the
settlement reader, who re-reads the source full text for every numeric conflict and produces
extraction-settled.csv. No discrepancy is settled by averaging or by preferring one extractor.
