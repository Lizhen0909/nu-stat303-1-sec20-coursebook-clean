---
title: "Chapter 2 Quiz: Your Python Environment and Project Files"
format:
  html:
    embed-resources: true
    toc: true
    number-sections: false
---

**Instructor copy for Canvas entry — correct answers are marked below.**

**Total: 20 points — Questions 1–4: 1 point each; Question 5: 16 points.**

Complete [Chapter 2’s Practice Activity](https://lizhen0909.github.io/nu-stat303-1-sec20-coursebook-clean/python_venv.html#practice-activity-find-your-python-and-your-data) before answering the quiz. That chapter section contains the complete activity and HTML preparation instructions. You may consult Chapter 2, your notebook, and your terminal. Choose **one best answer** for each multiple-choice question. The final question asks you to upload your own HTML report.

## Multiple-Choice Questions

### Question 1 — The Three Questions (1 point)

Before installing a package for this project, which set of checks best follows Chapter 2's three-question habit?

**A.** Check the notebook filename, the Python version number, and whether the last cell has output.

**B.** Check whether Explorer is open, whether the terminal has a prompt, and whether Pandas appears in an old notebook.

**C.** Check your shell name, whether the command is spelled correctly, and whether the notebook has been saved.

**D.** Check where you are typing, which Python executable the command will use, and the terminal's current folder. **(Correct answer)**


### Question 2 — Two Working Directories (1 point)

Your running notebook reports `stat303-setup` as its working directory. You enter `cd data` in the terminal and leave the terminal there. Without changing the notebook's directory, you rerun `Path.cwd()` in the notebook. Which observation is expected?

**A.** The terminal is inside `data`, while the notebook still reports `stat303-setup`. **(Correct answer)**

**B.** Both now report the `data` folder because they share a VS Code window.

**C.** The notebook reports `.venv` because its kernel comes from that folder.

**D.** The notebook's working directory becomes the folder containing the last file clicked in Explorer.


### Question 3 — Why Separate Environments? (1 point)

An older project needs version 1 of a library, while another project needs version 2. Both projects can use the same Python version. Which approach best fits Chapter 2?

**A.** Install version 2 in Anaconda `base`; newer library versions always support older projects.

**B.** Give each project its own environment and install a compatible set of packages in each. **(Correct answer)**

**C.** Give the projects different notebook filenames; that isolates their installed packages.

**D.** Create a separate environment for every notebook, including notebooks that belong to the same project and share requirements.


### Question 4 — Evidence That Python Matches (1 point)

Which result is the strongest evidence that your terminal and notebook are using the intended project environment?

**A.** Both display the same Python version number.

**B.** The terminal prompt includes `(.venv)` and the notebook kernel is labeled `Python 3`.

**C.** Both can import Pandas without an error.

**D.** The executable paths printed in the terminal and notebook identify the Python executable in the same project's `.venv`. **(Correct answer)**


## Question 5 — Upload Your Activity 2 HTML Report (16 points)

**Question type: File upload. Submit one file: `activity02.html`.**

Upload `activity02.html`, prepared by following the [Chapter 2 Practice Activity instructions](https://lizhen0909.github.io/nu-stat303-1-sec20-coursebook-clean/python_venv.html#practice-activity-find-your-python-and-your-data). Grading follows the criteria listed there.
