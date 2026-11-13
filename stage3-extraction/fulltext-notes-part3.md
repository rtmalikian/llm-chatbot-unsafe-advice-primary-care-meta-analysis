# Full-text notes - Review 4, batch 3 of 4 (fulltext-list-part3.csv, 171 records)

Assessor pass date: 2026-11-12 (PT). Protocol: stage0-protocol/protocol.md. Rules: stage2-screening/fulltext-rules.md (FT-R1 to FT-R8).

## Retrieval method

Route 1: Europe PMC - search API (by PMID or DOI) to identify PMCID/source ID, then fullTextXML. Route 2: DOI resolution to the publisher/preprint-server open-access page (Frontiers, MDPI, JMIR, BMC, Research Square, F1000 etc). Route 3 (failures and abstract-only captures): Europe PMC web article page, PMC search, medRxiv full-text/PDF endpoints, OSF download, Research Square PDF endpoint, Authorea, publisher-page re-check, and one browser text fetch / one title web search where noted. No paywall workarounds were used. At least two routes were tried for every NOT_RETRIEVED record.

Full texts saved to stage3-extraction/fulltexts/: 151 genuine full texts for this batch (157 files, of which 6 are publisher abstract/preview pages only - R2158, R2209, R2248, R2335, R2506, R2610 - and those records are coded NOT_RETRIEVED). File types: .xml (Europe PMC fullTextXML) or .txt (publisher/preprint HTML or PDF text extraction).

## Decision taxonomy as applied

- INCLUDE_PRIMARY: eligible and reports an explicit unsafe/harmful/dangerous tier with numerator + denominator (per-arm or study total as printed; derived counts flagged DERIVED in the note).
- INCLUDE_SECONDARY: eligible, no primary-pool data, but a secondary outcome (undertriage, or problematic-type inappropriate-medication/referral outcome) in poolable form (numerator + denominator, or percentage + printed denominator as noted).
- INCLUDE_NARRATIVE: eligible (clinician-rated safety/harm/risk outcome present) but nothing poolable as printed (e.g. Likert safety means, rating-level percentages, counts confined to figures/tables not in accessible text).
- EXCLUDE FT-R7: no clinician-rated safety outcome at all and no poolable secondary outcome (protocol eligibility item 4 fails). This is the boundary used between INCLUDE_NARRATIVE and FT-R7.
- EXCLUDE FT-R5: specialty-only sets per protocol, following the Stage 1 gate adjudications where they exist (e.g. achalasia, eye subspecialties, haemodialysis NO; bacterial vaginosis, herpes zoster, diabetic neuropathy, late-life depression YES). Where an out-of-scope paper nonetheless printed explicit-tier counts, the counts are recorded in its note for the coordinator.
- FT-R6 duplicates are within-batch only, per the task instruction; cross-batch duplicate studies (flagged in gate notes for e.g. R2099, R2105, R2116, R2333, R2402, R2681) received a normal decision on their own content and are left to the coordinator's cross-batch deduplication.

## Counts per decision (from fulltext-decisions-part3.csv)

- INCLUDE_PRIMARY: 17
- INCLUDE_SECONDARY: 6
- INCLUDE_NARRATIVE: 26
- EXCLUDE: 102
- NOT_RETRIEVED: 20
- EXCLUDE by code: {'FT-R7': 31, 'FT-R1': 1, 'FT-R5': 54, 'FT-R6': 4, 'FT-R4': 7, 'FT-R2': 2, 'FT-R3': 3}

## Per-record routes and decisions

### R2066 - EXCLUDE FT-R7
Title: Artificial Intelligence and Public Health: Evaluating ChatGPT Responses to Vaccination Myths and Misconceptions.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC10386180:200:149803b | saved: R2066.xml
Notes: Vaccination myths (WHO 11 myths) answered by GPT-3.5/GPT-4: outcomes are Correctness, Clarity and Exhaustiveness scores by two expert raters; no safety/harm rating and no poolable secondary outcome. (List DOI is erroneous; retrieved article is Vaccines 2023, 10.3390/vaccines11071217, PMID as listed.)

### R2085 - NOT_RETRIEVED FT-R8
Title: Potential safety concerns in use of the artificial intelligence chatbot 'ChatGPT' for perioperative patient communication.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI:FAIL:HTTPError:HTTP Error 403: Forbidden; EPMC-web:FAIL:HTTPError:HTTP Error 403: Forbidden | retry: epmc-xml-retry:FAIL HTTPError HTTP Error 404: ; pmc-search:FAIL HTTPError HTTP Error 404: Not Found; doi-retry-browserUA:FAIL HTTPError HTTP Error 403: Forbidden | saved: none
Notes: Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2086 - EXCLUDE FT-R1
Title: AI chatbots not yet ready for clinical use.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC10130576:200:40519b | saved: R2086.xml
Notes: Perspective/commentary article ('AI chatbots not yet ready for clinical use', Frontiers Health Informatics, editorially reviewed opinion piece). No primary study with rated responses.

### R2091 - NOT_RETRIEVED FT-R8
Title: What if your patient switches from Dr. Google to Dr. ChatGPT? A vignette-based survey of the trustworthiness, value, and danger of ChatGPT-generated responses to health questions.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI:FAIL:RemoteDisconnected:Remote end closed connection without response; EPMC-web:FAIL:RemoteDisconnected:Remote end closed connection without response | retry: epmc-xml-retry:FAIL HTTPError HTTP Error 404: ; pmc-search:FAIL HTTPError HTTP Error 404: Not Found; doi-retry-browserUA:FAIL HTTPError HTTP Error 403: Forbidden | saved: none
Notes: Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2099 - INCLUDE_PRIMARY
Title: A comparative cross-sectional evaluation of generative AI chatbots for patient-oriented bacterial vaginosis health advice: safety, accuracy, guideline concordance, empathy, and readability.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13627438:200:112923b | saved: R2099.xml
Notes: Bench; ChatGPT, Gemini, Microsoft Copilot, DeepSeek, Doubao; binary safety (potentially unsafe) Table 1: ChatGPT 4/61, Gemini 6/61, Copilot 5/61, DeepSeek 7/61, Doubao 9/61; total unsafe 31/305 responses (61 questions x 5 models). Bacterial vaginosis, primary-care presentation.

### R2100 - INCLUDE_PRIMARY
Title: Safety and quality of patient-facing frozen shoulder information from four generative AI chatbot interfaces: a cross-sectional study
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:71532chars:https://www.researchsquare.com/article/rs-10805692/v1 | saved: R2100.txt
Notes: Bench; ChatGPT, Gemini, DeepSeek, Doubao; potentially unsafe: ChatGPT 3/50, DeepSeek 5/50, Gemini 6/50, Doubao 7/50; total 21/200 (50 questions x 4 models), Research Square full text, abstract + Results.

### R2101 - INCLUDE_PRIMARY
Title: Large language models provide unsafe answers to patient-posed medical questions.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13013898:200:85767b | saved: R2101.xml
Notes: Bench; Claude 3.5 Sonnet, Gemini 1.5 Flash, GPT-4o, Llama-3.0/3.1-70B; 222 primary-care patient-posed questions, 222 responses/model, 888 total. Explicit 'Unsafe' tag. Per-arm counts DERIVED from printed percentages x printed denominator 222 (extraction-form derived rule, flagged): Claude 11/222 (5.0%), GPT-4o 30/222 (13.5%), Llama 29/222 (13.1%); Gemini unsafe % in Fig.3 only, not printed numerically. HealthAdvice set, Results/Fig.3.

### R2103 - EXCLUDE FT-R5
Title: Comparative evaluation of ChatGPT, DeepSeek, and Doubao for pediatric IgA vasculitis patient education: content quality, reliability, readability, understandability, and actionability.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13731278:200:120210b | saved: R2103.xml
Notes: Specialty-only: paediatric IgA vasculitis patient education (paediatric subspecialty vasculitis); safety discussed qualitatively via omissions, no explicit unsafe tier counts.

### R2104 - INCLUDE_PRIMARY
Title: Safety, accuracy, information quality, readability, and supportive communication of LLM-based chatbots in responses to researcher-developed consumer-oriented prompts on recurrent aphthous stomatitis: an exploratory cross-sectional comparative study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:63101chars:https://www.frontiersin.org/journals/oral-health/articles/10.3389/froh.2026.1968034/full | saved: R2104.txt
Notes: Bench; ChatGPT, Gemini, Copilot, DeepSeek, Doubao; binary safety (potentially unsafe/misleading) Table 1: ChatGPT 2/30, Gemini 3/30, Copilot 2/30, DeepSeek 5/30, Doubao 4/30; total 16/150. Recurrent aphthous stomatitis (mouth ulcers), primary-care presentation.

### R2105 - EXCLUDE FT-R5
Title: Safety, accuracy, empathic communication, information quality, and readability of five large language model interfaces answering public questions about interstitial cystitis/bladder pain syndrome.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13547468:200:116156b | saved: R2105.xml
Notes: Specialty-only: interstitial cystitis/bladder pain syndrome (urology subspecialty set, gate scope NO). Binary safety table exists in paper but study is out of scope.

### R2107 - INCLUDE_PRIMARY
Title: A cross-sectional evaluation of large language model chatbot interfaces for patient-facing herpes zoster information: safety, information quality, and readability.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13623941:200:147149b | saved: R2107.xml
Notes: Bench; ChatGPT-5.5 Instant, DeepSeek-V4-Pro, Doubao-Seed-2.0-Pro, Gemini 3.5 Flash, Qwen3.7-Plus; binary safety Table 1: 11/46, 12/46, 15/46, 14/46, 14/46; total 66/230. Herpes zoster, primary-care presentation.

### R2108 - INCLUDE_PRIMARY
Title: A comparative evaluation of generative AI chatbots for patient-oriented advice on painful diabetic peripheral neuropathy: safety, accuracy, guideline concordance, actionability, and readability.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13584960:200:115777b | saved: R2108.xml
Notes: Bench; ChatGPT, Gemini, Copilot, DeepSeek, Doubao; binary safety coded 0=safe 1=unsafe/potentially unsafe (Results, Safety): total unsafe 28/300 (60 questions x 5 models), safe 272/300 printed; per-model unsafe rates 5.0% (ChatGPT) to 15.0% (Doubao) in text/Fig.2A, per-arm counts not individually printed. Painful diabetic peripheral neuropathy.

### R2110 - EXCLUDE FT-R5
Title: Safety and quality of public chatbots for lung cancer prognostic information: a comparative evaluation.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13547269:200:102145b | saved: R2110.xml
Notes: Specialty-only: lung cancer prognostic information (oncology prognosis set). Binary safety counts exist (Table 1: ChatGPT 11/53, Gemini 5/53, Copilot 12/53, DeepSeek 20/53, Doubao 16/53; total 64/265) but out of scope - counts recorded here for the coordinator in case scope is revisited.

