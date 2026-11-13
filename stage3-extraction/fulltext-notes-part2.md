# Review 4 - full-text assessment notes, batch 2 of 4 (part 2 list, 171 records)

Assessor pass date: 2026-11-12. Rules: stage0-protocol/protocol.md eligibility; stage2-screening/fulltext-rules.md codes FT-R1 to FT-R8 (first applicable code). Retrieval was by legitimate routes only, at least two routes per record before a NOT_RETRIEVED (FT-R8) code: (1) Europe PMC search by PMID + Europe PMC fullTextXML via PMCID; (2) Unpaywall best open-access location for the DOI (publisher OA PDF/HTML, converted with pdftotext); plus, for records with a PMCID whose XML returned HTTP 500 and for failed OA fetches, a retry pass via Europe PMC fullTextXML / Europe PMC PDF render and a repeated OA fetch. No paywall workarounds were used. Saved full texts are in stage3-extraction/fulltexts/{record_id}.txt (the fulltexts folder is shared with the other batches).

## Decision counts (from fulltext-decisions-part2.csv)

- INCLUDE_PRIMARY: 3
- INCLUDE_SECONDARY: 4
- INCLUDE_NARRATIVE: 12
- EXCLUDE: 93
- NOT_RETRIEVED: 59
- Full texts saved for this batch: 112 of 171

Exclusion codes used: FT-R1 1, FT-R2 3, FT-R3 1, FT-R4 3, FT-R5 16, FT-R6 1, FT-R7 68, FT-R8 59

## Included records - counts at a glance

- **R0916** (INCLUDE_SECONDARY): Bench. Patient questions on cataract (27 questions; denominator as printed = 54 per model). Secondary problematic/inaccurate: prevalence of inaccurate responses - ChatGPT o3-mini 4/54 (7.41%), Gemini 2.0 Pro Experimental 5/54 (9.26%), DeepSeek Thinking R1 1/54 (1.85%), Kimi Thinking K1.5 7/54 (12.96%). Counts in Results text (accuracy section). No explicit unsafe tier, so not primary.
- **R1009** (INCLUDE_NARRATIVE): Human-user randomised preregistered study (Nature Medicine): 1,298 participants, 10 medical scenarios, arms GPT-4o, Llama 3, Command R+ vs control (own sources); LLM-alone bench arm also reported (condition identification 94.9%, disposition 56.3%). Eligible, but no explicit unsafe tier; disposition under-estimation of acuity is reported only as Mann-Whitney effect sizes/figures, with no undertriage numerator/denominator in the text - nothing poolable.
- **R1082** (INCLUDE_NARRATIVE): Bench. Celiac disease patient education, 20 questions x 3 models (ChatGPT-4, Claude 3.7, Gemini 2.0). Binary misinformation was rated, but counts are per EVALUATION, not per response: Gemini 2.0 16/120 evaluations (13.3%), ChatGPT-4 28/120 (23.3%), Claude 3.7 29/120 (24.2%) - Results section 3.3/Table 2. No explicit unsafe tier; response-level numerator not recoverable from the text - nothing poolable as defined.
- **R1085** (INCLUDE_PRIMARY): Bench. Ten fictional ophthalmological-emergency vignettes x 5 runs = 50 responses per model, rated with a standardised manual distinguishing wrong/conflicting/potentially harmful information. Explicit harmful tier: ChatGPT-4o 25/50 (50%), DeepSeek R1 19/50 (38%) - Table 1 and Results text ('Harmful answers (%) 50 / 38'). Total responses 100. Stratum: bench; red-flag/emergency presentations.
- **R1090** (INCLUDE_SECONDARY): Bench self-triage: 10 vignettes x 3 platforms = 30 outputs. Secondary undertriage (lower-acuity recommendation than NICE-based gold standard): ChatGPT 0/10, Gemini AI 0/10 (the single under-triaged output was the non-LLM NHS 111 checker, 1/10) - Table 3 and Results text. No unsafe tier reported, so not primary.
- **R1121** (INCLUDE_NARRATIVE): Bench. Thai public drug-information queries: 76 questions to ChatGPT-4o, Google Gemini, Microsoft Copilot, rated by clinical pharmacists. An explicit risk tier exists (No risk 2 pts / Low risk 1 pt / High risk 0 pts = 'significant risk to patient safety'), and all three systems produced some high-risk responses, but per-model high-risk numerators are not printed in the text (only a category note: pregnancy/lactation high-risk rate 1/76 per system). Nothing poolable from the text.
- **R1154** (INCLUDE_NARRATIVE): Bench. Common questions on drug-induced liver injury to 6 LLMs (incl LLaMA-3.1-405B, GPT-3.5-Turbo, GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, o1-preview). Accuracy has an explicit 'poor' tier (substantial errors that might significantly confuse the patient and result in potential harm; consensus = >=2 of 3 raters) and error analysis of poor responses, but 'poor' proportions appear only in Fig 3B; safety is a mean score. No numerator/denominator in the text - nothing poolable.
- **R1229** (INCLUDE_SECONDARY): Bench. Symptom-driven online medical consultations for a trigeminal neuralgia case set; ~233 responses per source. Secondary problematic/inaccurate: incorrect answers - ERNIE Bot 6/233 (2.58%), ChatGPT 17/233 (7.30%) (human doctors 2/233, 0.86%) - Results text/error analysis. No explicit unsafe tier, so not primary.
- **R1249** (INCLUDE_NARRATIVE): Bench. Consumer chatbots (general assistants and companion chatbots) prompted with adolescent emergent health-concern vignettes (mental-health and physical emergencies); 75 responses. Outcomes are 3-point appropriateness/empathy/understandability ratings and binary escalation-recognition (45/75 overall; general assistants 27/30 vs companions 18/45) and resource referral - no explicit unsafe tier, and escalation recognition is not undertriage against a reference disposition as defined. Nothing poolable.
- **R1313** (INCLUDE_NARRATIVE): Simulated-patient experiments: ERNIE Bot managing chronic diseases (hypertension, type 2 diabetes, unstable angina), 384 patient-AI trials; standardised-condition comparisons with ChatGPT-4o/DeepSeek and physicians also reported. Safety-relevant indicator is combined and not separable into an unsafe tier: 'inappropriate or even potentially harmful medications' in 57.8% of ERNIE Bot trials (95% CI 52.9-62.8; ~222/384) - Abstract/Results. No listed secondary outcome in poolable form.
- **R1366** (INCLUDE_NARRATIVE): Bench. ChatGPT-3.5 assessing OTC medication use in pregnancy; 87 responses rated against UpToDate. Safety is a 5-point Likert scale (1 = 'response will cause harm', 2 = high risk of complications, 3 = moderate risk/one significant error, 4 = mostly safe, 5 = completely safe); Table 1 distribution (n=87): scores 1-5 = 0, 1, 7, 9, 70. Authors describe 8/87 (9%) as evaluations with safety errors (scores 2-3). No named unsafe tier and no consensus unsafe numerator as defined - nothing poolable.
- **R1519** (INCLUDE_SECONDARY): Bench. Esophageal cancer questions of patient concern, 55 questions to ChatGPT (version not stated in text). Secondary problematic/inaccurate: authors dichotomise ratings as correct (categories 1-2) vs incorrect (categories 3-4); incorrect = 18/55 (32.7%, all category 3 'partially accurate, partially inaccurate'; category 4 'completely inaccurate/irrelevant' = 0/55); complete/correct 24/55, correct-but-incomplete 13/55 - Results text. No explicit unsafe tier, so not primary.
- **R1723** (INCLUDE_NARRATIVE): Bench. Self-care medicines/supplement guidance benchmark: 58 questions posed to multiple LLMs (incl GPT-4.0, GPT-3.5, Gemini, Gemini Advanced, Copilot, Perplexity) in Dutch, with English/context/repeat sub-studies. Responses rated 1-5 ('Inaccurate: completely incorrect and/or could lead to serious consequences' = score 1); authors call score-1 answers 'unsafe' and narrate that Perplexity produced 8 unsafe answers, but per-arm unsafe counts and denominators appear only in Fig 2, not in the text - nothing poolable as printed.
- **R1780** (INCLUDE_NARRATIVE): Bench. Drug information for patients from a search-engine chatbot (Bing Copilot): 10 patient questions x 50 drugs = 500 answers analysed. Accuracy/completeness are the all-response outcomes; potential harm was rated only in a preselected subset of 20 inaccurate chatbot answers, of which experts judged 66% potentially harmful (42% moderate-to-mild harm, 22% severe harm, as printed) - the harm denominator is the inaccurate subset, not all responses rated for safety, so nothing poolable for the primary outcome.
- **R1781** (INCLUDE_PRIMARY): Bench with real patient questions. 100 patient questions (20 per specialty x 5 specialties) answered by ChatGPT-4.0 and a web-based expert panel; the 100 ChatGPT answers were each classified by 3 physicians in the relevant specialty on a binary item 'Does the answer contain potentially harmful advice?' (yes/no). Potentially harmful: 16/100 ChatGPT responses flagged by >=1 of 3 physicians (15 flagged by exactly one physician, 1 additional flagged by two) - Results section 'Patients' Perception Showed No Difference Between Nonharmful and Potentially Harmful Advice'. Total ChatGPT responses rated = 100. No consensus-tier count is printed; numerator is the >=1-rater flag count as reported.
- **R1802** (INCLUDE_NARRATIVE): Simulated-patient study in LMIC primary care: ChatGPT (GPT-3.5-era, as discussed in the paper) managing 9 common diseases, 27 trials. Combined indicator, not separable into an unsafe tier: unnecessary or harmful medication suggestions in 23/27 trials (85%), and 16/27 (59%) even after a correct diagnosis - Abstract/Results. No listed secondary outcome in poolable form.
- **R1958** (INCLUDE_NARRATIVE): Bench. ChatGPT responses on self-managed medication abortion analysed qualitatively against the evidence base (inaccurate portrayal of self-managed abortion as dangerous, misleading/fabricated content documented thematically). Eligible topic, but no explicit unsafe tier and no numerator/denominator - nothing poolable.
- **R2036** (INCLUDE_NARRATIVE): Bench. ChatGPT (GPT-3.5-era) responses to 96 patient-perspective advice-seeking vignettes across preventive, acute and palliative care contexts, rated for clinical appropriateness against guidelines: 93/96 (97%) appropriate and not explicitly violating guidelines; 1 response with faulty follow-up reasoning described. Appropriateness is not an explicit unsafe/harmful tier and no harm counts are reported - nothing poolable.
- **R2042** (INCLUDE_PRIMARY): Bench. Triage recommendations for 37 emergency-department cases with sufficient triage data, rated against independent physicians: explicit 'unsafe' triage tier - ChatGPT-3.5 unsafe 15/37 (41%), ChatGPT-4.0 unsafe 8/37 (22%); agreement 22/37 and 28/37, too-cautious 0/37 and 1/37 - Abstract/Results text. (Non-LLM arms: Ada 5/37 unsafe, WebMD 7/37.) Total LLM responses = 74. Stratum: bench; disposition/triage presentations.

## Per-record retrieval routes and decisions

### R0855 - Benchmarking large language models for congenital cataract parent counseling: safety, readability, and knowledge translation of developmental and genetic information.
- PMID 41970961; DOI 10.1080/08164622.2023.2298812
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC13066122 HTTP 200 len=149928
- Saved: stage3-extraction/fulltexts/R0855.txt (65088 chars)
- Decision: EXCLUDE FT-R5 - Congenital cataract parent counselling (subspecialty ophthalmology/genetics). Safety was a scored rubric domain (median scores; 'highly unsafe' used only as a rubric definition for watchful-waiting answers); no unsafe numerator/denominator.

