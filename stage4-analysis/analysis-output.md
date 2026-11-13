# Analysis output, Review 4 (run 2026-11-12)

Software: Python (scipy), random-effects GLMM, logit link, binomial likelihood, ML estimator,
adaptive Gauss-Hermite quadrature (15 nodes), as specified in analysis-plan.md. R and metafor are
not installed in this environment; analysis.R is a documented stub. Code: analysis.py.
Dataset: analysis-dataset.csv (built from stage3-extraction/extraction-settled.csv plus
stage3-extraction/chasing-secondary-settled.csv for the chasing secondary units).

## Primary pool P1 (bench stratum, unsafe tier)
95 model arms from 23 studies; 552 unsafe of 4,868 rated responses (crude 11.34%).
GLMM pooled proportion 10.52% (95% CI 9.24 to 11.96); tau2 0.304; I2 42.0%;
95% prediction interval 3.75 to 26.20%.
Hartung-Knapp inverse-variance sensitivity (DL estimator, logit scale): 12.51% (11.26 to 13.86).
The GLMM estimate sits below the inverse-variance estimate because the GLMM needs no continuity
correction for the zero-event arms (Wen 2026, 0/100 across five arms; Bilgic 2026, 0/75) and weights
large arms more heavily. Both are reported wherever the pooled figure is used.
Excluded from P1: Draelos 2026 Gemini arm (unsafe count in a figure only) and Ariel 2026
(per-arm catastrophic counts not printed; the study's printed pooled catastrophic count is
37/504, 7.3%, reported in the text, not pooled). No human-user study reported response-level
primary data, so P2 was not fitted.

## Sensitivities on P1 (GLMM pooled, 95% CI)
Excluding preprints (87 arms, 21 studies): 10.31% (8.93 to 11.89).
Excluding derived-count arms (61 arms, 15 studies): 10.03% (8.25 to 12.14).
Era-late arms only (88 arms, 21 studies): 10.20% (8.96 to 11.60).
Excluding high overall risk of bias (76 arms, 17 studies): 10.62% (9.29 to 12.12).
The pooled estimate is stable at 10.0 to 10.6% across all four sensitivities.

## Subgroups (pre-specified, max 3)
1. Bench vs human-user: bench fitted (P1). Human-user stratum had no response-level primary data;
   no interaction test is possible. Reported as a between-strata description only.
2. Red-flag/emergency vs non-urgent: the protocol defines this subgroup within studies that split
   responses by urgency. No primary-pool study printed unsafe counts split by urgency (Xiao 2026b
   splits undertriage counts, not unsafe counts), so no interaction test was fitted. Descriptive:
   the one pure emergency-department triage set (Fraser 2023) had 23/74 unsafe (31.1%); the remaining
   22 studies had 529/4,794 (11.0%) crude. This is a between-study contrast of one study against
   the rest and is not a subgroup finding.
3. Model era (release before vs on or after 13 May 2024): era-early arms pooled 24.33%
   (14.40 to 38.08) on 3 arms from 2 studies (Armbruster 2024 GPT-4; Fraser 2023 GPT-3.5 and GPT-4);
   era-late arms pooled 10.20% (8.96 to 11.60) on 88 arms. Interaction on the logit scale -1.03,
   p = 0.001. The early level rests on two studies from 2023-2024 whose question sets and rating
   rules differ from the later studies, so the interaction is reported as hypothesis-generating,
   not as evidence that newer models are safer.

## Secondary pools
S1 Problematic (intermediate or inaccurate tier): 38 units from 17 studies (23 units from the main
set plus 15 from citation chasing), 2,147/8,190 (crude 26.21%); GLMM pooled 18.69% (17.23 to 20.23);
tau2 1.052; I2 96.6%; prediction interval 2.78 to 64.84%. Main-set only: pooled 18.44%
(17.19 to 19.76). Heterogeneity is very high and the tier definitions differ between studies
(intermediate accuracy grades, combined error tiers, "not acceptable" judgements), so the pooled
figure is a summary of unlike measures and is interpreted only as showing that intermediate-tier
problems are roughly twice as common as explicit unsafe ratings.
S2 Undertriage: 12 units from 7 studies, 120/2,686 (crude 4.47%); GLMM pooled 14.57%
(11.87 to 17.75); tau2 4.963; I2 91.9%; prediction interval 0.12 to 96.09%. The pool mixes two
large zero-event slice units (Harada 2026, 0/480 and 0/1,440) with small high-rate units
(Ramaswamy 2026, 33/64; Gokmen 2026, 10/24; Fraser 2023, 23/74), so the random-effects mean is far
above the crude rate and the prediction interval covers almost the whole scale. The undertriage
result is reported study by study; the pooled mean is not a usable summary.
S3 Fabrication: no pool study reported response-level fabrication counts, so no pool was fitted.
Fabrication appears in the narrative set only (fabricated references and citations).

## Hand-checks (statistician checks required by the plan)
1. Independent refit of P1 by direct numerical integration of the marginal likelihood
   (trapezoid rule over the random effect, grid over tau, golden-section over mu; no shared code):
   pooled 10.55%, against 10.52% from the GLMM script. Agreement to 0.03 percentage points.
   The tau2 estimate differed between routes (0.20 by grid integration vs 0.304 by quadrature);
   the likelihood is flat in tau2 in this range and the pooled proportion is insensitive to it.
2. Crude totals re-summed from the settled extraction sheet for every pool: P1 552/4,868;
   S1 2,147/8,190 (main 1,875/7,286 + chasing 272/904); S2 120/2,686 (main 109/2,372 + chasing
   11/314). All match the analysis dataset.
