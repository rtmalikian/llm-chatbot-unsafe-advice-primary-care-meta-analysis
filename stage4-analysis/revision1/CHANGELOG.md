# Re-analysis changelog, Review 4, peer-review revision 1 (2026-11-13)

Analysis round: peer-review revision 1. Code: analysis-revision1.py in this
folder. Outputs: revision1-results.json. Inputs are unchanged:
stage4-analysis/analysis-dataset.csv, built from the settled extraction
sheet. No settled extraction count was changed by this round. Every
discrepancy found is recorded here, not silently fixed.

## Why this round exists

Reviewer 2 (Blocker 1) showed that the printed confidence intervals for the
two heterogeneous secondary pools are mathematically impossible given the
paper's own tau squared and unit counts: for a random-effects mean on the
logit scale, SE(mu) is at least sqrt(tau2/k). The problematic pool implied
SE 0.050 against a floor of 0.166; the undertriage pool implied SE 0.120
against a floor of 0.643. The fault sits in analysis.py: the standard errors
come from a finite-difference Hessian (step 1e-4) taken at a Nelder-Mead
optimum of a non-adaptive quadrature objective and inverted with a
pseudo-inverse. The quadrature itself was also misdescribed: the code places
fixed Gauss-Hermite nodes around the fixed effect. It performs no per-unit
posterior mode or scale adaptation, although the manuscript, the analysis
plan and the code comment all say "adaptive Gauss-Hermite quadrature
(15 nodes)".

## What the revision code does

The marginal likelihood is maximised with adaptive Gauss-Hermite quadrature
(31 nodes; per-unit Laplace mode and scale), seeded from a profile grid over
tau and refined by Nelder-Mead. Standard errors come from the observed
information with central differences (step 0.01 on mu, 0.02 on log tau) and
are checked at half step; the two agree to four decimals on every reported
fit. Every interval is validated against the sqrt(tau2/k) floor before it is
reported. Hartung-Knapp inverse-variance logit fits (DerSimonian-Laird tau
squared; the 0.5 correction is applied to all arms, exactly as coded in
analysis.py) are reported for every pool and sensitivity with at least four
units, as the Methods promised. I squared is labelled for what it is: a
fixed-effect Q statistic computed on 0.5-corrected logits, not a product of
the GLMM.

## Results, old against new

Primary pool P1 (95 arms, 23 studies, 552 of 4,868, crude 11.3%):
- GLMM pooled: 10.52% before, 10.53% now. The point estimate does not move.
- GLMM 95% CI: 9.24 to 11.96 before; 9.29 to 11.92 now. Passes the floor
  check (SE 0.071 against floor 0.047).
- Tau squared: 0.304 before; 0.207 now. The revision value agrees with the
  filed independent refit by direct numerical integration (0.20), which the
  original output reported only for the point estimate. The original
  quadrature overstated tau squared by about a third; the pooled proportion
  is insensitive to it, the prediction interval is not.
- Prediction interval: 3.75 to 26.20% before; 4.51 to 22.70% now.
- Hartung-Knapp: 12.51% (11.26 to 13.86), unchanged; DerSimonian-Laird tau
  squared 0.137, now reported beside the GLMM tau squared.
- Study-level sensitivity (new; one aggregated value per study, 23 units):
  Hartung-Knapp 11.66% (9.34 to 14.46); GLMM on the aggregated values 10.32%
  (8.15 to 12.99). Reviewer 2's independent check gave 11.7% (9.3 to 14.5).
  It is reproduced.

Primary sensitivities (GLMM now; Hartung-Knapp in brackets, all previously
computed but withheld from the manuscript):
- Excluding preprints (87 arms): 10.34% (9.02 to 11.82) [12.36%].
- Excluding derived-count arms (61 arms, 306 of 2,621): 10.11% (8.35 to
  12.20), tau squared 0.339, prediction interval 3.33 to 26.88% [12.69%].
- Era-classified late arms only (88 arms; 4 unclassified arms excluded):
  10.23% (9.02 to 11.59) [12.18%].
- Excluding high risk of bias studies (76 arms): 10.63% (9.30 to 12.12)
  [12.54%].
The GLMM sensitivity range is 10.1 to 10.6%; the Hartung-Knapp range is
12.2 to 12.7%. Both ranges are reported wherever stability is claimed.