### R0860 - Evaluation of Artificial Intelligence Chatbots in Providing Brucellosis-Related Health Information: A Multidimensional Quality Assessment.
- PMID 41964131; DOI 10.1111/zph.70059
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R0864 - The Digital Native Paradox: A Framework for Critical Appraisal of Generative AI in Paediatric Medical Education.
- PMID 41952074; DOI 10.1111/jpc.70386
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; Unpaywall error ChunkedEncodingError; RETRY OA error ChunkedEncodingError
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200; Unpaywall error ChunkedEncodingError; RETRY OA error ChunkedEncodingError. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R0872 - Assessing the Safety and Clinical Appropriateness of Breast Cancer Advice From Consumer-Grade Large Language Models.
- PMID 41937254; DOI 10.1111/1754-9485.70092
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R0880 - Mental Health AI Chatbots as Pharmakon: A Tripartite Theory of Use despite Risk.
- PMID 41926568; DOI 10.1159/000551841
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R0882 - Multidisciplinary expert evaluation of large language models on questions regarding bariatric surgery: a comparative analysis of ERNIE Bot 4.0, ChatGPT-4, Claude 3 Opus, and Gemini Pro.
- PMID 41922459; DOI 10.1001/jamanetworkopen.2023.30320
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC13199474 HTTP 200 len=144223
- Saved: stage3-extraction/fulltexts/R0882.txt (77056 chars)
- Decision: EXCLUDE FT-R5 - Bariatric surgery question set (specialty-only). Outcomes are expert quality/accuracy scores for ERNIE Bot 4.0, ChatGPT-4, Claude 3 Opus, Gemini Pro; no unsafe tier counts.

### R0889 - Evaluating ChatGPT-5's Performance in Answering Common Patient Questions About Femoroacetabular Impingement and Hip Arthroscopy.
- PMID 41909018; DOI 10.1302/2633-1462.64.BJO-2024-0198.R1
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC13031688 HTTP 200 len=68121
- Saved: stage3-extraction/fulltexts/R0889.txt (30945 chars)
- Decision: EXCLUDE FT-R5 - Femoroacetabular impingement / hip arthroscopy (procedure-specific orthopaedics). Text states none of the 25 ChatGPT-5 responses contained unsafe information, but the question set is specialty-only.

### R0891 - Evaluating deepresearch and deepthink in total knee arthroplasty patient education: ChatGPT-4o excels in comprehensiveness, Deepseek R1 leads in clarity and readability of orthopedic information.
- PMID 41906842; DOI 10.1016/j.arth.2023.04.007
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC13374050 HTTP 200 len=61368
- Saved: stage3-extraction/fulltexts/R0891.txt (32032 chars)
- Decision: EXCLUDE FT-R5 - Total knee arthroplasty patient education (procedure-specific). Comprehensiveness/clarity/readability scores for ChatGPT-4o Deep Research and DeepSeek R1 DeepThink; no safety tier.

### R0892 - Investigating the Readability and Quality of AI Systems to Trending Questions About Food Poisoning.
- PMID 41902573; DOI 10.2196/69955
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC13032161 HTTP 200 len=92011
- Saved: stage3-extraction/fulltexts/R0892.txt (43038 chars)
- Decision: EXCLUDE FT-R7 - Food poisoning trending questions. Outcomes limited to readability, DISCERN/GQS-type quality scores; no explicit unsafe tier and no secondary outcome in poolable form.

### R0904 - Challenges of using generative AI for patient education in chronic heart failure: an evaluation of content quality, readability, and actionability in cross-platform LLM-generated texts.
- PMID 41869585; DOI 10.1145/3767695.3769514
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12999856 HTTP 200 len=151498
- Saved: stage3-extraction/fulltexts/R0904.txt (73862 chars)
- Decision: EXCLUDE FT-R7 - Chronic heart failure patient education across platforms. Outcomes are content quality, readability and actionability (PEMAT) scores; hallucination/fabrication discussed qualitatively, not counted per response.

### R0911 - Feasibility of a Large Language Model Chatbot to Support Parental Understanding in the PICU.
- PMID 41860987; DOI 10.1097/CCE.0000000000001378
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC13008162 HTTP 200 len=43611
- Saved: stage3-extraction/fulltexts/R0911.txt (23443 chars)
- Decision: EXCLUDE FT-R2 - Bespoke EHR-grounded BastionGPT (GPT-4o) PICU platform, system prompt with patient-specific EHR data entered by the principal investigator; not a general-purpose chatbot used as a layperson would use it. Accuracy/safety assessed at sentence level on a 3-point error-severity scale in a 14-parent feasibility study; no response-level unsafe tier.

### R0916 - Comparison of the performance of large language models in answering patient questions related to cataract.
- PMID 41847613; DOI 10.1007/s10916-023-02021-3
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12989843 HTTP 200 len=95606
- Saved: stage3-extraction/fulltexts/R0916.txt (43006 chars)
- Decision: INCLUDE_SECONDARY - Bench. Patient questions on cataract (27 questions; denominator as printed = 54 per model). Secondary problematic/inaccurate: prevalence of inaccurate responses - ChatGPT o3-mini 4/54 (7.41%), Gemini 2.0 Pro Experimental 5/54 (9.26%), DeepSeek Thinking R1 1/54 (1.85%), Kimi Thinking K1.5 7/54 (12.96%). Counts in Results text (accuracy section). No explicit unsafe tier, so not primary.

### R0921 - Evaluating the Performance of ChatGPT and DeepSeek in Bilingual Responses to Questions Regarding Craniofacial Microsomia.
- PMID 41842837; DOI 10.14309/ajg.0000000000003552
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R0922 - Can AI chatbots guide patients and physicians about neck pain? A reliability and readability comparison of ChatGPT-4 and Gemini.
- PMID 41841776; DOI 10.1177/10538127261433272
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R0924 - Disclaimers and Referral Patterns for Medical Advice Across Urgency Levels: Large Language Model Evaluation Study.
- PMID 41838894; DOI 10.5281/zenodo.17185348
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12991190 HTTP 200 len=105954
- Saved: stage3-extraction/fulltexts/R0924.txt (51687 chars)
- Decision: EXCLUDE FT-R7 - Disclaimer/referral-pattern study: 908 responses from GPT-4o, Claude Sonnet-4, Grok-3, DeepSeek-V3 to 227 authentic patient queries. Outcomes are 5-point ordinal disclaimer/referral classifications; no unsafe tier and no undertriage counts against a reference disposition.

### R0930 - Evaluation of DeepSeek-R1 and ChatGPT-4o as educational sources for upper tract urothelial carcinoma.
- PMID 41821914; DOI 10.5173/ceju.2025.0238
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12976754 HTTP 200 len=66508
- Saved: stage3-extraction/fulltexts/R0930.txt (32115 chars)
- Decision: EXCLUDE FT-R5 - Upper tract urothelial carcinoma (subspecialty oncology). 43 queries rated on a 4-point scale whose lowest category includes 'potentially dangerous information'; raters found none - but specialty-only set.

### R0934 - Simulated Patient Queries Reveal Limitations of ChatGPT in Dermatologic Image Classification.
- PMID 41814512; DOI 10.1111/ijd.70382
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R0936 - Can large language models be trusted? Reliability and readability of responses to perinatal depression FAQs.
- PMID 41810293; DOI 10.1016/S2589-7500(24)00197-3
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12968175 HTTP 200 len=120902
- Saved: stage3-extraction/fulltexts/R0936.txt (56875 chars)
- Decision: EXCLUDE FT-R7 - Perinatal depression FAQs. Outcomes are reliability (DISCERN-type), readability and trust scores for several LLMs incl DeepSeek; no explicit unsafe tier counts and no poolable secondary outcome.

### R0941 - Evaluation of Chat Generative Pretrained Transformer's Performance in Cosmetic Injection Consultation by Authoritative Plastic Surgeons.
- PMID 41797860; DOI 10.1097/GOX.0000000000007479
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12965984 HTTP 200 len=118922
- Saved: stage3-extraction/fulltexts/R0941.txt (41926 chars)
- Decision: EXCLUDE FT-R5 - Cosmetic injection consultation by plastic surgeons (specialty-only). Note for the record: explicit binary safety rating existed - 173/183 (94.54%) safe, 10/183 (5.46%) unsafe for ChatGPT (Results/Table 2) - but cosmetic-injection advice does not present in primary care.

### R0948 - Validity and reliability of ChatGPT's responses on dietary supplements in Japan: A quality assessment and content analysis.
- PMID 41782614; DOI 10.1016/j.pecinn.2026.100461
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12955162 HTTP 200 len=114989
- Saved: stage3-extraction/fulltexts/R0948.txt (54771 chars)
- Decision: EXCLUDE FT-R7 - Dietary supplements in Japan. Validity/reliability and content analysis of ChatGPT responses; inaccurate/ambiguous content described qualitatively, no unsafe tier numerator/denominator.

### R0949 - Accuracy, quality, and readability analyses of responses from large language models to questions on pediatric dental sedation.
- PMID 41781947; DOI 10.22599/bioj.377
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12994223 HTTP 200 len=169905
- Saved: stage3-extraction/fulltexts/R0949.txt (76651 chars)
- Decision: EXCLUDE FT-R5 - Pediatric dental sedation (procedure-specific specialty dentistry). Accuracy, quality and readability analyses only.

### R0952 - Evaluating GPT-4 Responses on Scars or Keloids for Patient Education: Large Language Model Evaluation Study.
- PMID 41773665; DOI 10.48550/arXiv.2501.09775
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12954683 HTTP 200 len=102578
- Saved: stage3-extraction/fulltexts/R0952.txt (44849 chars)
- Decision: EXCLUDE FT-R5 - Scars/keloids treatment education (plastic surgery/dermatology procedure set). Fabrication outcome is at reference level: 383/3250 references hallucinated (11.8%), denominator is references, not responses; response outcomes are accuracy/readability scores.

### R0958 - Do Large Language Models Perform Equally Across Languages? A Comparison of Responses to Frequently Asked Questions in Anesthesiology.
- PMID 41761593; DOI 10.12659/MSM.951815
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12958780 HTTP 200 len=90143
- Saved: stage3-extraction/fulltexts/R0958.txt (35116 chars)
- Decision: EXCLUDE FT-R5 - Frequently asked questions in anesthesiology (specialty-only). Text states the responses were free from unsafe or inaccurate recommendations; quality/readability comparison across languages only.

### R0968 - Patient perspective on large-language model responses to questions about Moyamoya.
- PMID 41748894; DOI 10.3171/FOC/2008/24/2/E16
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12948822 HTTP 200 len=104629
- Saved: stage3-extraction/fulltexts/R0968.txt (44056 chars)
- Decision: EXCLUDE FT-R5 - Moyamoya (rare neurosurgical disease; subspecialty counselling). Note: fabrication-type counts existed (responses including fabricated/unrealistic information: 11/40 and 15/40 for the two LLMs, 40 responses each, Results table) but the topic is specialty-only.

### R0986 - Guidelines vs. generative AI in CKD patient education: the role of prompt engineering and expert blinded evaluation.
- PMID 41721295; DOI 10.3390/medicina60030445
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC13032336 HTTP 200 len=72381
- Saved: stage3-extraction/fulltexts/R0986.txt (38595 chars)
- Decision: EXCLUDE FT-R7 - CKD patient education, prompt-engineering comparison with blinded expert scores (accuracy/completeness-type domain scores). No unsafe tier counts.

### R0990 - Implementing GPT-4 Learning Models in Dermatology: An Assessment of Medical Quality and Utility.
- PMID 41705408; DOI 10.12788/cutis.0843
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12914478 HTTP 200 len=63699
- Saved: stage3-extraction/fulltexts/R0990.txt (27889 chars)
- Decision: EXCLUDE FT-R4 - Not patient-posed: GPT-4/Copilot dermatology content generated on clinical topics and compared with UpToDate. 'Harmful' counts are per discordant treatment mention (ChatGPT-4 1/166, Copilot 1/68 unmatched treatments), not per response; no patient-facing question set.

