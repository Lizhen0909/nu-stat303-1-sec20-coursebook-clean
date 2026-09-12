# Chapter 3 Quiz: Reading Data — Instructor Key

Total: 20 points. Instructor-only; do not publish with student materials.

## Question 1: Interpreting dimensions

Correct answer: **A**. shape reports data rows and columns, excluding the index.

## Question 2: Selecting a variable

Correct answer: **C**. Selecting one named column with a single pair of brackets produces a Series.

## Question 3: Diagnosing an import

Correct answer: **B**. The semicolon delimiter must be parsed; a successful function call alone does not prove the table was read correctly.

## Question 4: Preserving the intended columns

Correct answer: **D**. index=False omits the row index; meaningful IDs stored in an index would need to be preserved when required.

## Final HTML upload — 16 points

Submit `activity03.html`; follow [Chapter 3 Practice Activity](https://lizhen0909.github.io/nu-stat303-1-sec20-coursebook-clean/Reading_data.html#practice-activity-read-inspect-and-export-movie-data).

- **Import and dataset interpretation (3 points):** 1 point: correct CSV import and requested previews; 1: correct shape/column evidence; 1: observation, variables, and index interpretation.

- **Inspection and Series explanation (5 points):** 1 point: dtypes and info output; 1: non-null count interpreted against total rows; 1: describe output with correct rating mean and median; 1: Series type/shape and explanation; 1: head limitation and attribute/method distinction (0.5 each).

- **Delimiter diagnosis and correction (4 points):** 1 point: raw preview and prediction; 1: default-import evidence interpreted; 1: correct explicit separator and successful import; 1: dimension/column comparison with CSV.

- **Export and verification (3 points):** 1 point: export with index=False and successful reimport; 1: visible structural checks interpreted; 1: default-row-number prediction and meaningful-ID explanation (0.5 each).

- **Readable completed HTML (1 points):** 0.5 point: name and organized code, outputs, and Markdown; 0.5: completion note describing fresh run, save, and HTML inspection. HTML alone does not prove execution history.
