# Gate 6 — Final Integrity Gate, Review 4

**Gate agent:** Gate 6 final integrity agent (fresh session; did not review this paper at Gates 0–5).
**Date:** 2026-11-13.
**Paper checked:** `stage5-manuscript/manuscript.md`, `manuscript.pdf` (30 pages, pdfinfo-verified), `manuscript.docx`.
**Protocol:** `~/workspace/work/peer-review-system-20261105/repo/PROTOCOL.md`, Gate 6 + `prompts/05_integrity_gate.md`.
**Method:** every item below was verified by this agent against the files, the analysis outputs and external sources. Claims in the peer-review record were treated as the record to audit, not as evidence.

---

## Item 1 — References: FAIL

`peer-review/citation-reverification.md` (49 entries as drafted, 50 as revised; 15 DOIs corrected) was taken as the record to audit. I independently resolved **12 DOIs through the Crossref API** on 2026-11-13 and compared author, year, title and venue with the final reference list:

| Reference | Independent result |
|---|---|
| Huo 2025, doi:10.1001/jamanetworkopen.2024.57879 | **Verified.** Crossref: Huo, Boyle, Marfo et al., 2025, JAMA Network Open, "Large Language Models for Chatbot Health Advice Studies". Matches the corrected record; the draft's arXiv DOI was indeed wrong. |
| Miao 2026, doi:10.3389/frph.2026.1967818 | **Verified.** Crossref: Miao et al., 2026, Frontiers in Reproductive Health, bacterial vaginosis title as cited. |
| Armbruster 2024, doi:10.2196/58831 | **Verified.** Crossref: Armbruster, Bussmann, Rothhaas et al., 2024, JMIR, "Doctor ChatGPT, Can You Help Me?" as cited. |
| Khan 2026, doi:10.64898/2026.05.13.26352828 | **Verified.** Crossref resolves to Khan MM, Anwar MN, "Clinical Safety of AI-Generated Antibiotic Prescribing Advice…", 2026. Filed full text `stage3-extraction/fulltexts/R3040.txt` carries the same title, authors, posted date (15 May 2026) and DOI on its first page. Its settled extraction rows (5 arms × 1,000) sum to 1,191 problematic of 5,000, matching the re-verification record. |
| Draelos 2026, doi:10.1038/s41746-026-02428-5 | **Verified.** Crossref: Draelos, Afreen, Blasko et al., 2026, npj Digital Medicine, "Large language models provide unsafe answers to patient-posed medical questions". |
| Bean 2026, doi:10.1038/s41591-025-04074-y | **Verified.** Crossref: Bean, Payne, Parsons et al., 2026, Nature Medicine, "Reliability of LLMs as medical assistants for the general public: a randomized preregistered study". |
| An 2026, doi:10.2196/105778 | **Verified.** Crossref: An, Huang, Cheung et al., 2026, JMIR, cancer survivorship title as cited. |
| Page 2021, doi:10.1136/bmj.n71 | **Verified.** Crossref: Page, McKenzie, Bossuyt et al., 2021, BMJ, PRISMA 2020 statement. |
| Gong 2026, doi:10.3389/fpubh.2026.1924162 | **Verified.** Crossref: Gong et al., 2026, Frontiers in Public Health, hand, foot and mouth disease title as cited (corrected DOI confirmed). |
| Ramaswamy 2026, doi:10.1038/s41591-026-04297-7 | **Verified.** Crossref: Ramaswamy, Tyagi, Hugo et al., 2026, Nature Medicine, "ChatGPT Health performance in a structured test of triage recommendations". |
| Ariel 2026, doi:10.64898/2026.05.09.26352813 | **Verified, with the documented variant.** Crossref resolves the DOI to Ariel et al. 2026 under the Crossref-metadata title ("Consumer chatbots gave similarly empathic answers…"); the manuscript cites the medRxiv title-page title, and the re-verification record documents both. Not a mismatch. |
| Buis 2023, doi:10.2196/49995 | **MISMATCH — author attribution wrong.** Crossref's author list for this DOI is Fraser, Crossland, Bacher, Ranney, Madsen, Hilliard — there is no author named Buis. PubMed (PMID 37788063) cites the paper as "Hamish Fraser et al., JMIR Mhealth Uhealth 2023", and the JMIR article page lists the same six authors; Lorraine Buis appears on that page as the journal **editor** ("Edited by L Buis"). The re-verification record's row 6 assertion "(first author Buis; Fraser is fourth author)" is itself incorrect. DOI, title, journal and year are correct, and the study's numbers are unaffected (2 arms, 23/74), but the manuscript cites the study as "Buis L, et al." and labels it "Buis 2023" throughout: reference list, Table 1, Table 2 ("Excluding Buis 2023"), Figures 1 and 3, the extraction/analysis study_id, and 17 occurrences in the DOCX. Under Protocol Rule 7 a reference whose author does not verify does not ship. |

