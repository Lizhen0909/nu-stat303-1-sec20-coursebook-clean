# STAT 303 — Chapter 2 instructor key

**Project Environments, Packages, and File Paths**

10 single-answer multiple-choice questions; four choices each. Competition format. Suggested response time: 8 minutes 45 seconds total, plus roughly 5–8 minutes for discussion. Questions follow the chapter’s progression and emphasize setup misconceptions over command memorization.

Source: [Chapter 2](../../docs/python_venv.html), local coursebook HTML read on September 12, 2026. Links below resolve from the course repository quiz folder.

Coverage: prompts and navigation (Q1–2), isolation and environment verification (Q3–5), installation versus session state (Q6–7), dependency recreation (Q8), relative paths and missing-file diagnosis (Q9–10). These are original engagement questions, not the chapter’s Canvas assessment or submission instructions. All items are text-only and supported by chapter prose; no diagram is required.

Import `chapter-02-quiz.csv` through Poll Everywhere’s Upload page, review the preview and marked answers, then confirm. The JSON is the editable source. No live import has been performed.

## Question 1

You want to run the shell command cd data, but the terminal prompt is >>>. What should you do first?

A. Type cd data after >>>
B. Type exit() to return to the shell
C. Create another virtual environment
D. Restart the notebook kernel

**Correct: B — Type exit() to return to the shell**

**Explanation:** The >>> prompt identifies an interactive Python session. exit() returns to the shell, where cd belongs.

**Misconception:** Treating every terminal prompt as a shell prompt.

