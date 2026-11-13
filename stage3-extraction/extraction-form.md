# Extraction form, piloted version 1, 2026-11-12

Specified before extraction. One row per arm. An arm is one model (with version and evaluation date where given) in one stratum, split further by presentation type only where the study reports the primary outcome that way.
Coding: a field the paper does not report is coded not_reported. A number is extracted only as printed or as a count directly verified by arithmetic from printed counts (the arithmetic is recorded in notes). No derived percentage is back-converted to a count unless both the percentage and its denominator are printed and the product is an integer within rounding; such cases are flagged derived and checked at settlement.

## Fields
1. record_id: search record ID, or CC ID for chasing records.
2. study_id: first author, year.
3. stratum: bench or human_user.
4. design: bench_evaluation, rct, quasi_experimental, other (specify in notes).
5. country_setting: as reported.
6. question_source: real patient questions, adapted patient questions, clinician-written vignettes in patient voice, scenarios, other.
7. presentation_scope: general primary care, mixed primary care topics, single condition that presents in primary care, mixed incl specialty (flag).
8. red_flag_split: whether the study splits responses into red-flag or emergency versus non-urgent sets (yes or no), with the split counts in fields 18 and 19 where given.
9. n_questions: number of questions or scenarios put to the model.
10. model_name: as printed.
11. model_version_date: version and access dates as printed.
12. model_era: gpt35_era, gpt4_era_plus, other_family (Claude, Gemini, Llama, and others are coded by release era of the version tested: pre-GPT-4o era models in era1 only if the tested version predates May 2024; the coding rule is: era is assigned by the model's release date, before 2024-05-13 is era_early, on or after is era_late; GPT-3.5 is always era_early; this field is also tabulated by family in a sensitivity table).
13. n_responses_rated_safety: total responses rated for safety in this arm (primary denominator).
14. n_unsafe: responses in the explicit unsafe, harmful, or dangerous tier (primary numerator).
15. unsafe_tier_label: the study's own label, verbatim.
16. n_problematic: responses in a combined problematic or inaccurate tier, where reported, with its denominator in field 17 if it differs.
17. n_rated_problematic: denominator for field 16.
18. n_undertriage / n_with_disposition: responses advising a lower disposition than reference, over responses with a reference disposition.
19. n_fabrication / n_rated_fabrication: responses with at least one fabricated medical fact, over responses rated for fabrication.
20. raters: number, profession, blinding as reported.
21. rating_scale: the full tier structure as printed.
22. human_user_outcomes: for human-user studies only, the decision outcome as printed (for example correct condition identification in participants using the model), with numerator and denominator.
23. funding_conflicts: as reported.
24. notes: page or table locations for every count, derivation flags, and any ambiguity carried to settlement.

## Pilot
The first five included studies are extracted by both extractors as the pilot. Any form change after the pilot is versioned here with its date, and the pilot studies are rechecked on the changed fields.
