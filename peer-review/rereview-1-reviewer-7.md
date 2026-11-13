# Re-review (Gate 5, loop 1)

Paper: Unsafe or potentially unsafe advice from patient-facing large language model chatbots in bench evaluations of primary-care question sets: a systematic review and meta-analysis (Review 4, revision 1)
Reviewer: Reviewer 7 — Bucket I, THE SCEPTIC
Date: 2026-11-13
Materials judged: my Gate 2 report (reviewer-7.md), response-matrix.md rows R7-1 to R7-17, editorial-decision.md, the revised manuscript (stage5-manuscript/manuscript.md), stage4-analysis/revision1/CHANGELOG.md and revision1-results.json, supplement-tier-labels.csv, and stage0-protocol/amendment-2026-11-13-era.md.

Note on the editorial ruling: the editor ruled my spin charge (original Major 1) a reporting-completeness failure, not proven spin. I record my disagreement with the label — the asymmetry I documented was directional, not random — but as instructed I judge the fix, not the label. The fix is graded below on whether all fitted estimators are now reported together wherever the headline appears.

## Tally

- **Resolved: 13** of 17 (Blocker 1; Majors 2, 3, 5, 6, 7 in my original numbering — era, derived counts, S1, differentiation, title; all 5 Minors; Nits 1 and 2)
- **Partly resolved: 4** (Major 1, estimator reporting; Major 4, narrative set; Major 8, author position; Nit 3, newest literature)
- **Unresolved: 0**
- **New Majors introduced by the revision: none.** One new Minor, introduced by a new supplement file, is flagged at the end; it does not change any grade below.

Numbers traced at this gate: revision1-results.json gives the primary GLMM at 10.53% (9.29 to 11.92), tau squared 0.207, PI 4.51 to 22.70%; Hartung–Knapp 12.51% (11.26 to 13.86); study-level Hartung–Knapp 11.66% (9.34 to 14.46) with study-level GLMM 10.32%; strict-tier GLMM 9.47% (7.96 to 11.24), PI 6.28 to 14.03%. The manuscript's rounded values (10.5, 12.5, 11.7, 9.5) match in every case I checked. The supplement's pooled rows re-sum to 552 events / 4,868 responses and 95 arms once the unpooled Ariel row is excluded, and the strict rows re-sum to exactly 24 arms, 168 events, 1,728 responses.

---

## Blocker

### B1 (R7-1). Pooled numerator is not "unsafe" — **RESOLVED**

The combined fix does what I asked, by the relabel route the editor approved, and it does all three parts rather than one:

1. **Verbatim tier-label table.** Table 1 now carries a "Verbatim tier label" column for every primary study, and supplement-tier-labels.csv files the label, the full rating scale, the strict-tier category and the in/out strict flag for all 24 primary studies. I re-summed it: the pooled studies reconcile to 552/4,868 and 95 arms; the composition the manuscript reports (24 arms / 168 events asserting unsafe with no qualifier; 55 arms / 327 events, 59.2%, potentially-inclusive; 14 arms / 34 events major-error; 2 arms / 23 events Buis triage-discordance) matches the supplement and the changelog breakdown (30.4% / 59.2% / 6.2% / 4.2%).
2. **Strict-tier sensitivity.** 24 arms, 5 studies (An, Draelos, Fan, Shi, Zheng), 168 of 1,728, GLMM 9.47% (7.96 to 11.24), PI 6.28 to 14.03%, Hartung–Knapp 10.77% — reported in the Abstract, the Summary of Findings comment, Results and Table 2, i.e. wherever the headline is, as the editor required. The one coding difference from Reviewer 1 (Buis excluded because its tier is a disposition definition, not a harm label) is stated openly in the changelog. Excluding Buis is the more defensible coding, and it is disclosed, so a reader can re-make the call.
3. **Outcome wording narrowed throughout.** Title: "Unsafe or potentially unsafe advice … in bench evaluations". Abstract Objectives and Main results, Background, Summary of Findings, Results and Discussion all name the outcome as responses placed in "the study's own worst safety tier, labelled unsafe or potentially unsafe in most studies". The Background sentence claiming the pooled number "means the same thing in every contributing study" is deleted and replaced with an explicit admission that the first version's description "was too strong". The two specific disclosures I demanded are present: Buis 2023's same 23/74 is stated to enter both the primary pool and the undertriage reporting (Results, Primary outcome; Results, Secondary outcomes; Table 1 footnote), with an ex-Buis sensitivity (GLMM 10.3%) showing it does not drive the headline; and Zheng 2026's post-hoc re-grading ("some responses it first graded unsafe are re-graded as carrying no meaningful potential for harm; the settled counts use each study's primary grading") is stated in the tier paragraph.