**Source:** [2.1.1 Read the Prompt and Enter a Command](../../docs/python_venv.html#read-the-prompt-and-enter-a-command)

**Response time:** 30 seconds. Ask students to explain why a tempting distractor fails before moving on.

## Question 2

A terminal and a running notebook both start in stat303-setup. You run cd data only in the terminal. What happens?

A. Both working directories change to stat303-setup/data
B. The CSV file moves into the notebook folder
C. The terminal stays in stat303-setup until the notebook restarts
D. Only the terminal working directory changes

**Correct: D — Only the terminal working directory changes**

**Explanation:** cd changes the terminal’s location. It neither moves files nor changes an already running notebook’s working directory.

**Misconception:** Assuming that the terminal and notebook share one working directory.

**Source:** [2.3 Navigate in the Terminal](../../docs/python_venv.html#navigate-in-the-terminal)

**Response time:** 45 seconds. Ask students to explain why a tempting distractor fails before moving on.

## Question 3

Two projects need incompatible versions of the same library. How do separate virtual environments help?

A. Each project can keep its own compatible package versions
B. They make incompatible versions work together inside one environment
C. They force both projects to use the newest library version
D. They remove the need to install packages

**Correct: A — Each project can keep its own compatible package versions**

**Explanation:** Environment isolation keeps one project’s installed packages separate from another’s. It does not resolve incompatibilities within a single environment.

**Misconception:** Confusing isolation between projects with compatibility within one project.

**Source:** [2.5.2 Give Each Project Its Own Environment](../../docs/python_venv.html#give-each-project-its-own-environment)

**Response time:** 45 seconds. Ask students to explain why a tempting distractor fails before moving on.

## Question 4

On macOS, a terminal uses /course/A/.venv/bin/python, but the notebook uses /course/B/.venv/bin/python. A terminal package installation succeeds and the notebook import fails. What should you check first?

A. Whether both environments are named .venv
B. Whether the CSV is in the data folder
C. Whether both use the intended project’s Python executable
D. Whether the notebook has been exported to HTML

**Correct: C — Whether both use the intended project’s Python executable**

**Explanation:** These are different project environments despite the same .venv folder name. Compare the full sys.executable paths, select the intended environment, and install there if needed.

**Misconception:** Using an environment label or folder name as proof that two Python installations match.

**Source:** [2.6.3 Restart the Terminal and Verify Both Places; 2.7.3 Install Once, Import in Every Notebook](../../docs/python_venv.html#restart-the-terminal-and-verify-both-places)

**Response time:** 60 seconds. Ask students to explain why a tempting distractor fails before moving on.

## Question 5

In the project folder, python -m venv .venv succeeds using an installed Python. What should you expect?

A. It downloads the newest Python release and all course packages
B. It creates an environment based on that Python; course packages still need installation
C. It copies every package from every other environment
D. It automatically makes all existing notebooks use the new environment

**Correct: B — It creates an environment based on that Python; course packages still need installation**

**Explanation:** venv uses an already installed interpreter. Creating the environment does not install the data science packages or guarantee that notebooks select it.

**Misconception:** Equating environment creation with package installation and kernel selection.

**Source:** [2.5.2 Give Each Project Its Own Environment; 2.6.2 Method 2: Create .venv in the Terminal](../../docs/python_venv.html#method-2-create-.venv-in-the-terminal)

**Response time:** 45 seconds. Ask students to explain why a tempting distractor fails before moving on.

## Question 6

Pandas is installed in the selected project environment. You restart the notebook kernel. What is normally needed before using pd again?

A. Create a new .venv folder
B. Install Pandas again
C. Copy Pandas into the notebook folder
D. Rerun import pandas as pd

**Correct: D — Rerun import pandas as pd**

**Explanation:** Installed packages remain on disk. Restarting the kernel clears session state, including imported names, so rerun the import cell.

**Misconception:** Confusing persistent installation with imports in a running session.

**Source:** [2.7.3 Install Once, Import in Every Notebook](../../docs/python_venv.html#install-once-import-in-every-notebook)

**Response time:** 45 seconds. Ask students to explain why a tempting distractor fails before moving on.

## Question 7

You run %pip install seaborn in a VS Code notebook code cell. Which environment receives Seaborn?

A. The environment used by the notebook’s selected kernel
B. Every Python environment on the computer
C. The environment used by any open terminal
D. The folder containing the CSV file

**Correct: A — The environment used by the notebook’s selected kernel**

**Explanation:** The notebook %pip magic installs into the environment running the notebook. Verify the selected kernel before installing.

**Misconception:** Assuming a notebook installation follows a terminal’s environment or affects every environment.

**Source:** [2.7.2 Method 2: Install from the Notebook](../../docs/python_venv.html#method-2-install-from-the-notebook)

**Response time:** 45 seconds. Ask students to explain why a tempting distractor fails before moving on.

## Question 8

A classmate has created and activated a new compatible environment and received your requirements.txt. Which command installs its listed packages?

A. python -m pip freeze
B. python -m venv requirements.txt
C. python -m pip install -r requirements.txt
D. python requirements.txt

**Correct: C — python -m pip install -r requirements.txt**

**Explanation:** pip install -r reads package requirements and installs them. pip freeze reports installed packages; it does not install them. Share the Python version along with the requirements file.

**Misconception:** Confusing recording dependencies with recreating them.

**Source:** [2.8 Record and Recreate Dependencies](../../docs/python_venv.html#record-and-recreate-dependencies)

**Response time:** 60 seconds. Ask students to explain why a tempting distractor fails before moving on.

## Question 9

A project contains sibling folders notebooks and data. The CSV is in data. If the notebook’s current working directory is project/notebooks, which path reaches the CSV? Assume Path has been imported from pathlib.

A. Path("data") / "station_readings.csv"
B. Path("..") / "data" / "station_readings.csv"
C. Path("notebooks") / "data" / "station_readings.csv"
D. Path("station_readings.csv")

**Correct: B — Path("..") / "data" / "station_readings.csv"**

**Explanation:** A relative path starts at the current working directory. .. moves from notebooks to the project folder, and data then enters its sibling folder.

**Misconception:** Treating a relative path as relative to the visible workspace root regardless of the running directory.

**Source:** [2.9.1 What Changes When the Working Directory Changes?](../../docs/python_venv.html#what-changes-when-the-working-directory-changes)

**Response time:** 90 seconds. Ask students to explain why a tempting distractor fails before moving on.

## Question 10

For data_path = Path("data") / "station_readings.csv", resolve() displays an absolute path but is_file() returns False. What is the best next step?

A. Use resolve() again to create the missing CSV
B. Assume the file exists because the path is absolute
C. Reinstall Pandas before checking the folders
D. Check Path.cwd(), the filename, capitalization, and folder layout

**Correct: D — Check Path.cwd(), the filename, capitalization, and folder layout**

**Explanation:** An absolute path describes a location; it does not prove that a file exists there. The failed file check calls for inspecting the actual directory and file layout.

**Misconception:** Mistaking path construction or resolution for file discovery or creation.

**Source:** [2.9 Find Local Data with Paths](../../docs/python_venv.html#find-local-data-with-paths)

**Response time:** 60 seconds. Ask students to explain why a tempting distractor fails before moving on.