**Result: 11 of 12 independently verified; 1 mismatch (Buis 2023 → Fraser et al. 2023). Item FAILS.**

## Item 2 — Headline numbers: PASS

Traced against `stage4-analysis/revision1/revision1-results.json` and by my own re-summing of `stage4-analysis/analysis-dataset.csv` and the manuscript's Table 1:

- Primary GLMM **10.5% (95% CI 9.3–11.9)** — analysis: 10.53% (9.29–11.92). ✓
- Hartung–Knapp **12.5% (11.3–13.9)** — analysis: 12.51% (11.26–13.86). ✓
- Study-level **11.7% (9.3–14.5)** — analysis HK study-level: 11.66% (9.34–14.46); the study-level GLMM (10.3%, 8.2–13.0) is also reported in Table 2. ✓
- **95 arms, 23 studies contributing arms of 24 in the primary pool** — re-sum of analysis-dataset P1 rows: 95 rows, 552 events, 4,868 total, 23 distinct record_ids (the 22 study_id labels collapse Wang C 2026 and Wang Y 2026 into "Wang, 2026"; the revision script counts by record_id). The 24th primary study is Ariel 2026, which contributes no arms (Table 1, 0 arms). ✓
- **552/4,868, crude 11.3%** — my re-sum: 552/4,868 = 11.34%. Table 1 rows independently re-sum to 95 arms / 552 / 4,868. ✓
- **tau² 0.21** (analysis 0.2068), **I² 42%** (analysis 42.0), **prediction interval 4.5–22.7%** (analysis 4.51–22.7). ✓
- Strict tier **9.5% (8.0–11.2), 24 arms, 168/1,728** — analysis: 9.47% (7.96–11.24), 24 units, 5 studies, 168/1,728. ✓
- Ex-Buis sensitivity **10.3%** — analysis GLMM ex-Buis 10.34% (9.16–11.65); the number traces (the study label is the Item 1 problem, not the number). ✓
- **GRADE very low for every pooled outcome** — Summary of findings and Table 3: worst-tier, problematic and undertriage all Very low; human-user response-level safety and fabrication are "not estimable / no rating possible", which is stated, not hidden. ✓
- **166 included studies (24 primary, 21 secondary, 121 narrative)** — internally consistent everywhere it appears: abstract, Results, PRISMA diagram (86 from search + 80 from chasing; 24 + 11 + 51 and 0 + 10 + 70). Secondary pools re-sum from the analysis dataset: S1 38 units / 17 studies / 2,147 of 8,190; S2 12 units / 7 studies / 120 of 2,686 — both match the manuscript. ✓

No headline number in the title, abstract, summary of findings or conclusions failed to trace. **15 headline values traced, 0 untraced.**

## Item 3 — Consistency (manuscript): PASS

Title, abstract, plain language summary, summary of findings, Tables 1–3, figure captions and conclusions are mutually consistent on every value in Item 2. Withdrawn numbers searched in `manuscript.md`: **"18.7" — 0 occurrences; "3.8 to 26.2" — 0; era "p=0.001" / "0.001" — 0.** The three "26.2" hits are unrelated current values (problematic-tier crude 26.2%, twice, and a reference article number). The withdrawn figures survive only as current claims in `stage5-manuscript/social-drafts.md`, which is dealt with under Items 7–8, not here; historical mentions in `peer-review/` files and `llm-team-log.md` are expected and are not failures.

## Item 4 — Figures and tables, visual: PASS

PDF rendered with `pdftoppm` at 110 dpi and inspected page by page. **Pages inspected: 4, 5 (summary of findings), 14 (GRADE Table 3), 21, 22, 23 (Tables 1–2), 24, 25, 26 (Figure 1, panels 1–3), 27, 28 (Figure 2, panels 1–2), 29 (Figure 3), 30 (Figure 4, PRISMA).**

