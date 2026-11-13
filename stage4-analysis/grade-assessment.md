# GRADE assessment, Review 4 (2026-11-12)

Starting point for every outcome below: Low certainty. The evidence is proportion evidence from
observational bench studies (and, for human-user decision outcomes, one field experiment),
which starts at Low in this series. No outcome is upgraded. Ratings follow the pressure points
named in grade-framework.md before results were seen (P1 definition heterogeneity, P2 risk of
bias, P3 inconsistency, P4 imprecision and indirectness).

## Outcome 1 (critical). Unsafe proportion, bench stratum (P1)
Pooled 10.52% (95% CI 9.24 to 11.96); 95 arms, 23 studies, 552/4,868; prediction interval
3.75 to 26.20%.
- Risk of bias (P2): downgrade 1. Six of the 24 primary studies are at high overall risk of
  bias on the adapted tool (unblinded raters in Miao 2026 and Gong 2026; edited responses and an
  appended physician-role prompt in Armbruster 2024; non-standardised prompting in Fraser 2023;
  pooled Llama versions and single-rater scoring in Draelos 2026; joint consensus scoring in
  Bilgic 2026). The sensitivity excluding high-risk studies gives 10.62%, close to the main
  estimate, which limits the damage but does not remove the concern.
- Inconsistency (P3): no further downgrade. I2 is 42.0% and tau2 is 0.304; the prediction
  interval (3.75 to 26.20%) is wide because question sets range from single-condition FAQ sets to
  emergency triage, a spread the subgroup and descriptive analyses partly explain.
- Indirectness (P1, P4): downgrade 1. Each study defines its own unsafe tier, and most question
  sets are investigator-written or forum-derived rather than questions patients typed into a
  chatbot in real use. The pooled figure describes rated responses to study question sets, not
  the rate at which patients meet unsafe answers in the wild.
- Imprecision: no downgrade. 4,868 rated responses; the confidence interval spans about
  3 percentage points.
- Publication bias: not formally assessed (no funnel-based test is valid for single-arm
  proportions of this kind in this series). The search covered preprint servers, which limits
  the risk; the OpenAlex full-text route was partial and is named in the limitations.
Certainty: VERY LOW (Low start, minus 1 risk of bias, minus 1 indirectness).

## Outcome 2 (critical). Unsafe proportion, human-user stratum (P2)
Not estimable. No human-user study reported response-level unsafe counts. The human-user
evidence reports decision outcomes instead (Bean 2026 randomised study; Si 2026 field
experiment, secondary pool). Certainty: no rating can be given for an outcome with no data;
the absence is itself a finding and is reported as such.

## Outcome 3 (important). Problematic proportion (S1)
Pooled 18.69% (17.23 to 20.23); 38 units, 17 studies, 2,147/8,190; prediction interval
2.78 to 64.84%.
- Risk of bias: downgrade 1 (same rating problems as Outcome 1, plus four secondary studies at
  high risk of bias, including Khan 2026 with undescribed classification of 5,000 responses).
- Inconsistency: downgrade 1. I2 96.6%; the prediction interval covers most of the plausible
  range, and tier definitions differ enough (intermediate accuracy grades, combined error
  tiers, "not acceptable" judgements) that the pooled mean summarises unlike measures (P1).
- Indirectness: counted inside the inconsistency downgrade to avoid double counting.
Certainty: VERY LOW.

## Outcome 4 (important). Undertriage proportion (S2)
Pooled 14.57% (11.87 to 17.75) with a prediction interval of 0.12 to 96.09%; 12 units,
7 studies, 120/2,686 (crude 4.47%).
- Risk of bias: downgrade 1 (Harada 2026, the largest contributor by responses, is at high risk
  of bias in the rating domain; its classification was mechanical against an author-set policy).
- Inconsistency: downgrade 1. I2 91.9%; the pool combines zero-event slices of thousands of
  responses with small emergency sets above 40%, so no single rate describes it.
Certainty: VERY LOW. The usable evidence is the study-level pattern, not the pooled mean.

## Outcome 5 (important). Fabrication proportion (S3)
Not estimable. No pool study reported response-level fabrication counts. Fabrication of
references and citations is documented in the narrative set only. No rating.

## Human-user decision outcomes (narrative, not pooled)
Bean 2026 (randomised, human-user): participant decision outcomes reported apart, per protocol.
Si 2026 (standardised-patient field experiment): inappropriate medication recommendations in
336/496 LLM encounters against 58/248 for primary care physicians, from derived counts
(printed percentages against a printed denominator). These outcomes start from their own
designs and are not combined with the bench proportions. Certainty for the direction of the
Si 2026 comparison is Low at best: one study, derived counts, high risk of bias in the rating
domain on the adapted tool.

---

## Revision 1 addendum (13 November 2026, Gate 4)

The GRADE judgements as printed in the revised manuscript (Table 3) are the version of record. Changes from the worksheet above, made under Reviewer 1 Major 3 and editorial item M22: (1) the primary outcome's definition heterogeneity (pressure point P1) is rated explicitly under the indirectness domain in the printed table, with the double-counting reasoning shown; (2) the primary outcome's inconsistency judgement is stated openly: no downgrade, with the wide prediction interval (4.5 to 22.7% at revision) reported wherever the estimate appears and the reasoning no longer resting on the era or Fraser contrasts; (3) the problematic tier's indirectness is named in both the inconsistency and indirectness columns of the printed table rather than folded silently into one downgrade; (4) a certainty statement for the human-user decision outcomes is printed (Low at best for the direction of the Si 2026 comparison; no rating for a pooled effect, since none was fitted). Certainty outcomes are unchanged: very low for the worst-tier, problematic and undertriage outcomes.