### R2111 - INCLUDE_PRIMARY
Title: Consumer chatbots gave similarly empathic answers whether safe or unsafe: a physician-rated evaluation in six languages
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI:FAIL:HTTPError:HTTP Error 403: Forbidden | retry: medrxiv-full:HTML 107666chars https://www.medrxiv.org/content/10.64898/2026.05.09.26352813v1.full | saved: R2111.txt
Notes: Bench; ChatGPT, Claude, DeepSeek, Gemini x 21 scenarios x 6 languages = 504 responses, 2 physician raters/response. Explicit catastrophic safety tier (response-level safety <=2 by mean of two raters): 37/504 catastrophic (7.3%), Results text. Per-chatbot catastrophic counts not printed in text (per-language only: English 3.6% to Thai/Hebrew 15.5% of ratings). Mixed primary-care/emergency scenarios incl one paranoid-ideation scenario (not crisis-only).

### R2112 - EXCLUDE FT-R5
Title: Completeness and guideline concordance of artificial intelligence chatbot responses to patient questions on regenerative therapies for erectile dysfunction: a multi-platform analysis.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13741058:200:101116b | saved: R2112.xml
Notes: Specialty-only: regenerative therapies for erectile dysfunction (urology subspecialty therapy); completeness/guideline concordance outcomes, no unsafe tier.

### R2114 - EXCLUDE FT-R7
Title: Effect of Disclaimers on the Public Perception of AI-Generated Medical Advice: Two Preregistered Survey Experiments
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:short5:https://osf.io/d2sz6 | retry: osf-download:HTML 34329chars https://idvyorynw6xy.compat.objectstorage.us-ashburn-1.oraclecloud.com/cos-prod-osf-1-files-ash/809d | Route 3: OSF download re-fetched in full (115,227-byte DOCX; first capture was truncated); text extracted from word/document.xml. | saved: R2114.txt
Notes: Two preregistered survey experiments on how disclaimers affect PUBLIC PERCEPTION of AI-generated medical advice (lay participants); responses were not clinician-rated for safety and no poolable secondary outcome. Retained record for this study; duplicate version record is R2115.

### R2115 - EXCLUDE FT-R6
Title: Effect of Disclaimers on the Public Perception of AI-Generated Medical Advice: Two Preregistered Survey Experiments
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:short5:https://osf.io/d2sz6_v1 | retry: osf-download:HTML 34329chars https://idvyorynw6xy.compat.objectstorage.us-ashburn-1.oraclecloud.com/cos-prod-osf-1-files-ash/809d | Route 3: OSF download re-fetched in full; byte-identical to R2114 (duplicate). | saved: R2115.txt
Notes: Duplicate report of R2114 (same OSF preprint, DOI 10.31234/osf.io/d2sz6 version record; downloaded file byte-identical to R2114). Retained record: R2114.

### R2116 - INCLUDE_PRIMARY
Title: Evaluation of generative AI-driven chatbots as sources of consumer health information on hand, foot, and mouth disease: a cross-sectional comparative study of safety, accuracy, information quality, readability, and empathy.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13503565:200:110162b | saved: R2116.xml
Notes: Bench; ChatGPT-4o, Gemini 2.5 Pro, Copilot, Doubao, DeepSeek-V3.2-Exp; binary safety Table 1: ChatGPT 1/20, Gemini 2/20, Copilot 2/20, DeepSeek 2/20, Doubao 3/20; total 10/100 (20 prompts x 5 models). Hand, foot and mouth disease.

### R2117 - EXCLUDE FT-R7
Title: Trusting Generative AI for Health Advice: Preregistered Survey Experiment.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13286080:200:144612b | saved: R2117.xml
Notes: Human-user survey experiment on trust/credibility of generative AI health advice (incl 'AI nurse' framing). No clinician-rated safety responses and no poolable secondary outcome.

### R2118 - EXCLUDE FT-R7
Title: Generative AI chatbots as sources of phimosis-related consumer health information: a cross-sectional comparison of quality, source transparency, and readability.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13677900:200:97658b | saved: R2118.xml
Notes: Phimosis consumer information: quality, source transparency and readability only; authors state clinical safety was not assessed. No safety rating, no poolable secondary outcome.

### R2120 - INCLUDE_PRIMARY
Title: Large Language Model Chatbot Responses to Cancer Survivorship Questions in Hong Kong: Bilingual Evaluation and Prompt Optimization Study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13691464:200:122538b | saved: R2120.xml
Notes: Bench; Gemini 3.1 Pro, HK Chat-0.6.2, DeepSeek-V3.2, Kimi-K2.5; 25 questions x 4 models x 2 languages = 200 responses; binary safe/unsafe by expert-panel consensus, Table 3 + Results: pooled per model Gemini 2/50, Kimi-K2.5 6/50, DeepSeek-V3.2 5/50, HK Chat 7/50; total 20/200 (10%). BORDERLINE scope: cancer survivorship set incl chronic-disease management and self-management domains - counted in scope, flagged for coordinator.

### R2121 - EXCLUDE FT-R5
Title: Evaluating Five Generative AI Chatbots for Myocarditis-Related Public Health Consultation: A Multidimensional Assessment of Safety, Accuracy, Empathy, Reliability, Quality, and Readability
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:6478chars:https://www.researchsquare.com/article/rs-10228718/v1 | Route 3: Research Square PDF (article/rs-10228718/v1.pdf via assets-eu.researchsquare.com) downloaded and text-extracted (pdftotext), replacing abstract-only landing page. | saved: R2121.txt
Notes: Specialty-only: myocarditis-specific consultation incl return-to-exercise clearance (cardiology, gate scope NO). Binary safety flagged responses described (21) but out of scope.

### R2123 - INCLUDE_PRIMARY
Title: Evaluation and comparison of large language model responses to patient questions after diagnosis of high-risk human papillomavirus infection: an expert-rated digital patient education study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13473150:200:126804b | saved: R2123.xml
Notes: Bench; ChatGPT-5.5 Instant, DeepSeek-V3; binary potential-harm tier by majority vote, Table 4: ChatGPT 3/45, DeepSeek 7/45; total 10/90. High-risk HPV patient questions.

### R2126 - EXCLUDE FT-R5
Title: Comparative evaluation of information quality, readability, and guideline consistency of large language model-generated educational content on hemodialysis complications: a cross-sectional assessment of generative AI-driven chatbots.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13390207:200:154560b | saved: R2126.xml
Notes: Specialty-only: haemodialysis complications (nephrology, gate scope NO); quality scales only, no unsafe tier.

### R2129 - EXCLUDE FT-R7
Title: An Assessment of GPT-3.5 and GPT-4.0 Responses to Scoliosis FAQs.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13117403:200:127196b | saved: R2129.xml
Notes: Scoliosis FAQs: expert spine surgeons rated perceived adequacy; authors state the aim was not to validate accuracy or safety. No safety rating, no poolable outcome.

### R2132 - INCLUDE_NARRATIVE
Title: Disclaimers and Referral Patterns for Medical Advice Across Urgency Levels: Large Language Model Evaluation Study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12991190:200:105735b | saved: R2132.xml
Notes: Bench; 4 LLMs, 908 responses to 227 authentic patient queries. Safety-relevant outcome is disclaimer/referral ordinal classification (GPT-4o as primary rater, human-validated subset): 97% (881/908) advised consulting a professional. No unsafe tier, no disposition-vs-reference undertriage counts - narrative only.

### R2134 - INCLUDE_PRIMARY
Title: Safety, Accuracy, Empathy, Information Quality, and Readability of Large Language Models in Answering Caregiver Questions About Pediatric Burn First Aid and Inpatient Care: A Cross-Sectional Comparative Study
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:50309chars:https://www.researchsquare.com/article/rs-10862831/v1 | saved: R2134.txt
Notes: Bench; ChatGPT, Gemini, DeepSeek, Doubao; binary safe vs potentially unsafe, 36 responses/model. Unsafe DERIVED as complement of printed safe counts (Results text): ChatGPT 3/36 (safe 33), Gemini 5/36 (safe 31), DeepSeek 6/36 (safe 30), Doubao 7/36 (safe 29); total 21/144. Caregiver paediatric burn first aid/inpatient questions; full text now retrieved (Research Square), superseding gate abstract-only derivation - same numbers.

### R2141 - EXCLUDE FT-R5
Title: Effect of Prompt Structure on Large Language Model-Recommended Triage Levels in Urologic Patient Messages
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:22250chars:https://www.researchsquare.com/article/rs-9453460/v1 | saved: R2141.txt
Notes: Specialty-only: urologic patient messages triage (gate scope NO). 'Unsafe undertriage' outcome had 0 events in all prompt arms of a single model (GPT-5.4 Thinking); out of scope in any case.

### R2143 - EXCLUDE FT-R5
Title: Evaluating the Performance of ChatGPT-5 in Answering Common Patient Questions on Developmental Dysplasia of the Hip and Periacetabular Osteotomy
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:29846chars:https://www.researchsquare.com/article/rs-10762343/v1 | saved: R2143.txt
Notes: Specialty-only: developmental dysplasia of the hip / periacetabular osteotomy (orthopaedic subspecialty, gate scope NO); safety a Likert domain, no unsafe tier.

### R2148 - EXCLUDE FT-R5
Title: Beyond Accuracy: A Multidimensional Evaluation of Large Language Models for Public-Facing Nutrition Questions in Hepatocellular Carcinoma
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:5436chars:https://www.researchsquare.com/article/rs-11391079/v1 | Route 3: Research Square PDF (article/rs-11391079/v1.pdf) downloaded and text-extracted, replacing abstract-only landing page. | saved: R2148.txt
Notes: Specialty-only: nutrition questions in hepatocellular carcinoma (oncology/hepatology, gate scope NO); non-safe bucket is a combined 'potentially harmful, misleading, or clinically inappropriate' category (47/310 first round), not an explicit unsafe tier.

### R2149 - EXCLUDE FT-R7
Title: Quality, Readability, and Content Deficiencies of Three Large Language Models in Bee Sting Health Information: A Comparative Evaluation with Patient Perspectives
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI:FAIL:HTTPError:HTTP Error 403: Forbidden | retry: medrxiv-full:HTML 46388chars https://www.medrxiv.org/content/10.64898/2026.09.29.26364282v1.full | saved: R2149.txt
Notes: Bee sting health information (medRxiv): quality/reliability, readability and content-deficiency dimensions plus a patient perspective survey (n=20); no clinician safety tier or safety rating outcome and no poolable secondary counts.

### R2150 - INCLUDE_NARRATIVE
Title: Assessing the Quality, Safety, and Readability of Large Language Model Responses from ChatGPT and Gemini for Knee Osteoarthritis Patient Education
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:38451chars:https://www.researchsquare.com/article/rs-10283211/v1 | saved: R2150.txt
Notes: Bench (Research Square); ChatGPT and Gemini, knee osteoarthritis patient education. Safety assessed within quality/safety/readability evaluation as scored outcome; no explicit unsafe-tier numerator/denominator printed - narrative only.