- Figure 1, panel 3 (p.26) carries the GLMM summary diamond (labelled "Pooled (GLMM) 10.5% (9.3 to 11.9)") and a separate 95% prediction interval bar (4.5 to 22.7). ✓
- Figures 2 and 3 carry no pooled diamond, and their captions say why (descriptive, reported study by study) — consistent with the revision. ✓
- No clipped axes or labels on any forest plot; axis scales are complete (0–70, 0–85, 0–105). PRISMA diagram (p.30) is legible and its counts match the text (3,732 → 3,106 → 569 sought → 138 not retrieved → 431 assessed; 166 included). Tables are complete with no overflow; no blank or broken pages in the 30-page PDF (figure pages carry generous white space by layout, not by failure). ✓
- The only visual defect is content, not rendering: Figures 1 and 3 label the Fraser et al. arms "Buis 2023" (Item 1).

## Item 5 — Reporting checklist: PASS

`stage5-manuscript/prisma-checklists.md` (corrected revision 1 version) checked against the manuscript text on the items changed in review:

- **Item 14 (reporting bias assessment):** manuscript Methods, "Reporting bias" paragraph exists and says what the checklist claims — no funnel-based test, with the reason given (not valid for single-arm proportions); 138 unretrieved reports and the partial OpenAlex route named. ✓
- **Item 16b (cited excluded studies):** manuscript states full-text exclusions with reasons are filed as a supplement (PRISMA item 16b); the supplement exists (see below). ✓
- **Item 17 (study characteristics):** Table 1 carries setting, topic, verbatim tier label, arms, counts and RoB for the primary pool; the secondary-characteristics supplement exists; the narrative set is characterised in aggregate, as the checklist states. ✓
- **Item 21 (reporting biases):** carried in the Methods reporting-bias paragraph and the Discussion, as claimed. ✓
- **Item 24 (registration and protocol):** title page, abstract registration line and Declarations all state not registered, PROSPERO-ready form completed before full screening and not submitted, no number claimed; the era amendment is filed at `stage0-protocol/amendment-2026-11-13-era.md`. ✓

Supplements named by the checklist and the manuscript, all confirmed present: `supplement-fulltext-exclusions.csv` (176,521 bytes), `supplement-search-strategies.md` (4,104 bytes), `supplement-secondary-characteristics.csv` (5,607 bytes), `supplement-tier-labels.csv` (11,989 bytes).

## Item 6 — Declarations: PASS

All present in `manuscript.md` and internally consistent: funding (none; LLM tooling costs borne by the author), conflicts of interest, author contributions, data availability, ethics, patient and public involvement, and a full AI-assistance note (RAISE-style, LLM team named as the method).

- **Pre-submission peer-review statement — exact Rule 1 wording confirmed** in the manuscript.md, in the DOCX, and in the extracted PDF text: "The draft received structured multi-agent pre-submission peer review under the author's published protocol. The human author reviewed every comment and is accountable for the final text."
- Nothing in the manuscript calls this journal, external or independent peer review (0 occurrences of each phrase in the manuscript text). No passage presents the author as currently licensed or practising, and no retired-status or "former physician" label is used (0 occurrences).
- **Corresponding-author contact line — confirmed in both required places, in both formats:**
  - Title block (manuscript.md and PDF p.1): "Corresponding author: Raphael Malikian, rtmalikian@gmail.com". ✓
  - Declarations, Correspondence entry (manuscript.md and PDF p.18): "Raphael Malikian, rtmalikian@gmail.com. Independent researcher, Palmdale, CA, USA. ORCID: 0009-0008-4326-4205." ✓ (In the rendered PDF the ORCID breaks across a line as "0009-" / "0008-4326-4205"; the full identifier is present.)

## Item 7 — Metadata match: FAIL

- **Zenodo** (`zenodo-package/zenodo-metadata.md`): **PASS.** Title updated to the final manuscript title word for word; description carries the final numbers (GLMM 10.5%, 9.3 to 11.9; Hartung–Knapp 12.5%, 11.3 to 13.9; prediction interval 4.5 to 22.7%; strict tier 9.5%, 8.0 to 11.2; 95 arms, 23 studies, 552 of 4,868; GRADE very low). File list matches the manuscript's data availability statement.
- **Journal package** (`journal-package/journal-shortlist.md`): **FAIL, in part.** The conference abstract inside it was corrected at revision 1 and matches the final title and numbers. But the package header still carries the **old title**: "**Manuscript:** Unsafe medical advice from patient-facing large language model chatbots in primary-care presentations: a systematic review and meta-analysis".
- **GitHub plan** (`github-package/github-plan.md`): **FAIL, in part.** The repository description carries no stale numbers, but the README structure, point 1, still instructs the README to state the **old interval**: "pooled unsafe proportion 10.5%, 95% CI 9.2 to 12.0, 23 studies, 4,868 responses, GRADE very low". The final interval is 9.3 to 11.9.

