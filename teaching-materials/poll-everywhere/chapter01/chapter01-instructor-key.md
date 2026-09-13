# Chapter 1 — Instructor Key

Source: [vscode_setup.html](../../../docs/vscode_setup.html), Chapter 1, “Jupyter Notebooks in VS Code.” Quiz prepared from the local rendered chapter on 2026-09-12.

Format: Competition; 10 single-answer questions with four options each. Three warm-ups, five applications, and two reasoning questions follow the chapter’s teaching flow. Suggested response/discussion time totals 8 minutes; allow additional time for transitions and extended discussion.

Coverage: tool roles, project organization, extensions, kernel identity, Markdown, kernel state, Quarto availability, Raw-cell settings, saved outputs, and HTML portability. Chapter 2 environment creation and package installation are outside scope. The activity’s arithmetic is not separately assessed.

Source limitations: none affecting these questions. All items are supported by chapter text; no screenshot or linked external resource is needed to answer. This is a classroom engagement quiz, separate from the Canvas submission activity.

Import the CSV through Poll Everywhere’s Upload/import flow and review its preview before confirming. The JSON is the editable SU26 intermediate, not a native Poll Everywhere upload. The files have not been uploaded.

Answer sequence: B, D, A, C, A, D, B, C, A, B.

## 1. In the STAT303 workflow, which tool actually executes the Python code in a notebook?

**Correct answer: B.** The selected Python kernel

**Explanation:** The kernel is the running process that executes notebook code. VS Code provides the workspace; Quarto creates the report.

**Misconception diagnosed:** Confusing the editor, execution process, and rendered document.

**Source:** [1.1.1 Why We Use VS Code Throughout STAT303](../../../docs/vscode_setup.html#why-we-use-vs-code-throughout-stat303).

**Suggested timing:** 30 seconds (warm-up).

## 2. You have downloaded setup-practice.zip. How should you start working with its notebooks in VS Code?

**Correct answer: D.** Extract the ZIP and open the stat303-setup folder.

**Explanation:** Opening the extracted project folder keeps the notebooks, data, and supporting files together in Explorer.

**Misconception diagnosed:** Treating a notebook as independent of its surrounding project files.

**Source:** [1.2 Open a Project Folder](../../../docs/vscode_setup.html#open-a-project-folder).

**Suggested timing:** 30 seconds (warm-up).

## 3. Which pair of Microsoft extensions does Chapter 1 ask you to enable for Python notebooks in VS Code?

**Correct answer: A.** Python and Jupyter

**Explanation:** The chapter requires the Python and Jupyter extensions. The Quarto extension is optional for this workflow.

**Misconception diagnosed:** Confusing notebook support with optional editing tools.

**Source:** [1.3 Check Your VS Code Extensions](../../../docs/vscode_setup.html#check-your-vs-code-extensions).

**Suggested timing:** 30 seconds (warm-up).

## 4. Two installed environments have similar “Python 3” labels. Which notebook code best identifies the Python executable used by the current kernel?

**Correct answer: C.** import sys; print(sys.executable)

**Explanation:** sys.executable reports the executable path. A version number, printed label, or arithmetic result does not uniquely identify the installation.

**Misconception diagnosed:** Assuming a kernel label or Python version uniquely identifies an environment.

**Source:** [1.4 Select a Notebook Kernel and Run a Test Cell](../../../docs/vscode_setup.html#select-a-notebook-kernel-and-run-a-test-cell).

**Suggested timing:** 45 seconds (application).

## 5. Your mean calculation runs correctly. You want to add a heading and a paragraph explaining the result in the report. Where should you write them?

**Correct answer: A.** In a Markdown cell near the calculation

**Explanation:** Markdown cells hold narrative explanations and headings. Code cells perform computation; the supplied Raw cell holds report configuration.

**Misconception diagnosed:** Using a configuration cell or execution interface for report narrative.

**Source:** [1.5 Code, Markdown, and Saved Outputs](../../../docs/vscode_setup.html#code-markdown-and-saved-outputs).

**Suggested timing:** 45 seconds (application).

## 6. In a Python notebook, you ran x = 8 and then deleted that cell. A remaining cell contains print(x + 2). No other cell defines x. What happens when you run the remaining cell now, then restart the kernel and run it again?

**Correct answer: D.** It prints 10 first, then raises NameError.

**Explanation:** Deleting a cell does not remove x from the running kernel. Restarting clears that state; without an earlier assignment, x is undefined.

**Misconception diagnosed:** Believing that deleting a cell undoes its effects, or that variables survive a kernel restart.

**Source:** [1.5 Code, Markdown, and Saved Outputs](../../../docs/vscode_setup.html#code-markdown-and-saved-outputs).

**Suggested timing:** 60 seconds (application).

## 7. In the VS Code terminal, quarto --version prints a version number. The Quarto VS Code extension is not installed. What does this tell you about rendering from the terminal?

**Correct answer: B.** The terminal can find Quarto; the extension is optional for rendering.

**Explanation:** A version response confirms that this terminal can find the Quarto application. It does not test notebook execution or compare Python environments.

**Misconception diagnosed:** Treating the Quarto extension as the application, or interpreting an installation check as an execution check.

**Source:** [1.7.1 Check Your Existing Quarto Installation](../../../docs/vscode_setup.html#check-your-existing-quarto-installation).

**Suggested timing:** 45 seconds (application).

## 8. The supplied notebook starts with YAML settings for title, author, and HTML output. You need to put your name on the report. What should you do?

**Correct answer: C.** Edit author in the existing Raw cell, preserving indentation and the --- lines.

**Explanation:** The report settings are YAML configuration in the supplied Raw cell. Preserve their structure while changing the author field.

**Misconception diagnosed:** Treating YAML as Python or ordinary Markdown instead of report configuration.

**Source:** [1.7.2 Keep the Template’s Report Settings](../../../docs/vscode_setup.html#keep-the-templates-report-settings).

**Suggested timing:** 45 seconds (application).

## 9. A saved notebook shows an old result. You change its calculation, save without rerunning, and successfully render the .ipynb using the chapter’s default Quarto workflow. Which conclusion is justified?

**Correct answer: A.** The HTML may still show the old result because rendering normally uses saved outputs.

**Explanation:** By default, Quarto renders saved notebook outputs without rerunning code. Restart, run all cells in order, save, render, and inspect to update and check the report.

**Misconception diagnosed:** Equating successful rendering or saving with fresh code execution.

**Source:** [1.7.3 Restart, Run All, Save, Render, Inspect](../../../docs/vscode_setup.html#restart-run-all-save-render-inspect).

**Suggested timing:** 75 seconds (reasoning).

## 10. Your report uses embed-resources: true. A copy of only the HTML opens in another folder with its ordinary figures and formatting intact. What has this check established?

**Correct answer: B.** The copied HTML carries the ordinary display resources checked, but you should keep the notebook and data for future work.

**Explanation:** Embedding resources helps ordinary figures and styling travel with the HTML. It does not package the Python environment or input data, and external services can still need internet access.

**Misconception diagnosed:** Confusing a portable report with a complete reproducible analysis environment.

**Source:** [1.7.2 Keep the Template’s Report Settings; 1.8.1 Render and Submit Your HTML](../../../docs/vscode_setup.html#keep-the-templates-report-settings).

**Suggested timing:** 75 seconds (reasoning).

Also see [1.8.1 Render and Submit Your HTML](../../../docs/vscode_setup.html#render-and-submit-your-html).
