# Editorial decision (Gate 3)

Paper: Unsafe medical advice from patient-facing LLM chatbots in primary-care presentations: a systematic review and meta-analysis (Review 4)
Round: 1
Date: 2026-11-13
Handling editor: coordinator, acting as handling editor under PROTOCOL.md

## Coverage check
Twelve domains (PROTOCOL.md S.2): all twelve examined. 2.1 R1/R3/R4/R7; 2.2 R1/R6; 2.3 R1/R3; 2.4 R2/R7; 2.5 R2/R3/R4/R7; 2.6 R1/R7; 2.7 R3/R4/R5; 2.8 R1/R6; 2.9 R2/R6; 2.10 R3/R4; 2.11 R5; 2.12 R6 (metadata) and coordinator (venue note on file). No domain missed.

## Panel totals
Reviewer 1 (B, methodologist): Major revision. 2 Blocker / 5 Major / 6 Minor / 2 Nit.
Reviewer 2 (C, statistician): Major revision. 1 Blocker / 8 Major / 6 Minor / 3 Nit.
Reviewer 3 (A, primary care): Major revision. 0 Blocker / 6 Major / 6 Minor / 3 Nit.
Reviewer 4 (E, patient): Major revision. 0 Blocker / 6 Major / 4 Minor / 3 Nit.
Reviewer 5 (F, ethics/regulatory): Major revision. 0 Blocker / 4 Major / 5 Minor / 3 Nit.
Reviewer 6 (H, information specialist/editor): Major revision. 9 Blocker / 6 Major / 6 Minor / 3 Nit.
Reviewer 7 (I, sceptic): Major revision. 1 Blocker / 8 Majors / 5 Minors / 3 Nits.
All seven reviewers independently returned Major revision. No Accept, no Reject-and-resubmit.

## The paper's central problem
Three independent lines converge on the same weakness: the headline is stated with more precision and more generality than the underlying material carries.
(1) The pooled numerator is not uniformly "unsafe" (R1-B1, R7-B1, agreed by both from the extraction sheet: 327/552 events, 59.2%, from "potentially unsafe / potentially harmful" tiers, 6.2% from "major safety error" labels, plus Buis triage-discordance).
(2) The numbers machinery is not fully sound as printed (R2-B1: S1/S2 GLMM intervals mathematically invalid; HK results computed but withheld; no study-level clustering).
(3) The reference list cannot be trusted as printed (R6-B1..B9: eight DOI/title mismatches and one unverifiable study, with a pattern indicating DOI harvesting from reference lists).
Disagreement preserved: R2 and R7 disagree in emphasis on the headline estimator — R7 calls headlining the GLMM over the HK 12.5% "spin"; R2's own study-level re-pool (11.7%, 9.3-14.5) sits between the two, and R2 frames the issue as withheld results rather than spin. Editor's ruling: this is a reporting-completeness failure, not proven spin; the fix is to report all fitted estimators together wherever the headline appears, not to swap the headline estimator. R4 (patient) and R3 (clinician) both demand the bench-only and pool-composition caveats move earlier and louder; R1 does not object but prioritises the tier-definition fix — editor rules both are required, they are compatible. R5's Majors are declaration facts; no reviewer contradicted them.

## Decision
**Major revision.** Loop 1 at Gate 4, full re-review at Gate 5.