## Item 8 — De-AI audit: FAIL (on stale claims in the social drafts; vocabulary clean)

Checked against `~/workspace/rules/de-ai-copy-rules.md` (banned list as filed there):

- **Manuscript abstract + plain language summary:** em dashes **0**; banned vocabulary **0 hits** across the full banned list. PASS.
- **`stage5-manuscript/social-drafts.md`:** banned vocabulary **0 hits**. Em dashes: **0 in the post copy itself** (X post text and LinkedIn post text); 2 in the file outside the post copy (the file's own heading and the "[ARTICLE LINK — paste…]" placeholder line), so the file's audit note ("no em dashes") is accurate for the drafts but not literally for the file.
- **The social drafts fail on substance, which the de-AI rule also covers (no claim stronger than, or different from, the paper):** the X draft states "95% CI 9.2–12.0" (superseded interval); the LinkedIn draft states "95% CI 9.2 to 12.0", "The prediction interval runs from 3.8% to 26.2%" (withdrawn interval), "Responses rated problematic in the broader sense pooled at 18.7%" (withdrawn pooled headline; the problematic pool is not pooled in the final version), and describes the primary outcome as "responses in a study's explicit unsafe, harmful or dangerous tier" (the outcome definition the revision withdrew). These drafts are marked NOT posted and held for a DOI, but as filed they would ship withdrawn numbers. They must be rewritten to the final values before any use.

## Item 9 — Author-confirmation items: LOGGED, travels to author sign-off (not a Gate 6 failure)

Confirmed: `peer-review/response-matrix.md`, row **L2-6**, logs the loop-2 conflicts wording ("That building is open-source and unpaid, and the author receives no income from clinical AI products or from any evaluated system or vendor") and the funding wording ("No external funding was received for this review, and the LLM tooling costs were borne by the author personally"), states the basis for both (the standing series declarations on the author record), and states explicitly that both wordings are logged "so the author can strike either at sign-off if wrong". The manuscript's Declarations carry exactly those wordings. Judgement: properly logged author-confirmation items; they travel to author sign-off and are **not** Gate 6 failures.

---

## Verdict: FAIL

Under the protocol there is no partial pass; a Fail loops the paper to Gate 4. The manuscript's analysis, headline numbers, consistency, figures, checklist, declarations and contact details all passed independent verification. The failures are citation and package hygiene, and all are fixable without re-analysis:

**Failed items:**

1. **Item 1 (References) — Blocker under Rule 7.** The study cited throughout as "Buis 2023" / "Buis L, et al." (doi:10.2196/49995) is Fraser H, Crossland D, Bacher I, Ranney M, Madsen T, Hilliard R, JMIR mHealth and uHealth 2023;11:e49995 (Crossref author list; PubMed PMID 37788063; JMIR article page, where Buis is the editor). The citation-reverification record's row 6 is also wrong on this point and must be corrected in the record. Fix: relabel the study as Fraser et al. 2023 in the reference list, text, Tables 1–2, Figures 1 and 3, and the dataset study_id (numbers unchanged: 2 arms, 23/74; the "excluding" sensitivity keeps its values under the corrected label).
2. **Item 7 (Metadata) —** GitHub plan README point 1 still states the superseded CI (9.2 to 12.0); journal shortlist header still states the superseded title. Fix both to the final title and the 9.3 to 11.9 interval.
3. **Item 8 (Public text) —** `social-drafts.md` X and LinkedIn drafts carry the superseded CI (9.2 to 12.0), the withdrawn prediction interval (3.8% to 26.2%), the withdrawn pooled problematic figure (18.7%), and the withdrawn outcome definition. Rewrite both drafts to the final manuscript's values and wording before they are used for anything.

**Travelling to author sign-off (not failures):** the Item 9 conflicts/funding wordings logged at response-matrix row L2-6, for the author to strike if wrong.

Signed: Gate 6 Final Integrity Gate agent, 2026-11-13.
