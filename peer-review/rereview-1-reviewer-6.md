# Re-review (Gate 5, loop 1) — Reviewer 6

Paper: Unsafe or potentially unsafe advice from patient-facing large language model chatbots in bench evaluations of primary-care question sets: a systematic review and meta-analysis (Review 4, revision 1)
Reviewer: Reviewer 6 — Bucket H. Information specialist / reporting-guidelines editor.
Date of re-review: 2026-11-13
Materials judged: the revised manuscript itself (`stage5-manuscript/manuscript.md`), the corrected `stage5-manuscript/prisma-checklists.md`, `peer-review/citation-reverification.md`, `peer-review/response-matrix.md` (Reviewer 6 rows R6-1 to R6-24), and the files on disk in the package. Words-only answers were treated as Unresolved; every "Fixed" claim below was checked against a file, not against the matrix.

## Verdict counts (my 24 original comments)

- **Resolved: 21**
- **Partly resolved: 3** (R6-14, R6-15, R6-21 — remainders specified below)
- **Unresolved: 0**

Blockers: 9 of 9 resolved (Blocker 9, Khan, ruled separately below — the revision's rebuttal is **accepted**, on the documented-source route my original comment itself offered).
Majors: 4 of 6 resolved, 2 partly resolved.
Minors: 5 of 6 resolved, 1 partly resolved.
Nits: 3 of 3 resolved.
**New Majors introduced by the revision: 1** (see final section).

## Package inventory (verified on disk, Gate 5)

`stage5-manuscript/` now contains, in addition to the manuscript, PDF and DOCX:

- `supplement-fulltext-exclusions.csv` (PRISMA 16b)
- `supplement-search-strategies.md` (PRISMA item 7 / PRISMA-S)
- `supplement-secondary-characteristics.csv` (PRISMA item 17, secondary pool — see the new Major)
- `supplement-tier-labels.csv`
- `prisma-checklists.md` (corrected at revision 1)

Also verified: `stage1-search/raw/ERRATUM-2026-11-13.md`; the authoritative-record note appended to `stage1-search/search-log.md`; the corrected file list in `zenodo-package/zenodo-metadata.md`; the corrected conference abstract in `journal-package/journal-shortlist.md`; the incident entries in `llm-team-log.md`.

---

## Blockers 1–9 (merged blocker B-D: the citation record)

The revision did what my report demanded and more: it re-verified **all 49 drafted references** at title-page level (`citation-reverification.md`), not just my sample of 18, and found the fault was wider than my sample — **15 corrected DOIs** (I had named 8), **1 corrected title**, **12 completed entries**, 0 unverifiable. The pattern I inferred (DOIs harvested from inside other papers' reference lists) is confirmed in the revision's own table and logged as Incident 2 in `llm-team-log.md`, with a standing rule recorded. The revised reference list in the manuscript carries the corrected identifiers, full journals and DOIs throughout; I checked every one of my nine entries against the printed list.

| # | Entry | Status | Evidence in the revised files |
|---|---|---|---|
| 1 | Miao 2026 | **Resolved** | Manuscript now cites Front Reprod Health 2026;8:1967818, doi:10.3389/frph.2026.1967818. Independently verified by me (below). |
| 2 | Zuo 2026 | **Resolved** | Manuscript now cites Front Public Health 2026;14:1926980, doi:10.3389/fpubh.2026.1926980, with the full title ending "…for traumatic brain injury and concussion questions". Independently verified by me (below). |
| 3 | Gong 2026 | **Resolved** | Manuscript now cites Front Public Health 2026;14:1924162, doi:10.3389/fpubh.2026.1924162, journal supplied — the identifier I gave in my report. |
| 4 | He 2026 | **Resolved in the reference list** | Manuscript now cites iScience 2026;29(3):115002, doi:10.1016/j.isci.2026.115002. (The superseded DOI survives in one supplement — see the new Major; that is a supplement fault, not a reference-list fault.) |
| 5 | Liang 2026 | **Resolved** | Manuscript now cites Front Public Health 2026;14:1955701, doi:10.3389/fpubh.2026.1955701, journal supplied. |
| 6 | Armbruster 2024 | **Resolved** | Manuscript now cites J Med Internet Res 2024;26:e58831, doi:10.2196/58831. Independently verified by me (below). |
| 7 | Huo 2025 (anchor review) | **Resolved** | Manuscript now cites the JAMA Network Open version, 2025;8(2):e2457879, doi:10.1001/jamanetworkopen.2024.57879. Independently verified by me (below). |
| 8 | Ariel 2026 (title) | **Resolved** | Manuscript now cites the title-page title, "Asymmetry between warmth and clinical substance in multilingual consumer health AI", doi unchanged. I confirmed the title against the filed title page (`stage3-extraction/fulltexts/R2111.txt`, medRxiv page header, Dean Ariel et al., same DOI). The revision's explanation — the draft had used Crossref's metadata title — is recorded in the verification table, so a reader arriving by either title can reconcile them. |
| 9 | Khan 2026 | **Resolved — rebuttal accepted** | Ruled separately below. |

### Blocker 9 (Khan 2026): ruling on the rebuttal

**The rebuttal is ACCEPTED. My "unverifiable" verdict does not stand, and the study may ship — on the documented-source ground, which was one of the three fixes my original comment offered.**

My independent evidence, gathered at this re-review:

1. **The filed full text is a genuine, internally consistent medRxiv preprint.** `stage3-extraction/fulltexts/R3040.txt` (28,758 bytes) opens with the exact cited title, "Clinical Safety of AI-Generated Antibiotic Prescribing Advice: Guideline Adherence and Misinformation Risk Among Large Language Models", authors Muhammad Mohsin Khan and Muhammad Naveed Anwar, University of Agriculture, Faisalabad, corresponding-author email, and the medRxiv footer line carrying the DOI string `10.64898/2026.05.13.26352828`, "posted May 15, 2026" and the CC-BY 4.0 licence notice. This is the publisher's own stamped first page, not a document the review team could have typed up to match a citation.
2. **The search record predates the dispute and is independent of the revision.** Row R3040 in `stage1-search/search-results.csv` — produced by the 12 November 2026 search run, before my report existed — records the source as Semantic Scholar, paper ID `70865e4901829704784261355af7cbe2635dc9a7`, with the same DOI, the same title and the same abstract. The revision did not create this record; it found it, which is what `citation-reverification.md` claims.
3. **The counts match.** The full text prints 1,000 vignettes × 5 models = 5,000 evaluations, 76.2% guideline-concordant, 328 responses (6.6%) unprompted overprescription and 17.3% coercion-mediated; the settled extraction's 1,191 inappropriate of 5,000 is the paper's own printed inappropriate total and is consistent with those printed components. The study extracted is the study cited.
4. **What I could not reproduce — stated plainly.** My own fresh web searches at this re-review (DOI string, exact title, Semantic Scholar and Crossref-flavoured queries) again returned **no** Khan record, exactly as on 2026-11-13. General web search does not surface this preprint. The revision's Crossref claim is therefore the one leg of its three-legged stool I could not independently re-walk; the other two legs (filed publisher-stamped full text; pre-existing Semantic Scholar search record) I verified myself and they agree with each other and with the extraction.

Ruling: Protocol Rule 7 bars a citation that *cannot be verified or does not resolve to the paper cited*. Khan now resolves, inside the package, to a reachable, checkable source whose title, authors, DOI and counts all match the citation — the third remedy my Blocker 9 itself specified ("document the source in the package so a Gate 6 checker can reach it"). The residual weakness is discoverability, not verifiability: a reader outside the package who types the DOI into a search engine may still find nothing. Two conditions, neither blocking at Gate 5: (a) the Zenodo deposit must include the Khan full text or a direct medRxiv link that Gate 6 confirms resolves — the current Zenodo list deposits the extraction sheets but does not name the fulltexts folder; (b) the manuscript's handling is already correct and must not soften — Khan is flagged at every use (61.1% of the problematic denominator, undescribed classification of 5,000 responses, D3 High), the problematic pool is demoted to study-by-study reporting, and Khan enters no pooled headline. The incident is logged from both sides in `llm-team-log.md` (Incident 1), which is the honest way to keep it.

### Independent re-check of corrected DOIs (my own lookups, 2026-11-13)

Four of the corrected identifiers were re-verified by me against real sources, outside the package:

- **Miao 2026 — correct.** The Frontiers in Reproductive Health record (published 17 September 2026) carries doi:10.3389/frph.2026.1967818, authors Miao L, Gu L, Gong Z, Gu Z, Qian X, Front Reprod Health 8:1967818 — and its results match the extraction: 61 questions × 5 interfaces = 305 responses, 31 (10.2%) classified unsafe or potentially unsafe, exactly Table 1's 31/305.
- **Zuo 2026 — correct.** Frontiers in Public Health record and PubMed (PMID 42745758) both carry doi:10.3389/fpubh.2026.1926980, Front Public Health 2026;14:1926980, Zuo X, Zuo H, Zhang M, Zheng W; 65 questions, 325 responses, 27 classified as potentially harmful — matching Table 1's 27/325.
- **Armbruster 2024 — correct.** The JMIR record carries J Med Internet Res 2024;26:e58831, doi:10.2196/58831, "Doctor ChatGPT, Can You Help Me?" The Patient's Perspective: Cross-Sectional Study, Armbruster J et al. — the paper whose identity matters for the early-era level is now beyond dispute.
- **Huo 2025 — correct.** PubMed (PMID 39903463; PMCID PMC11795331) carries Huo B et al., "Large Language Models for Chatbot Health Advice Studies: A Systematic Review", JAMA Network Open 2025;8(2):e2457879, doi:10.1001/jamanetworkopen.2024.57879 — the anchor review is now cited by its real identifier.

Four for four. Combined with the revision's full 49-entry table (whose internal detail — e.g. the Shi/Tan DOI swap at entries 23/47, the Gu and Hao corrections I had not sampled — is of a kind that cannot be produced without actually resolving each record), I accept the re-verification as complete. The citation promise is repaired.

---

## Majors

**Major 1 (R6-10) — abstract "searched in full" wording. RESOLVED.**
The revised abstract no longer contains the self-contradictory sentence. It now reads that PubMed, Europe PMC, Semantic Scholar and ClinicalTrials.gov "were searched on 12 November 2026", that "one OpenAlex route (title and abstract search) was searched in full", that "a second OpenAlex route (full-text search) was retrieved only in part and is not counted as searched", and names all six not-run sources in the same paragraph. The conference abstract in `journal-package/journal-shortlist.md` is corrected the same way (I read it: the partial route is named and not counted, and kappa is now labelled — three-way 0.52, binary 0.59 — which also settles the venue-fit flag in my domain check).

**Major 2 (R6-11) — raw search log contradiction. RESOLVED.**
`stage1-search/raw/ERRATUM-2026-11-13.md` exists, is dated, and does exactly what I asked: the raw file is **not** rewritten; the erratum reconciles all three discrepancies (the "searched in full" OpenAlex label, the 3,675/3,077 totals against the corrected 3,732/3,106, and the missing route-2 entry) and `stage1-search/search-log.md` now carries an explicit authoritative-record note naming itself authoritative and the raw JSON erroneous-but-preserved. A reader tracing the flow numbers now hits the correction in the raw folder itself.

**Major 3 (R6-12) — PRISMA items 14 and 21 claimed without manuscript text. RESOLVED.**
The manuscript now contains a headed **Reporting bias** section in Methods stating what was and was not assessed and why (no funnel-based test, with the single-arm-proportions reason; preprint coverage; the 138 unretrieved reports and the partial OpenAlex route named as the standing risks), and the substance is carried into the Discussion. The corrected checklist items 14 and 21 now point at text that exists. The checklist no longer promises what the paper does not contain.

**Major 4 (R6-13) — PRISMA item 16b supplement. RESOLVED.**
`supplement-fulltext-exclusions.csv` exists in the manuscript folder, is cited in Methods ("Full-text exclusions with reasons are filed as a supplement (PRISMA item 16b)"), and is formatted as a supplement with a reconciling header. I recounted it: 351 data rows = 321 eligibility exclusions with reason codes FT-R1 to FT-R7, plus 3 coordinator scope-ruling exclusions, plus 27 duplicate-link rows listed separately — exactly the composition the header and the response matrix claim, and consistent with the flow numbers (431 assessed − 324 − 21 = 86).

**Major 5 (R6-14) — PRISMA item 17, secondary and narrative characteristics. PARTLY RESOLVED.**
What is done: the narrative set is now characterised in aggregate with quantified outcome forms in the Narrative set section, and the corrected checklist entry states plainly that "no per-study narrative listing is presented" — the honest narrowing I offered as the alternative route. What remains, exactly:
(a) The secondary-characteristics supplement covers only **11 of the 21** secondary-pool studies — the search-arm eleven. The 10 citation-chasing secondary studies have no characteristics rows anywhere.
(b) The manuscript's Results text overclaims against its own supplement: "their characteristics are summarised in the secondary-characteristics supplement" is written of all 21 studies.
(c) The supplement itself contains a citation error and an incomplete row — detailed as the new Major below.
Remainder to close: extend the supplement to all 21 (the settled chasing extraction exists to build it from), correct the He DOI row, complete or annotate the Ratneswaran row, and align the Results sentence with whatever the supplement actually covers.

**Major 6 (R6-15) — search-strategy supplement and Zenodo file list. PARTLY RESOLVED.**
What is done, and it is most of the ask: `supplement-search-strategies.md` exists as a numbered supplement with the per-source strings as run, per-source counts, the citation-searching account and the not-run strings labelled NOT RUN; and the Zenodo file list in `zenodo-package/zenodo-metadata.md` now includes the search log, the search scripts, the raw outputs with their erratum, the stage-2 screening folder, the RoB sheets (both assessors and settled), all four manuscript supplements, the citation re-verification table and the team log. The deposit as now listed would let a reader inspect the search. What remains, exactly — the list still does not match the manuscript's Data availability statement **file for file**, which was my stated test:
(a) The Data availability statement promises "the GRADE worksheets"; the Zenodo list names no GRADE file (`stage4-analysis/grade-framework.md`, `grade-assessment.md` are not in items 1–10).
(b) The statement promises "the extraction sheets (both passes and settled…)"; Zenodo item 5 lists only the two settled CSVs, not the extractor A/B pass files.
Either add those files to the list or trim the statement; at present the two documents still disagree in detail, in the direction of the statement promising more than the deposit delivers — the same direction as the original fault, at much smaller scale.

---

## Minors

| # | Comment | Status | Note |
|---|---|---|---|
| Minor 1 (R6-16) | Abstract lacks registration and funding lines | **Resolved** | Both lines now close the abstract ("Registration… has not been submitted"; "Funding. None…"); checklist item 2 corrected to match. |
| Minor 2 (R6-17) | Not-run sources missing from Methods | **Resolved** | The Methods search paragraph names Embase, Scopus, Web of Science, CINAHL, CENTRAL **and OpenAIRE**; the abstract, Methods, Discussion, search log and checklist lists are now identical (also settles Nit 3). |
| Minor 3 (R6-18) | Semantic Scholar "searched in full" overstatement | **Resolved** | Methods now carries my suggested qualification almost verbatim: bulk route after the graph route's HTTP 429; "the bulk endpoint reports no total hit count, so the 81 records are the retrieved set, not a verified complete set." Checklist item 6 says the same. |
| Minor 4 (R6-19) | Chasing title triage: operator and rule unstated | **Resolved** | Methods now states the operator (the review team's information-specialist role), the rule, its known product-name gap, the awkward fact that 10 of the 269 titles do name technology (so the logged rule was not a pure keyword rule), and the revision re-screen (random 50 of 269, seed recorded, 0 eligible; the 10 technology-named titles checked individually). This is more disclosure than I asked for. |
| Minor 5 (R6-20) | Reference style; Bean and Page DOIs; truncated titles | **Resolved** | The list is rebuilt: journal, year and DOI for every entry; Bean gains doi:10.1038/s41591-025-04074-y; Page gains doi:10.1136/bmj.n71; An's full title is restored ("…and Prompt Optimization Study"). One copy-edit residue, not a blocker: a few titles still drop their published subtitles (Zuo's entry in the list is otherwise the full corrected title; Miao's omits the ": safety, accuracy, guideline concordance, empathy, and readability" subtitle the publisher record carries). Regularise at copy-edit. |
| Minor 6 (R6-21) | Protocol: no public location; same-day dating unevidenced | **Partly resolved** | The same-day dating is now disclosed openly in the manuscript itself (Author position: "the protocol in the review package is dated 12 November 2026, the same day as the search", with no external timestamp claimed) and in checklist item 24 — the evidence-by-disclosure half is done, and done honestly. The public-location half remains undone: no deposit, DOI or URL exists, and the response matrix correctly records this as an author step barred at this revision. It must be closed at the deposit gate, alongside the Khan condition above. |

## Nits

| # | Comment | Status | Note |
|---|---|---|---|
| Nit 1 (R6-22) | Author truncation; Xiao suffix placement | **Resolved** | Entries regularised to first author plus "et al." throughout. The (2026a)/(2026b) suffixes remain beside the Xiao author lines; the revision's reason (two same-author, same-year papers must be distinguishable in text citations) is sound and is the standard solution. |
| Nit 2 (R6-23) | PRISMA diagram merges databases and registers | **Resolved** | Checklist item 16a now notes the merged identification box and points to the per-source split in the search log and the search-strategy supplement, which carries it. |
| Nit 3 (R6-24) | OpenAIRE in checklist only | **Resolved** | OpenAIRE is now named in the abstract, Methods and Discussion not-run lists; all lists identical. |

---

## New Major introduced by the revision (stated explicitly, 1)

**New Major 1 — the revision-created secondary-characteristics supplement propagates a corrected-away DOI error and does not cover the set it claims to cover.**
`stage5-manuscript/supplement-secondary-characteristics.csv` was created at this revision to discharge PRISMA item 17. It contains 11 data rows for a 21-study pool (see Major 5 above), and its He 2026 row (R0916) gives the DOI as **10.1007/s10916-023-02021-3 — the very identifier Blocker 4 removed from the manuscript because it resolves to Song et al. 2023 (urolithiasis), not to He et al.** A reader who follows the supplement's DOI lands on the wrong paper, which is the original Blocker fault surviving in a file the revision itself created; it also proves the supplement was built from the uncorrected extraction list rather than from the re-verified records. The same file's Ratneswaran 2026 row has an empty `outcomes_contributed` field. Fix: rebuild the supplement from the verified reference records (He = doi:10.1016/j.isci.2026.115002), extend it to all 21 secondary studies, and complete the Ratneswaran row. This is a Major, not a Blocker, for one reason only: the manuscript's own reference list — the citation of record — is correct, and the supplement is a characteristics table, not the synthesis. It must still be fixed before deposit, because the supplement is on the Zenodo list and the fault is precisely the one this revision exists to repair.

No other new Majors. I specifically re-checked the places a revision of this size usually breaks: the abstract's search wording against the search log (consistent), the checklist's corrected items against manuscript text (14, 16a, 16b, 17, 21, 24 all now point at real text or files, with item 17's narrative limitation stated in the entry itself), the flow arithmetic in the new supplement (reconciles), and the conference abstract (corrected, not merely promised).

## Closing

At Gate 2 I wrote that checklists are promises and this one's citation promise was broken. At revision 1 the promise is kept in the manuscript itself: every reference re-verified, four of the corrections independently confirmed by me against publisher and PubMed records, the Khan rebuttal accepted on documented evidence with its discoverability caveat kept on the record, the raw-log contradiction corrected by erratum rather than by silent overwrite, and items 14, 16b and 21 now discharged by text and supplements that exist. Three remainders keep this from a clean pass, all of them small, named and fixable without new analysis: the secondary supplement's coverage and its one wrong DOI (new Major 1 / Major 5), the two-file gap between the Data availability statement and the Zenodo list (Major 6), and the still-outstanding public protocol location (Minor 6), which belongs to the deposit gate in any case. **Recommendation: the revision answers my report; pass Gate 5 from this bucket conditional on those three remainders being closed and re-checked at Gate 6, with the Khan full text (or a confirmed-resolving medRxiv link) included in the deposit.**
