# Re-review (Gate 5, loop 2) — Reviewer 2, Bucket C (meta-analysis statistician)

Paper: Unsafe or potentially unsafe advice from patient-facing LLM chatbots in bench evaluations of primary-care question sets (Review 4, revision 2 / loop 2)
Date: 2026-11-13
Materials judged: my Gate 5 loop-1 re-review (`peer-review/rereview-1-reviewer-2.md`), the Loop 2 addendum to `peer-review/response-matrix.md` (rows L2-3 and L2-4, in particular), Reviewer 1's loop-1 condition on the demoted problematic pool, and the current manuscript (`stage5-manuscript/manuscript.md`) at the places named below, cross-checked against the filed analysis supplement (`stage4-analysis/revision1/CHANGELOG.md`). Per the assignment, I judge only the three items put to me. Nothing else in my loop-1 report is reopened: every other comment of mine stood Resolved at loop 1 and no verdict below disturbs that.

## Verdict counts (3 items put to me)

- **Resolved: 3**
- **Partly resolved: 0**
- **Unresolved: 0**
- **New Majors or Minors introduced by the loop-2 revision: none within the scope judged**

---

## 1. Major 4, Partly at loop 1 (derived counts; the S1 no-derived estimate not printed in the body) — RESOLVED, closed under the handling editor's ruling

**What I asked for at loop 1.** The S1 no-derived sensitivity existed and was filed — 11 units, 5 studies, GLMM 8.24% (4.37–14.97), tau² 0.9513, prediction interval 0.86–48.22, floor-valid on my own recomputation (filed SE 0.3438 against a floor of sqrt(0.9513/11) = 0.2941) — but its value was not printed in the manuscript. The S1 paragraph said only that the refit "falls to 11 units from 5 studies with a much lower value", and I held the Major partly open on one remedy: one sentence printing 8.2% in the S1 paragraph, as the P1 no-derived value had been printed.

**The ruling I am asked to judge under.** The handling editor ruled the other way: the S1 refit values, the no-derived 8.2% included, belong in the supplement, not the body — adopting Reviewer 1's loop-1 condition that a pooled figure for the demoted problematic pool, if kept at all, live in the analysis supplement only. Loop-2 row L2-3 implements that ruling rather than my remedy. My task is to say whether the Major closes under it, not to re-run the placement argument I lost.

**It closes. I withdraw my loop-1 remedy as superseded, for three statistical reasons, each checked in the current text rather than the matrix:**

1. **The defect my Major was actually about is gone.** The loop-1 text made an unverifiable comparative claim in the body — a collapse ("a much lower value") whose size the reader could not see anywhere in the paper they were holding. The current S1 paragraph (Results, Secondary outcomes, "Problematic tier") contains no comparative claim at all: no "much lower", no "falls to", no halving language, and no S1 refit figure of any kind (I searched the paragraph and the manuscript body text at that section: 16.3%, 19.3% and 8.2% do not appear there). What replaced the claim is a pointer, not an assertion: "Refits under the corrected machinery are filed in the analysis supplement (revision changelog) and are not pooled claims of this review." A reader is no longer asked to take a number's direction on trust.
2. **The demotion no longer leans on the hidden number.** In the loop-1 text the collapse was doing load-bearing work for the poolability judgement while remaining unprinted. The current paragraph carries its demotion grounds in print, on facts a reader can check from the text itself: 27 of 38 units derived, carrying 2,023 of 2,147 events (94.2%) and 7,156 of 8,190 responses (87.4%); only 11 units from 5 studies remain when derived units are excluded; Khan 2026 alone supplies 61.1% of the denominator on an undescribed classification; the tier "changes meaning between studies"; unit-level shares run from 0% to 73.4%. The Methods poolability standard still names estimate collapse on removing derived units as one of its (disjunctive) criteria in general terms, but the S1 paragraph does not invoke it for this pool, and the printed grounds suffice without it. Nothing a statistician needs to accept the demotion is withheld from the body.
3. **Traceability — the substance of the Major — is fully preserved under the ruling.** The values are not deleted; they are filed where the ruling puts them. I re-checked the supplement: `stage4-analysis/revision1/CHANGELOG.md`, section "The problematic pool (S1): refits and judgement", prints the full refit set with intervals — all-units GLMM 16.29% (11.19 to 23.10), tau² 1.625, prediction interval 1.39 to 72.84%, Hartung–Knapp 19.33% (13.76 to 26.47); ex-Khan and ex-Si refits; and the no-derived refit at 8.24% (4.37 to 14.97) with the judgement "the point estimate halves" stated there, in the audit record, where a halving claim belongs. The Summary of findings row for this outcome likewise reads "not pooled in this version; see text" and points to the analysis supplement "for audit only", and the Abstract and Conclusions carry no S1 pooled value. Protocol Rule 6 — numbers traced, not trusted — is satisfied: every S1 refit value is traceable to a filed, floor-valid fit; none is asserted in the body.

**What I am not holding open, and why.** My loop-1 preference for printing 8.2% in the body was a reporting-placement preference between two defensible options, not a statistical requirement. Printing a quotable pooled figure — even a sensitivity figure — in the main text of a paper that itself declares this pool unpoolable is the outcome Reviewer 1's condition was written to prevent, and it carries its own misleading-reader risk, which is the harm a Major exists to prevent. There is nothing here a statistician cannot accept: the analysis is done, validated, filed and pointed to; the body asserts nothing about it that the body does not show. **Major 4 is Resolved and closed.**

---

## 2. New Minor A at loop 1 (undertriage Hartung–Knapp sentence) — RESOLVED

At loop 1 the undertriage sentence called the Hartung–Knapp value "filed in the supplement only" in the same sentence that printed it (11.5%, 3.2 to 33.9) — self-contradictory wording, Minor, no effect on any number.

The current undertriage paragraph (Results, Secondary outcomes, "Undertriage") reads: "A Hartung-Knapp sensitivity fit gives 11.5% (3.2 to 33.9); it is a filed sensitivity, not a pooled result of this review." The word "only" and the supplement-only claim are gone; the value is printed plainly and its status is labelled in the same breath, which is exactly the status undertriage has held throughout (no pooled mean reported; the mixed-model fit's failure of the validation floor is stated immediately before this sentence). The wording no longer contradicts itself, and the label "not a pooled result" is accurate. **Resolved.**

## 3. New Minor B at loop 1 (abstract "for every pool") — RESOLVED

At loop 1 the abstract's Data collection and analysis sentence claimed the Hartung–Knapp and study-level fits "are reported beside the main fit for every pool", which overstated the position for the two demoted secondary outcomes, neither of which has a main fit reported.

The current abstract sentence reads: "An inverse-variance fit with Hartung-Knapp adjustment and a study-level fit (one value per study) are reported beside the main fit for the primary pool." The correction Loop-2 row L2-4 promised — "for the primary pool" — is in the text verbatim, and it now matches what the manuscript actually does after L2-3: beside-the-main-fit reporting for the primary pool, study-by-study reporting with supplement-filed refits for the problematic tier and undertriage. **Resolved.**

---

## Closing position

All three items put to me in loop 2 are Resolved. My one Partly Major from loop 1 closes under the handling editor's supplement-only ruling, which I accept on the statistical merits set out above: the unverifiable in-body comparative claim that kept it open has been removed, the demotion stands on printed evidence, and the refit values remain filed, validated and traceable in the analysis supplement. The two revision-introduced Minors are corrected in the text as filed. Within the scope assigned to me, nothing remains open on statistics, and I raise nothing new.