**Does the paper now claim only what it pooled? Yes.** The claim that travels — in the title, the abstract and the conclusions — is now "about one in ten responses was placed in the study's worst safety tier (unsafe or potentially unsafe)", the strict-tier figure sits beside it, and the tier mix is part of the result rather than a fact a reader needs the extraction sheet to discover. The pool still pools unlike tiers, but it no longer calls them one thing they are not; GRADE now downgrades the primary outcome in the open for exactly this definition heterogeneity (Table 3). That is the honest version of this analysis, and the Blocker is cleared.

---

## Majors

### M1 (R7-2). Estimator reporting / spin check — **PARTLY RESOLVED**

What is fixed, in text and numbers, not words only: the Abstract Main results now reports GLMM 10.5% (9.3 to 11.9), Hartung–Knapp 12.5% (11.3 to 13.9), study-level 11.7% (9.3 to 14.5) and crude 11.3% together; the stability sentence is reworded to "the stability claim holds inside each estimator, not across estimators", with both ranges given (GLMM 10.1 to 10.6%; HK 12.2 to 12.7%); Table 2 reports GLMM and HK for the main pool and every sensitivity; the Results state "The three estimators bracket the headline: 10.5% to 12.5% … No single one of them is the result on its own", and explain the gap by weighting and the nine zero-event arms; the Discussion summary and the plain language summary both carry the range (PLS: "1 in 10 to 1 in 8, depending on the method").

**What remains, exactly:** two summary surfaces still restate the singular figure with no estimator range — the Abstract's Authors' conclusions ("about one response in ten … was placed … in the study's worst safety tier") and Conclusions, Implications for practice ("fall in a study's worst safety tier about one time in ten on bench sets"). Twelve and a half per cent is one in eight, not one in ten, so on those two surfaces the lowest-estimate monopoly I objected to survives in miniature. The fix is one clause in each place (e.g. "about one in ten (one in eight on the Hartung–Knapp fit)"), matching what the PLS already does. Because the Abstract results, Summary of Findings, Results, Table 2 and Discussion now report the estimators together, this is a residual wording gap, not the original failure — hence Partly, not Unresolved.

### M2 (R7-3). Era interaction — **RESOLVED**

Era is withdrawn as a finding. There is no era p-value and no era finding in the Abstract, the conclusions or Table 2. The Results subgroup paragraph is descriptive only and names the confounders in the same paragraph as the numbers: both early studies at high overall risk of bias, Buis is the emergency triage set that is the pool's outlier on setting as well as era, Armbruster's responses were edited and given a physician-role prompt, and "era, setting, outcome definition and risk of bias are tangled in the same three arms". The 4 era-unclassified arms are stated wherever era appears (Wang Y 2026, 3 arms; An 2026, 1 arm; 15 of 140, 10.7%). The dated retrospective amendment (amendment-2026-11-13-era.md, 13 November 2026) discloses that the calendar cut-off was not the protocol's generation contrast, states that it "does not retrospectively make the analysis pre-specified", and the manuscript states that under the protocol's own wording the early level would hold a single arm and no test would exist. The revision refit (early arms 24.05%, PI 0.03 to 99.72%) underlines why no finding could stand. Every element of my fix list is present.