### R0992 - Evaluation of AI language models in answering pregnancy-related questions assessed by obstetrics specialists.
- PMID 41699404; DOI 10.1007/s00330-022-08784-6
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC13000243 HTTP 200 len=73415
- Saved: stage3-extraction/fulltexts/R0992.txt (38380 chars)
- Decision: EXCLUDE FT-R7 - Pregnancy-related questions rated by obstetric specialists on Likert domains (accuracy, reliability, comprehensibility, patient-friendliness). Mean/domain scores only; no unsafe tier counts.

### R0995 - Patient Education in Bariatric Surgery: Can Artificial Intelligence-Based Chatbots Bridge the Knowledge Gap?
- PMID 41695397; DOI 10.1016/j.chbah.2024.100067
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12902178 HTTP 200 len=133900
- Saved: stage3-extraction/fulltexts/R0995.txt (61065 chars)
- Decision: EXCLUDE FT-R5 - Bariatric surgery patient education (specialty-only). Accuracy scale includes a -1 'completely inaccurate, potentially harmful' category and an irrelevant/harmful percentage comparison, but the set is procedure-specific.

### R0996 - Guideline-based, but not error-free: Multilingual risks in AI-powered patient counseling on gallstones.
- PMID 41689953; DOI 10.1016/j.ijmedinf.2026.106341
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R0998 - Exploring the Balance Between Artificial Intelligence and Human Expertise in Shaping Breast Reconstruction Outcomes: A Comparative Reflection Study.
- PMID 41682852; DOI 10.18502/ijph.v50i11.7600
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12898539 HTTP 200 len=89180
- Saved: stage3-extraction/fulltexts/R0998.txt (46311 chars)
- Decision: EXCLUDE FT-R5 - Breast reconstruction (plastic surgery, specialty-only). Comparative reflection/quality scores; no primary-care presentation set.

### R1005 - Comparison of online radiologists and large language model chatbots in responding to common radiology-related questions in Chinese: a cross-sectional comparative analysis.
- PMID 41669453; DOI 10.3390/diagnostics15040497
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12883469 HTTP 200 len=96217
- Saved: stage3-extraction/fulltexts/R1005.txt (52377 chars)
- Decision: EXCLUDE FT-R7 - Radiology-related questions in Chinese: 318 responses to 106 questions (LLM chatbots incl DeepSeek-R1 vs online radiologists). Potential harm rated on a 5-point Likert scale (means compared); no unsafe tier counts.

### R1006 - Evaluation of large Language models on pediatric asthma: a comparative study of Claude3-Opus, Gemini 2.0, ChatGPT-4o, and DeepSeek-a cross-sectional questionnaire study.
- PMID 41668028; DOI 10.1177/1367493519831493
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12990414 HTTP 200 len=93161
- Saved: stage3-extraction/fulltexts/R1006.txt (38056 chars)
- Decision: EXCLUDE FT-R7 - Pediatric asthma: Claude 3 Opus, Gemini 2.0, ChatGPT-4o, DeepSeek compared with questionnaire quality/accuracy scores. No explicit unsafe tier counts in text.

### R1007 - Optimizing Large Language Model Responses to Medical Queries: a Cross-sectional Study On the Effective Use of Chatgpt for Cancer-related Questions.
- PMID 41665699; DOI 10.1007/s10916-026-02344-x
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1009 - Reliability of LLMs as medical assistants for the general public: a randomized preregistered study.
- PMID 41663592; DOI 10.1016/j.sapharm.2021.02.020
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12920132 HTTP 200 len=103869
- Saved: stage3-extraction/fulltexts/R1009.txt (62968 chars)
- Decision: INCLUDE_NARRATIVE - Human-user randomised preregistered study (Nature Medicine): 1,298 participants, 10 medical scenarios, arms GPT-4o, Llama 3, Command R+ vs control (own sources); LLM-alone bench arm also reported (condition identification 94.9%, disposition 56.3%). Eligible, but no explicit unsafe tier; disposition under-estimation of acuity is reported only as Mann-Whitney effect sizes/figures, with no undertriage numerator/denominator in the text - nothing poolable.

### R1014 - Comparing AI and physician medical advice quality and humanistic care on social media platforms.
- PMID 41659054; DOI 10.1177/20552076261421341
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12881337 HTTP 200 len=140720
- Saved: stage3-extraction/fulltexts/R1014.txt (57965 chars)
- Decision: EXCLUDE FT-R7 - AI vs physician advice on social media platforms: quality and humanistic-care Likert ratings. No unsafe tier or poolable secondary outcome.

### R1020 - Potentially Harmful Consequences of Artificial Intelligence (AI) Chatbot Use Among Patients With Mental Illness: Early Data From a Large Psychiatric Service System.
- PMID 41649035; DOI 10.1111/acps.13440
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12967755 HTTP 200 len=31746
- Saved: stage3-extraction/fulltexts/R1020.txt (14911 chars)
- Decision: EXCLUDE FT-R5 - Mental-health only: case-note review in a psychiatric service for harms compatible with chatbot use; no LLM responses were rated. Goes to the mental-health narrative appendix territory, excluded from the primary-care pool.

### R1022 - Comparative analysis of Chinese large language model performance on atrial fibrillation questions.
- PMID 41639623; DOI 10.1093/europace/euad369
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12958689 HTTP 200 len=88278
- Saved: stage3-extraction/fulltexts/R1022.txt (46095 chars)
- Decision: EXCLUDE FT-R7 - Atrial fibrillation questions to Chinese LLMs. Correctness/completeness are median scores; dangerous advice (e.g. quinidine recommendations by 4 models) is listed qualitatively without a per-response unsafe numerator/denominator.

### R1024 - Vulnerability of Large Language Models to Prompt Injection When Providing Medical Advice.
- PMID 41632124; DOI 10.1056/AIcs2400390
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12717619 HTTP 200 len=78709
- Saved: stage3-extraction/fulltexts/R1024.txt (41173 chars)
- Decision: EXCLUDE FT-R2 - Adversarial prompt-injection simulation (216 patient-LLM dialogues; thalidomide-in-pregnancy POC 5 scenarios/model): the exposure is maliciously injected prompts, not a general-purpose chatbot used as a patient would use it. Outcomes are attack-success rates, not clinician-rated unsafe tiers for genuine patient questions.

### R1030 - Comparative evaluation of large language models for hip fracture-related patient questions: DeepSeek-V3-FW, Gemini 2.0 Flash, and ChatGPT-4.5.
- PMID 41623725; DOI 10.1215/2834703X-11556011
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12858731 HTTP 200 len=90484
- Saved: stage3-extraction/fulltexts/R1030.txt (39278 chars)
- Decision: EXCLUDE FT-R7 - Hip fracture-related patient questions (DeepSeek-V3-FW, Gemini 2.0 Flash, ChatGPT-4.5): quality/accuracy/readability scores. No unsafe tier counts.

### R1054 - Assessment of AI-generated responses to common pregnancy questions: A blinded expert evaluation.
- PMID 41539048; DOI 10.1016/j.ejogrb.2026.114960
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1055 - Readability, reliability, and quality of kyphosis-related information provided by artificial intelligence chatbots: A cross-sectional study.
- PMID 41536543; DOI 10.2106/JBJS.M.01228
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12796146 HTTP 200 len=96434
- Saved: stage3-extraction/fulltexts/R1055.txt (45856 chars)
- Decision: EXCLUDE FT-R7 - Kyphosis information from AI chatbots: readability, DISCERN-type reliability and GQS quality scores only.

### R1072 - Assessing the Quality of AI Responses to Patient Concerns About Axial Spondyloarthritis: Delphi-Based Evaluation.
- PMID 41499772; DOI 10.2196/58329
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12824573 HTTP 200 len=139717
- Saved: stage3-extraction/fulltexts/R1072.txt (49581 chars)
- Decision: EXCLUDE FT-R7 - Axial spondyloarthritis patient concerns: Delphi-based quality scores (incl an 'inaccurate or inappropriate content' score category reported as means). No unsafe tier counts.

### R1073 - Large Language Models in Patient Health Communication for Atherosclerotic Cardiovascular Disease: Pilot Cross-Sectional Comparative Analysis.
- PMID 41499171; DOI 10.1038/s43856-025-00802-0
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12824577 HTTP 200 len=141646
- Saved: stage3-extraction/fulltexts/R1073.txt (57179 chars)
- Decision: EXCLUDE FT-R7 - Atherosclerotic cardiovascular disease patient communication: cross-sectional Likert/domain score comparison across LLMs. No unsafe tier counts.

### R1077 - ChatGPT as a Glucagon-Like Peptide-1 Agonists Information Source: Balancing Quality, Readability, and Patient Safety.
- PMID 41489154; DOI 10.1177/19322968251409205
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12774803 HTTP 500 len=151; Unpaywall HTTP 200; OA fetch HTTP 200 len=103842 ct=text/html; charset=utf-8
- Saved: stage3-extraction/fulltexts/R1077.txt (10126 chars)
- Decision: EXCLUDE FT-R7 - ChatGPT as GLP-1 agonist information source: quality/readability scores; safety discussed qualitatively. Full text retrieved as publisher HTML.

### R1080 - Empathy AI in healthcare.
- PMID 41479969; DOI 10.1007/BF00846695
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12753942 HTTP 200 len=106724
- Saved: stage3-extraction/fulltexts/R1080.txt (59125 chars)
- Decision: EXCLUDE FT-R7 - Empathy/compassion experiment: 30 participants rated ChatGPT/Claude vs professional responses to 9 communication prompts. No medical-advice safety rating and no poolable outcome.

### R1082 - Efficacy of Large Language Models in Providing Evidence-Based Patient Education for Celiac Disease: A Comparative Analysis.
- PMID 41470773; DOI 10.3389/fdgth.2024.1287186
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12735979 HTTP 200 len=195343
- Saved: stage3-extraction/fulltexts/R1082.txt (76678 chars)
- Decision: INCLUDE_NARRATIVE - Bench. Celiac disease patient education, 20 questions x 3 models (ChatGPT-4, Claude 3.7, Gemini 2.0). Binary misinformation was rated, but counts are per EVALUATION, not per response: Gemini 2.0 16/120 evaluations (13.3%), ChatGPT-4 28/120 (23.3%), Claude 3.7 29/120 (24.2%) - Results section 3.3/Table 2. No explicit unsafe tier; response-level numerator not recoverable from the text - nothing poolable as defined.

### R1085 - Comparison of ChatGPT-4o and DeepSeek R1 in the Management of Ophthalmological Emergencies-An Analysis of Ten Fictional Case Vignettes.
- PMID 41464828; DOI 10.26188/28822919
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12734186 HTTP 200 len=92723
- Saved: stage3-extraction/fulltexts/R1085.txt (43809 chars)
- Decision: INCLUDE_PRIMARY - Bench. Ten fictional ophthalmological-emergency vignettes x 5 runs = 50 responses per model, rated with a standardised manual distinguishing wrong/conflicting/potentially harmful information. Explicit harmful tier: ChatGPT-4o 25/50 (50%), DeepSeek R1 19/50 (38%) - Table 1 and Results text ('Harmful answers (%) 50 / 38'). Total responses 100. Stratum: bench; red-flag/emergency presentations.

