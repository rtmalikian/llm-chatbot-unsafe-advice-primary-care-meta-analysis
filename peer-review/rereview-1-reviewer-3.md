# Re-review (Gate 5, loop 1) — Reviewer 3

Paper: Review 4 — Unsafe medical advice from patient-facing large language model chatbots in primary-care presentations: a systematic review and meta-analysis (revised title below)
Reviewer: Reviewer 3 — Bucket A. Primary care physician and former small-practice operator, 18 years community practice.
Date: 13 November 2026
Materials judged: my Gate 2 report (`reviewer-3.md`), response-matrix rows R3-1 to R3-15, the revised manuscript (`stage5-manuscript/manuscript.md`, revision 1, 13 November 2026), and `stage4-analysis/revision1/CHANGELOG.md` for the ex-Buis sensitivity.
Method: every verdict below is judged on the revised manuscript text itself, in line with Protocol Rule 5. The response matrix was used only to locate changes; a matrix claim with no corresponding text change would have been marked Unresolved. I filed no Blockers at Gate 2 and found no Rule 10 passage then; nothing in the revision changes that.

## Summary of verdicts

- **Resolved: 14** (all 6 Majors, 5 of 6 Minors, all 3 Nits)
- **Partly resolved: 1** (Minor R3-11)
- **Unresolved: 0**
- **New Majors introduced by the revision: none** (see final section)

## Majors

### R3-1 — Pool-composition honesty in title/abstract — **Resolved**
The retitle route I offered was taken, not the per-study justification column (the ask was either/or). New title: “Unsafe or potentially unsafe advice from patient-facing large language model chatbots in bench evaluations of primary-care question sets” — “bench evaluations” and “question sets” replace the promise of “primary-care presentations.” The Abstract’s Main results now states the composition a clinician reading only the abstract needs: “The primary pool holds 24 bench studies: 19 of the 24 use single-topic question sets and 19 of the 24 are based in China or Hong Kong.” Description of studies repeats it and names the exceptions (mixed sets Draelos 2026, Armbruster 2024 and Ariel 2026, with Xiao 2026a covering psychological support across chronic illness). The Plain language summary no longer implies undifferentiated everyday problems (see R3-10). An abstract-only reader can no longer take away the framing I objected to.

### R3-2 — Buis 2023 double-count disclosure + ex-Buis sensitivity — **Resolved**
All three parts are in the text. (1) Definition and dual entry: Results, Primary outcome states “For Buis 2023 the worst tier is a triage definition: an answer counts as unsafe when it recommends a lower level of urgency than the physician reference, which is undertriage. The same 23 events therefore enter this pool as worst-tier responses and the undertriage reporting as undertriage responses”; the same disclosure appears in the undertriage paragraph (“the same events as its primary-pool counts”), in Table 1 (tier label “unsafe (triage)”, topic note “same events counted as undertriage”) and in the Table 1 footnote. (2) The missing sensitivity is now fitted and reported in text and Table 2: excluding Buis 2023 (93 arms, 529 of 4,794) pools at 10.3% (9.2 to 11.7) by GLMM — which traces to the revision changelog’s 10.34% (9.16 to 11.65), the difference being rounding only — with the correct interpretation attached (“Buis does not drive the headline”). (3) The Background’s “means the same thing in every contributing study” claim is deleted; the Background now states the opposite honestly (most tiers are potentially unsafe/potentially harmful, some are major-error grades, “and one defines it by disagreement with a reference disposition”).

### R3-3 — Practice-implications narrowing (“base rate” removal, emergency qualifier) — **Resolved**
The phrase “base rate” appears nowhere in the revised manuscript. Implications for practice now offers “the bench range reported here, with its prediction interval and its very low certainty” as “the comparison such an evaluation can be set against; it is not an expected rate in real patient use, and a local audit should not be benchmarked against the single pooled figure” — the comparison the data supports, with the certainty attached in the same passage. The emergency sentence carries both qualifiers I asked for, in the Implications itself: “On emergency material the evidence is thinner: one emergency triage set sits at 31.1%, small emergency undertriage sets reach 41 to 52%, and no fitted subgroup test supports a general claim about emergency questions.” The one-in-ten restatement in the same section also carries “very low certainty” and the 5% to 23% range across new question sets.