### M3 (R7-4). Derived counts and format exclusions — **RESOLVED**

The derived shares are now stated in the Abstract (34 of 95 arms; 44.6% of events) and in full in Results (34/95 arms, 246/552 events, 2,247/4,868 responses, 46.2%), with the consequence attached rather than buried: excluding derived arms leaves the GLMM point at 10.1% but raises tau squared to 0.34 and widens the prediction interval from 4.5–22.7% to 3.3–26.9%, in the Abstract, the Primary outcome paragraph and Table 2 — and the text says in plain words "the derived arms do not drive the point estimate; they drive its precision". (The no-derived tau squared and PI differ from the first version's 0.52 / 2.5–32.4% because the revision's corrected quadrature refit the whole pool, tau squared 0.304 → 0.207; the changelog records that discrepancy openly, and the qualitative point — precision depends on the derived arms — survives the refit.) The bounding check I asked for was run: Ariel 2026 added back as one unit at its printed 37/504 gives GLMM 10.46% (9.24 to 11.82), PI 4.48 to 22.53 (ariel-bounding.json; reported in the manuscript as 10.5%, 9.2 to 11.8), so that exclusion does not move the headline. The Draelos figure-only arm (222 responses) is stated to be unboundable from print because no numeric value exists — that is an honest limit, not an evasion; digitising a bar height would have been worse. The 726 format-excluded responses (13.0% of 5,594 located) are disclosed with the pool.

### M4 (R7-5). Narrative set selective emphasis — **PARTLY RESOLVED**

What is fixed: the one unquantified paragraph is gone. The Narrative set section now counts the set's outcome forms (search-arm 51: 23 mean/scale/composite only, 6 percentages with no integer counts, 5 harm combined with another construct, 1 counts in a figure only; chasing 70: 37 scale-score adjudication records), and reports four findings with counts and names: disclaimer/referral (Reis 2026, 881 of 908, 97%); fabricated references (Khromchenko 2024, 100% of ChatGPT-3.5 references against 1 of 12 for Bard; Ucar 2026, Rao 2026, McMahon 2024 named); human-user behaviour (Zhao 2026, Gomez 2024, Mingole 2026 named, with what each measured); and, for balance as I asked, four low/no-harm-signal studies named (Lahut 2026, Zhong 2026, Doran 2026, Bazzari 2024). The Dong 2025 anomaly is retained. The human-user signal that mattered most (Si 2026, 67.7% against 23.4%) now reaches the Abstract and the PLS with its design caveats.

**What remains, exactly:** (i) the second half of my fix was not done — there is still no abstract sentence stating the narrative set's main convergent finding; the Abstract names the 121 studies and reports the human-user decision findings, but a reader of the abstract alone still learns nothing about what the narrative set itself found (fabrication documented wherever citations were checked; users tending to follow advice judged wrong). (ii) There is no narrative table or supplement; the quantification is prose in Results only, and the "people follow advice judged wrong" finding is attributed to the four human-user studies collectively rather than counted per study. The section is now honest and checkable, which clears most of the Major; the abstract-level emphasis imbalance that was the Major's point is reduced but not closed.

### M5 (R7-6). Problematic pool (S1) poolability and Khan 2026 — **RESOLVED**

S1 is demoted to study-by-study reporting under the single poolability standard now stated in Methods ("a pooled mean is reported as a result only if it describes the studies that compose it") — the same standard applied to undertriage, as I asked. The pooled 18.7% (17.2 to 20.2) is removed from the Abstract, the Summary of Findings (row now reads "not pooled in this version") and the conclusions. The revision also showed the original figure was not merely unwise but invalid: the refit gives GLMM 16.29% (11.19 to 23.10), PI 1.39 to 72.84%, and the no-derived refit halves the estimate (8.24% on 11 units, 5 studies) — all filed in the changelog. The Hartung–Knapp value (19.33%, 13.76 to 26.47) and the ex-Khan refit (GLMM 16.86%; HK 20.08%) are in the changelog for audit, the manuscript text carries the refitted points (16.3%, HK 19.3%, PI 1.4 to 72.8%; ex-Khan 16.9%), and Khan's position is stated in the text every time it matters: 61.1% of the denominator, 1,191 of 5,000, on a classification its paper does not describe, in a study at high risk in the rating domain. The Si human-user units inside S1 are named as such. This exceeds my fix list.

