# Presentation Rehearsal Feedback

`presentation-rehearsal-feedback-skill` is a platform-neutral Agent Skill for turning presentation rehearsal evidence into a prioritized improvement plan. It reconstructs what reviewers or audiences actually said, separates evidence from interpretation and recommendation, reconciles agreement and conflict, and keeps proposed edits behind an explicit approval boundary.

The skill supports research talks, thesis and dissertation defences, conference presentations, seminars, lectures, teaching demonstrations, technical talks, product demos, project reviews, business and sales presentations, startup or investor pitches, interview presentations, workshops, keynotes, community presentations, and public talks.

## Open input model

> The skill works with transcripts, notes, processed transcripts, reviewer feedback, and related presentation materials explicitly identified by the user, in any format the active agent can read.

Inputs can be structured, unstructured, mixed-format, speaker-labelled, unattributed, timestamped, or informal. No fixed filename, directory, schema, transcript provider, slide tool, or presentation type is required. Slides are optional unless the requested work is slide-specific.

The skill inspects only the materials the user designates and determines provenance from what each source actually contains. Missing timestamps, speaker labels, slides, or context become explicit limitations; they are never fabricated.

## What it produces

Depending on the request and evidence, the skill can produce:

- source-grounded feedback synthesis by participant, theme, source, section, or issue;
- atomic feedback items that distinguish direct comments, questions, explicit requests, inferred improvements, and agent recommendations;
- delivery, content, structure, timing, slide, visual, accessibility, and engagement recommendations;
- rehearsal-focus routing for delivery, content, Q&A preparation, timing, audience comprehension, comprehensive, and user-defined goals;
- systematic slide-content issue inventories that distinguish participant feedback from independently detected concerns;
- question-risk maps and answer-preparation plans when Q&A is in scope;
- consensus, reinforcement, conflict, uncertainty, unresolved-question, and decision logs;
- slide-by-slide or section-by-section revision plans;
- comparisons across multiple rehearsals;
- structured JSON when the user requests it or downstream tracking materially benefits from it.

Review, analysis, synthesis, comparison, coaching, and planning requests do not authorize edits. The skill proposes changes first and applies only the items the user explicitly approves, including partial-approval cases.

## Example requests

- “Use these two rehearsal transcripts to identify repeated issues, improvements, and regressions. I do not have slides.”
- “Synthesize the reviewer comments in this CSV and my typed notes. Preserve disagreements and give me a prioritized delivery plan.”
- “Review this product-demo rehearsal transcript and deck. Make a complete slide-by-slide plan, including slides that should stay unchanged.”
- “These notes have no speaker labels or timestamps. Separate note-derived observations from your recommendations and flag weak provenance.”
- “Compare the Spanish-English rehearsal notes with the timing log. Focus on audience comprehension without treating code-switching as a defect.”
- “Apply only recommendations R2 and R5 from the plan; leave every other presentation file unchanged.”
- “This is a thesis-defence Q&A rehearsal. Build a question-risk map and answer plan; do not turn it into a generic slide-design review.”

## Evidence-grounded workflow

The skill registers the user-designated sources, inspects each on its own terms, records the strongest available evidence anchor, extracts independently decidable feedback items, and then reconciles them across participants or sources. Direct evidence, faithful paraphrase, requested action, and agent-authored recommendation stay visibly separate.

Priorities reflect evidence strength, likely audience impact, presentation goals, dependencies, and effort—not the apparent seniority of a reviewer. Praise and resolved questions remain visible without automatically becoming tasks.

## Privacy

The portable workflow does not require web access, an external API, or a transcription service. It prefers local processing and instructs the agent not to inspect unrelated folders or transmit confidential material to an additional service without explicit authorization.

Privacy still depends on the active agent and tools chosen by the user. Review the platform’s data handling, connector, logging, and retention policies before using sensitive materials. Do not add real rehearsal content, participant names, or derived private reports to this repository.

## Installation

This repository contains one canonical, platform-neutral skill package. It intentionally does not contain `.agents/skills/`, `.claude/skills/`, `.cursor/skills/`, or `.github/skills/` copies. Do not maintain separate variants of `SKILL.md` for different agents.

To install it, copy or clone the complete repository folder into the skill directory used by the target agent. Keep the installed folder name `presentation-rehearsal-feedback-skill`:

| Platform | Project-level locations | User-level locations |
| --- | --- | --- |
| Codex | `.agents/skills/presentation-rehearsal-feedback-skill/` | `~/.agents/skills/presentation-rehearsal-feedback-skill/` |
| Cursor | `.cursor/skills/presentation-rehearsal-feedback-skill/` | `~/.cursor/skills/presentation-rehearsal-feedback-skill/` |
| Claude Code | `.claude/skills/presentation-rehearsal-feedback-skill/` | `~/.claude/skills/presentation-rehearsal-feedback-skill/` |
| GitHub Copilot | `.github/skills/presentation-rehearsal-feedback-skill/` | `~/.copilot/skills/presentation-rehearsal-feedback-skill/` |

Cursor and GitHub Copilot also support `.agents/skills/`; both document additional compatible locations. The native paths above keep the installation instructions easiest to understand. Regardless of location, install the same repository contents without modifying the portable core.

Install the complete folder rather than copying only `SKILL.md`, because the skill references `assets/revision-plan-template.md`.

