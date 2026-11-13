# Re-review (Gate 5, loop 1) — Reviewer 2, Bucket C (meta-analysis statistician)

Paper: Unsafe or potentially unsafe advice from patient-facing LLM chatbots in bench evaluations of primary-care question sets (Review 4, revision 1)
Date: 2026-11-13
Materials judged: my Gate 2 report (`peer-review/reviewer-2.md`), the revised manuscript (`stage5-manuscript/manuscript.md`), and the revision analysis files (`stage4-analysis/revision1/analysis-revision1.py`, `revision1-results.json`, `CHANGELOG.md`), with my own recomputations from `revision1-results.json` and from `stage4-analysis/analysis-dataset.csv`. The response matrix was used only to locate changes; every verdict below rests on the revised files and text themselves, per Protocol Gate 5. Words-only answers would have counted as Unresolved; none of the verdicts below rests on words alone where an analysis was demanded — each was checked against a filed number I could re-derive.

## Verdict counts (18 comments: 1 Blocker, 8 Majors, 6 Minors, 3 Nits)

- **Resolved: 17**
- **Partly resolved: 1** (Major 4, derived counts — the S1 no-derived estimate exists in the analysis files but its value is not printed in the manuscript)
- **Unresolved: 0**
- **Blocker: RESOLVED / cleared** (see below)
- **New Majors introduced by the revision: none** (two new Minor wording slips are recorded at the end; neither touches a headline number)

## My own recomputed floor checks (the Blocker test, re-run)

For a random-effects mean on the logit scale, SE(mu) ≥ sqrt(tau²/k). I recomputed the floor from each fit's filed tau² and k, and independently re-derived the implied SE from each printed CI on the logit scale, SE = [logit(hi) − logit(lo)] / (2 × 1.96). I also re-derived every Hartung–Knapp fit below from `analysis-dataset.csv` with an independent DerSimonian–Laird + Hartung–Knapp implementation, and recomputed the prediction intervals as mu ± t(k−2)·sqrt(tau² + SE²).

| Fit | k | tau² | Floor sqrt(tau²/k) | Filed SE | Implied SE from CI | Verdict |
|---|---|---|---|---|---|---|
| P1 main GLMM, revision | 95 | 0.2068 | 0.0467 | 0.0712 | 0.0711 | PASS (ratio 1.53) |
| P1 main GLMM, version 1 (for contrast) | 95 | 0.304 | 0.0566 | — | 0.0736 | passed then; now superseded |
| S1 problematic GLMM, revision | 38 | 1.6245 | 0.2068 | 0.2216 | 0.2216 | PASS (ratio 1.07 — narrow, but on the right side) |
| S1 problematic GLMM, version 1 | 38 | 1.0517 | 0.1664 | — | 0.0504 | was FAIL — the Blocker |
| S2 undertriage GLMM, revision | 12 | 8.0714 | 0.8201 | 0.0002 | 0.0000 | FAIL — and correctly flagged FAIL in the JSON and withheld from the manuscript |
| S2 undertriage GLMM, version 1 | 12 | 4.963 | 0.6431 | — | 0.1203 | was FAIL |
| P1 study-level GLMM | 23 | 0.3157 | 0.1172 | 0.1329 | 0.1327 | PASS (ratio 1.13) |
| P1 strict-tier GLMM | 24 | 0.0366 | 0.0391 | 0.0972 | 0.0973 | PASS (ratio 2.49) |
| P1 sensitivities (no preprints / no derived / era-late / no high RoB) | 87 / 61 / 88 / 76 | 0.2333 / 0.3388 / 0.1734 / 0.1673 | 0.0518 / 0.0745 / 0.0444 / 0.0469 | 0.0772 / 0.1076 / 0.0714 / 0.0758 | 0.0769 / 0.1077 / 0.0713 / 0.0756 | all PASS |
| S1 sensitivities (ex-Khan / ex-Si / no-derived / main-search only) | 33 / 36 / 11 / 23 | 1.3609 / 1.3165 / 0.9513 / 2.1158 | 0.2031 / 0.1912 / 0.2941 / 0.3033 | 0.2225 / 0.2081 / 0.3438 / 0.3179 | matches filed SEs | all PASS |
| Era-early descriptive GLMM | 3 | 0.2002 | 0.2583 | 0.3231 | 0.3232 | PASS |

Every filed SE also agrees with its half-step check in the JSON (identical to 4 decimals on every reported fit), which addresses the specific finite-difference failure mode of version 1.