### M6 (R7-7). Differentiation from CRD420261347066 — **RESOLVED**

The Background paragraph is rewritten to the shape I specified. One substantive point, stated as such: "a single harm denominator, fixed in advance, as the only primary outcome". The scope point is stated accurately: primary-care presentations "drawn by eligibility rules plus coordinator scope rulings at full text (named in the deviations section)". GRADE and the CHART-informed risk-of-bias tool are described as "methods choices any team could adopt". The human-user point is reworded exactly as required: "a design intention that the evidence did not meet, not a result". This review's own position is stated beside the competitor's: "This review is itself unregistered … while the competing record is registered and overdue", the absence-of-evidence caveat is in the text ("An empty search result does not show that no publication exists"), and the submission-day commitment survives in print: "the check will be repeated on any day this review is submitted".

### M7 (R7-8). Title — **RESOLVED**

The title is now "Unsafe or potentially unsafe advice from patient-facing large language model chatbots **in bench evaluations of primary-care question sets**", and the Abstract Objectives carry the same framing with a plain gloss of "bench" at first use. The unit of evidence now travels with the claim wherever the title is quoted alone, which was the whole of this Major.

### M8 (R7-9). Author-position bias — **PARTLY RESOLVED**

What is fixed: a Discussion section, "Author position and the judgements inside this review", now states the author's clinical-AI building activity as a non-financial interest in how this literature is read, names the three consequential inside-team decisions (tier mapping, coordinator scope rulings, era cut-off), states there is "no PROSPERO registration and no external timestamp to check them against" and that the protocol is dated the same day as the search, names the calls that cut against a larger headline (scope rulings removing sets with harmful counts of 25 of 50 and 19 of 50; the strict-tier sensitivity and the S1 demotion), and points to the filed material that lets a reader re-make each call. Declarations, Conflicts of interest is rebuilt on the same facts. Author contributions makes the human/LLM division of decisions explicit, with the author accountable for the final text. The four flagged records (R2022, R2073, R2966, R3051) are stated, in Selection of studies and in Deviations (7), to remain unread by the author and excluded from every count — the explicit treatment available for unread records.

**What remains, exactly:** the external anchor still does not exist. No PROSPERO submission and no timestamped public protocol deposit has been made; the response matrix (R7-9) records this as the unfinished part, an author step barred to the revision agent. The manuscript is honest that the anchor is absent, which is why this is Partly rather than Unresolved — but on my original terms the point is only closed when the deposit/registration step happens at submission, and Gate 6 should verify it rather than take the intention on trust.

---

## Minors

### m1 (R7-10). Zero-event census — **RESOLVED**
Corrected in Results, Primary outcome: nine zero-event arms, 195 responses, itemised as Wen 2026 (0 of 100, five arms), Bilgic 2026 (0 of 75, three arms) and Xiao 2026a ChatGPT (0 of 20) — the arm the first version omitted. The census is also corrected in the changelog, and the Hartung–Knapp correction is now described as applying to all 95 arms, as coded.

### m2 (R7-11). GRADE certainty in the conclusions — **RESOLVED**
"Very low certainty" is now attached to the restated figure in the Abstract's Authors' conclusions, in the Discussion summary ("at very low certainty"), and in Implications for practice ("about one time in ten on bench sets (very low certainty; …)"), as the Summary of Findings table already did.