Strict-tier sensitivity (new; Blocker B-A). Arms whose settled tier label is
explicitly unsafe with no qualifier (the labels "unsafe" or "Unsafe" only;
all "potentially..." tiers, the "major safety error" labels and the Fraser
triage-discordance arms are excluded): 24 arms from 5 studies (An 2026,
Draelos 2026, Fan 2026, Shi 2026, Zheng 2026), 168 of 1,728 responses
(crude 9.7%). GLMM 9.47% (7.96 to 11.24), tau squared 0.037, prediction
interval 6.28 to 14.03%; Hartung-Knapp 10.77% (9.44 to 12.27). The strict
pool is smaller but defensible, and its estimate sits just below the main
pool's. Note on coding: Reviewer 1 counted 26 strict arms and 191 events by
including the two Fraser arms, whose label contains the word unsafe. The
revision definition excludes Fraser because its tier is a triage-discordance
definition, as the task for this round specified; the difference is stated
here so the two codings can be reconciled. Full per-study labels are in
stage5-manuscript/supplement-tier-labels.csv: strict 24 arms and 168 events
(30.4% of pooled events); potentially-inclusive 55 arms and 327 events
(59.2%); error labels 14 arms and 34 events (6.2%); Fraser triage-discordance
2 arms and 23 events (4.2%).

Excluding Fraser 2023 (new; 93 arms, 22 studies, 529 of 4,794): GLMM 10.34%
(9.16 to 11.65); Hartung-Knapp 12.29% (11.13 to 13.55). Fraser does not drive
the headline.

Zero-event census (corrected): 9 arms and 195 responses (Wen 2026, five
arms, 0 of 100; Bilgic 2026, three arms, 0 of 75; Xiao 2026a ChatGPT arm,
0 of 20). The draft named only the first two studies.

Derived-count shares (now stated in the manuscript): primary pool 34 of 95
arms, 246 of 552 events (44.6%), 2,247 of 4,868 responses (46.2%).
Problematic pool 27 of 38 units, 2,023 of 2,147 events (94.2%), 7,156 of
8,190 responses (87.4%). Format-excluded responses in the primary question:
726 (Draelos 2026 Gemini arm, 222 rated, count in a figure only; Ariel 2026,
504 rated, per-arm counts not printed), which is 13.0% of the 5,594 rated
responses the review located.

## The problematic pool (S1): refits and judgement

- All 38 units, 17 studies, 2,147 of 8,190 (crude 26.2%): GLMM 16.29%
  (11.19 to 23.10), tau squared 1.625, prediction interval 1.39 to 72.84%.
  The printed 18.69% (17.23 to 20.23) was invalid and is withdrawn.
  Hartung-Knapp 19.33% (13.76 to 26.47), unchanged.
- Excluding Khan 2026 (33 units, 956 of 3,190): GLMM 16.86% (11.60 to
  23.88), prediction interval 1.77 to 69.57%; Hartung-Knapp 20.08%.
- Excluding the Si 2026 human-user arms (36 bench units, 1,811 of 7,694):
  GLMM 14.64% (10.24 to 20.50); Hartung-Knapp 17.39%.
- Excluding both (31 units, 620 of 2,694): GLMM 15.08% (10.74 to 20.76),
  prediction interval 2.27 to 57.61%; Hartung-Knapp 18.32%.
- Excluding derived-count units (11 units, 5 studies, 124 of 1,034): GLMM
  8.24% (4.37 to 14.97). The pool does not survive its own derived-count
  sensitivity: the point estimate halves.
- Main search set only (23 units, 8 studies): GLMM 14.61% (8.40 to 24.18).

Judgement, applying the standard the paper applied to undertriage: a pooled
mean is reported as a result only if it describes the studies that compose
it. S1 fails that standard on every count that condemned S2. Its prediction
interval spans 1.4 to 72.8%. Its tier definitions change meaning between
studies, by the paper's own text. It mixes two human-user arms with bench
units after the paper stated the strata were kept apart. And 94.2% of its
events are derived counts, with the no-derived refit halving the estimate.
S1 is therefore demoted to descriptive, study-by-study reporting, the same
treatment as undertriage. Its refitted pooled values are retained in this
changelog and in the analysis supplement for audit, with the
Hartung-Knapp interval, and are removed from the abstract, the summary of
findings as a pooled figure, and the conclusions. Khan 2026 stays in the
dataset and in the descriptive reporting, flagged: the citation
re-verification (peer-review/citation-reverification.md) verified Khan as a
medRxiv preprint through Crossref and through the full text on file, so the
editorial contingency of removing it does not arise. Its weight in S1
(61.1% of the denominator) is one of the reasons the pool is not headlined,
and the ex-Khan refit above is reported so a reader can see that removing
it does not rescue the pool either.