### R1090 - Evaluation of Artificial Intelligence for Patient Self-Triage: Comparison of General-Purpose AI Platforms With the NHS 111 Online Symptom Checker in the United Kingdom.
- PMID 41458776; DOI 10.7759/cureus.97834
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12741861 HTTP 200 len=44348
- Saved: stage3-extraction/fulltexts/R1090.txt (26591 chars)
- Decision: INCLUDE_SECONDARY - Bench self-triage: 10 vignettes x 3 platforms = 30 outputs. Secondary undertriage (lower-acuity recommendation than NICE-based gold standard): ChatGPT 0/10, Gemini AI 0/10 (the single under-triaged output was the non-LLM NHS 111 checker, 1/10) - Table 3 and Results text. No unsafe tier reported, so not primary.

### R1098 - Patient safety and quality implications of large language model use in healthcare: a risk-stratified assessment of artificial intelligence-assisted medical consultations.
- PMID 41442171; DOI 10.1093/intqhc/mzaf134
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1102 - Artificial Intelligence's Capacity to Detect Subtle Medical Misinformation: A Novel Reverse Prompting Approach.
- PMID 41432852; DOI 10.1007/s10916-025-02323-8
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1115 - Evaluation of physicians' opinions on receiving health information from ChatGPT; trustworthiness, value, and danger.
- PMID 41408965; DOI 10.1177/09514848251407117
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1121 - Effectiveness of ChatGPT, Google Gemini, and Microsoft Copilot in Answering Thai Drug Information Queries: Cross-Sectional Study.
- PMID 41397693; DOI 10.1016/j.pec.2021.08.028
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12750067 HTTP 200 len=79098
- Saved: stage3-extraction/fulltexts/R1121.txt (36619 chars)
- Decision: INCLUDE_NARRATIVE - Bench. Thai public drug-information queries: 76 questions to ChatGPT-4o, Google Gemini, Microsoft Copilot, rated by clinical pharmacists. An explicit risk tier exists (No risk 2 pts / Low risk 1 pt / High risk 0 pts = 'significant risk to patient safety'), and all three systems produced some high-risk responses, but per-model high-risk numerators are not printed in the text (only a category note: pregnancy/lactation high-risk rate 1/76 per system). Nothing poolable from the text.

### R1126 - Evaluating Generative AI Psychotherapy Chatbots Used by Youth: Cross-Sectional Study.
- PMID 41370787; DOI 10.1177/25152459251357566
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12694945 HTTP 200 len=148553
- Saved: stage3-extraction/fulltexts/R1126.txt (72374 chars)
- Decision: EXCLUDE FT-R5 - Mental-health only: generative-AI psychotherapy chatbots used by youth, rated with a therapy-chatbot framework (incl crisis handling). Not a primary-care presentation set.

### R1137 - Evaluating ChatGPT-generated psychoeducation for mood disorders: comparative insights from patients and mental health professionals.
- PMID 41353963; DOI 10.1016/j.jpsychires.2025.11.039
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 200 len=2767 ct=text/html;charset=UTF-8; RETRY OA fetch HTTP 200 len=2767
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 200 len=2767 ct=text/html;charset=UTF-8; RETRY OA fetch HTTP 200 len=2767. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1154 - Evaluating large language models' performance in answering common questions on drug-induced liver injury.
- PMID 41321931; DOI 10.1016/j.jhepr.2025.101579
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12657742 HTTP 200 len=103566
- Saved: stage3-extraction/fulltexts/R1154.txt (47620 chars)
- Decision: INCLUDE_NARRATIVE - Bench. Common questions on drug-induced liver injury to 6 LLMs (incl LLaMA-3.1-405B, GPT-3.5-Turbo, GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, o1-preview). Accuracy has an explicit 'poor' tier (substantial errors that might significantly confuse the patient and result in potential harm; consensus = >=2 of 3 raters) and error analysis of poor responses, but 'poor' proportions appear only in Fig 3B; safety is a mean score. No numerator/denominator in the text - nothing poolable.

### R1157 - Evaluation of the Quality and Reliability of ChatGPT-4's Responses on Allergen Immunotherapy Using Validated Instruments for Health Information Quality Assessment.
- PMID 41319041; DOI 10.1111/all.15023
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12665041 HTTP 200 len=119588
- Saved: stage3-extraction/fulltexts/R1157.txt (49163 chars)
- Decision: EXCLUDE FT-R7 - Allergen immunotherapy: ChatGPT-4 responses assessed with validated health-information instruments (DISCERN/GQS-type). No unsafe tier counts.

### R1164 - Comparative evaluation of viral hepatitis question responses: ChatGPT-4.5 outperforms three established models.
- PMID 41299590; DOI 10.1016/j.ebiom.2023.104770
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12659494 HTTP 200 len=78825
- Saved: stage3-extraction/fulltexts/R1164.txt (44094 chars)
- Decision: EXCLUDE FT-R7 - Viral hepatitis questions: ChatGPT-4.5 vs three models on Likert domains (accuracy, safety as mean scores). No unsafe tier counts.

### R1173 - Accuracy of Large Language Model Responses Versus Internet Searches for Common Questions About Glucagon-Like Peptide-1 Receptor Agonist Therapy: Exploratory Simulation Study.
- PMID 41284989; DOI 10.7759/cureus.38380
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12643393 HTTP 200 len=81700
- Saved: stage3-extraction/fulltexts/R1173.txt (41937 chars)
- Decision: EXCLUDE FT-R7 - GLP-1 receptor agonist questions, LLM vs internet search, SCORE framework mean scores (safety defined as non-hallucinated/non-misleading but reported as scores). No tier counts.

### R1177 - Assessing the Performance and Reliability of ChatGPT in Answering Patients' Questions on Voice Disorders across Time.
- PMID 41274812; DOI 10.1016/j.jvoice.2025.10.044
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; Unpaywall error ChunkedEncodingError; RETRY OA error ProxyError
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200; Unpaywall error ChunkedEncodingError; RETRY OA error ProxyError. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1183 - What do the current popular artificial intelligence chatbots offer us regarding patient information? Comparison of responses from the ten most popular chatbots about bladder cancer.
- PMID 41258614; DOI 10.1007/s11764-025-01921-2
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1187 - How accurately do large language models answer patient questions on anterior cruciate ligament tears? A comparative study.
- PMID 41253635; DOI 10.1016/j.knee.2025.11.002
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 403 len=5608 ct=text/html; charset=UTF-8; RETRY OA error ChunkedEncodingError
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 403 len=5608 ct=text/html; charset=UTF-8; RETRY OA error ChunkedEncodingError. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1188 - Evaluating the performance of Large language models in rheumatology for connective tissue Diseases: DeepSeek-R1, ChatGPT-4.0, Copilot, and Gemini-2.0.
- PMID 41252762; DOI 10.1016/j.ijmedinf.2025.106172
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1193 - Ctrl + Alt + Conceive: fertility awareness in the age of Artificial Intelligence, how do large language models compare?
- PMID 41243291; DOI 10.1080/14647273.2025.2584673
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; Unpaywall error ProxyError; RETRY OA error ChunkedEncodingError
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200; Unpaywall error ProxyError; RETRY OA error ChunkedEncodingError. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1209 - Diagnostic Accuracy and Counseling Quality of GPT-4o for Strabismus and Pseudostrabismus in Patient-Generated Mobile Photographs: A Preliminary Evaluation.
- PMID 41216185; DOI 10.1001/jamaophthalmol.2022.6010
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12596880 HTTP 200 len=53617
- Saved: stage3-extraction/fulltexts/R1209.txt (29792 chars)
- Decision: EXCLUDE FT-R5 - Strabismus/pseudostrabismus diagnosis from patient-generated photographs (specialty ophthalmology, diagnostic task). Outcomes are diagnostic accuracy and counselling-quality/Likert harm-likelihood scores; no unsafe tier counts.

### R1218 - Using artificial intelligence models to generate dietary recommendations for chronic kidney disease patients: A comparative cross-sectional study.
- PMID 41197595; DOI 10.1016/j.clnu.2025.10.014
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1229 - Comparing large language models and human doctors in symptom-driven online medical consultations: A case study on trigeminal neuralgia.
- PMID 41164151; DOI 10.1177/20552076251388140
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12559625 HTTP 200 len=129577
- Saved: stage3-extraction/fulltexts/R1229.txt (60394 chars)
- Decision: INCLUDE_SECONDARY - Bench. Symptom-driven online medical consultations for a trigeminal neuralgia case set; ~233 responses per source. Secondary problematic/inaccurate: incorrect answers - ERNIE Bot 6/233 (2.58%), ChatGPT 17/233 (7.30%) (human doctors 2/233, 0.86%) - Results text/error analysis. No explicit unsafe tier, so not primary.

### R1234 - Evaluating Web Retrieval-Assisted Large Language Models With and Without Whitelisting for Evidence-Based Neurology: Comparative Study.
- PMID 41159599; DOI 10.1101/2024.09.20.24314076
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12612646 HTTP 200 len=94127
- Saved: stage3-extraction/fulltexts/R1234.txt (40811 chars)
- Decision: EXCLUDE FT-R4 - Not patient-facing: web-retrieval LLMs answered clinician evidence-based neurology questions (AAN guideline queries), scored correct/inaccurate/wrong. No patient-posed questions or lay users.

### R1236 - Evaluating Large Language Models for Accuracy and Completeness of Vitiligo Patient Education: A Comparative Analysis.
- PMID 41158792; DOI 10.1038/s41746-024-01074-z
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12558161 HTTP 200 len=81587
- Saved: stage3-extraction/fulltexts/R1236.txt (41817 chars)
- Decision: EXCLUDE FT-R7 - Vitiligo patient education: Likert accuracy/completeness means (score 1 anchor mentions potentially harmful errors, but results are mean scores). No tier counts.

### R1243 - Comparison of ChatGPT-3.5, ChatGPT-4.0 and DeepSeek in generating dietary plans for patients with chronic kidney disease: A focus on nutritional accuracy and dietary inflammation.
- PMID 41135437; DOI 10.1016/j.nut.2025.112957
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1249 - Characteristics and Safety of Consumer Chatbots for Emergent Adolescent Health Concerns.
- PMID 41129154; DOI 10.2471/BLT.19.237636
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12550634 HTTP 200 len=34244
- Saved: stage3-extraction/fulltexts/R1249.txt (12822 chars)
- Decision: INCLUDE_NARRATIVE - Bench. Consumer chatbots (general assistants and companion chatbots) prompted with adolescent emergent health-concern vignettes (mental-health and physical emergencies); 75 responses. Outcomes are 3-point appropriateness/empathy/understandability ratings and binary escalation-recognition (45/75 overall; general assistants 27/30 vs companions 18/45) and resource referral - no explicit unsafe tier, and escalation recognition is not undertriage against a reference disposition as defined. Nothing poolable.

### R1269 - Artificial Intelligence Models for Dysphonia Patient Education.
- PMID 41084356; DOI 10.1097/SCS.0000000000010678
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12661483 HTTP 200 len=82583
- Saved: stage3-extraction/fulltexts/R1269.txt (32175 chars)
- Decision: EXCLUDE FT-R7 - Dysphonia patient education: Likert agreement ratings (incl 'safe, non-dangerous information' as a mean agreement score). No tier counts.

### R1280 - Comparative performance of large language models for patient-initiated ophthalmology consultations.
- PMID 41059182; DOI 10.1016/j.hlpt.2025.101013
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12497754 HTTP 200 len=100377
- Saved: stage3-extraction/fulltexts/R1280.txt (37589 chars)
- Decision: EXCLUDE FT-R5 - Patient-initiated ophthalmology consultations (specialty service). Accuracy/quality score comparison across LLMs; no unsafe tier counts.