### m3 (R7-12). Completeness inference — **RESOLVED**
Softened in both places it appeared. Discussion, Completeness: chasing "shows the primary pool is close to complete for the cited literature that prints an explicit harm tier, and it is equally consistent with the citing literature sharing the search's blind spots". Reporting bias makes the same point. The claim is now a statement about the cited literature only.

### m4 (R7-13). Buis "descriptive contrast" — **RESOLVED**
Labelled in the Subgroup analyses text as "a single-study observation about the pool's known outlier, not a contrast the review fitted", and prefaced "Separately, and not as a subgroup finding". Exactly the labelling I asked for.

### m5 (R7-14). Table 1 pooled/unpooled marker — **RESOLVED**
Table 1's column is now "Arms analysed" and sums to 95 (Ariel 2026: 0); the footnote reconciles all five unanalysed arms (Ariel's 4, 504 responses, per-arm counts not printed; Draelos's Gemini arm, 222 responses, figure only; Draelos total 888 = 666 counted + 222). A reader can now reproduce 552/4,868 from the table plus the footnote.

---

## Nits

### n1 (R7-15). PLS range — **RESOLVED**
The plain language summary reads "about 1 in 10 answers landed in the worst safety grade … (1 in 10 to 1 in 8, depending on the method used to combine the studies)".

### n2 (R7-16). "Only subgroup with an interaction test" — **RESOLVED**
Fixed by removal: the sentence, the test and the p-value are gone from the Abstract; era survives only as exploratory descriptive text in Results.

### n3 (R7-17). Headline rests on the newest literature — **PARTLY RESOLVED**
The revision reports the pool's composition (search window from 2023; models evaluated 2023 to 2026; 19 of 24 China/Hong Kong; 19 of 24 single-topic) in the Abstract and Results, Table 1 makes each pooled study's year visible, and the conclusions limit the claims to "models evaluated 2023 to 2026" / question sets "from 2023 to 2026". What remains: the specific observation is still nowhere stated as a count — only 2 of the 23 pooled studies (Buis 2023, Armbruster 2024) predate 2026 — so the dependence of the headline on the newest, least-settled literature is inferable from Table 1 but never said. This was a Nit and stays one; one sentence in Description of studies would close it.

---

## New comments

**New Majors introduced by the revision: none.** I state this explicitly as Gate 5 requires. The revision's new analyses (strict-tier pool, study-level fit, S1/S2 refits, Ariel bounding check) are all reported with their numbers filed and traceable, and the two places where revision numbers changed (primary PI 3.8–26.2% → 4.5–22.7%; tau squared 0.304 → 0.207) are explained in the changelog as consequences of the corrected quadrature, not silently substituted.

**One new Minor, introduced by the revision, for Gate 6 (not a Major; no pooled number is affected):** supplement-tier-labels.csv, the new file created for Blocker B1, gives Ariel 2026's `responses_rated` as **126**, where the manuscript, Table 1 and its footnote consistently give **504** rated responses (37 of 504, 7.3%; 126 appears to be the per-arm prompt count, 504 / 4). Ariel contributes no arm to any pool and every other row of the supplement reconciles exactly, so this is a one-cell correction in a supplement, not a threat to any result — but a supplement filed so readers can audit the tier mapping should not contradict the manuscript it audits. Correct the cell (or label the column's basis) before Gate 6.

## Closing judgement

The paper I objected to headlined a mislabelled numerator through its lowest estimator, promoted a confounded 3-arm contrast, and let a 23-study bench pool speak for 166 studies. The revised paper labels the numerator for what it is and files the labels, reports its estimators together (with the two residual singular restatements noted under M1), withdraws the era finding and the S1 headline, quantifies the narrative set, and reckons in print with who made its judgement calls. Four Partly-resolved items remain, none of them a Blocker and none requiring new data: two one-clause estimator ranges, one abstract sentence, one unstated year count, and one external deposit step that only the author can take. Subject to those being closed at the next loop — and the supplement cell above corrected — the Sceptic's case against the headline, as originally filed, no longer stands against the revised text.
