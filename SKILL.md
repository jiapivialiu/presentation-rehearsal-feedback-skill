---
name: presentation-rehearsal-feedback-skill
description: Synthesize evidence-grounded feedback from presentation rehearsals and produce prioritized recommendations for delivery, content, structure, timing, slides, visual materials, accessibility, and audience engagement. Use for presentation rehearsal feedback from raw, cleaned, processed, speaker-labelled, or unlabelled transcripts; handwritten or typed notes; reviewer comments; audience questions; facilitator or timing notes; delivery coaching; slide revision planning; feedback reconciliation; and comparison across rehearsal sessions for any presentation context.
---

# Presentation Rehearsal Feedback

Turn user-designated rehearsal materials into an auditable review and revision plan. Begin after the user has identified the transcript, notes, feedback, slides, or related materials to analyze. Do not transcribe recordings or require a transcription provider.

## Boundaries

1. Inspect only the materials the user identifies and files directly required to understand them. Do not search unrelated folders for more rehearsal data.
2. Treat every source as immutable. Analyze in place; write derived artifacts separately only when the user asks for files.
3. Use the active agent's existing reading capabilities. Do not require a filename, directory layout, input schema, file format, operating system, presentation tool, external API, or network access.
4. Adapt to the materials present. A transcript, notes, slides, speaker attribution, timestamps, and multiple sessions are all optional.
5. State material limitations instead of inventing missing context, timing, identity, attribution, quotations, or slide mappings.
6. Keep confidential materials private. Prefer local processing, avoid exposing source content in logs or tracked fixtures, and do not upload or transmit it to an additional service without the user's explicit authorization.
7. Analyze and plan first. Do not modify presentation materials until the user explicitly approves specific proposed changes.

## Workflow

### 1. Establish the task and inputs

- List the exact user-designated sources and the requested outcome.
- Capture presentation type, purpose, audience, target duration, language, venue, delivery mode, and constraints when supplied. Do not block analysis when they are absent.
- Identify whether the request covers synthesis, coaching, slide review, timing, comparison, implementation, or a combination.
- Preserve source versions and note any ambiguity about which version was rehearsed.

### 2. Inspect each source on its own terms

- Determine structure from actual content rather than expecting predetermined fields.
- Read structured and unstructured sources with the capabilities available for that format.
- For presentation files or visual materials, inspect the rendered content and speaker notes when available.
- For handwritten notes, distinguish legible text, uncertain readings, and visual marks. Never silently resolve uncertain handwriting.
- For multiple sources, examine each independently before reconciling them.

Create a small source register with a stable source label, filename or user-facing label, source type, session if known, and usable evidence anchors. Do not create a machine-readable artifact unless requested or useful for later comparison.

### 3. Establish evidence provenance

Use the strongest anchor each source actually provides. Possible anchors include timestamp, segment ID, speaker label, user-supplied participant name, line, paragraph, heading, page, slide, note heading, bullet, filename, source label, or a short supported excerpt.

- Never fabricate timestamps, speakers, names, slide numbers, or exact quotations.
- Preserve source speaker labels unless the user provides a reliable identity mapping.
- When attribution is reliable, reconstruct feedback participant by participant before combining it.
- When attribution is missing or unreliable, organize by theme, source, presentation section, or issue and label observations as unattributed.
- When precise provenance is absent, label the observation as note-derived or source-level and lower confidence as appropriate.
- Quote only wording directly supported by the source. Label faithful paraphrases as paraphrases.

For every substantive item, keep these layers distinct:

1. **Direct evidence** — the supported source location and optional short excerpt.
2. **Interpretation** — a faithful explanation of what the evidence means.
3. **Requested or implied action** — a change supported by the source.
4. **Agent recommendation** — independently labelled advice based on the evidence and presentation goals.

### 4. Extract atomic feedback

Create one item for each independently decidable issue. Do not treat every comment, question, or reaction as a requested change. Preserve praise and strengths that should remain unchanged.

Use these analytical aids when helpful; do not require them as input fields:

- source and evidence anchor;
- participant or source label;
- relevant slide or presentation section;
- feedback type: concern, question, suggestion, clarification, praise, disagreement, observation, or audience reaction;
- issue and rationale;
- requested or implied change;
- agent recommendation;
- change scope: delivery, content, structure, timing, slides, visual design, accessibility, audience engagement, interaction, multiple, or no action;
- priority, confidence, dependencies, and status.

Use `needs confirmation` for ambiguous attribution, uncertain wording, unresolved conflicts, weak evidence, or unclear slide mapping. Track whether discussion already resolved a question; use `no action` when no remaining change is supported.

### 5. Reconcile evidence

