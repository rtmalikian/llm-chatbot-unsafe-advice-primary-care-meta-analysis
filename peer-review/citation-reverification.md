# Citation re-verification, Review 4 (Gate 4, revision 1)

Date: 2026-11-13. Scope: every reference in the manuscript, 49 entries (35
included pool studies and 14 other cited works). Method: title-page level.
Each printed DOI was resolved through the Crossref API and the resolved
record (authors, year, title, journal) was compared with the cited study.
Each study whose printed DOI resolved elsewhere was re-identified by a
Crossref title search and checked against the filed full text where one is
held (stage3-extraction/fulltexts/). MedRxiv preprints were checked through
Crossref (the registration agency for the 10.64898 prefix), the filed full
text, and the Semantic Scholar record in the search set.

## Outcome

- Checked: 49.
- Verified as printed (identifier resolves to the cited study): 21.
- Corrected DOI (printed DOI resolved to a different, real paper): 15.
- Corrected title: 1 (Ariel 2026; see note).
- Completed (paper verified; journal, full title or DOI added where the
  draft omitted them): 12.
- Unverifiable: 0. Khan 2026 is verified (see verdict below).

The pattern Reviewer 6 identified is confirmed and is wider than the
sample: every wrong DOI resolves to a real paper that sits inside the cited
study's own reference list or topic area (a paper the study cites, or the
study the DOI was swapped with). DOIs were harvested from reference lists,
not read from title pages. Fifteen of 35 pool-study DOIs were wrong.

## Khan 2026 verdict: VERIFIED as a preprint

Khan MM, Anwar MN. Clinical Safety of AI-Generated Antibiotic Prescribing
Advice: Guideline Adherence and Misinformation Risk Among Large Language
Models. medRxiv preprint, posted 15 May 2026, doi:10.64898/2026.05.13.26352828.
Three independent records agree: (1) Crossref resolves the DOI to exactly
this title and these authors; (2) the full text is on file at
stage3-extraction/fulltexts/R3040.txt, carries the same title, authors and
DOI on its first page, and its counts match the settled extraction
(1,191 inappropriate recommendations of 5,000 evaluations); (3) the search
record (Semantic Scholar, paper 70865e4901829704784261355af7cbe2635dc9a7)
carries the same title, authors, abstract and DOI. Reviewer 6's
unverifiable verdict rested on web and DOI searching on 2026-11-13 that
did not surface the record; the record exists. Khan therefore stays in the
reference list and in the dataset. It is still flagged wherever it is used:
it supplies 61.1% of the problematic pool's denominator, its classification
of 5,000 responses is undescribed in the paper, and the problematic pool is
demoted to descriptive reporting in this revision in part for that reason
(see stage4-analysis/revision1/CHANGELOG.md). The incident is logged in
llm-team-log.md.

## Ariel 2026 note