### R2158 - NOT_RETRIEVED FT-R8
Title: ChatGPT Health and ChatGPT Plus in Urogynecology: A Blinded Comparison of Response Quality, Guideline Concordance, and Safety.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:14122chars:https://link.springer.com/article/10.1007/s00192-026-06893-0?error=cookies_not_supported&code=85cb742d-ffaa-4a57-9bcc-b4 | Route 3: publisher page re-checked - abstract + references only (paywalled body). Full text NOT retrieved. | saved: R2158.txt
Notes: Only publisher abstract/preview page accessible (Springer/Nature); Europe PMC holds no full text and publisher full text not open. Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2163 - EXCLUDE FT-R7
Title: Reliability and readability of five AI chatbots for concussion health advice across retrieval augmented and pretrained models.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13328287:200:118170b | saved: R2163.xml
Notes: Concussion advice: reliability (DISCERN/EQIP) and readability audit under CHART reporting; no safety rating of responses (safety discussed as framing only). No poolable outcome.

### R2164 - EXCLUDE FT-R5
Title: Guideline adherence and expert-rated potential safety concerns in AI-generated dietary advice for patients with cirrhosis: a comparative evaluation of large language models.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13689687:200:143488b | saved: R2164.xml
Notes: Specialty-only: complication-specific dietary advice in cirrhosis (hepatology, gate scope NO). Explicit Harm Flag exists (144 responses) but out of scope.

### R2172 - EXCLUDE FT-R5
Title: Benchmarking eye health advice from generative artificial intelligence in terms of factual accuracy, safety, comprehensiveness and readability
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:51703chars:https://www.researchsquare.com/article/rs-9383173/v1 | saved: R2172.txt
Notes: Specialty-only: eye health advice benchmark (ophthalmology subspecialties, cf gate R2222 scope NO); accuracy/safety/comprehensiveness scored, no poolable unsafe counts in scope.

### R2175 - EXCLUDE FT-R5
Title: Performance of a Small Language Model Versus a Large Language Model in Answering Glaucoma Frequently Asked Patient Questions: Development and Usability Study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12772937:200:94736b | saved: R2175.xml
Notes: Specialty-only: glaucoma frequently asked questions (ophthalmology); small vs large LM comparison on accuracy/quality outcomes.

### R2177 - EXCLUDE FT-R5
Title: Accuracy, readability, and health information quality of AI chatbot responses for patient education on intermittent fasting in chronic kidney disease: a prospective structured evaluation.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13259986:200:93428b | saved: R2177.xml
Notes: Specialty-only: intermittent fasting in chronic kidney disease (nephrology/dietetics complex cases); accuracy/readability/quality outcomes, no safety tier.

### R2180 - EXCLUDE FT-R5
Title: Can Large Language Models Provide High-Quality Information for Patients with Multidrug-Resistant Organism Infections: A Multidimensional Comparative Analysis of DeepSeek-V3, ChatGPT-5.2, Gemini-3, and Grok-4
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:4838chars:https://www.researchsquare.com/article/rs-9067671/v1 | Route 3: Research Square PDF (article/rs-9067671/v1.pdf) downloaded and text-extracted, replacing abstract-only landing page. | saved: R2180.txt
Notes: Specialty-only: multidrug-resistant organism infections (hospital infection subspecialty information); multidimensional quality comparison, no poolable unsafe tier in scope.

### R2184 - EXCLUDE FT-R5
Title: Patient perspective on large-language model responses to questions about Moyamoya.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12948822:200:104145b | saved: R2184.xml
Notes: Specialty-only: Moyamoya disease (rare cerebrovascular subspecialty); patient perception/quality evaluation, no unsafe tier.

### R2187 - EXCLUDE FT-R4
Title: Expert Evaluation of the Perceived Accuracy, Relevance, and Safety of Large Language Model-Generated Patient Information in Geriatrics: Cross-Condition Study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13184597:200:108230b | saved: R2187.xml
Notes: Not patient-facing: experts rated 50 LLM-generated geriatrics statements (not responses to patient-posed questions) on Likert accuracy/relevance/potential-harm scales; medians only, no unsafe tier (gate-verified).

### R2190 - EXCLUDE FT-R7
Title: Evaluating the accuracy, reliability, and readability of AI chatbots in delivering postpartum depression information.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13506791:200:111329b | saved: R2190.xml
Notes: Postpartum depression information: accuracy, reliability and readability only; authors state clinical safety was not evaluated. No poolable outcome.

### R2195 - NOT_RETRIEVED FT-R8
Title: Digital Food Safety: Insights from Fact-Checking ChatGPT Consumer Interactions
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404:  | retry:  | Route 3: web search by exact title found a possibly related Journal of Food Protection article (PMID 42398831 in search results) but the record carries no DOI/PMID/URL to confirm identity, so no full text was retrieved for this record. | saved: none
Notes: Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2199 - EXCLUDE FT-R2
Title: Evaluating Generative AI Psychotherapy Chatbots Used by Youth: Cross-Sectional Study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12694945:200:148237b | saved: R2199.xml
Notes: Systems evaluated are dedicated generative-AI psychotherapy chatbots for youth, not general-purpose LLM chatbots; mental-health therapy context. (Harm-avoidance counts in the paper - e.g. avoided harmful statements 71/80 - relate to dedicated therapy bots.)

### R2201 - EXCLUDE FT-R7
Title: Can Artificial Intelligence Support Patient Education in Scabies? A Comparative Analysis of Large Language Model Responses.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13206425:200:79687b | saved: R2201.xml
Notes: Scabies patient education: comparative quality/accuracy/readability evaluation; safety appears only as background rationale. No safety rating, no poolable outcome.

### R2204 - INCLUDE_PRIMARY
Title: Large language models for late-life depression: a blinded benchmark of clinical safety, geriatric appropriateness, and triage.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13613085:200:233622b | saved: R2204.xml
Notes: Bench; GPT-5.5 Instant (ChatGPT), Gemini 3.5 Flash, Seed2.0 Pro (Doubao); prespecified binary 'major safety error', full-text table: ChatGPT 5/90, Gemini 9/90, Doubao 15/90; total 29/270 (primary round only). Late-life depression set is not crisis-only (medication, delirium, falls, triage) - in scope per gate adjudication.

### R2209 - NOT_RETRIEVED FT-R8
Title: Evaluating the Performance of Large Language Models for Breast Cancer Patient Education: A Comparative Study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:21154chars:https://link.springer.com/article/10.1007/s13187-026-02918-w?error=cookies_not_supported&code=208f2cf4-c84d-4c5a-a80c-98 | Route 3: publisher page re-checked - abstract only. Full text NOT retrieved. | saved: R2209.txt
Notes: Only publisher abstract/preview page accessible (Springer/Nature); Europe PMC holds no full text and publisher full text not open. Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2210 - INCLUDE_NARRATIVE
Title: Quality, readability, and patient safety of ChatGPT-generated responses to fall-related questions in older adults: a multidisciplinary evaluation.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13506134:200:66405b | saved: R2210.xml
Notes: Bench; ChatGPT (5.2), 10 fall-related questions in older adults, multidisciplinary panel. Patient safety assessed within quality/readability evaluation (expert ratings, ICC reported); no explicit unsafe-tier counts - narrative only.

### R2216 - EXCLUDE FT-R7
Title: Guidelines vs. generative AI in CKD patient education: the role of prompt engineering and expert blinded evaluation.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13032336:200:71929b | saved: R2216.xml
Notes: CKD patient education (journal version): quality/accuracy-type outcomes with prompt engineering and blinded expert evaluation; safety mentioned only in discussion. No safety rating, no poolable outcome. Preprint duplicate is R2276.

### R2217 - EXCLUDE FT-R5
Title: Accounting for Insulin-on-board in Large Language Model Advice about Pediatric Hyperglycemia
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI:FAIL:RemoteDisconnected:Remote end closed connection without response | retry: medrxiv-full:HTML 14977chars https://www.medrxiv.org/content/10.64898/2026.11.06.26367316v1.full | saved: R2217.txt
Notes: Specialty-only: paediatric type 1 diabetes insulin-on-board dosing advice (specialist diabetes management); 'potential safety failure' reported as percentages only (baseline 34.2% Opus 5.5 to 98% ChatGPT chat interface; 120 prompts API arms, 50 chat arms) and rated mainly by an LLM judge (GPT-5.5) - also not clinician-rated counts. Out of scope; recorded for coordinator.

### R2219 - INCLUDE_SECONDARY
Title: Are Frontier Large Language Models Safer Than Government-Backed Symptom Checkers for Clinical Self-Triage? A Standardised Vignette Evaluation
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI:FAIL:HTTPError:HTTP Error 403: Forbidden | retry: medrxiv-full:HTML 33690chars https://www.medrxiv.org/content/10.64898/2026.09.01.26361908v1.full | saved: R2219.txt
Notes: Bench self-triage; 45 Semigran vignettes (15 emergency/15 GP/15 self-care) x 6 LLM configurations (ChatGPT GPT-5.2 free / GPT-5.3 Instant Plus, Claude Sonnet 4.6 free / Opus 4.7 Pro, Gemini default/best) = 270 LLM evaluations. Undertriage outcome poolable as critical misses (emergency triaged as self-care): 0/270 for LLMs (printed, 95% CI 0-1.4%); emergency sensitivity 80.0-86.7% (undertriage of emergencies 13.3-20%); per-system undertriage rates in tables not captured in text. Healthdirect comparator (non-LLM) had 2 critical misses. medRxiv full text.

### R2220 - EXCLUDE FT-R5
Title: Public-facing health information on achalasia generated by large language models: a multidimensional comparative study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13619586:200:112077b | saved: R2220.xml
Notes: Specialty-only: achalasia (uncommon gastroenterology condition, gate scope NO). Explicit potentially unsafe classification exists (27/240 in abstract) but out of scope.

### R2222 - EXCLUDE FT-R5
Title: Digital guides in eye care: Comparing AI model accuracy and reliability.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13065264:200:109046b | saved: R2222.xml
Notes: Specialty-only: ophthalmology patient education across subspecialties (gate scope NO). Potentially unsafe tier exists (19/200) but out of scope.

### R2223 - EXCLUDE FT-R7
Title: Accuracy, reliability, readability, and European respiratory society guideline consistency of six generative artificial intelligence chatbots in providing health advice for chronic cough: A cross-sectional comparative assessment.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13087341:200:150696b | saved: R2223.xml
Notes: Chronic cough: accuracy, reliability, readability and ERS guideline consistency only. No safety rating, no poolable outcome.

