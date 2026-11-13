# 📄 Download the full article — PDF

[![Download PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge)](https://github.com/rtmalikian/llm-chatbot-unsafe-advice-primary-care-meta-analysis/raw/main/manuscript.pdf)

**[Click here to download the PDF](https://github.com/rtmalikian/llm-chatbot-unsafe-advice-primary-care-meta-analysis/raw/main/manuscript.pdf)**

One click — no sign-up, no paywall.

---

# Unsafe or potentially unsafe advice from patient-facing large language model chatbots in bench evaluations of primary-care question sets: a systematic review and meta-analysis

**Review 4 of the Weekly Clinical AI Evidence Series**
Author: Raphael Malikian, independent researcher, Palmdale, CA, USA
Corresponding author: Raphael Malikian, rtmalikian@gmail.com
ORCID: 0009-0008-4326-4205

## What this review asked

Patients now ask general-purpose LLM chatbots the questions they once brought to primary care. This Cochrane-level systematic review and meta-analysis estimated the proportion of chatbot responses that clinician raters placed in a study's own worst safety tier, the tier labelled unsafe or potentially unsafe, for questions about primary-care presentations.

## Headline result

Across 95 model arms from 23 bench studies, 552 of 4,868 clinician-rated responses fell in the studies' worst safety tiers. The pooled proportion was 10.5% (95% CI 9.3 to 11.9) by random-effects generalised linear mixed model, with a 95% prediction interval of 4.5 to 22.7%. The Hartung-Knapp sensitivity gave 12.5% (11.3 to 13.9) and a strict-tier sensitivity (tiers labelled unsafe with no qualifier) gave 9.5% (8.0 to 11.2). GRADE certainty was very low for every pooled outcome.

No human-user study reported response-level safety ratings, so the human-user stratum could not be pooled. That absence is reported in the paper as a finding. The intermediate (problematic) tier and undertriage are reported study by study.

In total, 3,106 records were screened in duplicate and 166 studies were included (24 primary, 21 secondary, 121 narrative). The review passed the series multi-agent peer-review Gates 0 to 6 (pre-submission review by an LLM panel under a published protocol; this is not journal peer review) before deposit.

## What is in this repository

- manuscript.pdf, manuscript.md, manuscript.docx: the paper
- stage0-protocol: protocol and PROSPERO-ready form (no PROSPERO number has been issued; none is claimed)
- stage1-search and stage1-scoping-gate: search log, competitor registry re-check, and the go/no-go gate report
- stage2-screening: screening decisions and kappa computation
- stage3-extraction: both extraction passes and the settled sheets, both risk-of-bias assessors and the settled sheet
- stage4-analysis: analysis dataset, code (analysis.py, revision1 re-analysis with changelog), results, GRADE worksheets
- peer-review: the full Gates 0 to 6 record (panel, independent reviews, synthesis, response matrix, re-review, integrity gate)
- supplement files: tier-label table, full-text exclusions, secondary characteristics, search strategies, PRISMA checklists
- llm-team-log.md: transparency log for the LLM-team method

## How to reproduce the analysis

python3 stage4-analysis/analysis.py

## Citation

Malikian R. Unsafe or potentially unsafe advice from patient-facing large language model chatbots in bench evaluations of primary-care question sets: a systematic review and meta-analysis. 2026. Preprint (Zenodo): https://doi.org/10.5281/zenodo.24209763 (all-versions DOI: https://doi.org/10.5281/zenodo.24209762)

## Licence

CC BY 4.0 for text and data, MIT for code. The author welcomes collaboration and correspondence: rtmalikian@gmail.com