## The undertriage pool (S2)

The revision GLMM does not identify a usable mean for S2: the profile
likelihood is nearly flat for tau above about 2.5 (log likelihood -298.1 at
tau squared 4.0 against -297.3 at tau squared 9.0), and the Wald standard
error fails the floor check (0.0002 against a floor of 0.820), so no GLMM
interval is printed for S2. The Hartung-Knapp fit, 11.54% (3.21 to 33.86),
is retained in the supplement only. The manuscript reports undertriage
study by study, as before. Two content corrections from the settled
extraction: Harada 2026's red-flag slice reports hard undertriage at 100%
in both prompts under near-deterministic decoding and 100% / 99.7% under
stochastic prompt-only runs, as percentages; the exact numerator is not
printed because per-condition denominators are not printed, so the slice
cannot enter the pool, but the concentration statement no longer rests on
an unprinted numerator alone. Xiao 2026b records high-risk-stratum unsafe
counts (major safety error tier) of 4 of 30 (ChatGPT), 6 of 30 (Gemini) and
10 of 30 (Doubao), against study-level unsafe shares of 5 of 90, 9 of 90
and 15 of 90 across all strata; that within-study contrast is now reported
descriptively in the manuscript, correcting the draft's statement that no
primary study splits unsafe counts by urgency.

## Era analysis

Demoted to exploratory and descriptive (see
stage0-protocol/amendment-2026-11-13-era.md). Era-early arms (3 arms, 2
studies, 39 of 174, crude 22.4%) refit at 24.05% (14.39 to 37.37) with a
prediction interval of 0.03 to 99.72%, which is another way of saying three
arms cannot carry a subgroup finding. No interaction p-value is carried in
the abstract or the conclusions. The 4 era-unclassified arms (Wang Y 2026,
3 arms; An 2026 HK Chat arm, 1 arm; 15 of 140 responses, crude 10.7%) are
disclosed wherever the era analysis is mentioned. The era-late sensitivity
and the era-late subgroup level are the same fit and are no longer
presented as two corroborations.

## Citation-chasing triage re-screen (M23)

The 269 title-triage-excluded candidates were reconstructed by set
difference between citation-chasing-candidates.csv (968) and
citation-chasing-screening.csv (699): 269 records, confirmed. A
deterministic random sample of 50 (seed 20261113; sample filed at
stage3-extraction/chasing-triage-rescreen-sample.csv) was re-screened on
titles by a second reader against the review's eligibility criteria.
Yield: 0 of 50 eligible; none would have passed to dual screening. Nearest
misses, all still ineligible: a symptom-checker self-triage study (excluded
by the dedicated symptom-checker rule); a systematic review of
conversational-agent interventions (reviews are excluded); a DeepSeek
hospital-adoption commentary (no advice rating); a DeepSeek-R1 against
OpenAI o1 ophthalmology diagnosis study (clinician-facing, specialty). The
last two name products without a technology word, which confirms the
product-name gap in the triage rule as a real weakness, bounded by this
sample: the observed miss rate for eligible studies is 0 of 50. One
sampled title names LLMs outright (a prompt-engineering methods paper,
also ineligible), and 10 of the 269 titles name LLM technology or a
product, so the triage as logged was not a pure keyword rule; each of
those 10 was also checked on its title and none is a patient-facing
primary-care advice rating study. The manuscript's completeness sentence
is softened accordingly: chasing speaks to the cited literature, not to
the whole field.

## Addendum (same date): format-exclusion bounding check (Reviewer 7, Major 3)

Adding Ariel 2026 back as a single unit at its printed pooled catastrophic share (37/504) gives GLMM 10.46% (9.24 to 11.82), tau2 0.206, PI 4.48 to 22.53 (file: ariel-bounding.json). The format exclusion of Ariel does not move the headline. The Draelos 2026 figure-only arm (222 responses) cannot be bounded from print: no numeric value exists to add, and digitising a bar height was not treated as data.