### R2226 - NOT_RETRIEVED FT-R8
Title: ChatGPT as a Patient Education Tool in Female Sexual Dysfunction: A Clinician-Based Evaluation.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI:FAIL:HTTPError:HTTP Error 403: Forbidden; EPMC-web:FAIL:HTTPError:HTTP Error 403: Forbidden | retry: epmc-xml-retry:FAIL HTTPError HTTP Error 404: ; pmc-search:FAIL HTTPError HTTP Error 404: Not Found; doi-retry-browserUA:FAIL HTTPError HTTP Error 403: Forbidden | saved: none
Notes: Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2227 - EXCLUDE FT-R7
Title: Reliability and readability of AI platforms for pediatric health advice: a comparative analysis.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13438843:200:112156b | saved: R2227.xml
Notes: Paediatric health advice platforms: reliability and readability comparative analysis; no clinician safety rating outcome and no poolable secondary counts.

### R2234 - INCLUDE_PRIMARY
Title: Safety, accuracy, empathy, information quality, and readability of publicly accessible LLM-based chatbots for traumatic brain injury and concussion questions: a cross-sectional comparative study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13574619:200:111786b | saved: R2234.xml
Notes: Bench; ChatGPT, Gemini, Copilot, DeepSeek, Doubao; safety coded 0=safe 1=potentially unsafe/harmful by majority vote: total 27/325 (65 questions x 5 models), full text; per-model unsafe counts not individually printed. Traumatic brain injury/concussion public questions (first-contact/disposition topic).

### R2238 - EXCLUDE FT-R7
Title: Comparing the Accuracy of ChatGPT-4o, DeepSeek-V3, and Gemini 2.5 Flash in Answering Frequently Asked Questions About Systemic Lupus Erythematosus: Quantitative Study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13245641:200:99881b | saved: R2238.xml
Notes: Systemic lupus erythematosus FAQs: accuracy, completeness, empathy and readability only (authors note safety frameworks as future work). No poolable outcome.

### R2244 - INCLUDE_SECONDARY
Title: Patient-Facing AI Chatbots vs Primary Care Physicians: A Standardized Patient Field Experiment in China
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:53519chars:https://www.researchsquare.com/article/rs-9988886/v1 | saved: R2244.txt
Notes: Human-user (standardized patients); ChatGPT-4o and DeepSeek-R1 vs primary-care physicians, unstable angina + asthma cases, 744 SP encounters (248 per exposure arm). Secondary problematic-type safety outcome: inappropriate medication recommendations ChatGPT-4o 73.4% and DeepSeek-R1 62.1% of 248 encounters each (percentages + denominator printed, counts not printed); unnecessary testing 90.3% and 96.4%. Research Square full text, Abstract/Results.

### R2245 - INCLUDE_NARRATIVE
Title: Can artificial intelligence counsel expectant mothers? Expert evaluation of ChatGPT's educational performance in gestational diabetes mellitus.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13741499:200:67943b | saved: R2245.xml
Notes: Bench; ChatGPT-5, gestational diabetes FAQs rated by obstetrics specialists on 5-point Likert domains incl safety (mean 3.88 +/- 0.34); no unsafe-tier counts - narrative only. Journal version; preprint duplicate is R2411.

### R2247 - EXCLUDE FT-R7
Title: Evaluation of the Quality and Reliability of ChatGPT-4's Responses on Allergen Immunotherapy Using Validated Instruments for Health Information Quality Assessment.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12665041:200:118747b | saved: R2247.xml
Notes: Allergen immunotherapy: quality and reliability via validated instruments (DISCERN/JAMA-type); no safety rating of responses, no poolable outcome.

### R2248 - NOT_RETRIEVED FT-R8
Title: Can ChatGPT Be Trusted for Urologic Patient Education? A Comparative Study of Stress Urinary Incontinence-Related Information From Versions 3.5 and 4.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:14739chars:https://link.springer.com/article/10.1007/s00192-026-06685-6?error=cookies_not_supported&code=eaf5e408-d607-4c99-921f-84 | Route 3: publisher page re-checked - abstract + references only. Full text NOT retrieved. | saved: R2248.txt
Notes: Only publisher abstract/preview page accessible (Springer/Nature); Europe PMC holds no full text and publisher full text not open. Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2252 - INCLUDE_PRIMARY
Title: Clinical Safety and Reliability of Large Language Models in Answering Hemorrhoid-Related Patient Questions: A Comparative Study of ChatGPT, Gemini, and DeepSeek.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13361431:200:87900b | saved: R2252.xml
Notes: Bench; ChatGPT (GPT-5.3), Gemini 3.1, DeepSeek R1; 25 haemorrhoid questions/model. Explicit standalone critical-error tier (could delay evaluation, false reassurance, miss serious conditions, harmful recommendations): 0/25 per model, total 0/75, full text. (The combined 1-point category of the global 5-point score was NOT used.)

### R2254 - INCLUDE_SECONDARY
Title: AI chatbots abandon sleep apnoea referral when simulated patients minimise symptoms
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI:FAIL:HTTPError:HTTP Error 403: Forbidden | retry: medrxiv-full:HTML 38698chars https://www.medrxiv.org/content/10.64898/2026.10.09.26365165v1.full | saved: R2254.txt
Notes: Bench simulated-patient conversations; GPT-5, Gemini 2.5 Flash, Claude Sonnet 4.6, DeepSeek V4 Flash, Grok-4.3; 7 OSA vignettes x 10 conversations x 2 conditions, N=700. Undertriage-type outcome (referral abandonment): referral maintained 350/350 (100%) neutral vs 225/350 (64.3%) under symptom minimisation, i.e. 125/350 referrals abandoned under minimisation, human-confirmed capitulations, Results. medRxiv full text.

### R2263 - EXCLUDE FT-R5
Title: Patient education for neuromyelitis optica spectrum disorder using large language models: combining expert assessment and real-world patient interaction.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13534020:200:133927b | saved: R2263.xml
Notes: Specialty-only: neuromyelitis optica spectrum disorder (rare neurology subspecialty) patient education; expert + real-world interaction quality evaluation, no poolable unsafe tier in scope.

### R2264 - NOT_RETRIEVED FT-R8
Title: Mixed methods assessment of the influence of demographics on medical advice of ChatGPT.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:FAIL:HTTPError:HTTP Error 500: ; DOI:FAIL:HTTPError:HTTP Error 403: Forbidden; EPMC-web:FAIL:HTTPError:HTTP Error 403: Forbidden | retry: epmc-xml-retry:FAIL HTTPError HTTP Error 404: ; pmc-search:FAIL HTTPError HTTP Error 404: Not Found; doi-retry-browserUA:FAIL HTTPError HTTP Error 403: Forbidden | saved: none
Notes: Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2266 - INCLUDE_NARRATIVE
Title: Beyond accuracy: a three-stage evaluation of large language models for postpartum health consultation and nursing decision support.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13727638:200:131332b | saved: R2266.xml
Notes: Bench + patient-rating stage; ChatGPT 5.5, DeepSeek V3 and others, postpartum health consultation. Safety a scored domain (DeepSeek higher, Holm-adjusted p=0.001); no unsafe-tier counts - narrative only.

### R2267 - EXCLUDE FT-R7
Title: Large language models' performance in answering common patient questions about colonoscopy: an expert-based evaluation.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13632202:200:136783b | saved: R2267.xml
Notes: Colonoscopy patient questions: accuracy/comprehensiveness/patient-centredness expert evaluation; safety only in discussion. No poolable outcome.

### R2272 - NOT_RETRIEVED FT-R8
Title: Evaluating the quality of artificial intelligence responses to psoriasis-related clinical and patient questions: a comparative study of ChatGPT, Gemini, and Microsoft Copilot.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:FAIL:HTTPError:HTTP Error 500: ; DOI:FAIL:HTTPError:HTTP Error 403: Forbidden; EPMC-web:FAIL:RemoteDisconnected:Remote end closed connection without response | retry: epmc-xml-retry:FAIL HTTPError HTTP Error 404: ; pmc-search:FAIL HTTPError HTTP Error 404: Not Found; doi-retry-browserUA:FAIL HTTPError HTTP Error 403: Forbidden | saved: none
Notes: Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2276 - EXCLUDE FT-R6
Title: Guidelines vs Generative AI in CKD Patient Education: The Role of Prompt Engineering and Expert Blinded Evaluation
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:33706chars:https://www.researchsquare.com/article/rs-7507934/v1 | saved: R2276.txt
Notes: Duplicate report of R2216 (same CKD guidelines-vs-generative-AI study; this is the Research Square preprint, R2216 is the journal version). Retained record: R2216.

### R2278 - EXCLUDE FT-R5
Title: Benchmarking freely accessible large language models for pediatric epilepsy care: a prospective mixed-methods study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13739821:200:100702b | saved: R2278.xml
Notes: Specialty-only: paediatric epilepsy benchmark, authors' own 'specialty-specific' design, rated by paediatric neurologists. Critical safety flags printed (DeepSeek 0/10, Gemini 0/10, ChatGPT 3/10, Perplexity 8/10; total 11/40) but out of scope - counts recorded for coordinator.

### R2279 - EXCLUDE FT-R7
Title: Benchmarking public large language model responses to patient-facing varicose veins questions: informational quality, verifiability indicators, and readability.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13303600:200:127644b | saved: R2279.xml
Notes: Varicose veins benchmark: informational quality, verifiability indicators and readability; authors state it does not assess claim-level clinical accuracy or safety. No poolable outcome.

### R2294 - INCLUDE_SECONDARY
Title: Quality safety and disparity of an AI chatbot in managing chronic diseases: simulated patient experiments.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12462510:200:111757b | saved: R2294.xml
Notes: Simulated-patient experiments (bench); ERNIE Bot main system, 384 patient-AI trials (hypertension and unstable angina). Secondary problematic-type safety outcome: inappropriate or potentially harmful medication prescribing in 57.8% of ERNIE Bot trials (95% CI 52.9-62.8) and unnecessary lab-test requests 91.9%, Results text with per-condition breakdowns; comparator model subsets reported as percentages. Counts per arm not printed beyond trial totals.

### R2297 - EXCLUDE FT-R5
Title: Performance of ChatGPT-4o in Providing Information on Pediatric Inborn Errors of Immunity: A Cross-Sectional Evaluation.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13257705:200:166576b | saved: R2297.xml
Notes: Specialty-only: paediatric inborn errors of immunity (rare immunology subspecialty) FAQs; reliability/quality/readability outcomes.

### R2299 - EXCLUDE FT-R2
Title: Evaluating the Ethical and Clinical Implications of Generative AI in Patient-Centric Medical Applications
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:33021chars:https://www.researchsquare.com/article/rs-7666314/v1 | saved: R2299.txt
Notes: One of two systems tested (Med-PaLM 2) is not a publicly available general-purpose chatbot; hallucination/safety checks described narratively without poolable or clearly rated counts. Not eligible as a patient-facing public-chatbot evaluation.

### R2300 - INCLUDE_NARRATIVE
Title: Artificial Intelligence Models for Dysphonia Patient Education.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12661483:200:81974b | saved: R2300.xml
Notes: Bench; AI models for dysphonia (voice disorder) patient education; patient safety graded on a 5-point Likert scale alongside comprehensiveness/accuracy/appropriateness; no tier counts - narrative only.

