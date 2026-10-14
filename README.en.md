<div align="center">

**[简体中文](README.md) · English**

![paper-to-html](docs/images/cover.svg)

**Turn research papers into interactive, explained HTML reading guides.**

A reusable **Codex Skill + HTML reader toolkit** for Chinese-first, source-faithful paper explanations.

[![License: MIT](https://img.shields.io/badge/License-MIT-35644d.svg)](LICENSE)
[![Recommended: v2](https://img.shields.io/badge/Recommended-v2-35644d.svg)](skills/paper-to-html-v2/SKILL.md)

[Download v2](https://github.com/BerryIcey/paper-to-html/releases/latest) · [Read the Skill](skills/paper-to-html-v2/SKILL.md) · [See the demo](#see-it-in-action) · [Report an issue](https://github.com/BerryIcey/paper-to-html/issues)

</div>

## Why this project exists

A paper explanation can contain plenty of text and still leave the reader guessing: What does this point represent? Higher than which group? Why did the authors perform the next experiment?

This project turns useful conversational teaching practices into a repeatable workflow:

**Question → comparison design → actual observation → reasoning → supported conclusion → remaining question.**

The reader components reduce the friction of switching figure panels, looking up unfamiliar terms, and finding your place afterward.

This is a Skill that guides Codex in creating a paper-reading website, together with working components and validation scripts. It is not a standalone system that automatically understands arbitrary PDFs. Generated scientific explanations still require review.

## See it in action

The demo uses original explanatory text and invented chart values. It contains no real paper, private notes, or author datasets. The English feature demo omits translation blocks and highlights figure explanations, argument transitions, knowledge lookups, highlighting, and notes. It is a separate illustrative interface; the default Skill workflow remains Chinese-first.

![Synchronized figure and explanation panels](docs/images/en-figure-reader.png)

<details>
<summary>Show the reading overview and notes panel</summary>

![Reading overview](docs/images/en-reader-overview.png)
![Collapsible notes panel](docs/images/en-notes-bookmark.png)

</details>

[Download the demo HTML](demo/en/paper-reading.html) and open it in a browser. GitHub displays its source rather than running it. The static file supports panel switching, zooming, knowledge cards, and returning to your previous position. Saving project notes requires the local service described below.

## Features

| Reading task | What the project provides |
|---|---|
| Understand the text | Continuous source text, complete translations of the core sections, clear conclusions, and detailed explanations |
| Read each figure panel | Figure overviews and every main panel, with captions, translations, explicit legend mappings, and guided observations |
| Follow the research argument | An argument map explaining why each result leaves a question and why the next method addresses it |
| Evaluate the paper | A closing reader assessment covering contributions, credible findings, limitations, and another perspective |
| Look up terminology | Centered knowledge cards and an exact return to the previous panel and scroll position |
| Read comfortably | Side-by-side figures and independently scrolling explanations, with responsive panel switching |
| Annotate | An explicit highlighter toggle, undo, and a separate toggle for term category colors |
| Queue questions | A draggable edge bookmark and notes/screenshots saved to the paper project for the next assistant session |
| Keep versions manageable | One fixed latest desktop copy, plus the current release and zero, one, or two historical backups in the project |

The default output covers the complete first-reading core. Full Methods references, supplementary figure walkthroughs, quizzes, and other extensions are generated only when selected.

Content follows four zones: **core article → knowledge → advanced article content → advanced knowledge**. The closing reader assessment is required in the initial output even though it belongs to the last zone. Zone names do not determine which modules are optional.

## Quick start

### 1. Install v2

Download `paper-to-html-v2.zip` from [Releases](https://github.com/BerryIcey/paper-to-html/releases/latest). Extract it and place the complete `paper-to-html-v2` folder in your configured Codex user Skill directory, commonly `~/.codex/skills/`. Confirm that the Skill is available in the next turn or a new chat.

Alternatively, clone this repository and copy `skills/paper-to-html-v2/`. If you already have an older installation, back it up outside the Skill discovery directory to avoid both versions being selected automatically. Repository updates do not automatically update installed copies on other devices.

### 2. Give Codex a paper

```text
$paper-to-html-v2
Create a core Chinese HTML walkthrough of this paper.
Explain every main figure panel and review the text explanations,
figure walkthroughs, and argument map against the Skill.
Keep the same teaching detail throughout the paper.
```

Provide a PDF you are entitled to use. The assistant builds a fresh source/evidence ledger and panel inventory for that paper; it must not reuse scientific facts or numbers from the demo or another paper. Missing sources or supplementary materials should be disclosed.

### 3. Read and continue

Use the fixed latest desktop HTML for routine reading. Open the paper's local reader when you want to save questions. Notes are stored in the project and read by the assistant in a later session; **they do not trigger an immediate GPT response**.

On the first local launch, choose overwrite mode or one/two historical backups. The offline HTML displays the policy at export time; the project settings file is authoritative. If you postpone the choice, a timestamped working copy can still be delivered without deleting history.

## Try the components without a model

Run the local service for the synthetic demo:

```sh
git clone https://github.com/BerryIcey/paper-to-html.git
cd paper-to-html
python skills/paper-to-html-v2/assets/reader-components/reading_server.py --root demo/en --port 18765
```

Open `http://127.0.0.1:18765/paper-reading.html`. This is a temporary demo server. For a persistent paper project, follow the Skill's independent background-service instructions. The project queue stays on your machine and does not require an OpenAI API key.

## Versions and updates

| Version | Skill directory | Purpose |
|---|---|---|
| v1.0.0 | [paper-reading-web](skills/paper-reading-web/SKILL.md) | Preserved original snapshot for comparison and rollback |
| v2.0.2 | [paper-to-html-v2](skills/paper-to-html-v2/SKILL.md) | Recommended version with unified rules and corrected publication/settings behavior |

v1 retains its original instructions, including rules superseded by v2. Do not mix reference files from the two versions. Future development is maintained here; the personal Skill library links to this project rather than distributing replacement copies.

See the [v2 change notes](docs/v2-changes.md), currently in Chinese. Each downloadable ZIP contains one Skill root folder and has a SHA-256 checksum. The Skill version and an individual paper's HTML release number are independent.

## Requirements and limitations

- Producing a full paper walkthrough requires a Skill-capable assistant, PDF-reading capabilities, and suitable image tools. The reader, assembler, publisher, and local server use the Python standard library. The PDF crop renderer requires PyMuPDF; JavaScript syntax checks use Node.js.
- Source text, translations, statistics, legends, and scientific reasoning must be reviewed unit by unit. Passing structural tests does not establish scientific correctness or reader comprehension.
- The static reader does not depend on a CDN. Highlights and drafts are stored in the browser; submitted notes and settings are stored in the project. Automatic retry of offline submissions, cross-device synchronization, and instant GPT chat are not implemented.
- The loopback server is accessible from the same machine only. Reading an offline HTML on a phone does not let that phone submit notes to a computer's `127.0.0.1`. Remote access requires a separately configured secure service.
- The Windows persistence approach uses a current-user scheduled task and a supervisor. Other platforms need an appropriate background-service mechanism. Crash recovery and survival of an actual application restart are separate checks.
- The current Skill and generated reader are Chinese-first. This README makes the project accessible to English-speaking readers; it does not promise a fully English-localized workflow.
- Code and general workflow documentation are MIT-licensed. User-supplied papers, third-party images, and generated paper-specific content retain their applicable rights and usage conditions. They are not distributed by this repository.

## Contribute

Useful reports include the version, operating system/browser, expected behavior, observed behavior, reproduction steps, and a minimal screenshot you can share publicly. For teaching issues, identify which object, comparison, inference, or transition remains unclear.

Please do not upload private notes, account details, or paper full texts without permission.

Priorities include understandable reasoning for first-time readers, consistent detail across large outputs, real touchscreen behavior, and legend conventions across disciplines.

If this helps you understand a paper, a Star is appreciated. Even more useful is telling us where the explanation still makes you guess.