### R1292 - [Not Available].
- PMID 41037377; DOI 10.1701/4573.45793
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1293 - [Not Available].
- PMID 41037364; DOI 10.1701/4573.45780
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1313 - Quality safety and disparity of an AI chatbot in managing chronic diseases: simulated patient experiments.
- PMID 40999038; DOI 10.3390/ijerph18105060
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12462510 HTTP 200 len=112378
- Saved: stage3-extraction/fulltexts/R1313.txt (55276 chars)
- Decision: INCLUDE_NARRATIVE - Simulated-patient experiments: ERNIE Bot managing chronic diseases (hypertension, type 2 diabetes, unstable angina), 384 patient-AI trials; standardised-condition comparisons with ChatGPT-4o/DeepSeek and physicians also reported. Safety-relevant indicator is combined and not separable into an unsafe tier: 'inappropriate or even potentially harmful medications' in 57.8% of ERNIE Bot trials (95% CI 52.9-62.8; ~222/384) - Abstract/Results. No listed secondary outcome in poolable form.

### R1322 - Transforming cataract care through artificial intelligence: an evaluation of large language models' performance in addressing cataract-related queries.
- PMID 40979436; DOI 10.1186/s12889-021-10801-0
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12447166 HTTP 200 len=82508
- Saved: stage3-extraction/fulltexts/R1322.txt (37427 chars)
- Decision: EXCLUDE FT-R7 - Cataract-related queries: 7-point Likert accuracy means (anchors mention potentially harmful mistakes at scores 2-3, results reported as scores). No tier counts.

### R1325 - Quality of information on hypospadias from artificial intelligence chatbots: How safe is AI for patient and family information?
- PMID 40975653; DOI 10.1016/j.jpurol.2025.08.029
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1329 - Evaluating large language models in pediatric fever management: a two-layer study.
- PMID 40970139; DOI 10.1016/j.urology.2023.05.010
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12441047 HTTP 200 len=87738
- Saved: stage3-extraction/fulltexts/R1329.txt (45487 chars)
- Decision: EXCLUDE FT-R7 - Pediatric fever management, two-layer (doctor/relative) questionnaire study of 30 questions x 4 models. Outcomes are scores; responses deemed to pose safety risks were removed and scored 0, with the count only in supplementary files, not the main text - no poolable unsafe numerator/denominator.

### R1333 - Evaluating the perspectives of ChatGPT and Gemini on glenohumeral osteoarthritis management.
- PMID 40959025; DOI 10.2196/47479
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12435021 HTTP 200 len=65454
- Saved: stage3-extraction/fulltexts/R1333.txt (31666 chars)
- Decision: EXCLUDE FT-R7 - Glenohumeral osteoarthritis management perspectives from ChatGPT and Gemini: guideline-concordance/quality scores. No unsafe tier counts.

### R1337 - Comparative evaluation of large language models in delivering guideline-compliant recommendations for topical NSAID use in musculoskeletal pain: a multidimensional analysis.
- PMID 40952435; DOI 10.3390/biomedicines12050974
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12568900 HTTP 200 len=87094
- Saved: stage3-extraction/fulltexts/R1337.txt (40870 chars)
- Decision: EXCLUDE FT-R7 - Topical NSAID use in musculoskeletal pain: multidimensional guideline-compliance scores across LLMs. No unsafe tier counts.

### R1342 - A comparative study of ChatGPT and DeepSeek in spinal cord injury patient education: Can artificial intelligence "speak" spinal cord injury?
- PMID 40938207; DOI 10.48550/arXiv.2407.07666
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC13123067 HTTP 500 len=151; Unpaywall HTTP 404; RETRY https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13123067/fullTextX HTTP 500 len=151; RETRY https://europepmc.org/articles/PMC13123067?pdf=render HTTP 403 len=5608
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; EPMC fullTextXML PMC13123067 HTTP 500 len=151; Unpaywall HTTP 404; RETRY https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13123067/fullTextX HTTP 500 len=151; RETRY https://europepmc.org/articles/PMC13123067?pdf=render HTTP 403 len=5608. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1343 - Reducing Hallucinations and Trade-Offs in Responses in Generative AI Chatbots for Cancer Information: Development and Evaluation Study.
- PMID 40934488; DOI 10.2196/48002
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12425422 HTTP 200 len=111048
- Saved: stage3-extraction/fulltexts/R1343.txt (50248 chars)
- Decision: EXCLUDE FT-R2 - Chatbots were researcher-developed RAG variants (GPT-4/GPT-3.5 combined with Cancer Information Service content, Google search, or no retrieval; 62 cancer questions) built via API for the study - not general-purpose public chatbots used as a patient would use them. Hallucination (defined as medically harmful or misinformation) rates 0%-~40% by variant are therefore out of scope.

### R1363 - How Accurate Is AI? A Critical Evaluation of Commonly Used Large Language Models in Responding to Patient Concerns About Incidental Kidney Tumors.
- PMID 40869522; DOI 10.1186/s12967-025-06751-5
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12386662 HTTP 200 len=94113
- Saved: stage3-extraction/fulltexts/R1363.txt (46398 chars)
- Decision: EXCLUDE FT-R7 - Incidental kidney tumours: six-domain Likert rubric means (accuracy, completeness, clarity, currency, risk of harm, hallucinations) from five urologists. No tier counts.

### R1366 - Accuracy and Safety of ChatGPT-3.5 in Assessing Over-the-Counter Medication Use During Pregnancy: A Descriptive Comparative Study.
- PMID 40863701; DOI 10.3390/healthcare12161637
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12389367 HTTP 200 len=59018
- Saved: stage3-extraction/fulltexts/R1366.txt (29939 chars)
- Decision: INCLUDE_NARRATIVE - Bench. ChatGPT-3.5 assessing OTC medication use in pregnancy; 87 responses rated against UpToDate. Safety is a 5-point Likert scale (1 = 'response will cause harm', 2 = high risk of complications, 3 = moderate risk/one significant error, 4 = mostly safe, 5 = completely safe); Table 1 distribution (n=87): scores 1-5 = 0, 1, 7, 9, 70. Authors describe 8/87 (9%) as evaluations with safety errors (scores 2-3). No named unsafe tier and no consensus unsafe numerator as defined - nothing poolable.

### R1367 - Perceived Accuracy of Spine-Related Medical Advice From ChatGPT, TikTok, and the North American Spine Society Clinical Practice Guidelines.
- PMID 40861605; DOI 10.7759/cureus.88808
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12377256 HTTP 200 len=51409
- Saved: stage3-extraction/fulltexts/R1367.txt (30533 chars)
- Decision: EXCLUDE FT-R7 - Spine-related advice from ChatGPT vs TikTok vs NASS guidelines: perceived accuracy on a 10-point Likert scale. No unsafe tier.

### R1369 - Assessing the response quality and readability of ChatGPT in stuttering.
- PMID 40848602; DOI 10.1016/j.jfludis.2025.106149
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1370 - ChatGPT-4o as a digital health tool for diabetes technology education: insights on reliability, quality, and readability.
- PMID 40848113; DOI 10.1007/s12020-025-04400-x
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1374 - Analyses of different prescriptions for health using artificial intelligence: a critical approach based on the international guidelines of health institutions.
- PMID 40832454; DOI 10.3389/frai.2024.1493716/full
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 200 len=2294274 ct=application/pdf
- Saved: stage3-extraction/fulltexts/R1374.txt (88136 chars)
- Decision: EXCLUDE FT-R7 - AI-generated prescriptions assessed against international guidelines with mean scores and qualitative hallucination examples. No per-response unsafe tier counts.

### R1378 - Artificial intelligence in endometriosis care: A comparative analysis of large language model and human specialist responses to endometriosis-related queries.
- PMID 40829501; DOI 10.1016/j.ejogrb.2025.114625
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; Unpaywall error ChunkedEncodingError; RETRY OA fetch HTTP 403 len=5598
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200; Unpaywall error ChunkedEncodingError; RETRY OA fetch HTTP 403 len=5598. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1387 - Is Readability a Proxy for Reliability? A Qualitative Evaluation of ChatGPT-4.0 in Orthopaedic Trauma Communication.
- PMID 40810381; DOI 10.1111/jep.70238
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1392 - Assessing the Role of Large Language Models Between ChatGPT and DeepSeek in Asthma Education for Bilingual Individuals: Comparative Study.
- PMID 40802989; DOI 10.2196/53787
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12349887 HTTP 200 len=112821
- Saved: stage3-extraction/fulltexts/R1392.txt (52979 chars)
- Decision: EXCLUDE FT-R7 - Asthma education for bilingual individuals (ChatGPT-4o vs DeepSeek): seven-dimension scores; the safety dimension (1 = fatal harm to 4 = no harm) is reported only as mean scores (supplementary file). No tier counts.

### R1394 - Using Artificial Intelligence ChatGPT to Access Medical Information About Chemical Eye Injuries: Comparative Study.
- PMID 40802972; DOI 10.2196/49368
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12349736 HTTP 200 len=111393
- Saved: stage3-extraction/fulltexts/R1394.txt (60299 chars)
- Decision: EXCLUDE FT-R7 - Chemical eye injuries: ChatGPT accuracy/completeness-type scores vs comparator. No unsafe tier counts.

### R1416 - Evaluation of large language models in patient education and clinical decision support for rotator cuff injury: a two-phase benchmarking study.
- PMID 40760478; DOI 10.2147/NSS.S495654
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12323112 HTTP 200 len=69184
- Saved: stage3-extraction/fulltexts/R1416.txt (37144 chars)
- Decision: EXCLUDE FT-R7 - Rotator cuff injury: two-phase benchmarking of LLMs for patient education and clinician decision support using quality/accuracy scores. No unsafe tier counts.

### R1418 - Comparing the Quality of Patient Guidance on Dermatologic Care Generated by ChatGPT vs Reddit.
- PMID 40758526; DOI 10.12788/cutis.1222
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 200 len=1312860 ct=application/pdf
- Saved: stage3-extraction/fulltexts/R1418.txt (34098 chars)
- Decision: EXCLUDE FT-R7 - Dermatologic guidance ChatGPT vs Reddit: quality scores (incl misinformation discussed qualitatively). No unsafe tier counts.

### R1419 - Using large language models to generate child-friendly education materials on myopia.
- PMID 40755959; DOI 10.2214/ajr.24.31696
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12317229 HTTP 200 len=105043
- Saved: stage3-extraction/fulltexts/R1419.txt (47393 chars)
- Decision: EXCLUDE FT-R4 - Not patient-posed advice: LLMs were prompted by researchers to generate child-friendly myopia education materials at set reading levels. Potential harm was a Likert distribution, but the task is materials generation, not patient-facing advice.

### R1432 - Evaluation of ChatGPT-4 as an Online Outpatient Assistant in Puerperal Mastitis Management: Content Analysis of an Observational Study.
- PMID 40705609; DOI 10.1097/APO.0000000000000397
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12288767 HTTP 200 len=104831
- Saved: stage3-extraction/fulltexts/R1432.txt (47213 chars)
- Decision: EXCLUDE FT-R7 - Puerperal mastitis: ChatGPT-4 as online outpatient assistant, content-analysis quality scores. No unsafe tier counts.

### R1435 - Application of Large Language Models in Stroke Rehabilitation Health Education: 2-Phase Study.
- PMID 40694436; DOI 10.1001/jama.2023.9651
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12306586 HTTP 200 len=134883
- Saved: stage3-extraction/fulltexts/R1435.txt (63577 chars)
- Decision: EXCLUDE FT-R7 - Stroke rehabilitation health education (2-phase): accuracy/quality scores for ChatGPT-4 and comparators; hallucinations noted qualitatively. No unsafe tier counts.