### R2302 - EXCLUDE FT-R5
Title: Patient Education in Bariatric Surgery: Can Artificial Intelligence-Based Chatbots Bridge the Knowledge Gap?
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12902178:200:132901b | saved: R2302.xml
Notes: Specialty-only: bariatric surgery patient education (surgical subspecialty); quality/readability outcomes.

### R2305 - EXCLUDE FT-R5
Title: Evaluating ChatGPT-5's Performance in Answering Common Patient Questions About Femoroacetabular Impingement and Hip Arthroscopy.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13031688:200:67652b | saved: R2305.xml
Notes: Specialty-only: femoroacetabular impingement and hip arthroscopy (orthopaedic surgery, gate scope NO); Likert domains only, no unsafe tier.

### R2307 - INCLUDE_SECONDARY
Title: ChatGPT Health performance in a structured test of triage recommendations.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13190235:200:75773b | saved: R2307.xml
Notes: Bench; ChatGPT Health; 960 responses (480 clear-vignette analysis set). Undertriage poolable: gold-standard emergencies undertriaged 33/64 (51.6%) to 24-48h evaluation, Results/Fig.1 and Extended Data confusion matrix (per-acuity undertriage counts printed; A-level overtriage 83/128 is not undertriage). No explicit unsafe tier (gate-verified).

### R2308 - EXCLUDE FT-R5
Title: Quality, readability, and clinical-risk signals of default public-interface LLM responses to vascular and perioperative patient questions: a cross-sectional snapshot.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13500567:200:164122b | saved: R2308.xml
Notes: Specialty-only: vascular and perioperative patient questions (surgical subspecialty snapshot); clinical-risk signals described, no explicit unsafe tier counts in scope.

### R2321 - EXCLUDE FT-R5
Title: Evaluating the accuracy and patient perception of AI-generated answers on pectus surgery.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12645766:200:54317b | saved: R2321.xml
Notes: Specialty-only: pectus surgery patient questions (surgical subspecialty); accuracy and patient perception outcomes, no safety tier.

### R2326 - EXCLUDE FT-R4
Title: AI-generated patient information leaflets for oral anticoagulants: quality, usability, readability, and reproducibility compared with FDA-referenced materials.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13731713:200:133967b | saved: R2326.xml
Notes: Generation task: AI-generated patient information leaflets for oral anticoagulants compared with FDA materials (quality/usability/readability); no patient-posed questions answered and no safety tier.

### R2328 - INCLUDE_NARRATIVE
Title: Divergence Between Clinical Accuracy and Readability in Large Language Models: A Comparative Study in Hypogonadism
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:22779chars:https://www.researchsquare.com/article/rs-9941676/v1 | saved: R2328.txt
Notes: Bench (Research Square); ChatGPT, Gemini, Claude, 20 hypogonadism FAQs. Binary unsafe definition prespecified (incorrect TRT indication, fertility harm, unnecessary imaging, omitted warnings) but unsafe counts not printed in accessible text (safety comparison p=0.895 only) - narrative only. NOTE: record title in the list ('low back pain divergence') does not match the retrieved article (hypogonadism FAQs) - flagged for coordinator.

### R2331 - EXCLUDE FT-R5
Title: Evaluation of ChatGPT-5 responses to patient-centered questions on stromal vascular fraction for knee osteoarthritis: fair to good quality and content.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13104398:200:112099b | saved: R2331.xml
Notes: Specialty-only: stromal vascular fraction (regenerative therapy) for knee osteoarthritis; NLAT-AI safety domain is a mean score, no tier counts; subspecialty therapy set.

### R2333 - INCLUDE_NARRATIVE
Title: Artificial intelligence-powered chatbots in search engines: a cross-sectional study on the quality and risks of drug information for patients.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC11874309:200:96098b | saved: R2333.xml
Notes: Bench; Bing Copilot (search chatbot), patient drug information. Quality/risk evaluation of all responses plus harm-potential scales applied only to a preselected subset of 20 inaccurate answers (gate-verified) - no all-response unsafe tier and no poolable secondary denominator - narrative only.

### R2335 - NOT_RETRIEVED FT-R8
Title: Analyses of different prescriptions for health using artificial intelligence: a critical approach based on the international guidelines of health institutions.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:24623chars:https://link.springer.com/article/10.1007/s13755-025-00368-0?error=cookies_not_supported&code=05fe869d-a214-47c0-a30c-fc | Route 3: publisher page re-checked - abstract only. Full text NOT retrieved. | saved: R2335.txt
Notes: Only publisher abstract/preview page accessible (Springer/Nature); Europe PMC holds no full text and publisher full text not open. Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2336 - INCLUDE_NARRATIVE
Title: Clinical Evaluation of ChatGPT-5.3 Responses to Patient-Oriented Questions on Scoliosis: A Multidimensional Expert Analysis.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13256305:200:111928b | saved: R2336.xml
Notes: Bench; ChatGPT-5.3, 20 scoliosis patient questions. Clinical risk classified harmless/low/moderate/high at expert-rating level (no high-risk responses; percentages across ratings, denominator is ratings not responses) - no response-level poolable counts - narrative only.

### R2337 - EXCLUDE FT-R7
Title: The Impact of Google Search versus ChatGPT on Patient Understanding and Potential Adherence in PICC Line Care: A Comparative Analysis.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12554316:200:72851b | saved: R2337.xml
Notes: PICC line care: comparative study of patient understanding and potential adherence (Google Search vs ChatGPT); responses not clinician-rated for safety. No poolable outcome.

### R2338 - EXCLUDE FT-R5
Title: Comparative performance of large language models for patient-initiated ophthalmology consultations.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12497754:200:100108b | saved: R2338.xml
Notes: Specialty-only: patient-initiated ophthalmology consultations; safety a Likert domain (means only), ophthalmology-only set (cf gate R2681 scope NO).

### R2342 - NOT_RETRIEVED FT-R8
Title: ChatGPT 4.0's efficacy in the self-diagnosis of non-traumatic hand conditions.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:FAIL:HTTPError:HTTP Error 500: ; DOI-html:short13:https://linkinghub.elsevier.com/retrieve/pii/S0974322725000110; EPMC-web:FAIL:RemoteDisconnected:Remote end closed connection without response | retry: epmc-xml-retry:FAIL HTTPError HTTP Error 404: ; pmc-search:FAIL HTTPError HTTP Error 404: Not Found; doi-retry-browserUA:short 13 https://linkinghub.elsevier.com/retrieve/pii/S0974322725000110 | saved: none
Notes: Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2347 - EXCLUDE FT-R5
Title: Assessing the Quality and Accuracy of ChatGPT-3.5 Responses to Patient Questions About Hip Arthroscopy.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12734417:200:97315b | saved: R2347.xml
Notes: Specialty-only: hip arthroscopy patient questions (orthopaedic surgery, gate scope NO); Likert domains only, no unsafe tier.

### R2350 - INCLUDE_NARRATIVE
Title: Evaluation of ChatGPT-4 as an Online Outpatient Assistant in Puerperal Mastitis Management: Content Analysis of an Observational Study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12288767:200:104590b | saved: R2350.xml
Notes: Bench; ChatGPT-4 as outpatient assistant for puerperal (postpartum) mastitis, 15 patient questions in Turkish; accuracy, clarity and clinical safety assessed by content analysis (categorical/Likert judgements); no explicit unsafe-tier numerator/denominator - narrative only.

### R2359 - EXCLUDE FT-R5
Title: The Role of Large Language Models in the Promotion of Minimally Invasive Interventional Radiologic Methods in Gynecology and Obstetrics.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13163413:200:76481b | saved: R2359.xml
Notes: Specialty-only: promotion of minimally invasive interventional radiology methods in gynaecology/obstetrics (procedural subspecialty); one system (OpenEvidence) is clinician-facing. Accuracy/completeness/safety-consideration narrative only.

### R2360 - INCLUDE_PRIMARY
Title: Psychological support for depression and anxiety across chronic illness contexts: a comparative evaluation of three general-purpose AI chatbots.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:81868chars:https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2026.1962615/full | saved: R2360.txt
Notes: Bench; ChatGPT, Gemini, Doubao; prespecified binary 'major clinical or safety error' (Table 6, s3.5): first round ChatGPT 0/20, Gemini 2/20 (10.0%), Doubao 3/20 (15.0%); total 5/60 first-round responses (120 responses incl test-retest round). Psychological support for depression/anxiety across chronic illness - not crisis-only.

### R2361 - INCLUDE_PRIMARY
Title: Evaluating large language models for myocardial infarction public health education: a comparative study on information quality, transparency and readability.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13601339:200:126065b | saved: R2361.xml
Notes: Bench; Gemini 3.5 Flash, Claude Opus 4.8, ChatGPT 5.5; 4-level safety scale with explicit tier (4) 'Potentially Harmful', s3.2: ChatGPT 2/25, Claude 1/25, Gemini 1/25; total 4/75. Myocardial infarction public education (symptoms, first aid/disposition, prevention).

### R2366 - EXCLUDE FT-R5
Title: A cross-sectional comparison of five large language models in answering Chinese-language patient queries on visual field defects associated with brain diseases.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13739588:200:152565b | saved: R2366.xml
Notes: Specialty-only: visual field defects associated with brain diseases (neuro-ophthalmology); safety a 1-5 scored domain, no tier counts.

### R2368 - INCLUDE_NARRATIVE
Title: Assessing the Role of Large Language Models Between ChatGPT and DeepSeek in Asthma Education for Bilingual Individuals: Comparative Study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12349887:200:112595b | saved: R2368.xml
Notes: Bench; ChatGPT-4o and DeepSeek-V3, 53 real-patient asthma questions (English/Chinese); 7-dimension framework incl a scored safety dimension; no unsafe-tier counts - narrative only. Asthma is a primary-care presentation.

### R2369 - NOT_RETRIEVED FT-R8
Title: Evaluating the Performance of ChatGPT and DeepSeek in Bilingual Responses to Questions Regarding Craniofacial Microsomia.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI:FAIL:RemoteDisconnected:Remote end closed connection without response; EPMC-web:FAIL:HTTPError:HTTP Error 403: Forbidden | retry: epmc-xml-retry:FAIL HTTPError HTTP Error 404: ; pmc-search:FAIL HTTPError HTTP Error 404: Not Found; doi-retry-browserUA:FAIL HTTPError HTTP Error 403: Forbidden | saved: none
Notes: Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2372 - EXCLUDE FT-R7
Title: Quality and readability of AI-generated information on bipolar disorder: a cross-sectional content analysis.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13479570:200:93109b | saved: R2372.xml
Notes: Bipolar disorder information: quality and readability content analysis; authors state findings are not evidence of clinical accuracy or safety. No poolable outcome.

