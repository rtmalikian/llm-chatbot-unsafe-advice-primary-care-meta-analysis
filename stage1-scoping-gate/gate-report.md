# Go and no-go gate report, Review 4, 2026-11-12

Gate rule (protocol, fixed 2026-11-12 before screening): proceed to full screening only if the scoping screen finds at least 15 studies reporting the primary numerator and denominator (explicit unsafe, harmful, or dangerous tier count over total responses rated for safety) for primary-care presentations, covering at least 3 models, with at least 2,000 responses in total.

## How the screen ran
The Stage 1 search set (3,106 deduplicated records) was scanned for an abstract-level safety signal (unsafe, harmful, dangerous, harm wording with a patient-facing LLM): 401 candidate records. Eight gate checkers, working in slices, coded all 401 records for primary-care scope and explicit-tier status against abstracts and, where legitimately open, full texts (gate-check-1.csv to gate-check-8.csv). Duplicate reports were linked by full normalised title and by study identity, and each study was counted once (gate-tally.json, computed by code from the eight files).

## Counts
Unique studies with scope YES, explicit tier YES, and retrieved numerator and denominator: 15.
Summed responses in those studies: 364 unsafe of 2,940 rated.
Studies: ED triage (Ada/WebMD comparison, LLM arms only) 23/74; bacterial vaginosis 31/305; painful diabetic peripheral neuropathy 28/300; mpox 31/312; high-risk HPV 10/90; traumatic brain injury and concussion 27/325; hand, foot and mouth disease 10/100; frozen shoulder 21/200; herpes zoster 66/230; recurrent aphthous stomatitis 16/150; paediatric burn first aid 21/144 (derived, see caveats); late-life depression 29/270 (adjudicated, see caveats); vegetarian and vegan nutrition 47/290; haemorrhoids 0/75; myocardial infarction public education 4/75.
Models covered by the 15: ChatGPT and GPT series (3.5, 4, 5.5), Gemini, Microsoft Copilot, DeepSeek, Doubao, Qwen. At least 3 models: met many times over.
Not counted toward the gate: Draelos et al. 2026 (R2101, HealthAdvice, 888 responses), whose unsafe percentages are printed per arm with the denominator 222 but whose Gemini arm appears only in a figure, coded partial; and seven further unique in-scope studies with an explicit tier whose counts were not retrieved from accessible text (appendicitis R2875; "Doctor ChatGPT" R1781; sexual health R2882; altered consciousness R0188; LMIC simulated patients R1802; RepVig R1712; and one duplicate-linked record). These studies go forward to full-text screening and may add to the pool.

## Caveats, recorded with the verdict
1. The study count sits exactly on the threshold, 15 of at least 15. If the full-text stage reclassifies a study out of scope, the primary pool could fall to 14 studies. The gate is a scoping decision taken on the evidence above; the pool as finally extracted is reported as found, and no eligibility rule will be loosened to protect the count.
2. Late-life depression (R2204, 29/270) drew opposite scope calls from two checkers. The coordinator adjudicated by the protocol text: the boundary excludes mental-health crisis and self-harm content from the primary pool; this question set is not crisis-only (it covers medication, delirium, falls, and triage in older adults, all core primary care), so it counts in scope, with any crisis-specific items to be excluded at extraction if they are separable. One checker had coded it NO; the disagreement and the ruling are recorded here and in llm-team-log.md.
3. Paediatric burn first aid (R2134) counts are derived: the abstract prints safe counts per model and the denominator; unsafe counts are the complement, flagged derived in gate-check-5.csv and to be verified against the full text at extraction.
4. The gate screen covered records with an abstract-level safety signal. A study with an explicit tier described only in its full text, and no safety wording in its abstract, would be missed by the gate screen and found at full screening instead. The gate therefore understates, rather than overstates, the pool on this point.

## Verdict
GATE PASSED on all three thresholds (15 studies, at least 3 models, 2,940 responses). Full screening proceeds under Standard v2. The fallback (symptom-checker undertriage) is not activated.
