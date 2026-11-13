# Risk of bias form, ADAPTED tool, version 1, 2026-11-12

Specified before extraction. This tool is an adaptation, and it is named as adapted wherever it is used. No off-the-shelf tool fits bench and human-user LLM advice studies: RoB 2 covers randomised human-user trials, ROBINS-I covers non-randomised human studies, and QUADAS-2 covers diagnostic accuracy. The adaptation takes QUADAS-2 structure and QUADAS-AI signalling questions as its base and adds CHART-informed reporting items for chatbot health advice studies (Huo et al. 2025; CHART statement, BMJ Medicine 2025). Human-user randomised studies are also checked against RoB 2 randomisation items inside Domain 1.

## Domains and signalling questions
Domain 1, question and participant selection.
- Were the questions or scenarios sampled from a defined source (real patient questions, a published set, a clinic log) rather than written to favour or to trip the model?
- Was the sampling method described well enough to repeat?
- For human-user studies: were participants recruited and allocated in a way that avoids selection bias (randomisation and concealment for RCTs)?
- Does the question set cover the primary-care scope it claims, without cherry-picked easy or adversarial-only items? (Adversarial sets are not penalised if they are labelled as stress tests and analysed apart; they are rated high concern if pooled silently with routine questions.)

Domain 2, the index test: model conduct.
- Are the model, version, and access dates reported?
- Were prompts put as a patient would put them, in full, with the prompt text or set available?
- Was each question put once, or were repeat runs and any selection among runs described?
- Were model settings (temperature, system prompt, browsing on or off) reported?

Domain 3, the reference standard: safety rating.
- Were responses rated by clinicians with relevant primary-care competence?
- Were raters blind to which model produced each response?
- Was the rating rubric defined before rating, with an explicit unsafe tier defined in words?
- Were at least two raters used, with agreement or adjudication reported?

Domain 4, flow and timing.
- Do all responses generated appear in the denominators (no silent dropping of refusals, empty answers, or repeat runs)?
- Is the time between model access and rating short enough that the rated object is the object described?
- For human-user studies: did all participants and scenarios analysed match those enrolled, with missing data explained?

## Judgements
Each domain: Low, Some concerns, or High, with a support quote or location for every signalling answer (Yes, Probably yes, Probably no, No, No information).
Overall: Low if all domains Low. High if any domain is High. Some concerns otherwise, with one conditional route to High carried from the Review 3 form: three or more domains at Some concerns give High only where the combination leaves question selection, model conduct, and rating all unchecked at once; the adjudicator reads that route against the paper before it is applied.
Two assessors rate apart. Disagreements go to an adjudicator who reads the paper and both rationales. No mechanical rule settles a disagreement.
