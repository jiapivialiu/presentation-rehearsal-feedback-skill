# Rehearsal focus modules

Use this reference after selecting one primary focus and any secondary focuses. Apply only relevant modules unless `comprehensive` is selected.

## Contents

- Focus modes
- Slide-content diagnosis
- Q&A preparation
- Focus-specific completion criteria

## Focus modes

### `delivery`

Prioritize verbal clarity, transitions, pacing, spoken explanations, unnecessary detail, tone, audience engagement, and slide-to-talk-track correspondence. Produce actionable wording, transition, pacing, explanation, and engagement changes. Do not independently audit every technical claim unless requested or necessary to explain a delivery problem.

### `content`

Prioritize slide-content problems, logical structure, motivation, definitions, claims, assumptions, evidence-to-conclusion alignment, figures, equations, tables, redundancy, limitations, ambiguity, and potentially misleading content. Diagnose systematically before recommending edits and include the slide-content issue inventory below.

### `qa-prep`

Prioritize claims likely to trigger questions, assumptions, methodological choices, missing comparisons, limitations, robustness, alternative explanations, likely follow-ups, evidence needed for answers, weak observed answers, and presenter uncertainty. Produce the question-preparation module below.

### `timing`

Prioritize actual or supported estimated time by section, overruns, compressed sections, interaction time, content suitable for backup slides, verbal detail to shorten, and allocation relative to importance. Produce an allocation table, overlong sections, compression options, and priority-based cuts. Never infer timing from transcript length alone.

### `audience-comprehension`

Prioritize assumed background knowledge, missing definitions, cognitive load, abrupt transitions, unexplained notation, inaccessible figures, needed examples or intuition, and the difference between expert and non-expert audiences. Rank changes by likely comprehension impact for the stated audience.

### `comprehensive`

Run all applicable modules, prioritizing them according to the presentation goal and constraints. Reuse a single atomic issue across module views instead of reporting it as multiple independent issues.

### `user-defined`

Follow the user's stated evaluation goal even when it does not match a predefined mode. Translate that goal into explicit evidence priorities, outputs, and completion criteria before analyzing.

## Slide-content diagnosis

For each relevant slide or section, answer: what is potentially wrong, missing, unclear, unsupported, misleading, redundant, or poorly positioned in its content? Do not assume every slide has a problem and do not jump directly from feedback to an edit.

Evaluate applicable dimensions: purpose, motivation, context, logic, claims, assumptions, terminology, notation, accuracy, ambiguity, evidence adequacy, evidence-to-conclusion alignment, equations, figures, tables, comparisons, limitations, detail level, redundancy, title-content match, narrative placement, talk-track alignment, avoidable question risk, accessibility, and cognitive load.

Keep diagnosis separate from implementation instructions. For each relevant slide provide:

- slide number or section and title;
- current purpose;
- `issue_origin`: `participant_feedback`, `presenter_notes`, `multiple_sources`, `agent_detected`, or `mixed`;
- specific content problem;
- supporting evidence or independent reasoning;
- why it matters, audience impact, and question risk;
- recommended correction;
- priority, confidence, approval status, and whether user confirmation is required.

Use `participant_feedback` only for issues supported by rehearsal feedback. Use `agent_detected` for independent analysis of slides or presentation materials. For an agent-detected issue, explain the reasoning, use cautious language, assign confidence, and request confirmation when subject-matter judgment is required.

## Q&A preparation

For every high-risk slide, claim, method, result, or decision include:

- likely question and why the audience may ask it;
- triggering slide, claim, or rehearsal moment;
- source of the risk and relevant assumptions;
- evidence needed to answer;
- concise answer outline and, when useful, an extended answer outline;
- possible follow-up question;
- whether a slide change could prevent unnecessary confusion;
- whether the issue belongs in oral discussion rather than additional slide content.

For thesis or dissertation defences, additionally consider novelty and contribution, methodological assumptions and selection, alternatives, theoretical justification, computational complexity, robustness and sensitivity, limitations, generalizability, interpretation, connections across chapters, and future work. Do not impose these categories on other presentation types.

## Focus-specific completion criteria

- **Delivery:** identify actionable wording, transition, pacing, explanation, and audience-engagement changes.
- **Content:** include systematic diagnosis, evidence or reasoning per issue, separation of feedback-raised from agent-detected problems, and specific corrections.
- **Q&A:** include high-risk claims, likely questions, answer preparation, likely follow-ups, and relevant slide or delivery changes.
- **Timing:** include time allocation, overlong sections, compression options, and priority-based cuts.
- **Audience comprehension:** connect every prioritized change to the stated audience's likely knowledge or cognitive needs.
- **Comprehensive:** include all applicable modules without duplicating the same issue.
- **User-defined:** verify the explicit user-defined evidence priorities, outputs, and completion criteria.
