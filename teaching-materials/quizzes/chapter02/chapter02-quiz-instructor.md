# Instructor Guide — Chapter 2 Quiz

This is an instructor-only companion to `chapter02-quiz.md`. Do not include this file in the student practice kit or public course website.

## Suggested LMS Configuration

- Title: Chapter 2 Quiz: Your Python Environment and Project Files.
- Open-book individual practice; students complete Activity 2 before answering.
- 4 single-answer multiple-choice questions, 1 point each: 4 points.
- One final file-upload question, manually graded: 16 points.
- Total: 20 points.
- Use Chapter 2’s Practice Activity as the single source of student instructions. Paste the quiz introduction link into Canvas; do not copy the activity instructions into the quiz. Keep the upload question last.
- If supported, allow one `.html` upload and shuffle answer choices. Select correct answers by their text, not by their displayed letters after shuffling.
- Recommended feedback timing: release the answer key after the quiz closes. Set dates, attempts, and any time limit according to course policy; none is assumed in these files.
- The HTML quiz draft is an instructor copy with correct answers marked. When entering questions in Canvas, omit the visible answer markers and set the correct choices using Canvas quiz controls. It is not an LMS import package or an automatically graded quiz.

## Answer Key and Feedback

| Question | Answer | Rationale / feedback |
|---|---|---|
| 1 | D | The three checks establish input context, the Python executable, and current directory. Familiar labels or old output do not establish these facts. |
| 2 | A | Changing the terminal's directory does not change an already running notebook's working directory. Students should observe this while the terminal is still inside `data`. |
| 3 | B | Separate project environments can contain different package versions even when they use the same Python version. A new environment is not required for every notebook in the same project. |
| 4 | D | Executable paths identify the actual environments. Matching version numbers, generic kernel labels, prompts, or successful imports alone do not prove a match. |

## Question 5 Rubric — 16 Points

Award each item below independently. Grade the submitted HTML; no separate requirements-file upload is needed because students include its evidence in the report.

| Category | Points | Full-credit evidence and partial-credit rule |
|---|---:|---|
| Tools and command context | 2 | 1 point: identifies shell and explains a terminal use. 1 point: explicitly answers all three pre-installation questions with meaningful responses. |
| Environment and packages | 4 | 1 point: explains project isolation rather than sharing `base`. 1 point: supplies terminal and notebook executable paths identifying the course `.venv` and explains the match. 1 point: records appropriate terminal installation and notebook `%pip` commands. 1 point: successful visible NumPy, Pandas, Matplotlib, and Seaborn imports/version checks. |
| Navigation comparison | 3 | 1 point: commands/output establish the project directory and its listing. 1 point: enters `data`, lists the CSV, and shows the notebook directory while the terminal remains inside `data`, explaining the difference. 1 point: returns to the project directory and verifies it. |
| Paths and data | 3 | 1 point: correct relative path, resolved path, and successful real-file check. 1 point: recorded predictions and observations for real (`True`) and wrong (`False`) paths, plus a reasonable diagnostic check. 1 point: displays the first three CSV lines and explains that the relative path starts from the notebook process's working directory. |
| Dependencies | 2 | 1 point: correct export command and project-root file location. 1 point: two actual package/version entries with a correct explanation. |
| HTML and completion | 2 | 1 point: a named, readable HTML report containing code, output, and explanations. 1 point: records a successful restart/run-all/save check and has no unexplained execution errors or missing required code outputs. |
| **Total** | **16** | Award 0.5 points for a substantially correct but incomplete 1-point item; use 0 for absent or incorrect evidence. |

### Grading Notes

- Machine-specific usernames, absolute paths, Python versions, package versions, shell formatting, and requirements-file length will vary. Do not require exact matches to instructor examples.
- Accept the chapter's direct-executable method when activation is unavailable, provided the student's evidence identifies the correct project Python.
- A successful notebook kernel already demonstrates functioning kernel support; students need not explicitly import `ipykernel`.
- A correct multiple-choice answer does not replace evidence in the HTML. Grade the two parts separately.
- The supplied notebook uses a separate `wrong_path`; it does not require students to damage a real path or leave an intentional exception in the report.
- Navigation and installation happen outside notebook cells. Accept readable copied terminal text; do not require screenshots.
- A fresh-run statement is student-reported evidence. Consistent visible outputs support it, but an HTML file alone cannot prove the student's full execution history.
- For unreadable or incorrect-format uploads, follow the course's existing resubmission policy. No late-work or resubmission penalty is invented here.

## Alignment and Preparation

The existing `activity02.ipynb` provides four complete diagnostic code cells and two broad Markdown prompts. The canonical student instructions in Chapter 2 add labeled work requirements without changing that starter notebook: explicit three-question responses, an explanation of isolation, NumPy verification, a directory comparison while the terminal is inside `data`, path predictions, and requirements-file excerpts.

The final rendering step builds on the students' STAT201 Quarto experience. The Quarto refresher is included in Chapter 1, and the exact rendering command is provided in Chapter 2. The assessment does not require plotting, statistical analysis, or creating a second environment.

| Chapter skill | MCQ coverage | Report evidence |
|---|---|---|
| Terminal versus Python input | 1 | A–B |
| Three checks before commands | 1 | B |
| Directory navigation and independent processes | 2 | A, C |
| Project isolation and environment verification | 3, 4 | A–B |
| Package installation | Assessed through report | B |
| Relative paths and file checks | Assessed through report | D |
| Dependency records | Assessed through report | E |
| Fresh execution and HTML submission | Assessed through report | E and final upload |