- Merge only semantically equivalent items that lead to the same decision; retain all supporting anchors.
- Mark **consensus** when independent sources support the same issue and compatible action.
- Mark **reinforcement** when another source adds evidence or scope without creating a separate decision.
- Mark **conflict** when recommendations are incompatible or expose a real tradeoff. Preserve each view and recommend an option with rationale; do not average the views into false consensus.
- Preserve minority and dissenting feedback. Do not give a view extra weight merely because its speaker appears senior.
- Separate explicit requests from inferred improvements and from the agent's own recommendations.
- Flag unclear evidence, unresolved questions, and decisions requiring user judgment.

### 6. Analyze the presentation

Prioritize recommendations by evidence strength, likely audience impact, presentation goals, dependencies, and effort. Frequency may increase confidence but does not automatically make an issue urgent.

When supported, assess:

- **Delivery:** opening, conclusion, transitions, verbal explanations, terminology, pacing, emphasis, confidence cues, handling questions, audience interaction, and details to shorten or omit.
- **Content and structure:** narrative, purpose, claims, support, ordering, signposting, likely confusion, missing context, and alignment with the audience.
- **Timing:** target versus observed duration, section balance, overruns, pauses, interaction time, and concrete places to shorten or expand. Do not invent timing from text alone.
- **Slides and visuals:** purpose, visible content, figures, tables, equations, labels, layout, sequence, cognitive load, and coordination with spoken delivery.
- **Accessibility:** readable text, contrast, non-color-only encoding, captions, descriptions, clear labels, pacing, and accessible supporting materials.

When slides or visual materials are supplied, review them in presentation order and map feedback to exact slides when grounded. Otherwise map to presentation topics or sections. For a requested complete slide-by-slide plan, include slides that should remain unchanged. Do not require or request slides for delivery-only analysis.

### 7. Compare sessions when provided

For multiple rehearsal sessions, keep source versions and sessions distinct. Identify repeated issues, resolved issues, regressions, new issues, changes in participant views, delivery or timing improvements, and differences associated with revisions. Do not mistake missing feedback in a later session for proof that an issue was resolved.

### 8. Produce the review plan

Adapt the response to the user's request and evidence. Default to a readable report rather than mandatory JSON. Use structured JSON only when requested, needed for cross-session tracking, or materially useful to downstream work.

Include, as applicable:

1. scope, sources, context, and material limitations;
2. strengths to preserve;
3. source-grounded synthesis by participant when attribution is reliable, otherwise by theme, source, section, or issue;
4. prioritized delivery, content, structure, timing, slide, visual, accessibility, and engagement recommendations;
5. slide-by-slide or section-by-section plan when relevant;
6. consensus, reinforcement, conflicts, resolved issues, unresolved questions, and low-confidence observations;
7. a decision log with tradeoffs, recommended option, alternatives, dependencies, status, and feedback intentionally not converted into action;
8. a clear list of changes awaiting approval.

For a detailed written artifact, adapt [assets/revision-plan-template.md](assets/revision-plan-template.md) and remove inapplicable sections. Do not force empty sections or create a database-ready output by default.

### 9. Respect the approval boundary

A request to review, analyze, synthesize, summarize, compare, coach, or create a plan authorizes analysis only.

Before editing any presentation, notes, script, or supporting material:

1. Present the proposed changes with evidence, priority, confidence, and dependencies.
2. Ask the user to approve, reject, defer, or revise them.
3. Apply only the explicitly approved changes, preserving unapproved material.
4. Record partial approval accurately; do not treat approval of one item as approval of related items.
5. Verify the implementation against the approved scope and report any limitation.

## Inclusive guidance

- Optimize for comprehensibility and audience fit, not accent conformity or sounding "more native."
- Do not infer gender, ethnicity, seniority, expertise, disability, or identity from voices, names, language use, or communication style.
- Do not treat accent, dialect, code-switching, speech disability, multilingual delivery, or nonstandard phrasing as inherently incorrect.
- Treat formality, directness, storytelling, humor, and interaction as context-dependent rather than universally good or bad.
- Support multilingual materials whenever they can be read reliably; identify translation or interpretation uncertainty.
- Recommend communication changes only when grounded in audience needs, presentation goals, accessibility, or evidence from the rehearsal.

## Final quality check

- Every substantive claim has a resolvable evidence anchor or is explicitly labelled as an agent recommendation.
- Quotations, identities, timestamps, participant attribution, and slide mappings are supported.
- Atomic items preserve evidence after deduplication.
- Consensus, reinforcement, conflict, uncertainty, and resolved questions are represented accurately.
- Delivery, content, structure, timing, slide, and accessibility changes are classified clearly.
- Strengths and feedback that should not become action items remain visible.
- Recommendations are prioritized without automatically privileging seniority or one communication style.
- No source material was modified during analysis.
- No presentation material was changed without explicit approval, including partial-approval cases.