### R2373 - EXCLUDE FT-R7
Title: Evaluation of AI language models in answering pregnancy-related questions assessed by obstetrics specialists.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13000243:200:72988b | saved: R2373.xml
Notes: Pregnancy-related questions: accuracy evaluation by obstetrics specialists (scored correctness); no safety rating outcome, no poolable counts.

### R2375 - INCLUDE_NARRATIVE
Title: Quality of artificial intelligence-generated responses on pediatric celiac disease: Comparative assessment of Open AI ChatGPT and Google Gemini.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13151005:200:74378b | saved: R2375.xml
Notes: Bench; ChatGPT and Gemini, 34 parent questions on paediatric coeliac disease; accuracy, safety, completeness and understandability assessed (scored); no unsafe-tier counts - narrative only.

### R2400 - EXCLUDE FT-R7
Title: Evaluation of large Language models on pediatric asthma: a comparative study of Claude3-Opus, Gemini 2.0, ChatGPT-4o, and DeepSeek-a cross-sectional questionnaire study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12990414:200:92503b | saved: R2400.xml
Notes: Paediatric asthma: mixed caregiver/patient-focused (7) and clinician-focused (8) question categories; outcomes are accuracy-type performance scores, no safety rating outcome. No poolable outcome.

### R2402 - INCLUDE_NARRATIVE
Title: Evaluating the accuracy of ChatGPT in delivering patient instructions for medications: an exploratory case study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC11996888:200:63630b | saved: R2402.xml
Notes: Bench; ChatGPT medication patient instructions vs CareNotes, rated by pharmacy experts/interns incl potential to cause harm on a 5-point Likert agreement scale (gate-verified: no categorical tier) - narrative only.

### R2409 - EXCLUDE FT-R5
Title: Comparison of DeepSeek, ChatGPT-4, and Online Medical Platforms in Addressing Chronic Pancreatitis Related Questions
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:6777chars:https://www.researchsquare.com/article/rs-10249657/v1 | Route 3: Research Square PDF (article/rs-10249657/v1.pdf) downloaded and text-extracted, replacing abstract-only landing page. | saved: R2409.txt
Notes: Specialty-only: chronic pancreatitis questions (gastroenterology subspecialty); safety considerations scored in expert phase, patient phase rated empathy/satisfaction; no tier counts.

### R2410 - EXCLUDE FT-R5
Title: Comparison of the performance of large language models in answering patient questions related to cataract.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12989843:200:95413b | saved: R2410.xml
Notes: Specialty-only: cataract patient questions ('specialized domain of ophthalmology' per authors); accuracy/completeness/safety/consistency scored, no tier counts in scope.

### R2411 - EXCLUDE FT-R6
Title: Can Artificial Intelligence Counsel Expectant Mothers? Expert Evaluation of ChatGPT’s Educational Performance in Gestational Diabetes Mellitus
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:32875chars:https://www.researchsquare.com/article/rs-7983164/v1 | saved: R2411.txt
Notes: Duplicate report of R2245 (same gestational diabetes ChatGPT evaluation; this is the Research Square preprint, R2245 is the journal version). Retained record: R2245.

### R2414 - EXCLUDE FT-R7
Title: Patient Cognitive Bias in Large Language Model-Supported Health Consultations: Simulation-Based Comparative Study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13258194:200:110992b | saved: R2414.xml
Notes: Human-user simulation study of patient cognitive bias in LLM-supported consultations: outcome is diagnostic/advice shift under bias, not clinician-rated safety of responses. No poolable outcome.

### R2417 - INCLUDE_NARRATIVE
Title: Large language models as sources of diabetic retinopathy patient education: a comparative evaluation of safety, health information quality, and readability.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:72440chars:https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2026.1945318/full | saved: R2417.txt
Notes: Bench; ChatGPT, Gemini, DeepSeek, Doubao, Copilot, Perplexity; 50 diabetic retinopathy questions x 6 models = 300 responses. Binary safety (0=safe, 1=potentially unsafe/misleading/harmful) prespecified, but per-model safe rates given only as a range (86.0-94.0%) in text and counts not printed in accessible text (tables/figures) - narrative only, flagged for extractor to check publisher PDF figures. Diabetes-complication set counted in scope (cf gate R2108 diabetic neuropathy YES).

### R2423 - NOT_RETRIEVED FT-R8
Title: A Comparative Analysis of Three Large Language Models in Answering Patient Queries on Otolaryngology Emergencies
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI:FAIL:HTTPError:HTTP Error 403: Forbidden | retry: authorea:FAIL RemoteDisconnected Remote end closed connection without response; doi-retry-browserUA:FAIL HTTPError HTTP Error 403: Forbidden | saved: none
Notes: Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2425 - INCLUDE_NARRATIVE
Title: GPT-4o and DeepSeek-V3 responses to common migraine questions: a cross-sectional comparative study of accuracy, completeness, empathy, readability and safety
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:26694chars:https://www.researchsquare.com/article/rs-10488975/v1 | saved: R2425.txt
Notes: Bench (Research Square); GPT-4o and DeepSeek-V3, 100 migraine questions (25 red-flag). Safety rated on a 0-5 structured rubric (means only, adjusted p=0.075); no unsafe-tier counts - narrative only. Migraine is a primary-care presentation.

### R2426 - EXCLUDE FT-R3
Title: Bridging Artificial and Human Intelligence: Comparative Performance of AI Models and Neurologists in Stroke Recognition- A Cross-Sectional Study
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:43470chars:https://f1000research.com/articles/15-1128/v1 | saved: R2426.txt
Notes: Clinician-facing diagnostic task: AI models vs neurologists on stroke recognition cases; not patient-posed questions or lay use.

### R2440 - INCLUDE_NARRATIVE
Title: ChatGPT-5 versus other mainstream large language models in core diabetic retinopathy patient queries.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13057549:200:126021b | saved: R2440.xml
Notes: Bench; ChatGPT-5 vs other LLMs, core diabetic retinopathy patient queries rated by two retinal specialists on 1-5 Likert domains incl safety; no tier counts - narrative only. In scope as diabetes-complication education (cf R2417).

### R2444 - EXCLUDE FT-R7
Title: Readability, quality, and reliability of AI-generated ınformation on myofascial pain syndrome: A comparative analysis of ChatGPT, Gemini, and Perplexity.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13235886:200:178008b | saved: R2444.xml
Notes: Myofascial pain syndrome information: readability, quality and reliability only. No safety rating, no poolable outcome.

### R2445 - EXCLUDE FT-R5
Title: How Accurate Is AI? A Critical Evaluation of Commonly Used Large Language Models in Responding to Patient Concerns About Incidental Kidney Tumors.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12386662:200:93831b | saved: R2445.xml
Notes: Specialty-only: incidental kidney tumours (urology/oncology, gate scope NO); harm a Likert domain, combined misleading/incomplete flag is not an unsafe tier.

### R2450 - INCLUDE_NARRATIVE
Title: Large language model accuracy in inhaler technique counselling for asthma and COPD: A comparison of free and paid models across ten devices.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13477548:200:141952b | saved: R2450.xml
Notes: Bench; free vs paid tiers of multiple LLMs, 50 inhaler-technique prompts x 10 devices in triplicate = 1500 outputs (asthma/COPD). Safety measured as safety-warning completeness (%) and critical-error counts per response (means, e.g. critical errors 0.48 free vs 0.02 paid per response) - error counts are per-response means, not a response-level unsafe tier with numerator/denominator - narrative only.

### R2453 - EXCLUDE FT-R4
Title: Quality of AI-generated exercise awareness messages for older adults aligned with the ICFSR consensus: a comparative study of three LLMs.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13673795:200:80215b | saved: R2453.xml
Notes: Generation task: AI-generated exercise awareness messages for older adults rated on Likert dimensions (incl safety and absence of fabrication as scored dimensions, no counts); no patient-posed questions.

### R2454 - EXCLUDE FT-R7
Title: Readability, reliability, and quality of kyphosis-related information provided by artificial intelligence chatbots: A cross-sectional study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12796146:200:95284b | saved: R2454.xml
Notes: Kyphosis information: readability, reliability and quality only. No safety rating, no poolable outcome.

### R2455 - INCLUDE_NARRATIVE
Title: Discordance Between Textual Reasoning and Visual Interpretation in Large Language Models for Low Back Pain: Cross-Sectional Quantitative Evaluation and Exploratory Multimodal Stress Test.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13494679:200:122755b | saved: R2455.xml
Notes: Bench; LLMs for low back pain, textual vs multimodal stress test (300 tasks). Safety outcome is safety-disclaimer coverage (207/250 textual, 14/50 multimodal) - a process measure, not an unsafe tier/undertriage/fabrication count - narrative only.

### R2456 - EXCLUDE FT-R7
Title: Communication features of ChatGPT responses and care-seeking intention for syphilis in Japan: a controlled dialogue experiment.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13389713:200:111620b | saved: R2456.xml
Notes: Syphilis dialogue experiment (human participants): outcomes are communication features and care-seeking intention; misinformation noted qualitatively with low rater agreement. No clinician-rated safety tier or poolable counts.

### R2457 - EXCLUDE FT-R3
Title: A two-stage evaluation of large language models for guideline-based Q&amp;A and draft rehabilitation planning in stroke care.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13546465:200:102219b | saved: R2457.xml
Notes: Clinician-facing task: guideline Q&A plus draft rehabilitation planning for stroke care evaluated by senior clinicians; not patient-facing advice.

### R2465 - EXCLUDE FT-R5
Title: Evaluating Chatbot responses to patient questions in the field of glaucoma.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC11267485:200:52240b | saved: R2465.xml
Notes: Specialty-only: glaucoma patient questions (ophthalmology); accuracy, comprehensiveness and safety evaluated for ChatGPT in the glaucoma sub-domain - out of scope as an ophthalmology-only set, no poolable tier in scope.

### R2466 - EXCLUDE FT-R5
Title: Risk-centered benchmarking of large language models for AI-enabled counseling in chronic autoimmune thyroid eye disease.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13311113:200:169587b | saved: R2466.xml
Notes: Specialty-only: chronic autoimmune thyroid eye disease counselling (rare orbital subspecialty); risk-centred benchmarking - out of scope, no poolable unsafe tier in primary-care scope.

### R2468 - INCLUDE_SECONDARY
Title: Prompt Framing Modulates Safety in Shoulder and Elbow Red-Flag Vignettes: A Large Language Model Study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13205240:200:88139b | saved: R2468.xml
Notes: Bench; ChatGPT GPT-5.2 Instant only; 80 shoulder/elbow vignettes (24 red-flag, 56 non-urgent) x 3 prompt types = 240 responses. Undertriage poolable: safety-critical undertriage 19/72 red-flag responses (26.4%); patient-oriented prompts 10/24, GP-oriented 6/24, specialist-oriented 3/24 (Abstract/Results). Patient-prompt stratum is the patient-facing arm.

