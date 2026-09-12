# Chapter 1 Quiz: Jupyter Notebooks in VS Code — Instructor Key

Total: 20 points. Instructor-only; do not publish with student materials.

## Question 1: Open the practice project

Correct answer: **B**. Opening the extracted project folder keeps the notebook and related files together and visible in Explorer. The Python installation folder is not the project folder.

## Question 2: Verify the notebook Python

Correct answer: **D**. Workspace interpreter selection and notebook kernel selection are separate. The executable path printed by the notebook verifies which Python actually runs its cells. Chapter 1 uses a familiar existing environment, not a required new .venv.

## Question 3: Choose the right cell type

Correct answer: **A**. Markdown cells provide formatted narrative and headings. Code cells perform computations. Terminal text is not automatically saved as notebook content.

## Question 4: Check that the notebook runs from the beginning

Correct answer: **C**. A running kernel can retain values from deleted cells, and a notebook can retain saved output. Restarting and running all cells checks that the current notebook includes the definitions it needs.

## Final HTML upload — 16 points

Submit `activity01.html`; follow [Chapter 1 Practice Activity](https://lizhen0909.github.io/nu-stat303-1-sec20-coursebook-clean/vscode_setup.html#practice-activity-your-first-vs-code-notebook).

- **Name and readable Markdown (2 points):** 1 point for the student name in the notebook/report; 1 point for explanations displayed as readable Markdown text. Do not require the name to appear in a particular metadata field.

- **Python identification (4 points):** 2 points for visible output from the supplied environment-information cell (Python version, executable, and working directory); 2 points for a Markdown sentence identifying the selected Python installation consistently with the output. Accept the familiar working STAT201 environment; do not require .venv or any fixed Python version or path.

- **Mean calculation (4 points):** 1 point for defining a list of three numerical readings; 2 points for computing their mean using sum() and len(); 1 point for a visible correct result for the student’s chosen values. The example readings are not mandatory.

- **Explanation of code and kernel (4 points):** 2 points for explaining how the code computes the mean; 2 points for distinguishing the notebook document from the kernel process that executes its code and retains values. Award 1 point within each component for a partially correct explanation.

- **Completion and submitted HTML (2 points):** 1 point for the starter notebook’s requested record of restart/run-all and reopening checks; 1 point for a readable HTML file containing the completed code and outputs without unexplained execution errors. Treat the fresh-run record as student-reported evidence, not proof of execution history.