### R3-4 — Geography / applicability (19 of 24 China/Hong Kong) — **Resolved**
Table 1 gains a Setting column for every primary study. The aggregate is stated at Abstract level (19 of 24 based in China or Hong Kong, R3-1 above) and in Description of studies with the full split: China 18, Hong Kong 1 (An 2026); United States (Buis 2023, Draelos 2026), Germany (Armbruster 2024), Türkiye (Bilgic 2026), and one multilingual study coordinated from Israel (Ariel 2026). The applicability consequence is stated where a clinician will see it, in Description of studies: “What counts as a primary-care question, which medicines are available, and what disposition is correct all differ between health systems, and most of these sets come from systems without the gatekeeping structure of, for example, British general practice; the pooled result should be read with that composition in mind.” Discussion, Completeness and applicability repeats the 19-of-24 composition. Question language is also now reported as recorded (bilingual An 2026; multilingual Ariel 2026 in six languages; the rest not stating interaction language beyond the interface).

### R3-5 — Overtriage balance (disposition framing) — **Resolved**
All three sub-asks are answered in the undertriage passage itself. (1) Overtriage: “overtriage (advising a higher level of care than the reference) is the other half of disposition behaviour, and it is barely extractable here: Buis 2023’s scale records a ‘too cautious’ category, but its counts were not extracted in poolable form, and Harada 2026 prints hard over-triage as absent in its mild slice (0 of 480). A system can score perfectly on undertriage by sending everyone to emergency care, and this evidence cannot judge that trade-off.” That is the explicit not-extractable statement plus the one printed count, which is the fallback route I specified. (2) Reference/safety-netting caveats, in the same passage: undertriage “is counted against a reference disposition that the review treats as correct; bench ratings cannot capture safety-netting advice in the same answer… which in practice is part of what makes a lower disposition safe or unsafe.” (3) Harada gap: the concentration sentence no longer rests on a missing numerator — the same paragraph first reports Harada 2026’s red-flag slice as printed percentages (hard undertriage 100% in both prompts under near-deterministic decoding; 100% and 99.7% under stochastic runs), states that “the exact numerator is not printed, because per-condition denominators are not printed, so the slice cannot enter the pool,” and only then concludes that undertriage “concentrates in emergency and red-flag material and in small vignette sets.”

### R3-6 — Si 2026 caveats travelling with the comparison — **Resolved**
The Results paragraph (Primary outcome: human-user stratum) now carries every caveat in the same paragraph as the numbers: “a standardised-patient field experiment in 62 primary health care institutions in China, on unstable angina and asthma presentations, reported as a 2026 preprint,” the counts flagged as derived, then “The physician figure itself shows how specific the definition and setting are… The comparison is not an estimate of how LLM advice compares with primary care physicians in routine practice.” The caveats also travel, in compressed form appropriate to each surface, wherever the LLM-versus-physician comparison itself (not merely the 67.7% figure) appears: Abstract (“in one standardised-patient field experiment… on definitions specific to that study”), Summary of findings (“on that study’s definitions, in standardised patients with two conditions in China,” certainty “Low at best”), and Plain language summary (“trained pretend patients in China… on that study’s own definitions”). The GRADE table likewise carries “Standardised patients, two conditions, one country for Si 2026.” No surface presents the near three-fold contrast bare.

## Minors

### R3-7 — Mental-health boundary — **Resolved**
Methods, Types of questions states the operational line at set level (a set whose primary content is crisis or self-harm advice was excluded; depression sets that are not crisis-only — Xiao 2026a and Xiao 2026b named — were included), and states the limit of what can be known: “Neither Xiao set separates crisis-specific items in its published counts, so no crisis items were separately excluded at extraction.” Deviations (4) records the same adjudication. The reader is told both the rule and that item-level presence of crisis content is not separable in the published sets, rather than being given a false assurance.

