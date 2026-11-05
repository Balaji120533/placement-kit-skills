# Placement Kit

Practise every placement round, from round-1 aptitude to the DSA interview, and learn to explain your answers the way interviewers want to hear them.

Placement Kit is four open Agent Skills that turn an AI assistant into a placement trainer for Indian campus placements. It makes you attempt each step instead of handing you the answer, and it checks questions before showing them.

## What's inside

| Skill | Covers | Try saying |
| --- | --- | --- |
| `aptitude-coach` | Quant, logical reasoning, verbal | "Teach me time and work" |
| `cs-fundamentals` | OS, DBMS/SQL, networks, OOP, C/Java output | "10 OS MCQs, medium" |
| `dsa-coach` | DSA problems, debugging, explaining your approach, mock interviews, no-library rounds | "Help me solve Two Sum" |
| `mock-placement` | Full round-1 mock tests with a section-wise report | "Round 1 mock, 30 questions, 40 minutes" |

## Install

Install once, then just chat. The assistant picks the right skill and mode from your wording.

**1. Get the files**

```
git clone https://github.com/Balaji120533/placement-kit-skills.git
cd placement-kit-skills
```

No git? On GitHub, click **Code → Download ZIP**, unzip it and open a terminal in that folder.

**2. Add the skills to your tool**

**Claude Code**

Windows (PowerShell):
```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item dsa-coach, cs-fundamentals, aptitude-coach, mock-placement -Destination "$HOME\.claude\skills" -Recurse -Force
```

Mac / Linux:
```bash
mkdir -p ~/.claude/skills
cp -r dsa-coach cs-fundamentals aptitude-coach mock-placement ~/.claude/skills/
```

Then start a new Claude Code session.

**Codex CLI**

Windows (PowerShell):
```powershell
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
Copy-Item dsa-coach, cs-fundamentals, aptitude-coach, mock-placement -Destination "$HOME\.codex\skills" -Recurse -Force
```

Mac / Linux:
```bash
mkdir -p ~/.codex/skills
cp -r dsa-coach cs-fundamentals aptitude-coach mock-placement ~/.codex/skills/
```

**Claude website (claude.ai)**

1. Zip each skill. In PowerShell, from the cloned folder:
   ```powershell
   'dsa-coach','cs-fundamentals','aptitude-coach','mock-placement' | ForEach-Object { tar -a -c -f "$_.zip" $_ }
   ```
   On Mac / Linux: `for s in dsa-coach cs-fundamentals aptitude-coach mock-placement; do zip -r $s.zip $s; done`
2. Open **Settings → Capabilities → Skills** and upload the four zip files.
3. Turn each skill on.

Skills need a plan that supports them, and the menu names may change.

**ChatGPT website and other AI chats (Gemini, Copilot and similar)**

These sites don't load skill folders. Use a Project (or custom GPT / Gem) instead:
1. Create a new Project and paste the contents of a skill's `SKILL.md` into its instructions.
2. Upload that skill's `modes` and `references` files to the Project.
3. Make one Project per skill.

**Other tools that support SKILL.md** (Cursor, Copilot, Gemini CLI): copy the four folders into that tool's skills folder. Check its docs for the path.

Only Claude Code has been tested. The other routes follow the SKILL.md format but are unconfirmed.

## What you can ask for

**DSA Coach**

| Mode | Example | What you get |
| --- | --- | --- |
| Coach | "Help me solve this: …" | One question at a time, with hints that unlock after you try |
| Learn | "Teach me sliding window" | Intuition, dry run, template, traps, practice ladder |
| Debug | "My code gives TLE: …" | The failing input and exact line, without rewriting your code |
| Explain-back | "Check my approach: …" | Your explanation graded against an interview rubric |
| Mock Interview | "Mock interview, medium, 45 min" | A full interview, a scorecard and a practice verdict |
| Pattern Drill | "Pattern drill, 10 questions" | Name the pattern from the problem statement alone |
| Placement | "Zoho round style, no library" | C or Java problems with no built-in helpers |
| Quick | "Quick: Two Sum" | Five lines for last-minute revision |

**Aptitude Coach and CS Fundamentals**

| Mode | Example | What you get |
| --- | --- | --- |
| Learn Shortcut | "Teach me time and work" | Formulas, shortcuts and solved examples |
| Practice | "10 percentage questions, medium" | One question at a time with instant explanation |
| Timed Test | "20 mixed questions, 25 minutes" | Answers only at the end, with section scores |
| Mistake Review | "Explain my mistakes" | The trick you missed and your weak topics |
| Company Pattern | "Zoho aptitude questions" | Sourced pattern, then practice questions in that pattern |

## How questions are checked

- Each question is solved before it's shown, and answers are solved again before marking.
- Code is used to check answers where the platform allows it. If code can't run, you're told the key wasn't executed.
- Every explanation shows its working, so you can check it.
- Company information comes with source links and dates. If there's no source, it says "no reliable data".

## Company questions

Questions are rewritten in new words with new numbers, then labelled with where they came from. They are practice questions, not actual papers: companies rarely repeat exact questions, and "previous year" lists online are often recycled or wrong. Copyrighted banks are linked, not copied.

## Limits

- Progress isn't tracked across chats.
- Chat can't run a real countdown, so you track the time yourself.
- Answers can still occasionally be wrong. Check the working, especially on questions marked as not executed.
- The hire or no-hire verdict is for practice only.

## Evaluation

The kit was tested by running fresh Claude Code sessions with scripted replies, not real students. The author graded the answers and is not a neutral judge. Quant, code, SQL and puzzle answers were checked by running code; blood-relation and verbal questions were judged by reasoning and could be wrong.

**With and without the kit (DSA, 15 problems)**

| Check | With kit | Without kit |
| --- | --- | --- |
| Holds back the code in the first reply | 14 / 15 | 0 / 14 |
| Complexity stated correctly | 15 / 15 | 14 / 14 |

**With the kit**

| Check | Result |
| --- | --- |
| Aptitude: answer key correct (30 questions) | 22 / 30 |
| Aptitude: exactly one valid option | 21 / 30 |
| CS: answer key correct (30 questions) | 19 / 30 |
| CS: exactly one valid option | 12 / 30 |
| Company data: nothing invented | 2 / 3 |
| Explain-back catches missing items | 2 / 3 |
| Right skill and mode for the prompt | 11 / 15 |

**What the results show**

- **Coach mode works.** Without the kit, all 14 sessions gave a full solution straight away. With it, 14 of 15 held the code back.
- **Most failures came from the skill not loading.** In the first run the aptitude and CS skills loaded in only 8 of 30 and 6 of 30 sessions, and every wrong key, missing correct option or open-ended question came from sessions where it hadn't.
- **The skill descriptions were rewritten to fix that.** On the 10 prompts that had failed, the re-test loaded the skill, gave the right key and had exactly one valid option every time (10 of 10, up from 0 of 10). This used new questions on the same prompts, chosen after the failures, so it is a before-and-after check and not a controlled test.

**Known gaps**

- Short prompts that paste code or an explanation sometimes don't load the skill: "My code gives TLE", "Check my approach", "Quick: Two Sum" and a pasted C snippet missed in the routing test. When the skill doesn't load, the kit's rules (for example, don't rewrite the student's code) don't apply.
- Asking which companies ask a given problem can still get a list from memory when web search is off, where the kit should say there is no reliable data.

- Answers can still be wrong. Check the working, especially on questions marked as not executed.