## Merged comment list (disagreements preserved in full in the individual reports)
### Blockers
- B-A Tier definition (R1-B1 = R7-B1): primary pool does not implement the protocol's explicit unsafe/harmful/dangerous tier definition; no tier-label table exists to audit the mapping. Fix requires: a per-study tier-label table (supplement), a strict-tier sensitivity refit (arms whose tier label is explicitly unsafe/harmful/dangerous only), and outcome wording narrowed throughout so the claim matches what was pooled, OR a re-pool under the strict definition as primary. Editor: narrowing + strict sensitivity + table is acceptable if the strict result is reported wherever the headline is; if the strict pool collapses below a defensible size, the primary outcome must be redefined openly as a dated amendment.
- B-B Era subgroup deviation (R1-B2, R7-M2 in part): the analysed 13 May 2024 release-date cut-off is not the protocol's GPT-3.5 vs GPT-4/4o contrast and no amendment was filed; 4 era-unclassified arms (15/140) undisclosed. Fix: dated amendment filed now disclosing the deviation, era analysis demoted to exploratory everywhere, unclassified arms disclosed, abstract loses the finding-level p = 0.001 billing or carries it with its 3-arm/2-study/high-RoB confounding in the same sentence.
- B-C Invalid intervals (R2-B1): S1 and S2 GLMM confidence intervals are mathematically impossible given the paper's own tau-squared and k. Fix: recompute with a correct method, report HK intervals for every pool and sensitivity as the Methods promise, and validate every printed interval against the sqrt(tau2/k) floor before resubmission.
- B-D Citations (R6-B1..B9): Miao, Zuo, Gong, He, Liang, Armbruster, Huo (anchor), Ariel (title), Khan (unverifiable). Fix: title-page-level re-verification of the ENTIRE reference list (not spot fixes), corrected DOIs/titles filed in a verification table; Khan 2026 — if no record can be verified, it cannot remain a cited study: remove it from the reference list and report an S1 sensitivity excluding Khan, with the incident logged. (Khan supplies 61% of the S1 denominator per R2/R7; the S1 pool's status must be re-judged after this.)

### Majors (merged, deduplicated; numbering for the response matrix)
- M1 Estimator reporting: GLMM/HK/study-level results reported together; abstract's "holds at 10.0-10.6% across sensitivities" labelled GLMM-conditional (R2-M1, R7-M1).
- M2 Clustering: add study-level (one pooled value per study) sensitivity — R2's check gave 11.7% (9.3-14.5) — or a three-level/cluster-robust refit; report in Results (R2-M2).
- M3 Derived counts disclosed: shares (P1 34/95 arms, 44.6% events; S1 27/38 units, 94.2% events) in Results; no-derived sensitivity's tau2/PI reported; 726 format-excluded responses (Draelos figure-only arm, Ariel) disclosed with the pool (R2-M4, R7-M3).
- M4 Quadrature description corrected (non-adaptive nodes as coded) and the independent refit's tau2 discrepancy (0.20 vs 0.304) reported (R2-M5).
- M5 Zero-event census corrected to 9 arms; HK 0.5-correction applies to all arms in code — text corrected; HK DL tau2 reported (R2-M8).
- M6 Buis double-count disclosed in both Results sections; ex-Buis sensitivity for the primary pool added (R3-M2, R2-M7).
- M7 S1 problematic pool: strata mixing disclosed (Si human-user arms inside S1 contradicts "kept apart at every stage" — correct the claim or move the arms); consistency of poolability judgement with S2 (either demote S1 to descriptive-with-HK or justify the asymmetry); S1 re-judged after Khan (R1-M1, R2-M6, R7-M5).
- M8 Red-flag subgroup premise corrected: Xiao 2026b DOES record high-risk-stratum unsafe counts (4/30, 6/30, 10/30) in the settled extraction — report that within-study contrast descriptively and correct the text (R1-M4).
- M9 Pool composition honesty: abstract and Description of studies state 19/24 single-topic sets and 19/24 China/Hong Kong-based sets; applicability section discusses geography/language/gatekeeping; Table 1 gains a setting column or the text carries it (R3-M1, R3-M4).
- M10 Practice implications narrowed: delete or reword "the base rate" authority; restore the one-study qualifier on the emergency-material claim (R3-M3, R5-Minor5 in substance, R4).
- M11 Disposition balance: overtriage exists in the data and is unreported — add the balancing figures/caveat; reference disposition not assumed infallible; Harada's unprinted red-flag numerator flagged wherever the red-flag concentration claim rests on it (R3-M5).
- M12 Si 2026 caveats travel with the comparison (standardised patients, China, two conditions, preprint) in Results (R3-M6).
- M13 Human-user findings reach abstract/PLS/conclusions: what human-user studies found (Bean; Si) stated, not only that response-level data are absent (R4-M3, R7-M4 in part).
- M14 PLS restructure: bench caveat in the first paragraph, GRADE very low + spread (PI) in the PLS, MH-crisis exclusion and undertriage told to the lay reader, 23-vs-24 confusion fixed, general signposting line for a worried reader (R4-M1, M2, M4, minors).
- M15 Applicability of populations: who is missing — question language overall, older users, low health literacy/digital confidence — discussed from the extraction data where recorded, and stated as unrecorded where not (R4-M5, R3-M4 in part).
- M16 Patient involvement: state plainly there was no patient/public involvement in the question, harm definition or PLS (R4-M6).
- M17 Ethics/governance basis for included evidence added (published aggregate data; primary studies' own governance; no patient-level data accessed by this review) (R5-M1).
- M18 Rule 1 pre-submission peer-review statement added to Declarations, verbatim: "The draft received structured multi-agent pre-submission peer review under the author's published protocol. The human author reviewed every comment and is accountable for the final text." (R5-M2).
- M19 AI-assistance note completed: name the tools as recorded in the team log (system, provider, access dates in Nov 2026) without inventing version numbers not in the record; align role descriptions between manuscript, abstract wording and PROSPERO form field 8; make the accountable-human adjudication chain explicit (R5-M3).
- M20 Conflicts declaration reconciled with "now building clinical AI": state plainly the author builds clinical AI tools not among the evaluated systems, has no interest in any evaluated system/vendor, and who bore tool costs if the funding line needs it (R5-M4, R5-Minor4).
- M21 Deviations consolidated: a single deviations paragraph/table — no pilot extraction (as prescribed by the review's own extraction form), coordinator scope rulings into and out of the pool (R3023, R2120 named), mental-health boundary adjudication, PROSPERO form completed but NOT submitted (stated in the manuscript, not only the form head), PRISMA item 24 corrected (R1-M2, R5-Minor1).
- M22 GRADE transparency: per-outcome GRADE domain table in the manuscript; inconsistency judgement for the primary outcome reasoned in the open (PI 3.8-26.2%), noting very-low is the floor (R1-M3).
- M23 Citation-chasing triage: limitation stated with its numbers (269/968 title-only exclusions), plus a sample re-screen of the excluded set by a second reader with the yield reported (R1-M5).
- M24 Search/PRISMA reporting: abstract "searched in full" wording fixed; raw search_run_log.json discrepancy corrected via an erratum note filed with the search log (raw file itself not rewritten silently); PRISMA 14/21 claims corrected or a reporting-bias passage added; 16b full-text exclusion reasons provided as a supplement; secondary-pool characteristics summarised (17); full search strategies filed as a supplement; Zenodo file list corrected to match the Data Availability promise (R6-M1..M6).
- M25 Differentiation paragraph rewritten honestly: the single-denominator point is the real one; empty human-user stratum not touted as a differentiator; this review's own unregistered status stated beside the competitor's overdue one (R7-M6).
- M26 Author-position bias: a Discussion paragraph reckoning with single human author + own LLM team making tier mapping, scope rulings and era cut-off, no timestamped external anchor, 4 flagged records unread by the author (R7-M8, R1 in part).
- M27 Title narrowed so it does not promise a real-world patient risk measurement (editor's ruling: keep the topic, add the evaluation-studies framing) (R7-M7, R4-M1 in part).
- M28 Narrative set quantified: the 121-study set gets quantified reporting of its main safety-relevant findings, not one unquantified paragraph (R7-M4).

### Minors and Nits
All Minors/Nits in the seven reports go into the response matrix individually (33 Minor, 20 Nit total). Minors with numbers attached (rounding, 23/24 PLS count, abstract terms "bench-only"/"response-level" unexplained, user-blaming sentence in narrative-set description) are fix-in-loop items under the protocol.

## Revision brief (ordered by severity)
1. B-D citations: full re-verification first, because Khan's status can change S1.
2. B-C + M1/M2/M4/M5: re-analysis pass with corrected intervals and all estimators reported.
3. B-A: tier table + strict-tier sensitivity + wording narrowing.
4. B-B + M8: era amendment, demotion, Xiao contrast reported.
5. M6/M7/M11/M12: pool-composition and disposition fixes.
6. M9/M13/M14/M15/M16/M27: framing, PLS, applicability, title.
7. M17-M20: declarations.
8. M21-M26, M28: transparency, GRADE, deviations, narrative set.
9. All Minors/Nits. Rebuild PDF/DOCX, visual QA of figure/table pages, de-AI audit re-run.