The DOI (10.64898/2026.05.09.26352813) is correct and resolves to the
extracted study (504 responses, catastrophic tier). The draft cited it
under the title held in Crossref metadata ("Consumer chatbots gave
similarly empathic answers whether safe or unsafe: a physician-rated
evaluation in six languages"). The medRxiv title page, as filed at
stage3-extraction/fulltexts/R2111.txt, carries a different title:
"Asymmetry between warmth and clinical substance in multilingual consumer
health AI". The revised manuscript cites the title-page title and this
table records the Crossref variant, so a reader arriving by either title
can confirm the study.

## Verification table

Verdicts: V = verified as printed. CD = corrected DOI. CT = corrected
title. C = completed (verified paper; missing journal, full title or DOI
supplied).

| # | Reference | Printed DOI | Verified record (authors, year, journal, DOI) | Verdict |
|---|---|---|---|---|
| 1 | An 2026, cancer survivorship | 10.2196/105778 | An H et al. 2026. Journal of Medical Internet Research 28:e105778. Full title ends "and Prompt Optimization Study". doi:10.2196/105778 | V, title completed |
| 2 | Ariel 2026, multilingual consumer health AI | 10.64898/2026.05.09.26352813 | Ariel D et al. 2026. medRxiv preprint. Title-page title "Asymmetry between warmth and clinical substance in multilingual consumer health AI". doi:10.64898/2026.05.09.26352813 | CT |
| 3 | Armbruster 2024, Doctor ChatGPT | 10.1016/j.jormas.2023.101471 (resolves to Balel 2023, oral surgery) | Armbruster J et al. 2024. Journal of Medical Internet Research 26:e58831. doi:10.2196/58831 | CD |
| 4 | Bilgic 2026, haemorrhoids | 10.3390/healthcare14131909 | Bilgic E, Karacan E. 2026. Healthcare 14(13):1909. doi:10.3390/healthcare14131909 | V |
| 5 | Brown 2025, self-triage | 10.7759/cureus.97834 | Brown HL. 2025. Cureus. doi:10.7759/cureus.97834 | V |
| 6 | Fraser 2023, ED triage | 10.2196/49995 | Fraser H, Crossland D, Bacher I, Ranney M, Madsen T, Hilliard R. 2023. JMIR mHealth and uHealth 11:e49995. doi:10.2196/49995. Title: "Comparison of Diagnostic and Triage Accuracy of Ada Health and WebMD Symptom Checkers, ChatGPT, and Physicians for Patients in an Emergency Department: Clinical Data Analysis Study" (corrected at Gate 6; see correction note below) | V, corrected at Gate 6 |
| 7 | Chowdhury 2026, symptom checkers | 10.64898/2026.09.01.26361908 | Chowdhury AR, Chowdhury B. 2026. medRxiv preprint. doi:10.64898/2026.09.01.26361908 | V |
| 8 | Draelos 2026, unsafe answers | 10.1038/s41746-026-02428-5 | Draelos RL et al. 2026. npj Digital Medicine 9:241. doi:10.1038/s41746-026-02428-5 | V |
| 9 | Duan 2025, online consultation | 10.1177/20552076251388140 | Duan L et al. 2025. Digital Health. doi:10.1177/20552076251388140 | V |
| 10 | Fan 2026, COPD | 10.2196/104836 | Fan L et al. 2026. JMIR Medical Informatics 14:e104836. doi:10.2196/104836 | V |
| 11 | Gokmen 2026, shoulder/elbow red flags | 10.3390/diagnostics16101439 | Gokmen MY et al. 2026. Diagnostics 16(10):1439. doi:10.3390/diagnostics16101439 | V |
| 12 | Gong 2026, hand foot and mouth disease | 10.1038/s41746-023-00873-0 (resolves to Mesko and Topol 2023) | Gong Z et al. 2026. Frontiers in Public Health 14:1924162. doi:10.3389/fpubh.2026.1924162 | CD |
| 13 | Gu 2026, diabetic peripheral neuropathy | 10.7759/cureus.35179 (resolves to Alkaissi and McFarlane 2023, hallucinations in scientific writing) | Gu L et al. 2026. Frontiers in Public Health 14:1942799. doi:10.3389/fpubh.2026.1942799 | CD |
| 14 | Hao 2026, high-risk HPV | 10.1097/JFN.0000000000000126 (resolves to Scannell 2016, HPV vaccine recommendations) | Hao Z et al. 2026. Frontiers in Public Health. doi:10.3389/fpubh.2026.1915867 | CD |
| 15 | Harada 2026, self-triage audit | 10.7759/cureus.105878 | Harada Y. 2026. Cureus. doi:10.7759/cureus.105878 | V |
| 16 | He 2026, cataract | 10.1007/s10916-023-02021-3 (resolves to Song et al. 2023, urolithiasis) | He Q et al. 2026. iScience 29(3):115002. doi:10.1016/j.isci.2026.115002 | CD |
| 17 | Khan 2026, antibiotic prescribing | 10.64898/2026.05.13.26352828 | Khan MM, Anwar MN. 2026. medRxiv preprint, posted 15 May 2026. doi:10.64898/2026.05.13.26352828. See verdict above | V |
| 18 | Liang 2026, herpes zoster | 10.1093/humrep/deaf135 (Human Reproduction abstract record, Naghdi et al. 2025) | Liang D et al. 2026. Frontiers in Public Health 14:1955701. doi:10.3389/fpubh.2026.1955701 | CD |
| 19 | Lv 2026, myocardial infarction education | 10.3389/fpubh.2026.1914167 | Lv T et al. 2026. Frontiers in Public Health 14:1914167. doi:10.3389/fpubh.2026.1914167 | V |
| 20 | Miao 2026, bacterial vaginosis | 10.1038/s41586-023-05881-4 (resolves to Moor et al. 2023, Nature) | Miao L et al. 2026. Frontiers in Reproductive Health 8:1967818. doi:10.3389/frph.2026.1967818 | CD |
| 21 | Ramaswamy 2026, ChatGPT Health triage | 10.1038/s41591-026-04297-7 | Ramaswamy A et al. 2026. Nature Medicine 32(5):1671-1675. doi:10.1038/s41591-026-04297-7 | V |
| 22 | Ratneswaran 2026, sleep apnoea referral | 10.64898/2026.10.09.26365165 | Ratneswaran D et al. 2026. medRxiv preprint. doi:10.64898/2026.10.09.26365165 | V |
| 23 | Shi 2026, paediatric vitamin D | 10.1177/20552076261427505 (resolves to Tan et al. 2026, pediatric healthcare; that DOI belongs to reference 44) | Shi P et al. 2026. Frontiers in Pediatrics 14:1927624. doi:10.3389/fped.2026.1927624 | CD |
| 24 | Si 2026, standardised-patient experiment | 10.21203/rs.3.rs-9988886/v1 | Si Y et al. 2026. Research Square preprint. doi:10.21203/rs.3.rs-9988886/v1 | V |
| 25 | Wang C 2026, paediatric burn first aid | 10.21203/rs.3.rs-10862831/v1 | Wang C et al. 2026. Research Square preprint. doi:10.21203/rs.3.rs-10862831/v1 | V |
| 26 | Wang Y 2026, aphthous stomatitis | 10.3389/froh.2026.1968034 | Wang Y et al. 2026. Frontiers in Oral Health 7:1968034. doi:10.3389/froh.2026.1968034 | V |
| 27 | Wen 2026, diabetic foot ulcer | 10.1038/s41746-025-01684-1 (resolves to Gaber et al. 2025, clinical decision support workflows) | Wen Y et al. 2026. Frontiers in Endocrinology 17:1977377. doi:10.3389/fendo.2026.1977377 | CD |
| 28 | Xiao 2026a, psychological support | 10.1177/20101058251389342 (resolves to a 2025 diabetes chatbot narrative review) | Xiao W et al. 2026. Frontiers in Psychiatry 17:1962615. doi:10.3389/fpsyt.2026.1962615 | CD |
| 29 | Xiao 2026b, late-life depression | 10.3389/fpsyt.2026.1817890 (resolves to Chen et al. 2026, late-life depression videos on social media) | Xiao W et al. 2026. Frontiers in Psychiatry 17:1956736. doi:10.3389/fpsyt.2026.1956736 | CD |
| 30 | Yu F 2025, oesophageal cancer | 10.4103/jfmpc.jfmpc_1236_24 | Yu F et al. 2025. Journal of Family Medicine and Primary Care. doi:10.4103/jfmpc.jfmpc_1236_24 | V |
| 31 | Yu S 2026, diabetic kidney disease | 10.3389/fmed.2026.2007153 | Yu S et al. 2026. Frontiers in Medicine 13:2007153. doi:10.3389/fmed.2026.2007153 | V |
| 32 | Zang 2026, frozen shoulder | 10.21203/rs.3.rs-10805692/v1 | Zang Q et al. 2026. Research Square preprint. doi:10.21203/rs.3.rs-10805692/v1 | V |
| 33 | Zheng 2026, mpox | 10.1097/MD.0000000000039305 (resolves to Hanci et al. 2024, readability of chatbot responses) | Zheng Q et al. 2026. Frontiers in Public Health 14:1913260. doi:10.3389/fpubh.2026.1913260 | CD |
| 34 | Zhou 2026, vegetarian nutrition | 10.1371/journal.pone.0325982 (resolves to Solomon and Laye 2025, sports nutrition knowledge) | Zhou J et al. 2026. Frontiers in Public Health 14:1921819. doi:10.3389/fpubh.2026.1921819 | CD |
| 35 | Zuo 2026, traumatic brain injury | 10.1007/s13187-017-1181-z (resolves to Azer et al. 2017, cancer websites) | Zuo X et al. 2026. Frontiers in Public Health 14:1926980. doi:10.3389/fpubh.2026.1926980 | CD |
| 36 | Bean 2026, LLM medical assistants RCT | no DOI in draft | Bean AM et al. 2026. Nature Medicine 32:609-615. doi:10.1038/s41591-025-04074-y | C |
| 37 | Campbell 2023 (CC220), thyroid nodules | no DOI in draft | Campbell DJ et al. 2023. Thyroid. doi:10.1089/thy.2023.0491. Title: "Evaluating ChatGPT Responses on Thyroid Nodules for Patient Education" | C |
| 38 | Campbell 2023 (CC221), sleep apnoea | no DOI in draft | Campbell DJ et al. 2023. Journal of Clinical Sleep Medicine. doi:10.5664/jcsm.10728. Title: "Evaluating ChatGPT responses on obstructive sleep apnea for patient education" | C |
| 39 | Coskun 2023 (CC628), methotrexate | no DOI in draft | Coskun BN et al. 2023. Rheumatology International. doi:10.1007/s00296-023-05473-5. Real title: "Assessing the accuracy and completeness of artificial intelligence language models in providing information on methotrexate" | C |
| 40 | Huo 2025, anchor review | 10.48550/arXiv/2401.12874 (resolves to Luo and Specia, explainability survey) | Huo B et al. 2025. JAMA Network Open 8(2):e2457879. doi:10.1001/jamanetworkopen.2024.57879. Title: "Large Language Models for Chatbot Health Advice Studies" | CD |
| 41 | Kassab 2024 (CC594), primary care | no DOI in draft | Kassab J et al. 2024. American Journal of Preventive Medicine. doi:10.1016/j.amepre.2024.02.006. Title: "Accuracy of Online Artificial Intelligence Models in Primary Care Settings" | C |
| 42 | Khromchenko 2024 (CC005), pregnancy | no DOI in draft | Khromchenko K et al. 2024. Cureus. doi:10.7759/cureus.65543 | C |
| 43 | Lakdawala 2023 (CC177), dermatitis and acne | no DOI in draft | Lakdawala N et al. 2023. JMIR Dermatology. doi:10.2196/50409 | C |
| 44 | Lee 2024 (CC224), atrial fibrillation | no DOI in draft | Lee TJ et al. 2024. Cureus. doi:10.7759/cureus.61680. Title: "Evaluating ChatGPT Responses on Atrial Fibrillation for Patient Education" | C |
| 45 | Okubo and Grein, registered protocol | no DOI (registry record) | PROSPERO CRD420261347066, registered 25 March 2026. Registry record, no DOI exists | V |
| 46 | Page 2021, PRISMA 2020 | journal details in draft, DOI omitted | Page MJ et al. 2021. BMJ 372:n71. doi:10.1136/bmj.n71 | C |
| 47 | Tan 2026 (CC102), pediatric healthcare | no DOI in draft (its DOI was printed against Shi 2026) | Tan J et al. 2026. Digital Health 12. doi:10.1177/20552076261427505. Title: "Safety and user perception of general-purpose large language models in pediatric healthcare" | C |
| 48 | Tanaka 2025 (CC230), emergency visit recommendations | no DOI in draft | Tanaka C et al. 2025. Acute Medicine and Surgery. doi:10.1002/ams2.70042 | C |
| 49 | Tiller 2026 (CC524), misinformation | no DOI in draft | Tiller NB et al. 2026. BMJ Open. doi:10.1136/bmjopen-2025-112695 | C |
| 50 | Whiting 2011, QUADAS-2 | as printed | Whiting PF et al. 2011. Annals of Internal Medicine 155(8):529-536 | V |

Rows are numbered to 50 because references 37 and 38 are two distinct
Campbell 2023 papers that the draft listed as one entry; the revised list
cites them separately. Total distinct manuscript entries checked: 49 as
drafted, 50 as revised.

A further metadata fault outside the reference list: the extraction list
for Fraser 2023 (R2042) carries DOI 10.1515/dx-2018-0009, an earlier
symptom-checker paper. The manuscript already cited the correct DOI; the
list fault is recorded here and in llm-team-log.md, and the list itself is
not silently rewritten.

## Correction note (Gate 6 loop, 13 November 2026)

Row 6 as originally filed in this record was wrong. It asserted "Buis L
et al. 2023" and "(first author Buis; Fraser is fourth author)". That
assertion is incorrect and is corrected above, not silently: the Crossref
record for doi:10.2196/49995 and PubMed PMID 37788063 both list the
authors as Fraser H, Crossland D, Bacher I, Ranney M, Madsen T and
Hilliard R, under the title given in the corrected row. Lorraine Buis is
not an author of this paper; she appears on the JMIR article page as the
journal editor ("Edited by L Buis"), which is the apparent source of the
error. The Gate 6 final integrity gate (peer-review/gate-6-integrity.md,
Item 1) caught the mismatch under Protocol Rule 7. The study label has
been corrected from "Buis 2023" to "Fraser 2023" in the manuscript,
extraction and analysis datasets and supplements; the study's numbers
are unchanged (2 arms in the primary pool, 23 of 74). The correction is
also logged in llm-team-log.md. Earlier entries in llm-team-log.md that
state the reverse correction are left as filed history and are
superseded by that log's Gate 6 incident entry.