Prediction intervals recomputed by me: P1 4.51–22.69% (filed 4.51–22.70); S1 1.39–72.85% (filed 1.39–72.84); study-level 3.35–27.66% (filed identically); strict-tier 6.28–14.03% (filed identically). All match.

Hartung–Knapp fits re-derived by me from the dataset, against the filed values: P1 arm-level 12.51% (11.26–13.86), DL tau² 0.1367 — exact match; **study-level 11.66% (9.34–14.46), DL tau² 0.207 — exact match to `P1_study_level.hk`** (the manuscript's 11.7% [9.3–14.5] is its correct rounding); S1 19.33% (13.76–26.47) — exact match; S2 11.54% (3.21–33.86) — exact match. **Strict-tier fit verified from the outputs: GLMM 9.47% (7.96–11.24), tau² 0.0366, PI 6.28–14.03; HK 10.77% (9.44–12.27)** — the manuscript's 9.5% (8.0–11.2), HK 10.8% (9.4–12.3) and PI 6.3–14.0% are correct roundings.

## Blocker

**Blocker 1 (invalid GLMM intervals for S1/S2; P1 interval untrusted by association) — RESOLVED, cleared.**

- S1 was refitted with per-unit adaptive quadrature: GLMM 16.29% (11.19–23.10), tau² 1.625, PI 1.39–72.84, HK 19.33% (13.76–26.47). The interval now passes the floor (above), the old headline 18.7% (17.2–20.2) appears nowhere in the revised manuscript, and S1 is demoted from headline to study-by-study reporting in the abstract, Summary of findings and Results — the pooled values survive only as audit values in the changelog.
- S2's revision GLMM is declared, in the JSON, the changelog and the manuscript, to fail the floor check (filed SE 0.0002 against floor 0.820, `floor_check: FAIL`), its likelihood is described as nearly flat at large tau², and no GLMM point or interval for S2 is printed anywhere in the manuscript. The HK value 11.54% (3.21–33.86) — which I re-derived exactly — is not headlined; the outcome is reported study by study. (One wording slip: the Results sentence calls the HK value "filed in the supplement only" in the same sentence that prints it. That is a new Minor, below, not a reopening of the Blocker: the value is presented as a filed sensitivity, not as a result, and the Summary of findings row reads "not pooled".)
- P1: tau² corrected 0.304 → 0.207, GLMM 10.53% (9.29–11.92), PI now 4.51–22.70 (was 3.75–26.20). The corrected tau² agrees with the filed independent refit by direct numerical integration (0.20), which is now reported in the manuscript itself. The interval passes the floor with room (ratio 1.53).
- On the "validated software" route: the analysis of record is still Python, not metafor — `analysis-revision1.py`, with the R stub (`stage4-analysis/analysis.R`) filed and the Methods now stating plainly that R/metafor were not installed. I accept this as the "equivalent checked implementation" my comment allowed, because the checks that version 1 lacked are now present and verifiable from the files: genuinely adaptive quadrature in the code (see Major 5), observed-information SEs stable at half step, a floor validation on every fit with the one failure flagged rather than printed, and an independent computation route agreeing on both the point estimate and tau² for the headline pool. The Blocker was a claim about invalid numbers; the numbers are now valid, traceable and cross-checked.

## Majors

**Major 1 (GLMM–HK gap headlined one-sidedly; promised HK results withheld) — Resolved.**
GLMM, HK and study-level values are now reported together in the abstract, Summary of findings, Results and Table 2 (10.5% / 12.5% / 11.7%, crude 11.3%), with the text stating "No single one of them is the result on its own." Table 2 carries HK point estimates *and* intervals for every primary sensitivity; the sensitivity ranges are given per estimator (GLMM 10.1–10.6%, HK 12.2–12.7%) and the stability claim is reworded to hold "inside each estimator, not across estimators" in the abstract, Results and Discussion. S1/S2 HK values are filed with intervals in the revision outputs (S1 19.33% [13.76–26.47]; S2's HK interval is also printed once in the Results as a filed value). S1's HK interval lives in the changelog rather than the manuscript body, but since S1 is no longer a reported pool that is where its pooled values were consigned; I do not hold this Major open on it.

**Major 2 (no allowance for within-study clustering; arm-based PI degrees of freedom) — Resolved — and, on the specific question put to me: the three-level GLMM not being fitted does NOT leave this Major open.**
My report offered two routes: a three-level / nested GLMM, *or, at minimum*, a study-level aggregated sensitivity for the primary pool reported in Table 2 with prediction intervals on study-based degrees of freedom. The minimum route was taken in full and I verified it from the outputs rather than the matrix: the study-level fit (23 units, arms aggregated within study) gives HK 11.66% (9.34–14.46) — reproducing my own Gate 2 check of 11.7% (9.3–14.5) to the decimal, and re-derived exactly by me from the dataset — and GLMM 10.32% (8.15–12.99), with a prediction interval of 3.35–27.66% computed on k = 23 (t on 21 df), printed in Table 2 as 11.7% (9.3–14.5) and PI 3.4–27.7%. The non-independence of arms is stated in the Methods ("arms within a study share the question set, the raters and the rating scale and are not independent data points") and the study-level fit sits beside the main fit in the abstract and Summary of findings. The main pool's own PI remains arm-based, but a reader now has the study-based interval in the same table, which is exactly what my stated minimum demanded. The unfitted three-level model is a disclosed limitation, not an open Major: **this Major is closed.**

**Major 3 (era interaction over-claimed; 4 unclassified arms undisclosed; duplicated fit) — Resolved.**
No interaction p-value remains anywhere in the manuscript (I searched: no "p = 0.001", no interaction test carried as a finding; Table 2 has no era interaction row). Era is a descriptive, exploratory paragraph: early level 24.1% (14.4–37.4) on 3 arms / 2 studies — matching the revision fit 24.05% (14.39–37.37), which passes its floor — with the confounding (both early studies at high risk of bias, Buis's setting, Armbruster's edited responses) stated in the same paragraph, the protocol-wording untestability stated, the 4 unclassified arms disclosed with counts (15/140, 10.7%), and the duplication labelled in words: "the era-late sensitivity above and the era-late level here are the same fit, not two corroborations."

**Major 4 (derived counts dominate; scale unstated; no-derived heterogeneity unreported; no S1 sensitivity) — Partly resolved.**
Done: derived shares are stated per pool in the abstract, Results and S1 paragraph (P1: 34/95 arms, 246/552 events [44.6%], 2,247/4,868 responses [46.2%]; S1: 27/38 units, 2,023/2,147 events [94.2%], 7,156/8,190 responses [87.4%], Khan's 61.1% denominator share named). The P1 no-derived sensitivity is reported in full: 10.1% (8.4–12.2) with tau² rising to 0.34 (filed 0.3388) and PI widening to 3.3–26.9% (filed 3.33–26.88), in Results and Table 2. The S1 no-derived sensitivity now exists and is filed: 11 units, 5 studies, GLMM 8.24% (4.37–14.97), tau² 0.9513, PI 0.86–48.22 — the estimate halves, as my comment feared.
*Exactly what remains:* that S1 no-derived value is **not printed in the manuscript**. The S1 paragraph says only that the refit "falls to 11 units from 5 studies with a much lower value", and the Methods poolability standard ("whose estimate collapses when derived-count units are removed") leans on the collapse without showing it. One sentence printing 8.2% in the S1 paragraph (as the P1 value was printed) closes this. This is the sole remaining item from my report; it is a reporting gap in the text, not an analytic one — the fit is done, filed and floor-valid.

**Major 5 (quadrature misdescribed as adaptive; tau² discrepancy hidden) — Resolved.**
I read the revision code: `unit_ll` in `analysis-revision1.py` finds each unit's posterior mode by Newton iteration and its Laplace scale from the curvature, and places the 31 Gauss–Hermite nodes on that per-unit mode and scale — that is adaptive quadrature as the revised Methods now describe it ("31 nodes; per-unit Laplace mode and scale"), and the Methods also state honestly that version 1's implementation was non-adaptive and its SEs failed. The tau² discrepancy is in the manuscript (Results: independent refit 10.55% against 10.53% from the revision script, tau² 0.20 against 0.207, "the first version's quadrature estimate of tau squared (0.304) was the outlier") and in the changelog. The corrected PI carries the consequence.

**Major 6 (S1 mixes human-user strata and unit types against the paper's own rule) — Resolved.**
S1 is demoted to study-by-study reporting under a single poolability standard now stated in Methods and applied to both secondary outcomes. The Si 2026 units are named in the S1 paragraph as human-user encounters that "do not belong with bench units", and reported in the human-user Results; unit definitions are stated (model arms except study-level slices printed as single units, e.g. Tiller 2026). The abstract's selection criteria no longer claim the strata "were kept apart at every stage" — it now says they were kept apart for the primary outcome and that the one secondary pool that mixed them "is no longer pooled".

**Major 7 (Buis 2023's same 23 events counted in two pools, undisclosed) — Resolved.**
The disclosure sentence appears in both the primary Results ("The same 23 events therefore enter this pool as worst-tier responses and the undertriage reporting as undertriage responses…") and the undertriage paragraph ("the same events as its primary-pool counts"), Table 1 carries the footnote and the tier label "unsafe (triage)", and the admission justification is stated under the relabelled outcome. An ex-Buis sensitivity was added and I verified it in the outputs: GLMM 10.34% (9.16–11.65), HK 12.29% (11.13–13.55) — manuscript 10.3% (9.2–11.7), HK 12.3%.

**Major 8 (zero-event census incomplete; HK correction mechanics misdescribed; DL tau² unreported) — Resolved.**
The census is corrected in the Results to 9 arms and 195 responses (Wen 5 arms, 0/100; Bilgic 3 arms, 0/75; Xiao 2026a ChatGPT arm, 0/20), the correction is described as applying "to all 95 arms" as coded, and the DL tau² (0.14, filed 0.1367) is reported beside the GLMM tau² (0.21) in the Results and Methods. One file artefact, not a manuscript error: the JSON's zero-event `detail` field collapses duplicate arms via a sorted set (it lists 3 study/total pairs), although its `arms: 9, responses: 195` totals and the manuscript text are correct.

## Minors

1. **I² presented as a GLMM product — Resolved.** Methods defines I² as "a fixed-effect Q statistic on 0.5-corrected logits" and states tau² and the PI carry the heterogeneity message; the primary Results label it inline ("I squared 42.0% (fixed-effect Q on corrected logits)"). The abstract and GRADE table use the bare figure under that Methods definition.
2. **Table 1 arms column sums to 100 — Resolved.** Column retitled "Arms analysed", sums to 95 (Ariel 0, Draelos 3), footnote reconciles all five unanalysed arms and Draelos's 888 total.
3. **S1 main-search sensitivity without study count — Resolved.** The pool is demoted, and its composition split is now stated wherever it is summarised (23 units from 8 search studies; 15 units from 9 chasing studies); the refitted main-search-only audit value in the changelog (14.61%) carries its 23 units / 8 studies.
4. **S2 "units" not a consistent entity — Resolved.** Unit definitions are stated in the Figure 3 note (arms except Harada's two presentation slices, n = 480 and n = 1,440, and Brown's two slices of n = 10 each) and the undertriage text describes the slices as such.
5. **Era interaction row without SE/CI — Resolved** by removal, the alternative my comment offered: the test and its rows are out of Table 2 and the abstract.
6. **Crude proportion absent from the abstract — Resolved.** Crude 11.3% appears in the abstract's Main results beside the fitted values, and in the Summary of findings and Discussion.

## Nits

1. **Refit quoted at one decimal — Resolved.** Quoted at two decimals (10.55% against 10.53%; the comparison is now refit against the revision script, consistently in manuscript and changelog).
2. **Summary of findings undertriage row — Resolved.** The row reads "not pooled; see text", as does the problematic row.
3. **Table 2 sensitivity rows without events/totals — Resolved.** An events/total column is present for every row (e.g. 306/2,621 for the no-derived fit), and I spot-checked the column against the revision JSON for all rows: all match.

## New Majors introduced by the revision

**None.** No new Major is raised. Two new Minor wording slips, neither affecting any headline number, are recorded for the next loop's tidy-up, not as Gate 5 loops in themselves:

- *New Minor A:* the undertriage sentence says the HK value "is filed in the supplement only" while printing it (11.5%, 3.2 to 33.9) in that same sentence. Delete "only" or move the value out of the sentence; the current wording contradicts itself.
- *New Minor B:* the abstract's Data collection sentence says the HK and study-level fits "are reported beside the main fit for every pool", which overstates the position for the two demoted secondary outcomes (their fits are audit-filed, not reported beside a main fit, since neither has one). The Methods version of the sentence is accurate; the abstract should match it.

## Closing position

The inferential layer I blocked on has been refitted, and the refit survives the arithmetic test that killed version 1: every printed interval passes the sqrt(tau²/k) floor on my own recomputation, the one fit that still fails is flagged as failing and withheld, and the Hartung–Knapp and study-level numbers reproduce exactly under an independent implementation. The clustering Major is closed on the minimum remedy my own report specified. One Partly item remains — print the S1 no-derived estimate (8.2%) in the manuscript text — and it loops to Gate 4 as a text fix with the analysis already done. On statistics, this revision is otherwise ready to proceed.