### Download for Codex

Project-level installation (run from the target project root):

```bash
mkdir -p .agents/skills/presentation-rehearsal-feedback-skill
curl -fsSL https://github.com/jiapivialiu/presentation-rehearsal-feedback-skill/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=1 -C .agents/skills/presentation-rehearsal-feedback-skill
```

User-level installation:

```bash
mkdir -p ~/.agents/skills/presentation-rehearsal-feedback-skill
curl -fsSL https://github.com/jiapivialiu/presentation-rehearsal-feedback-skill/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=1 -C ~/.agents/skills/presentation-rehearsal-feedback-skill
```

### Download for Cursor

Project-level installation (run from the target project root):

```bash
mkdir -p .cursor/skills/presentation-rehearsal-feedback-skill
curl -fsSL https://github.com/jiapivialiu/presentation-rehearsal-feedback-skill/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=1 -C .cursor/skills/presentation-rehearsal-feedback-skill
```

User-level installation:

```bash
mkdir -p ~/.cursor/skills/presentation-rehearsal-feedback-skill
curl -fsSL https://github.com/jiapivialiu/presentation-rehearsal-feedback-skill/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=1 -C ~/.cursor/skills/presentation-rehearsal-feedback-skill
```

### Download for Claude Code

Project-level installation (run from the target project root):

```bash
mkdir -p .claude/skills/presentation-rehearsal-feedback-skill
curl -fsSL https://github.com/jiapivialiu/presentation-rehearsal-feedback-skill/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=1 -C .claude/skills/presentation-rehearsal-feedback-skill
```

User-level installation:

```bash
mkdir -p ~/.claude/skills/presentation-rehearsal-feedback-skill
curl -fsSL https://github.com/jiapivialiu/presentation-rehearsal-feedback-skill/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=1 -C ~/.claude/skills/presentation-rehearsal-feedback-skill
```

### Download for GitHub Copilot

Project-level installation (run from the target project root):

```bash
mkdir -p .github/skills/presentation-rehearsal-feedback-skill
curl -fsSL https://github.com/jiapivialiu/presentation-rehearsal-feedback-skill/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=1 -C .github/skills/presentation-rehearsal-feedback-skill
```

User-level installation:

```bash
mkdir -p ~/.copilot/skills/presentation-rehearsal-feedback-skill
curl -fsSL https://github.com/jiapivialiu/presentation-rehearsal-feedback-skill/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=1 -C ~/.copilot/skills/presentation-rehearsal-feedback-skill
```

These commands target macOS and Linux shells. They download the same canonical package for every agent and do not create platform-specific copies in this repository.

After installation, verify discovery and invoke the skill explicitly once:

- Codex: run `/skills` or mention `$presentation-rehearsal-feedback-skill` in the prompt.
- Cursor: open **Customize → Skills**, then use `/presentation-rehearsal-feedback-skill`.
- Claude Code: use `/presentation-rehearsal-feedback-skill`; restart Claude Code if `.claude/skills/` did not exist when the session started.
- GitHub Copilot: open the Skills configuration or type `/skills`, then invoke `/presentation-rehearsal-feedback-skill` where slash-command invocation is available.

Official references: [OpenAI Codex skills](https://learn.chatgpt.com/docs/build-skills), [Cursor Agent Skills](https://cursor.com/docs/skills), [Claude Code skills](https://code.claude.com/docs/en/skills), and [GitHub Copilot agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills).

The portable core is [SKILL.md](SKILL.md). [agents/openai.yaml](agents/openai.yaml) is optional OpenAI-specific interface metadata and is not required by the core workflow.

## Tested compatibility

- The skill structure and metadata are validated with OpenAI’s skill-creator validation tooling.
- The raw skill is forward-tested in Codex against synthetic transcript-only, notes-only and unattributed, combined transcript-and-handwritten-note, slide-based, multi-session, and partial-approval scenarios.
- Cursor, Claude Code, and GitHub Copilot compatibility is supported by the shared Agent Skills format and documented discovery paths, but live platform smoke tests remain required before marking them tested alongside Codex.

## Evaluation

Synthetic cases under [evals](evals) cover twenty-one required scenarios using plain text, Markdown, JSON, JSONL, CSV, YAML, and a synthetic handwritten-note image. They test source grounding, attribution, action precision and coverage, unsupported claims, scope classification, consensus and conflict detection, uncertainty, inclusive guidance, approval compliance, cross-session comparison, focus adaptation, slide-content diagnosis, Q&A preparation, timing, and user-defined evaluation goals.

Run the repository checks with:

```bash
python3 -m unittest discover -s tests -v
```

Use [evals/evaluation-checklist.md](evals/evaluation-checklist.md) for qualitative forward evaluation. The fixtures are synthetic and intentionally do not share one transcript schema.

## Known limitations

- The skill is not a transcription or optical-character-recognition system; it relies on the active agent’s ability to read the user-selected material.
- Poor audio-derived text, illegible handwriting, missing provenance, and ambiguous attribution reduce confidence.
- Timing analysis requires actual timing evidence; transcript length alone is insufficient.
- Slide-specific advice requires slides or reliable slide references.
- Recommendations are analytical guidance, not proof that a change will improve a live audience outcome.

## License

This project is licensed under the [MIT License](LICENSE).