### R1441 - GPT- 4 as a virtual fitness coach: a case study assessing its effectiveness in providing weight loss and fitness guidance.
- PMID 40665245; DOI 10.1186/s12889-025-22739-8
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12261634 HTTP 200 len=110864
- Saved: stage3-extraction/fulltexts/R1441.txt (55414 chars)
- Decision: EXCLUDE FT-R7 - Single-case study of GPT-4 as a virtual fitness coach (weight loss/fitness guidance for one case). No clinician-rated unsafe tier with numerator/denominator.

### R1445 - ChatGPT Performance Deteriorated in Patients with Comorbidities When Providing Cardiological Therapeutic Consultations.
- PMID 40648622; DOI 10.1016/j.cjca.2024.05.022
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12249446 HTTP 200 len=95441
- Saved: stage3-extraction/fulltexts/R1445.txt (40596 chars)
- Decision: EXCLUDE FT-R7 - Cardiological therapeutic consultations in patients with comorbidities (simulated cases): performance/appropriateness scores; harmful recommendations (e.g. dabigatran in ESRD) described qualitatively only.

### R1455 - ChatGPT-4.0 and DeepSeek-R1 does not yet provide clinically supported answers for knee osteoarthritis.
- PMID 40618549; DOI 10.1016/j.knee.2025.06.007
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; Unpaywall error ChunkedEncodingError; RETRY OA error ChunkedEncodingError
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200; Unpaywall error ChunkedEncodingError; RETRY OA error ChunkedEncodingError. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1469 - An assessment of generative artificial intelligence in responding to clinical queries on tapering antidepressants.
- PMID 40579346; DOI 10.1016/j.sapharm.2025.06.107
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 200 len=2726 ct=text/html;charset=UTF-8; RETRY OA fetch HTTP 200 len=2727
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 200 len=2726 ct=text/html;charset=UTF-8; RETRY OA fetch HTTP 200 len=2727. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1470 - Evaluating the effectiveness of chatbots and traditional resources in patient education on dry eye disease.
- PMID 40569014; DOI 10.1080/08164622.2025.2517750
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1515 - Large language model evaluation in autoimmune disease clinical questions comparing ChatGPT 4o, Claude 3.5 Sonnet and Gemini 1.5 pro.
- PMID 40399509; DOI 10.1002/art.42646
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12095533 HTTP 200 len=76372
- Saved: stage3-extraction/fulltexts/R1515.txt (42692 chars)
- Decision: EXCLUDE FT-R7 - Autoimmune disease clinical questions (65 questions; ChatGPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro): 10-point performance scores. No unsafe tier counts.

### R1519 - Discussion of the ability to use chatGPT to answer questions related to esophageal cancer of patient concern.
- PMID 40396096; DOI 10.4103/jfmpc.jfmpc_1236_24
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12088566 HTTP 200 len=41742
- Saved: stage3-extraction/fulltexts/R1519.txt (23027 chars)
- Decision: INCLUDE_SECONDARY - Bench. Esophageal cancer questions of patient concern, 55 questions to ChatGPT (version not stated in text). Secondary problematic/inaccurate: authors dichotomise ratings as correct (categories 1-2) vs incorrect (categories 3-4); incorrect = 18/55 (32.7%, all category 3 'partially accurate, partially inaccurate'; category 4 'completely inaccurate/irrelevant' = 0/55); complete/correct 24/55, correct-but-incomplete 13/55 - Results text. No explicit unsafe tier, so not primary.

### R1536 - Artificial Intelligence-Generated Answers to Patients' Questions on Asthma: The Artificial Intelligence Responses on Asthma Study.
- PMID 40345326; DOI 10.1016/j.jaip.2025.04.051
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1539 - Comparing Artificial Intelligence-Generated and Clinician-Created Personalized Self-Management Guidance for Patients With Knee Osteoarthritis: Blinded Observational Study.
- PMID 40332991; DOI 10.1001/jamainternmed.2023.1835
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12096024 HTTP 200 len=124095
- Saved: stage3-extraction/fulltexts/R1539.txt (60561 chars)
- Decision: EXCLUDE FT-R7 - Knee osteoarthritis personalised self-management guidance (AI vs clinician): safety is a continuous score (domains 0-20, total /100). No unsafe tier counts.

### R1540 - Comparison of artificial intelligence-generated and physician-generated patient education materials on early diabetic kidney disease.
- PMID 40331140; DOI 10.1007/s10994-023-06495-7
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12052532 HTTP 200 len=68564
- Saved: stage3-extraction/fulltexts/R1540.txt (36856 chars)
- Decision: EXCLUDE FT-R7 - Early diabetic kidney disease patient education materials (AI vs physician): quality/accuracy scores. No unsafe tier counts.

### R1543 - Are Large Language Model-Based Chatbots Effective in Providing Reliable Medical Advice for Achilles Tendinopathy? An International Multispecialist Evaluation.
- PMID 40322749; DOI 10.1177/23259671251332596
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12046157 HTTP 200 len=78364
- Saved: stage3-extraction/fulltexts/R1543.txt (40733 chars)
- Decision: EXCLUDE FT-R7 - Achilles tendinopathy advice: international multispecialist Likert evaluation; 'unsatisfactory' responses discussed without poolable unsafe counts.

### R1553 - Are chatbots a reliable source for patient frequently asked questions on neck masses?
- PMID 40307608; DOI 10.1007/s00405-025-09433-6
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1556 - AI in Home Care-Evaluation of Large Language Models for Future Training of Informal Caregivers: Observational Comparative Case Study.
- PMID 40294407; DOI 10.1016/j.gaceta.2012.05.012
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12070015 HTTP 200 len=114925
- Saved: stage3-extraction/fulltexts/R1556.txt (53892 chars)
- Decision: EXCLUDE FT-R7 - LLMs evaluated for future training of informal home-care caregivers: quality/error scores; hallucinations explicitly reported as not observed but no response-level unsafe tier or counts.

### R1560 - Nurses' assessment of artificial ıntelligence chatbots for health literacy education.
- PMID 40271238; DOI 10.4103/jehp.jehp_1195_24
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12017437 HTTP 200 len=69794
- Saved: stage3-extraction/fulltexts/R1560.txt (33302 chars)
- Decision: EXCLUDE FT-R7 - Nurses' assessment (survey/qualitative) of AI chatbots for health-literacy education. Responses were not clinician-rated into an unsafe tier; no poolable outcome.

### R1564 - An artificial intelligence perspective on geriatric syndromes: assessing the information accuracy and readability of ChatGPT.
- PMID 40257746; DOI 10.1016/j.jamda.2023.06.008
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; Unpaywall error ChunkedEncodingError; RETRY OA fetch HTTP 403 len=5587
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200; Unpaywall error ChunkedEncodingError; RETRY OA fetch HTTP 403 len=5587. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1572 - Evaluating the accuracy of ChatGPT in delivering patient instructions for medications: an exploratory case study.
- PMID 40235859; DOI 10.1039/D3DD00112A
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11996888 HTTP 200 len=63866
- Saved: stage3-extraction/fulltexts/R1572.txt (38088 chars)
- Decision: EXCLUDE FT-R7 - Exploratory case study of ChatGPT patient instructions for 3 medications: Likert ratings of correctness, completeness, harmfulness and adherence by participants. No unsafe tier counts.

### R1578 - Evaluating ChatGPT-4's correctness in patient-focused informing and awareness for atrial fibrillation.
- PMID 40224268; DOI 10.1101/2023.08.08.23293689
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11993680 HTTP 200 len=69962
- Saved: stage3-extraction/fulltexts/R1578.txt (34180 chars)
- Decision: EXCLUDE FT-R7 - Atrial fibrillation patient informing (ChatGPT-4): correctness scores. No unsafe tier counts.

### R1580 - Does the use of generative AI chatbots by patients introduce risk of adverse drug events?
- PMID 40220270; DOI 10.1080/14740338.2025.2493351
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1589 - The Role of ChatGPT in osteoporosis management: a comparative analysis with clinical expertise.
- PMID 40205011; DOI 10.3390/bioengineering11040337
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 403 len=409 ct=text/html; RETRY OA fetch HTTP 403 len=413
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 403 len=409 ct=text/html; RETRY OA fetch HTTP 403 len=413. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1604 - Effectiveness of Generative Artificial Intelligence-Driven Responses to Patient Concerns in Long-Term Opioid Therapy: Cross-Model Assessment.
- PMID 40149612; DOI 10.1007/s10916-024-02136-1
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11940240 HTTP 200 len=107339
- Saved: stage3-extraction/fulltexts/R1604.txt (46026 chars)
- Decision: EXCLUDE FT-R7 - Long-term opioid therapy patient concerns: cross-model quality/appropriateness scores. No unsafe tier counts.

### R1641 - ChatGPT 4.0's efficacy in the self-diagnosis of non-traumatic hand conditions.
- PMID 40007763; DOI 10.59249/ztoz1966
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11849648 HTTP 500 len=151; Unpaywall HTTP 200; OA fetch HTTP 200 len=1817 ct=text/html; charset=utf-8; RETRY https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11849648/fullTextX HTTP 500 len=151; RETRY error ProxyError; RETRY OA fetch HTTP 200 len=1816
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; EPMC fullTextXML PMC11849648 HTTP 500 len=151; Unpaywall HTTP 200; OA fetch HTTP 200 len=1817 ct=text/html; charset=utf-8; RETRY https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11849648/fullTextX HTTP 500 len=151; RETRY error ProxyError; RETRY OA fetch HTTP 200 len=1816. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1642 - Assessing the Validity, Safety, and Utility of ChatGPT's Responses for Patients with Frozen Shoulder.
- PMID 40003671; DOI 10.1111/bjet.13454
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11857066 HTTP 200 len=112151
- Saved: stage3-extraction/fulltexts/R1642.txt (52034 chars)
- Decision: EXCLUDE FT-R7 - Frozen shoulder: ChatGPT-4.0 answers to 14 questions rated on 5-point Likert validity/safety/utility; all safety ratings were 4-5 (92.9% scored 5). No unsafe tier.

### R1646 - Comparing physician and large language model responses to influenza patient questions in the online health community.
- PMID 39986122; DOI 10.1016/j.ijmedinf.2025.105836
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1653 - Evaluating large language models as patient education tools for inflammatory bowel disease: A comparative study.
- PMID 39958450; DOI 10.3748/wjg.v31.i6.102090
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11752706 HTTP 200 len=79376
- Saved: stage3-extraction/fulltexts/R1653.txt (39629 chars)
- Decision: EXCLUDE FT-R7 - Inflammatory bowel disease patient education: 45 answers (15 questions x 3 LLMs) with median expert scores (accuracy anchor at 1 mentions serious errors that may harm, but results are scores). No tier counts.

### R1675 - Assessing the performance of AI chatbots in answering patients' common questions about low back pain.
- PMID 39874229; DOI 10.1136/ard-2024-226202
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1677 - Are AI chatbots concordant with evidence-based cancer screening recommendations?
- PMID 39862490; DOI 10.1016/j.pec.2025.108677
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 200 len=2715 ct=text/html;charset=UTF-8; RETRY OA fetch HTTP 200 len=2716
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 200 len=2715 ct=text/html;charset=UTF-8; RETRY OA fetch HTTP 200 len=2716. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1687 - ChatGPT and oral cancer: a study on informational reliability.
- PMID 39833819; DOI 10.1016/j.disamonth.2020.100988
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11745001 HTTP 200 len=80051
- Saved: stage3-extraction/fulltexts/R1687.txt (33693 chars)
- Decision: EXCLUDE FT-R7 - Oral cancer information from ChatGPT: DISCERN-type reliability/quality scores. No unsafe tier counts.

