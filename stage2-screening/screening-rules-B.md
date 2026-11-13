# Screening rules, Set B (exclusion-first decision tree), v1, 2026-11-12

Screener B reads title and abstract and applies the tree in order. Stop at the first node that decides.
B1. Is it a primary study with rated LLM responses or rated layperson use? No: EXCLUDE (BX1, not primary rated evidence). Unclear: MAYBE.
B2. Is the system a general-purpose LLM chatbot in public hands? No: EXCLUDE (BX2). Unclear: MAYBE.
B3. Is any arm patient-facing (patient-posed questions, patient scenarios, lay users)? No: EXCLUDE (BX3, clinician-facing only). Unclear: MAYBE.
B4. Are the topics confined to a specialty that does not present in primary care, or to mental-health crisis only? Yes: EXCLUDE (BX4). Mixed or general: continue.
B5. Is safety or harm rated with a tier, scale, or category, by clinicians or a clinical rubric? Yes: INCLUDE. Only general accuracy or quality with no safety or harm element visible: MAYBE (full text may hold a harm tier). No rating at all: EXCLUDE (BX5).
Record one reason code per record. INCLUDE means the record looks eligible on the abstract; MAYBE means a specific named gap needs the full text.