### R2470 - EXCLUDE FT-R5
Title: Evaluation of large language models in patient education and clinical decision support for rotator cuff injury: a two-phase benchmarking study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12323112:200:68924b | saved: R2470.xml
Notes: Specialty-only: rotator cuff injury set spanning patient education and clinical decision support (orthopaedic subspecialty); safety a Likert domain, no tier counts.

### R2476 - INCLUDE_NARRATIVE
Title: Toward safer digital sexual health communication: evaluating the public health reliability of large language model responses on sexually transmitted infections.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13553913:200:132683b | saved: R2476.xml
Notes: Bench; LLMs answering sexually transmitted infection questions; quality, safety, readability and destigmatisation evaluated (safety as scored outcome); no explicit unsafe-tier counts in text - narrative only. Sexual health is a primary-care presentation.

### R2477 - EXCLUDE FT-R7
Title: Performance Comparison Between Domestic and International Large Language Models in Patient Education for Chinese Patients with Lumbar Disc Herniation: A Cross-Sectional Study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13451686:200:98625b | saved: R2477.xml
Notes: Lumbar disc herniation patient education (8 domestic/international models): standardised quality assessment of diagnosis/treatment/surgical-risk content; no safety rating outcome identified in full text, no poolable counts.

### R2489 - EXCLUDE FT-R5
Title: Comparative evaluation of large language models for hip fracture-related patient questions: DeepSeek-V3-FW, Gemini 2.0 Flash, and ChatGPT-4.5.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12858731:200:90035b | saved: R2489.xml
Notes: Specialty-only: hip fracture patient questions (orthopaedic emergency/surgical condition); model performance comparison, no poolable unsafe tier in scope.

### R2490 - INCLUDE_NARRATIVE
Title: Configuring large language models to deliver patient-facing explanations of pathology reports.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13281924:200:66843b | saved: R2490.xml
Notes: Bench; LLMs configured (incl RAG) to explain pathology reports to patients; structured rubric incl safety domain + arena ranking; no unsafe-tier counts - narrative only.

### R2499 - INCLUDE_PRIMARY
Title: Comparison of Diagnostic and Triage Accuracy of Ada Health and WebMD Symptom Checkers, ChatGPT, and Physicians for Patients in an Emergency Department: Clinical Data Analysis Study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC10582809:200:98287b | saved: R2499.xml
Notes: Bench; LLM arms only: ChatGPT-3.5 15/37 unsafe triage, ChatGPT-4.0 8/37; total 23/74 (37 ED cases x 2 LLM arms), full text. Ada Health and WebMD arms are dedicated symptom checkers (no LLM) and are not counted. Emergency-department patient cases with reference triage.

### R2506 - NOT_RETRIEVED FT-R8
Title: Assessing large language models' accuracy in providing patient support for choroidal melanoma.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:FAIL:HTTPError:HTTP Error 500: ; DOI-html:200:12832chars:https://www.nature.com/articles/s41433-024-03231-w?error=cookies_not_supported&code=9194d759-1222-4cab-afcb-f894ba8c71ce | Route 3: publisher page re-checked - abstract + references only. Full text NOT retrieved. | saved: R2506.txt
Notes: Only publisher abstract/preview page accessible (Springer/Nature); Europe PMC holds no full text and publisher full text not open. Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2516 - INCLUDE_NARRATIVE
Title: Reducing Under-Triage Risk in Large Language Model Based Clinical Triage Using UMLS-CUI Augmentation
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI:FAIL:HTTPError:HTTP Error 403: Forbidden | retry: medrxiv-full:HTML 31545chars https://www.medrxiv.org/content/10.64898/2026.08.07.26358932v1.full | saved: R2516.txt
Notes: Bench (medRxiv); GPT-4o-mini and MedGemma 27B +/- UMLS-CUI augmentation, 960 vignette-factor combinations. Undertriage reported as percentages only (GPT-4o-mini 9.2% -> 6.9% with CUI; MedGemma 14.0% -> 12.1%); per-arm numerators not printed and percentage x denominator is non-integer - not poolable as printed - narrative only. MedGemma is a medical-domain model; GPT-4o-mini arms are the general-purpose component.

### R2519 - INCLUDE_NARRATIVE
Title: ChatGPT-4o-Generated Exercise Plans for Patients with Type 2 Diabetes Mellitus-Assessment of Their Safety and Other Quality Criteria by Coaching Experts.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12031090:200:91132b | saved: R2519.xml
Notes: Bench; ChatGPT-4o-generated exercise plans for type 2 diabetes assessed by coaching experts for safety and other quality criteria (scored); no unsafe-tier counts - narrative only.

### R2520 - EXCLUDE FT-R7
Title: Artificial Intelligence Chatbots as Sources of Cancer Pain Information: A Comparative Evaluation of Quality, Transparency, and Readability.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13633712:200:112513b | saved: R2520.xml
Notes: Cancer pain information: information quality, transparency, educational utility and readability; authors state claim-level clinical accuracy and safety were not evaluated. No poolable outcome.

### R2524 - EXCLUDE FT-R5
Title: Using large language models to generate child-friendly education materials on myopia.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12317229:200:103884b | saved: R2524.xml
Notes: Specialty-only: LLM-generated child-friendly myopia education materials (ophthalmology/optometry), potential harm rated only as Likert (gate-verified scope NO). Generation task also noted.

### R2528 - NOT_RETRIEVED FT-R8
Title: Comparison of ChatGPT, Gemini, and Le Chat with physician interpretations of medical laboratory questions from an online health forum.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:short0:https://www.degruyterbrill.com:443/document/doi/10.1515/cclm-2024-0246/html; EPMC-web:FAIL:HTTPError:HTTP Error 403: Forbidden | retry: epmc-xml-retry:FAIL HTTPError HTTP Error 404: ; pmc-search:FAIL HTTPError HTTP Error 404: Not Found; doi-retry-browserUA:short 159 https://www.degruyterbrill.com:443/document/doi/10.1515/cclm-2024-0246/html | saved: none
Notes: Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2533 - NOT_RETRIEVED FT-R8
Title: A comparative study of ChatGPT and DeepSeek in spinal cord injury patient education: Can artificial intelligence "speak" spinal cord injury?
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:FAIL:HTTPError:HTTP Error 500: ; DOI:FAIL:HTTPError:HTTP Error 403: Forbidden; EPMC-web:FAIL:HTTPError:HTTP Error 403: Forbidden | retry: epmc-xml-retry:FAIL HTTPError HTTP Error 404: ; pmc-search:FAIL HTTPError HTTP Error 404: Not Found; doi-retry-browserUA:FAIL RemoteDisconnected Remote end closed connection without response | saved: none
Notes: Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2534 - EXCLUDE FT-R5
Title: Use of large language model-based chatbots in managing the rehabilitation concerns and education needs of outpatient stroke survivors and caregivers.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC11111889:200:70233b | saved: R2534.xml
Notes: Specialty-only: stroke rehabilitation concerns collected in a rehabilitation-medicine specialist clinic (gate scope NO); accuracy/safety/relevance on a 3-point rubric pooled overall, no explicit unsafe tier.

### R2539 - EXCLUDE FT-R7
Title: AI in Hidradenitis Suppurativa: Expert Evaluation of Patient-Facing Information.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC11539865:200:40772b | saved: R2539.xml
Notes: Hidradenitis suppurativa patient-facing information: expert evaluation of quality/accuracy-type domains; safety appears only as background risk framing. No safety rating, no poolable outcome.

### R2541 - EXCLUDE FT-R7
Title: Assessing the role of large language models in adolescent idiopathic scoliosis care: a comparison between ChatGPT and Google Gemini.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12362497:200:125668b | saved: R2541.xml
Notes: Adolescent idiopathic scoliosis: accuracy and communication quality comparison; safety/ethics raised qualitatively in conclusions. No safety rating outcome, no poolable counts.

### R2542 - EXCLUDE FT-R4
Title: Evaluating sports nutrition advice provided by general-purpose large language models for recreational female marathon runners: a multidimensional descriptive audit.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:120661chars:https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2026.1902377/full | saved: R2542.txt
Notes: Not a primary-care patient presentation: descriptive audit of sports nutrition advice for a healthy recreational marathon runner (wellness/performance advice, no condition presentation); safety boundaries described, no clinician-rated unsafe tier counts.

### R2544 - EXCLUDE FT-R5
Title: Risks and benefits of ChatGPT in informing patients and families with rare kidney diseases: an explorative assessment by the European Rare Kidney Disease Reference Network (ERKNet).
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12296756:200:73943b | saved: R2544.xml
Notes: Specialty-only: rare kidney diseases (ERKNet rare-disease reference network set); risks/benefits explorative assessment, no explicit unsafe tier counts. Journal version; preprint duplicate is R2598.

### R2545 - INCLUDE_NARRATIVE
Title: Evaluating GPT-4 Responses on Scars or Keloids for Patient Education: Large Language Model Evaluation Study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12954683:200:102380b | saved: R2545.xml
Notes: Bench; GPT-4 responses on scars/keloids rated with NLAT-AI (accuracy, safety, appropriateness domains, scored) and references validated for citation hallucination (citation fabrication, not fabricated medical facts) - no poolable primary or secondary counts - narrative only.

### R2551 - EXCLUDE FT-R5
Title: Multidisciplinary expert evaluation of large language models on questions regarding bariatric surgery: a comparative analysis of ERNIE Bot 4.0, ChatGPT-4, Claude 3 Opus, and Gemini Pro.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13199474:200:143314b | saved: R2551.xml
Notes: Specialty-only: bariatric surgery questions (surgical subspecialty), multidisciplinary expert quality evaluation; no poolable unsafe tier in scope.

### R2555 - NOT_RETRIEVED FT-R8
Title: Assessing Large Language Model Utility and Limitations in Diabetes Education: A Cross-Sectional Study of Patient Interactions and Specialist Evaluations
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI:FAIL:HTTPError:HTTP Error 403: Forbidden | retry: medrxiv-full:FAIL HTTPError HTTP Error 403: Forbidden; medrxiv-pdf:FAIL HTTPError HTTP Error 403: Forbidden; doi-retry-browserUA:FAIL HTTPError HTTP Error 403: Forbidden | Route 3: browser text fetch of medRxiv full text also rejected (403). Full text NOT retrieved. | saved: none
Notes: Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2556 - EXCLUDE FT-R5
Title: Online platform vs. doctors: a comparative exploration of congenital cataract patient education from virtual to reality.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12170551:200:83398b | saved: R2556.xml
Notes: Specialty-only: congenital cataract patient education (ophthalmology); correctness/completeness/safety Likert by ophthalmologist panel, no tier counts in scope.

### R2569 - EXCLUDE FT-R5
Title: ChatGPT-4 for addressing patient-centred frequently asked questions in age-related macular degeneration clinical practice.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12209409:200:91321b | saved: R2569.xml
Notes: Specialty-only: age-related macular degeneration FAQs in clinical practice (ophthalmology); accuracy/quality evaluation, no unsafe tier in scope.