### R3-8 — Scope ruling reconciled with Buis, Lv and Wang C — **Resolved**
Methods, Types of questions now works the three borderline cases I named: the Buis 2023 general emergency-department triage set “stayed in because its cases are general presentations”; Lv 2026 (myocardial infarction public education) “stayed in because recognising an emergency and acting on it is first-contact content”; Wang C 2026 (paediatric burn first aid) “stayed in because first aid is what a parent asks first”; and a single-specialty ophthalmological emergency-protocol set “was ruled out on the same standard.” The boundary can now be judged rather than trusted.

### R3-9 — “Primary care is where most of these questions belong” — **Resolved**
Background paragraph 1 now reads: “Primary care is a natural frame for a safety estimate, since these are the questions a family doctor fields first when a patient can reach one.” The unsupported population claim is gone; the softened claim is the one the review needs.

### R3-10 — Plain language summary framing — **Resolved**
“Everyday health problems” is gone. The summary opens with the bench caveat before any number (“This review is about test questions, not about answers real patients received… It is not the chance that an answer you received was unsafe”), describes the sets as health questions researchers wrote and put to chatbots, and singles out the emergency department triage set separately (R3-13). The lay framing now matches the corrected professional framing.

### R3-11 — Narrative claim “people often follow chatbot advice” unquantified — **Partly resolved**
What is fixed: “often” is removed (now “people tending to follow them”), and the Narrative set section names the human-user studies in the same paragraph with what each measured (Zhao 2026: 120 postpartum women rating answers to their own 360 questions, on scale scores only; Gomez 2024: triage accuracy and confidence change; Mingole 2026: harm-scale means; Bean 2026 on decision outcomes in the secondary set). What remains: the concluding follow claim itself is still not tied to any one named study’s measured following/adherence count or denominator — none of the measurements listed beside it quantifies following, and the Plain language summary repeats the sentence (“people tended to follow them, including answers the study team judged wrong”) with no study named at all. One sentence naming which study measured following, and its count, or a further downgrade of the claim to what those listed measures show, would close this. Minor severity; it does not hold the gate.

### R3-12 — “Bench” and “disposition” used before definition — **Resolved**
Abstract Objectives glosses bench at first use (“studies in which investigators put test questions to a chatbot and clinician raters grade the answers afterwards”), and Objectives item 2 glosses disposition at first use (“a disposition is the level of care an answer advises, such as self-care, routine primary care, urgent care or emergency care”).

## Nits

### R3-13 — PLS should name the emergency set as emergency-department triage — **Resolved**
Plain language summary: “one emergency department triage set produced about 3 in 10.”

### R3-14 — Table 1 topic labels in consistent (condition-first) form — **Resolved**
Xiao 2026a now reads “Depression and anxiety (psychological support in chronic illness)” — condition first, study aim in parentheses — and the remaining Table 1 topics follow the same condition-first form.

### R3-15 — Promote the variation content into Authors’ conclusions — **Resolved**
Abstract, Authors’ conclusions now leads with the pooled figure and the variation together: “about one response in ten… with wide variation between question sets (prediction interval 4.5 to 22.7%) and very low certainty” (the interval is the revision’s updated 4.5 to 22.7%, correctly carried through).

## New Majors introduced by the revision

**None.** I checked the changes within my remit for new over-claims: the relabelled outcome in the title, the estimator range in the Plain language summary (1 in 10 to 1 in 8, explained as method-dependent), the Harada red-flag percentages in the Summary of findings (carried as “about 100% by percentage, with the exact count not printed”), and the new Implications sentence on local audits (which narrows, rather than widens, the claim). None introduces a new Major, and no new Rule 10 clinical-advice passage appears; the added Plain language signposting sentence is general information (“check it with your own doctor, pharmacist or local urgent care service”), not individual advice.

## Gate 5 position (Reviewer 3)

All six of my Majors are Resolved on the revised text; the single Partly resolved item is a Minor (R3-11) with the remainder stated exactly above. From this reviewer’s seat there is nothing left that loops back to Gate 4 as a Major.