### R1692 - Proficiency, Clarity, and Objectivity of Large Language Models Versus Specialists' Knowledge on COVID-19's Impacts in Pregnancy: Cross-Sectional Pilot Study.
- PMID 39794312; DOI 10.2196/55957
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11840386 HTTP 200 len=108754
- Saved: stage3-extraction/fulltexts/R1692.txt (63229 chars)
- Decision: EXCLUDE FT-R7 - COVID-19 impacts in pregnancy: proficiency/clarity/objectivity scores for LLMs vs specialists. No unsafe tier counts.

### R1699 - Burn Patient Education in the Modern Age: A Comparative Analysis of ChatGPT and Google Performance Answering Common Questions on Burn Injury and Management.
- PMID 39761346; DOI 10.1093/jbcr/irae211
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1712 - The RepVig framework for designing use-case specific representative vignettes and evaluating triage accuracy of laypeople and symptom assessment applications.
- PMID 39715767; DOI 10.1016/j.jen.2017.06.010
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11666565 HTTP 200 len=124475
- Saved: stage3-extraction/fulltexts/R1712.txt (61688 chars)
- Decision: EXCLUDE FT-R1 - Framework paper (RepVig) for designing representative vignettes; the LLM triage figures are capability-comparison scores imported from a prior symptomcheckR study, not a primary rating of LLM responses, and no poolable undertriage numerator/denominator for LLMs is reported.

### R1716 - ChatGPT as a patient education tool in colorectal cancer-An in-depth assessment of efficacy, quality and readability.
- PMID 39690137; DOI 10.1111/codi.17267
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1718 - Evaluating reliability, quality, and readability of ChatGPT's nutritional recommendations for women with polycystic ovary syndrome.
- PMID 39673813; DOI 10.1016/j.nutres.2024.11.005
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1723 - The role of large language models in self-care: a study and benchmark on medicines and supplement guidance accuracy.
- PMID 39644377; DOI 10.1186/s13223-018-0280-7
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC12335388 HTTP 200 len=108422
- Saved: stage3-extraction/fulltexts/R1723.txt (47474 chars)
- Decision: INCLUDE_NARRATIVE - Bench. Self-care medicines/supplement guidance benchmark: 58 questions posed to multiple LLMs (incl GPT-4.0, GPT-3.5, Gemini, Gemini Advanced, Copilot, Perplexity) in Dutch, with English/context/repeat sub-studies. Responses rated 1-5 ('Inaccurate: completely incorrect and/or could lead to serious consequences' = score 1); authors call score-1 answers 'unsafe' and narrate that Perplexity produced 8 unsafe answers, but per-arm unsafe counts and denominators appear only in Fig 2, not in the text - nothing poolable as printed.

### R1731 - Impact of artificial intelligence in managing musculoskeletal pathologies in physiatry: a qualitative observational study evaluating the potential use of ChatGPT versus Copilot for patient information and clinical advice on low back pain.
- PMID 39610054; DOI 10.12701/jyms.2024.01151
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11812099 HTTP 200 len=53279
- Saved: stage3-extraction/fulltexts/R1731.txt (25495 chars)
- Decision: EXCLUDE FT-R7 - Low back pain: ChatGPT vs Copilot answers to 27 questions (with/without clinical context) rated on a 4-point validity/safety/usefulness scale (score 1 = 'significant and certain danger'), reported as descriptive scores in a qualitative study. No tier counts.

### R1744 - Assessment of Personalized Exercise Prescriptions Issued by ChatGPT 4.0 and Intelligent Health Promotion Systems for Patients with Hypertension Comorbidities Based on the Transtheoretical Model: A Comparative Analysis.
- PMID 39539514; DOI 10.1080/17538157.2023.2252066
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11559245 HTTP 200 len=155274
- Saved: stage3-extraction/fulltexts/R1744.txt (70046 chars)
- Decision: EXCLUDE FT-R7 - Personalised exercise prescriptions for hypertension comorbidities (ChatGPT-4.0 vs an intelligent health promotion system): guideline/transtheoretical-model scores. No unsafe tier counts.

### R1748 - Evaluating a generative artificial intelligence accuracy in providing medication instructions from smartphone images.
- PMID 39515421; DOI 10.1016/j.japh.2024.102284
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1749 - AI in Hidradenitis Suppurativa: Expert Evaluation of Patient-Facing Information.
- PMID 39507766; DOI 10.1148/radiol.230922
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11539865 HTTP 200 len=40894
- Saved: stage3-extraction/fulltexts/R1749.txt (22575 chars)
- Decision: EXCLUDE FT-R7 - Hidradenitis suppurativa patient-facing information: expert Likert ratings. No unsafe tier counts.

### R1752 - Assessing the ability of GPT-4o to visually recognize medications and provide patient education.
- PMID 39501020; DOI 10.4103/NRR.NRR-D-24-00165
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11538418 HTTP 200 len=78517
- Saved: stage3-extraction/fulltexts/R1752.txt (39126 chars)
- Decision: EXCLUDE FT-R7 - GPT-4o visual medication recognition and patient education: 3-point accuracy scores for 20 medications; text states none was labelled incorrect or directly harmful. No unsafe tier.

### R1780 - Artificial intelligence-powered chatbots in search engines: a cross-sectional study on the quality and risks of drug information for patients.
- PMID 39353736; DOI 10.1111/j.1742-1241.2010.02408.x
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11874309 HTTP 200 len=96360
- Saved: stage3-extraction/fulltexts/R1780.txt (45634 chars)
- Decision: INCLUDE_NARRATIVE - Bench. Drug information for patients from a search-engine chatbot (Bing Copilot): 10 patient questions x 50 drugs = 500 answers analysed. Accuracy/completeness are the all-response outcomes; potential harm was rated only in a preselected subset of 20 inaccurate chatbot answers, of which experts judged 66% potentially harmful (42% moderate-to-mild harm, 22% severe harm, as printed) - the harm denominator is the inaccurate subset, not all responses rated for safety, so nothing poolable for the primary outcome.

### R1781 - "Doctor ChatGPT, Can You Help Me?" The Patient's Perspective: Cross-Sectional Study.
- PMID 39352738; DOI 10.1016/j.jormas.2023.101471
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11480680 HTTP 200 len=92658
- Saved: stage3-extraction/fulltexts/R1781.txt (40908 chars)
- Decision: INCLUDE_PRIMARY - Bench with real patient questions. 100 patient questions (20 per specialty x 5 specialties) answered by ChatGPT-4.0 and a web-based expert panel; the 100 ChatGPT answers were each classified by 3 physicians in the relevant specialty on a binary item 'Does the answer contain potentially harmful advice?' (yes/no). Potentially harmful: 16/100 ChatGPT responses flagged by >=1 of 3 physicians (15 flagged by exactly one physician, 1 additional flagged by two) - Results section 'Patients' Perception Showed No Difference Between Nonharmful and Potentially Harmful Advice'. Total ChatGPT responses rated = 100. No consensus-tier count is printed; numerator is the >=1-rater flag count as reported.

### R1785 - Evaluating the scientific reliability of ChatGPT as a source of information on asthma.
- PMID 39328581; DOI 10.1016/j.jacig.2024.100330
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11426030 HTTP 200 len=38496
- Saved: stage3-extraction/fulltexts/R1785.txt (15313 chars)
- Decision: EXCLUDE FT-R7 - Asthma reliability: single combined 5-point accuracy scale whose anchors mix inaccuracy and harm (1 = very poor/unacceptable inaccuracies to 5 = no inaccuracies); median score 4, five responses scored <=3. Safety cannot be separated from the combined quality score and no unsafe tier is reported.

### R1802 - Quality and Accountability of ChatGPT in Health Care in Low- and Middle-Income Countries: Simulated Patient Study.
- PMID 39250188; DOI 10.3184/003685008X284628
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11420570 HTTP 200 len=29808
- Saved: stage3-extraction/fulltexts/R1802.txt (13211 chars)
- Decision: INCLUDE_NARRATIVE - Simulated-patient study in LMIC primary care: ChatGPT (GPT-3.5-era, as discussed in the paper) managing 9 common diseases, 27 trials. Combined indicator, not separable into an unsafe tier: unnecessary or harmful medication suggestions in 23/27 trials (85%), and 16/27 (59%) even after a correct diagnosis - Abstract/Results. No listed secondary outcome in poolable form.

### R1813 - Evaluating the effectiveness of large language models in patient education for conjunctivitis.
- PMID 39214677; DOI 10.1136/bjo-2024-325599
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1829 - Evaluating the Efficacy of ChatGPT as a Patient Education Tool in Prostate Cancer: Multimetric Assessment.
- PMID 39141904; DOI 10.1002/pon.5158
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11358656 HTTP 200 len=137090
- Saved: stage3-extraction/fulltexts/R1829.txt (54488 chars)
- Decision: EXCLUDE FT-R7 - Prostate cancer patient education: PEMAT/readability metrics; fabrication assessed at reference level (2 hallucinated references of 30 references), denominator is references, not responses. No unsafe tier.

### R1836 - Artificial Intelligence-Generated Patient Education Materials for Helicobacter pylori Infection: A Comparative Analysis.
- PMID 39097925; DOI 10.1111/hel.13115
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; Unpaywall error ChunkedEncodingError; RETRY OA error ChunkedEncodingError
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200; Unpaywall error ChunkedEncodingError; RETRY OA error ChunkedEncodingError. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1859 - Assessment of the information provided by ChatGPT regarding exercise for patients with type 2 diabetes: a pilot study.
- PMID 38964828; DOI 10.2337/dc23-0197
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11227747 HTTP 200 len=54376
- Saved: stage3-extraction/fulltexts/R1859.txt (24286 chars)
- Decision: EXCLUDE FT-R7 - Exercise information for type 2 diabetes: 14 ChatGPT-4.0 responses rated on Likert validity/safety/utility categories; results are category/score summaries with no unsafe tier counts.

### R1864 - The future of patient education: A study on AI-driven responses to urinary incontinence inquiries.
- PMID 38944693; DOI 10.1002/ijgo.15751
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 403 len=5624 ct=text/html; charset=UTF-8; RETRY OA error ChunkedEncodingError
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 403 len=5624 ct=text/html; charset=UTF-8; RETRY OA error ChunkedEncodingError. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1880 - The assessment of the validity, safety, and utility of ChatGPT for patients with herniated lumbar disc: A preliminary study.
- PMID 38847711; DOI 10.1097/MD.0000000000038445
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11155576 HTTP 200 len=55967
- Saved: stage3-extraction/fulltexts/R1880.txt (21843 chars)
- Decision: EXCLUDE FT-R7 - Herniated lumbar disc: ChatGPT responses rated on Likert validity/safety/utility; authors report none of the answers was inaccurate or erroneous. No unsafe tier.

### R1886 - Appropriateness of ChatGPT in Answering Heart Failure Related Questions.
- PMID 38821760; DOI 10.1016/j.hlc.2024.03.005
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 200 len=2641 ct=text/html;charset=UTF-8; RETRY OA fetch HTTP 200 len=2641
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 200 len=2641 ct=text/html;charset=UTF-8; RETRY OA fetch HTTP 200 len=2641. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1890 - Comparison of ChatGPT, Gemini, and Le Chat with physician interpretations of medical laboratory questions from an online health forum.
- PMID 38804035; DOI 10.2196/32578
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 202 len=0 ct=text/html; charset=UTF-8; RETRY OA fetch HTTP 202 len=0
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 202 len=0 ct=text/html; charset=UTF-8; RETRY OA fetch HTTP 202 len=0. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1893 - Use of large language model-based chatbots in managing the rehabilitation concerns and education needs of outpatient stroke survivors and caregivers.
- PMID 38784703; DOI 10.1177/20552076231183542
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11111889 HTTP 200 len=70454
- Saved: stage3-extraction/fulltexts/R1893.txt (37163 chars)
- Decision: EXCLUDE FT-R7 - Stroke survivors'/caregivers' rehabilitation concerns answered by LLM chatbots: accuracy/readability scores plus qualitative themes (hallucinated resources noted qualitatively). No unsafe tier counts.

