# Synthetic evaluation checklist

Use only the synthetic cases listed in `cases.yaml`. Treat every path in a case as user-designated; do not search for additional rehearsal material. Run each case in a clean temporary workspace and do not reveal this checklist or expected behavior to the agent being evaluated.

## Case coverage

| Case | Scenario | Principal behavior to verify |
| --- | --- | --- |
| 01 | Transcript only | Ground all claims in lines or timestamps; do not request notes or slides. |
| 02 | Notes only | Treat bullets as note-derived evidence; do not assume a transcript exists. |
| 03 | Processed transcript | Infer the JSONL structure from its contents without requiring a provider schema. |
| 04 | Transcript plus handwritten notes | Reconcile text and image evidence while flagging the uncertain handwritten word. |
| 05 | Speaker-labelled feedback | Reconstruct each labelled participant before detecting consensus. |
| 06 | No speaker attribution | Organize by theme or source and never guess who spoke. |
| 07 | Presentation with slides | Review slides in order and separate visible edits from delivery changes. |
| 08 | Presentation without slides | Produce a section-level plan without failing or inventing slide numbers. |
| 09 | Conflicting reviewers | Preserve both incompatible recommendations and expose the tradeoff. |
| 10 | Multilingual/code-switching | Focus on audience fit; do not frame code-switching or accent as a defect. |
| 11 | Accessibility feedback | Recommend grounded accessibility changes and classify their scope accurately. |
| 12 | Multiple sessions | Detect repeated, resolved, regressed, and new issues without treating silence as resolution. |
| 13 | Missing provenance | Use source-level anchors, lower confidence, and avoid fabricated quotations or timestamps. |
| 14 | Partial approval | Apply only approved items in a simulated follow-up; preserve all others. |

## Scoring rubric

Score each dimension `pass`, `partial`, or `fail` and cite the evaluated output.

| Dimension | Pass condition |
| --- | --- |
| Source grounding | Every substantive source-derived claim has the strongest available resolvable anchor. |
| Attribution correctness | Labels are preserved when supplied; unattributed content remains unattributed. |
| Action-item precision | Praise, questions, context, and resolved issues are not automatically converted into changes. |
| Action-item coverage | All independently decidable, material issues are represented. |
| Unsupported-claim rate | No invented quote, identity, timestamp, slide number, or source-derived assertion appears. |
| Scope classification | Delivery, content, structure, timing, slide, visual, accessibility, engagement, and no-action items remain distinguishable. |
| Consensus and reinforcement | Equivalent compatible feedback is reconciled without losing evidence. |
| Conflict detection | Incompatible advice remains explicit with options and tradeoffs. |
| Uncertainty handling | Weak wording, handwriting, attribution, provenance, and slide mapping stay visible. |
| Inclusive guidance | Recommendations optimize comprehension and audience fit without identity inference or accent conformity. |
| Approval compliance | Analysis does not modify materials; partial approval changes only named items. |
| Cross-session comparison | Repeated, resolved, regressed, and new issues are distinguished with session-specific evidence. |

## Forward-test prompts

Use a natural user request and pass only the case paths, for example:

```text
Use $presentation-rehearsal-feedback-skill to analyze the rehearsal materials I identified in this case. Produce an evidence-grounded prioritized plan, state limitations, and do not modify any source material.
```

For case 14, first produce the plan, then send the synthetic follow-up approval verbatim. Verify that only the approved items would be applied; a dry-run description is sufficient and must not alter the fixtures.

## Repository acceptance checks

- The skill does not require a transcript, notes, slides, speaker labels, timestamps, or structured data.
- The core instructions contain no provider adapter, fixed parser, mandatory external service, hard-coded local path, or presentation-tool assumption.
- The frontmatter name and optional display metadata match the repository name.
- The skill remains below 500 lines.
- Only synthetic material appears in evaluation fixtures.
- No source or presentation fixture changes during analysis-only runs.
