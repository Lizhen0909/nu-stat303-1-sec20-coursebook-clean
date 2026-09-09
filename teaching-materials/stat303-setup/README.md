# STAT 303-1 setup practice kit

Extract this entire folder and open stat303-setup in VS Code. Keep the four notebooks beside data/. Do not work inside the ZIP viewer. The textbook provides the instructions for each activity and the integrated assignment.

- activity01.ipynb: notebook/editor practice with an existing Python environment.
- activity02.ipynb: after creating .venv and installing packages, verify Python and local data.
- activity03.ipynb: run, save, and render a report with Quarto.
- setup_assignment.ipynb: complete all written sections and the provided computational workflow; submit setup_assignment.html according to the instructor's directions.

The six temperature records are illustrative. Create your .venv and requirements.txt locally; neither is supplied. Use the same verified project kernel for activities 2–3 and the integrated assignment. Packages: ipykernel, numpy, pandas, matplotlib, seaborn.

All notebook outputs are initially empty. Run and save the notebook before rendering. From this folder:

    quarto render setup_assignment.ipynb --to html

Quarto is a separately installed application. The template embeds ordinary assets into HTML. Copy the rendered HTML alone to a separate folder and inspect it. Keep your notebook/data/requirements for reproducibility, but do not submit .venv. The templates contain work areas, not completed student answers.