### R1894 - Educating patients on osteoporosis and bone health: Can "ChatGPT" provide high-quality content?
- PMID 38769125; DOI 10.1007/s00590-024-03990-y
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1909 - Mixed methods assessment of the influence of demographics on medical advice of ChatGPT.
- PMID 38679900; DOI 10.1016/j.wneu.2023.11.062
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11339520 HTTP 500 len=151; Unpaywall HTTP 200; RETRY https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11339520/fullTextX HTTP 500 len=151; RETRY https://europepmc.org/articles/PMC11339520?pdf=render HTTP 403 len=5629
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; EPMC fullTextXML PMC11339520 HTTP 500 len=151; Unpaywall HTTP 200; RETRY https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11339520/fullTextX HTTP 500 len=151; RETRY https://europepmc.org/articles/PMC11339520?pdf=render HTTP 403 len=5629. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R1919 - Evaluating ChatGPT's efficacy in assessing the safety of non-prescription medications and supplements in patients with kidney disease.
- PMID 38638404; DOI 10.1177/20552076241248082
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11025428 HTTP 200 len=68769
- Saved: stage3-extraction/fulltexts/R1919.txt (33584 chars)
- Decision: EXCLUDE FT-R7 - Outcome is the accuracy of ChatGPT's own classification of 124 non-prescription medications/supplements as generally safe / potentially harmful / unknown toxicity against Micromedex (GPT-3.5: 11/124 labelled potentially harmful; GPT-4: 29/124) - the responses themselves were not clinician-rated for safety, so there is no unsafe tier of responses.

### R1920 - Quality of Answers of Generative Large Language Models Versus Peer Users for Interpreting Laboratory Test Results for Lay Patients: Evaluation Study.
- PMID 38630520; DOI 10.1681/ASN.0000000000000166
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11063893 HTTP 200 len=140400
- Saved: stage3-extraction/fulltexts/R1920.txt (62040 chars)
- Decision: EXCLUDE FT-R7 - Lab test result interpretation for lay patients (LLMs vs peer users): Likert means for correctness, helpfulness, relevance and potential harm. No unsafe tier counts. This journal version (JMIR) is the RETAINED report for the duplicate pair with R1938.

### R1938 - Quality of Answers of Generative Large Language Models vs Peer Patients for Interpreting Lab Test Results for Lay Patients: Evaluation Study.
- PMID 38529075; DOI 10.2466/pr0.1966.19.1.3
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC10962749 HTTP 200 len=112229
- Saved: stage3-extraction/fulltexts/R1938.txt (51229 chars)
- Decision: EXCLUDE FT-R6 - Duplicate report of R1920: this is the arXiv/preprint version of the same lab-test-results study (He et al.) published in JMIR as R1920, which is retained.

### R1939 - Using artificial intelligence for exercise prescription in personalised health promotion: A critical evaluation of OpenAI's GPT-4 model.
- PMID 38524814; DOI 10.3390/sports7010016
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC10955739 HTTP 200 len=238850
- Saved: stage3-extraction/fulltexts/R1939.txt (102681 chars)
- Decision: EXCLUDE FT-R7 - Exercise prescription in personalised health promotion (GPT-4): critical evaluation with scores against guidelines. No unsafe tier counts.

### R1943 - Assessing the Accuracy of Generative Conversational Artificial Intelligence in Debunking Sleep Health Myths: Mixed Methods Comparative Study With Expert Analysis.
- PMID 38501898; DOI 10.1038/s41746-023-00856-1
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC11061787 HTTP 200 len=108633
- Saved: stage3-extraction/fulltexts/R1943.txt (51348 chars)
- Decision: EXCLUDE FT-R7 - Sleep health myth debunking: accuracy scores from expert analysis (mixed methods). No unsafe tier counts.

### R1944 - Quality and Dependability of ChatGPT and DingXiangYuan Forums for Remote Orthopedic Consultations: Comparative Analysis.
- PMID 38483451; DOI 10.1148/radiol.232561
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC10979330 HTTP 200 len=104512
- Saved: stage3-extraction/fulltexts/R1944.txt (46925 chars)
- Decision: EXCLUDE FT-R7 - Remote orthopedic consultations (ChatGPT vs DingXiangYuan forum): quality/dependability scores. No unsafe tier counts.

### R1958 - Automating untruths: ChatGPT, self-managed medication abortion, and the threat of misinformation in a post-Roe world.
- PMID 38419805; DOI 10.1371/journal.pone.0226417
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC10900507 HTTP 200 len=71491
- Saved: stage3-extraction/fulltexts/R1958.txt (33736 chars)
- Decision: INCLUDE_NARRATIVE - Bench. ChatGPT responses on self-managed medication abortion analysed qualitatively against the evidence base (inaccurate portrayal of self-managed abortion as dangerous, misleading/fabricated content documented thematically). Eligible topic, but no explicit unsafe tier and no numerator/denominator - nothing poolable.

### R1976 - Use of ChatGPT for Determining Clinical and Surgical Treatment of Lumbar Disc Herniation With Radiculopathy: A North American Spine Society Guideline Comparison.
- PMID 38291746; DOI 10.48550/arXiv.2304.14454
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC10992643 HTTP 200 len=73930
- Saved: stage3-extraction/fulltexts/R1976.txt (40652 chars)
- Decision: EXCLUDE FT-R3 - Clinician-facing task: ChatGPT used to determine clinical and surgical treatment of lumbar disc herniation against North American Spine Society guidelines (guideline-concordance coding). Not patient-facing advice.

### R1987 - Utilizing ChatGPT in Telepharmacy.
- PMID 38230387; DOI 10.7759/cureus.52365
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC10790595 HTTP 200 len=203862
- Saved: stage3-extraction/fulltexts/R1987.txt (170050 chars)
- Decision: EXCLUDE FT-R7 - Telepharmacy: ChatGPT answers to drug-information questions scored on a 4-point accuracy scale; text states no answer was directly harmful or entirely/mostly incorrect. No unsafe tier.

### R2013 - A Novel Approach: Evaluating ChatGPT's Utility for the Management of Thyroid Nodules.
- PMID 38021609; DOI 10.7759/cureus.47576
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC10666652 HTTP 200 len=63284
- Saved: stage3-extraction/fulltexts/R2013.txt (32898 chars)
- Decision: EXCLUDE FT-R7 - Thyroid nodule management questions: Likert-type recommendation/benefit scores. No unsafe tier counts.

### R2020 - Artificial intelligence and allergic rhinitis: does ChatGPT increase or impair the knowledge?
- PMID 37968109; DOI 10.1093/pubmed/fdad219
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 403 len=5779 ct=text/html; charset=UTF-8; RETRY OA fetch HTTP 403 len=5779
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 403 len=5779 ct=text/html; charset=UTF-8; RETRY OA fetch HTTP 403 len=5779. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R2025 - Heart-to-heart with ChatGPT: the impact of patients consulting AI for cardiovascular health advice.
- PMID 37945282; DOI 10.3390/ijerph20043378
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC10649823 HTTP 200 len=77340
- Saved: stage3-extraction/fulltexts/R2025.txt (37255 chars)
- Decision: EXCLUDE FT-R7 - Qualitative interview study of patients consulting ChatGPT for cardiovascular advice (impact/perceptions). No LLM responses were clinician-rated; no poolable outcome.

### R2030 - Assessment of ChatGPT in the Prehospital Management of Ophthalmological Emergencies - An Analysis of 10 Fictional Case Vignettes.
- PMID 37890504; DOI 10.1055/a-2149-0447
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 200 len=4789 ct=text/html;charset=UTF-8; RETRY OA fetch HTTP 200 len=4789
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200; OA fetch HTTP 200 len=4789 ct=text/html;charset=UTF-8; RETRY OA fetch HTTP 200 len=4789. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R2036 - A vignette-based evaluation of ChatGPT's ability to provide appropriate and equitable medical advice across care contexts.
- PMID 37857839; DOI 10.1136/dtb.2019.000008
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC10587094 HTTP 200 len=48167
- Saved: stage3-extraction/fulltexts/R2036.txt (24424 chars)
- Decision: INCLUDE_NARRATIVE - Bench. ChatGPT (GPT-3.5-era) responses to 96 patient-perspective advice-seeking vignettes across preventive, acute and palliative care contexts, rated for clinical appropriateness against guidelines: 93/96 (97%) appropriate and not explicitly violating guidelines; 1 response with faulty follow-up reasoning described. Appropriateness is not an explicit unsafe/harmful tier and no harm counts are reported - nothing poolable.

### R2042 - Comparison of Diagnostic and Triage Accuracy of Ada Health and WebMD Symptom Checkers, ChatGPT, and Physicians for Patients in an Emergency Department: Clinical Data Analysis Study.
- PMID 37788063; DOI 10.1515/dx-2018-0009
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC10582809 HTTP 200 len=98442
- Saved: stage3-extraction/fulltexts/R2042.txt (49309 chars)
- Decision: INCLUDE_PRIMARY - Bench. Triage recommendations for 37 emergency-department cases with sufficient triage data, rated against independent physicians: explicit 'unsafe' triage tier - ChatGPT-3.5 unsafe 15/37 (41%), ChatGPT-4.0 unsafe 8/37 (22%); agreement 22/37 and 28/37, too-cautious 0/37 and 1/37 - Abstract/Results text. (Non-LLM arms: Ada 5/37 unsafe, WebMD 7/37.) Total LLM responses = 74. Stratum: bench; disposition/triage presentations.

### R2048 - The Potential of ChatGPT as a Self-Diagnostic Tool in Common Orthopedic Diseases: Exploratory Study.
- PMID 37713254; DOI 10.1145/2702613.2732865
- Routes: EPMC search HTTP 200; EPMC fullTextXML PMC10541638 HTTP 200 len=115141
- Saved: stage3-extraction/fulltexts/R2048.txt (49670 chars)
- Decision: EXCLUDE FT-R7 - Self-diagnosis in common orthopedic diseases: diagnostic accuracy percentages only; no safety rating of responses.

### R2050 - Can artificial intelligence replace biochemists? A study comparing interpretation of thyroid function test results by ChatGPT and Google Bard to practising biochemists.
- PMID 37699796; DOI 10.1177/00045632231203473
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; Unpaywall error ChunkedEncodingError; RETRY OA error ChunkedEncodingError
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200; Unpaywall error ChunkedEncodingError; RETRY OA error ChunkedEncodingError. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R2059 - Artificial intelligence chatbot performance in triage of ophthalmic conditions.
- PMID 37572695; DOI 10.1016/j.jcjo.2023.07.016
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200; Unpaywall error ProxyError; RETRY OA error ProxyError
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200; Unpaywall error ProxyError; RETRY OA error ProxyError. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R2061 - Will artificial intelligence chatbots replace clinical pharmacologists? An exploratory study in clinical practice.
- PMID 37566133; DOI 10.1007/s00228-023-03547-8
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R2063 - Exploring the Role of a Large Language Model on Carpal Tunnel Syndrome Management: An Observation Study of ChatGPT.
- PMID 37530687; DOI 10.1016/j.jhsa.2023.07.003
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

### R2064 - Head-to-Head Comparison of ChatGPT Versus Google Search for Medical Knowledge Acquisition.
- PMID 37529853; DOI 10.1002/ohn.465
- Routes: EPMC search HTTP 200; Unpaywall HTTP 200
- Saved: no
- Decision: NOT_RETRIEVED FT-R8 - Full text not retrieved after >=2 legitimate routes. Routes tried: EPMC search HTTP 200; Unpaywall HTTP 200. Europe PMC abstract (where available) was not used to exclude on content, per FT-R8.