### R2582 - EXCLUDE FT-R5
Title: Performance of ChatGPT-4 and Bard chatbots in responding to common patient questions on prostate cancer <sup>177</sup>Lu-PSMA-617 therapy.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC11272524:200:61598b | saved: R2582.xml
Notes: Specialty-only: prostate cancer 177Lu-PSMA-617 therapy questions (subspecialty nuclear-medicine oncology); ChatGPT-4/Bard quality evaluation, no unsafe tier.

### R2584 - EXCLUDE FT-R5
Title: Application of Large Language Models in Stroke Rehabilitation Health Education: 2-Phase Study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12306586:200:134644b | saved: R2584.xml
Notes: Specialty-only: stroke rehabilitation health education (specialist rehabilitation set, cf R2534); Likert accuracy/safety in phase 1, patient phase 2 - out of scope as a rehabilitation-specialty set.

### R2589 - INCLUDE_NARRATIVE
Title: Comparative analysis of Chinese large language model performance on atrial fibrillation questions.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12958689:200:87939b | saved: R2589.xml
Notes: Bench; Chinese LLMs, 231 responses to atrial fibrillation questions; SCECCE scoring system incl a safety aspect (scored); no unsafe-tier counts - narrative only.

### R2594 - EXCLUDE FT-R7
Title: Evaluation and Comparison of Large Language Model Responses to Frequently Asked Questions Regarding Patellofemoral Pain Syndrome: A Quality and Readability Assessment Study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13565727:200:95520b | saved: R2594.xml
Notes: Patellofemoral pain syndrome FAQs: quality and readability assessment; authors state findings are not evidence of clinical safety. No poolable outcome.

### R2598 - EXCLUDE FT-R6
Title: Risks and benefits of ChatGPT in informing patients and families with rare kidney diseases- an explorative assessment by the European Rare Kidney Disease Reference Network (ERKNet)
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:30321chars:https://www.researchsquare.com/article/rs-5827993/v1 | saved: R2598.txt
Notes: Duplicate report of R2544 (same ERKNet rare kidney disease ChatGPT study; this is the Research Square preprint, R2544 is the journal version). Retained record: R2544.

### R2610 - NOT_RETRIEVED FT-R8
Title: "Comparative analysis of large language models against the NHS 111 online triaging for emergency ophthalmology".
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:FAIL:HTTPError:HTTP Error 500: ; DOI-html:200:11281chars:https://www.nature.com/articles/s41433-025-03605-8?error=cookies_not_supported&code=cc403245-fd54-4b53-a931-eb237ac7c490 | Route 3: publisher page re-checked - abstract + references only. Full text NOT retrieved. | saved: R2610.txt
Notes: Only publisher abstract/preview page accessible (Springer/Nature); Europe PMC holds no full text and publisher full text not open. Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2613 - EXCLUDE FT-R5
Title: ChatGPT for advice on common GI endoscopic procedures: the promise and the peril.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12851080:200:206272b | saved: R2613.xml
Notes: Specialty-only: advice on GI endoscopic procedures (gastroenterology procedural advice); appraised for correctness and potential safety issues narratively, no tier counts.

### R2621 - EXCLUDE FT-R5
Title: Guideline-Concordant Answer Quality of Five Large Language Models on Indication Criteria for Total Hip Arthroplasty in Hip Osteoarthritis: A Single-Run Benchmark Against the 2021 German S3 Guideline (EKIT-Hip).
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13706208:200:165153b | saved: R2621.xml
Notes: Specialty-only: indication criteria for total hip arthroplasty against the German S3 guideline (surgical indication benchmark); structured context-free questions, not patient-posed advice; no safety outcome.

### R2625 - EXCLUDE FT-R5
Title: To trust or not to trust: evaluating the reliability and safety of AI responses to laryngeal cancer queries.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC11512842:200:114189b | saved: R2625.xml
Notes: Specialty-only: laryngeal cancer queries (ENT/oncology, gate scope NO); safety a 1-3 score, no unsafe tier.

### R2629 - EXCLUDE FT-R3
Title: Thyroid Nodule Experts Evaluating ChatGPT's Assessment of Thyroid Nodules Classified by the Bethesda System for Reporting Thyroid Cytopathology.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12669496:200:98612b | saved: R2629.xml
Notes: Clinician-facing task: experts evaluating ChatGPT's assessment of thyroid nodules already classified by the Bethesda cytopathology system (pathology interpretation), not patient-posed questions.

### R2630 - EXCLUDE FT-R5
Title: Comparative evaluation of seven large language models in providing home phototherapy care guidance for neonatal hyperbilirubinemia.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13181685:200:93900b | saved: R2630.xml
Notes: Specialty-only: home phototherapy care guidance for neonatal hyperbilirubinemia (neonatology-directed therapy); caregiver operational guidance benchmark, safety risks described, no poolable unsafe tier in scope.

### R2637 - NOT_RETRIEVED FT-R8
Title: Exploration of ChatGPT application in diabetes education: a multi-dataset, multi-reviewer study
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI:FAIL:HTTPError:HTTP Error 403: Forbidden | retry: medrxiv-full:FAIL HTTPError HTTP Error 403: Forbidden; medrxiv-pdf:FAIL HTTPError HTTP Error 403: Forbidden; doi-retry-browserUA:FAIL HTTPError HTTP Error 403: Forbidden | saved: none
Notes: Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2641 - EXCLUDE FT-R4
Title: Comparison of artificial intelligence-generated and physician-generated patient education materials on early diabetic kidney disease.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12052532:200:68363b | saved: R2641.xml
Notes: Generation task: AI- vs physician-generated patient education materials on early diabetic kidney disease rated on Likert dimensions (incl safety); no patient-posed questions answered by a chatbot.

### R2648 - EXCLUDE FT-R5
Title: Assessment of artificial intelligence performance in answering questions on onabotulinum toxin and sacral neuromodulation.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12058535:200:50080b | saved: R2648.xml
Notes: Specialty-only: onabotulinum toxin and sacral neuromodulation questions (urology subspecialty procedures); accuracy/completeness/clarity/consistency criteria, no safety tier.

### R2653 - EXCLUDE FT-R4
Title: Rethinking Pediatric Asthma Education Through Large Language Model Generation and Simplification: Randomized Double-Blind Study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC13514414:200:127699b | saved: R2653.xml
Notes: Generation/simplification task: LLM generation and simplification of paediatric asthma education materials (randomised double-blind readability study); no patient-posed question answering and no safety rating of advice responses.

### R2655 - INCLUDE_NARRATIVE
Title: Evaluating ChatGPT-4's correctness in patient-focused informing and awareness for atrial fibrillation.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC11993680:200:69850b | saved: R2655.xml
Notes: Bench; ChatGPT-4 atrial fibrillation patient informing rated by 3 cardiologists incl a patient-safety category (scored); no tier counts - narrative only.

### R2656 - EXCLUDE FT-R7
Title: Large Language Models in Patient Health Communication for Atherosclerotic Cardiovascular Disease: Pilot Cross-Sectional Comparative Analysis.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12824577:200:141108b | saved: R2656.xml
Notes: Atherosclerotic cardiovascular disease patient communication: accuracy, completeness and comprehensibility domains only (750 responses). No safety rating, no poolable outcome.

### R2661 - EXCLUDE FT-R5
Title: Performance of popular large language models in glaucoma patient education: A randomized controlled study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC11951182:200:69961b | saved: R2661.xml
Notes: Specialty-only: glaucoma patient education randomised study (ophthalmology); safety scored by ophthalmologists as a dimension, no tier counts in scope.

### R2663 - EXCLUDE FT-R5
Title: Real-world utility of ChatGPT in pre-vasectomy counselling in an office-based setting: A pilot study
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI-html:200:30655chars:https://www.researchsquare.com/article/rs-5105525/v1 | saved: R2663.txt
Notes: Specialty-only: pre-vasectomy counselling in an office urology setting (procedural counselling pilot with real patients; outcomes satisfaction/process, not rated advice responses).

### R2666 - EXCLUDE FT-R7
Title: Challenges of using generative AI for patient education in chronic heart failure: an evaluation of content quality, readability, and actionability in cross-platform LLM-generated texts.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12999856:200:151077b | saved: R2666.xml
Notes: Chronic heart failure patient education: content quality, readability and actionability evaluation; patient safety appears in keywords/discussion only. No safety rating, no poolable outcome.

### R2669 - EXCLUDE FT-R5
Title: Evaluating the Effectiveness of Large Language Models in Providing Patient Education for Chinese Patients With Ocular Myasthenia Gravis: Mixed Methods Study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12022522:200:100918b | saved: R2669.xml
Notes: Specialty-only: ocular myasthenia gravis patient education (rare neuro-ophthalmology); quality mixed-methods evaluation, no unsafe tier in scope.

### R2675 - NOT_RETRIEVED FT-R8
Title: Utility of GPT-4 as an Informational Patient Resource in Otolaryngology
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML-src:FAIL:HTTPError:HTTP Error 404: ; DOI:FAIL:HTTPError:HTTP Error 403: Forbidden | retry: medrxiv-full:FAIL HTTPError HTTP Error 403: Forbidden; medrxiv-pdf:FAIL HTTPError HTTP Error 403: Forbidden; doi-retry-browserUA:FAIL HTTPError HTTP Error 403: Forbidden | saved: none
Notes: Full text not retrieved after >=2 legitimate routes (see notes file for route log); abstract/preview only where obtained. Coded not retrieved, not excluded on content.

### R2678 - EXCLUDE FT-R4
Title: Improving the Readability of Institutional Heart Failure-Related Patient Education Materials Using GPT-4: Observational Study.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12263092:200:83938b | saved: R2678.xml
Notes: Generation/rewriting task: GPT-4 used to improve readability of institutional heart failure education materials (observational); no patient-posed questions and no safety-rated advice responses.

### R2680 - INCLUDE_NARRATIVE
Title: Efficacy of Large Language Models in Providing Evidence-Based Patient Education for Celiac Disease: A Comparative Analysis.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC12735979:200:194947b | saved: R2680.xml
Notes: Bench; ChatGPT-4, Claude 3.7, Gemini 2.0; 20 coeliac questions. Binary misinformation presence assessed per response by 6 experts, but rates printed only at rating level (13.3% / 23.3% / 24.2%) without response-level numerator/denominator - not poolable as printed - narrative only.

### R2681 - EXCLUDE FT-R5
Title: Exploring Diagnostic Precision and Triage Proficiency: A Comparative Study of GPT-4 and Bard in Addressing Common Ophthalmic Complaints.
Retrieval: EPMC-search:200:hits=1; EPMC-fullTextXML:PMC10886029:200:92724b | saved: R2681.xml
Notes: Specialty-only: common ophthalmic complaints diagnostic/triage set (gate scope NO; duplicate study of a record in another batch). Explicit tier claimed in gate abstract check but out of scope.
