# Review 4 — Concept and Protocol (v1, dated 2026-11-12)

## Title
Unsafe medical advice from patient-facing large language model chatbots in primary-care presentations: a Cochrane-level systematic review and meta-analysis

## Status
Gap scan completed 2026-11-12 (12/15, top pick). Protocol fixed before screening, per Cochrane-Level Standard v2 (Robust). NOT yet registered on PROSPERO — no registration number is claimed. Registration is the immediate next step and must cite and differentiate from CRD420261347066.

## Why this topic
- No meta-analysis this week: Reviews 1-3 are complete (ambient scribes, 2026-10-22; LLM citation fabrication, 2026-10-22; clinical summarisation errors, 2026-10-31). Week 4 and Week 5 of the weekly series were papers, not meta-analyses.
- Wearable AF alerts, the 2026-10-31 fallback (13/15), is now closed as framed: PROSPERO CRD420261455991 (registered 21 Jul 2026, planned end 19 Sep 2026) and CRD420261489388 (30 Aug 2026) cover its downstream outcomes. Residual anxiety/utilisation slice has no shared denominator (<8 studies per outcome) — Review 3 trap risk.
- Patient-facing LLM harm was next on 2026-10-31 (12/15) and re-scored 12/15 on 2026-11-12, now top.
- Demand signals (gap scan): ECRI ranked AI chatbot misuse #1 health technology hazard for 2026; ChatGPT Health launched 7 Jan 2026 with >230M people/week asking health questions; Draelos et al. npj Digit Med 2026 reported unsafe responses 5% to 13-13.5% across 888 responses to 222 primary-care questions; Bean et al. Nat Med 2026 (n=1,298 RCT) found models alone identified conditions in 94.9% of cases vs <34.5% for patients using them, no better than control.
- Anchor review Huo et al. JAMA Network Open 2025: 137 studies, search ended 27 Oct 2023, only 13 primary-care, <1/3 addressed safety, no pooled harm rate.

## PICO
- P: Laypeople seeking advice for primary-care presentations. Two strata, analysed separately, never pooled together: (a) bench response-evaluation studies, (b) human-user experimental studies.
- I/E: General-purpose LLM chatbot used directly by the layperson, no clinician in the loop, 2023-2026, any version.
- C: Blinded clinician / guideline reference (bench) or usual sources / control (human-user).
- O: See primary outcome.

## Primary outcome — exact denominator (anti-Review-3 safeguard)
Proportion of responses rated unsafe = responses in the study's explicit unsafe / harmful / dangerous tier ÷ total responses rated for safety.
Studies without that numerator and denominator are excluded from the primary pool and listed. No accuracy score, readability, or empathy measure is a primary outcome.

## Secondary outcomes
- Problematic / inaccurate proportion (same denominator, separate pool)
- Undertriage: responses advising a lower disposition than reference ÷ responses with a reference disposition
- Fabrication: responses with at least 1 fabricated medical fact ÷ responses rated for fabrication

## Pre-specified subgroups (max 3)
1. Bench vs human-user
2. Red-flag / emergency vs non-urgent presentations
3. GPT-3.5-era vs GPT-4/4o-era and later (model family as sensitivity)

## Go / no-go gate — Stage 1 scoping screen
Proceed to full screening only if the scoping screen finds at least 15 studies reporting the primary numerator/denominator, covering at least 3 models and at least 2,000 responses. Expected from the gap scan: 25-40 such studies (estimate, not a scoping count). If the gate fails, activate the fallback immediately: AI symptom checkers / self-triage undertriage (9/15; primary denominator = cases with urgent/emergency reference disposition advised lower ÷ all cases with urgent/emergency reference disposition).

## Differentiation from CRD420261347066
That registration (25 Mar 2026, planned end 31 Jul 2026, still listed ongoing at 2026-11-12, no publication located in the scan): non-randomised only, no GRADE, no reporting-bias assessment, no single harm denominator. Review 4 differentiates on: single pre-specified harm denominator, primary-care presentations only, human-user RCTs included, GRADE applied, CHART-informed risk of bias. Re-check the guarantors' names on PubMed / Scholar on registration day — absence in the scan is not proof of non-publication.

## Boundaries
- Rate published advice descriptively. Make no medication-specific or clinical recommendations.
- Mental-health crisis / self-harm advice excluded from the primary pool (narrative appendix only).
- Date-stamp every result by model version and search date. Conclusions are about models evaluated 2023-2026, not a verdict on a current product.
- Reviews 1-3 topics are excluded. Dedicated non-LLM symptom-checker apps belong to the fallback, not this review.

## Method (Standard v2 summary)
Protocol first; full retrieval, blocked sources retried twice; dual independent screening with real adjudication by reading; two fully independent extractions with field-by-field discrepancy rate; RoB in duplicate, adjudicated by reading (adapted tool pre-specified, named as adapted); random-effects meta-analysis with tau-squared, I-squared, prediction intervals, Hartung-Knapp or justification; GRADE per critical outcome; forest plots with summary diamonds and logged visual inspection of every figure page; multi-agent peer review Gates 0-6 before any Zenodo / journal / conference step; free publication only.

## Files
- Gap scan report: ~/workspace/research_notes/review4-gap-scan-health-tech-family-medi-20261113-0049/report.md
- This protocol: concept-and-protocol.md in this folder
