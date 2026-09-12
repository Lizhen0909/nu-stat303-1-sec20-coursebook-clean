# Reading Data: review and revision record

The initial review covered Reading_data.ipynb and the Chapter 1/2 setup practice sections and notebooks. The sections below record the issues identified before revision. Reading Data retains the published Chapter 3 quiz label; check book numbering and links when rebuilding the website.

## Priority 1: make every core example reproducible

- Standardize paths: the repository directory is `Datasets`, while the chapter uses `./datasets`, `../Data`, and `../data`. Case-sensitive systems will fail. Use one documented project layout and filenames that exist.
- The tab-delimited example reads `movie_ratings.txt`, which is absent; the repository contains `movies_tab.txt`. Correct both the ordinary and automatic-detection examples.
- Keep generated exports in a separate output folder, rather than overwriting instructional data files. Use a direct file existence check and a reimport check.
- Replace the reference to `movie_ratings['Rating']` with the actual `IMDB Rating` column.
- Refresh saved outputs after corrections. The book configuration disables notebook execution, so rendering does not test code or refresh stale results.

## Priority 2: correct explanations that can create misconceptions

- `read_csv()` infers types, but does not generally parse date columns automatically. Teach checking `dtypes`, then explicitly requesting date parsing when needed. Text dtype names can vary across pandas versions; do not grade a single spelling. [read_csv reference](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- A pandas index is a row-label axis, not necessarily a generated row-number column or a unique primary key. Explain the default RangeIndex separately from an index made from existing data. Explain why `set_index()` without assignment does not change the original in the shown example. [Indexing guide](https://pandas.pydata.org/docs/user_guide/indexing.html)
- Remove the claim that Series size is immutable; new labels can enlarge a Series. Describe one dimension and one dtype, rather than promising all elements are identical Python types. [Enlargement](https://pandas.pydata.org/docs/user_guide/indexing.html#setting-with-enlargement)
- Replace “always use index=False” with a decision: omit disposable row numbers, but preserve meaningful index identifiers when needed. [to_csv reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)
- Correct the claim that CSV files always use commas; inspect actual delimiters instead of trusting filename extensions. Distinguish tabular structure from the stronger claim that a table is relational merely because its rows describe movies.
- `info()` prints a summary and returns None. Teach students to call it directly. Avoid implying that a successful read or non-null counts establish overall data validity.
- `read_html(..., attrs=headers)` does not set request headers: `attrs` selects HTML tables. Use the request library's headers argument when fetching HTML, then parse the response, or supported storage options. Avoid promising that a User-Agent solves every 403. [read_html reference](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html)

## Priority 3: simplify the teaching sequence

Suggested order: learning objectives → inspect raw file and predict its table → read CSV → head/shape/columns → dtypes/info/describe → Series and default index → diagnose delimiter → export and read back → in-class practice. Keep the detailed method table as a reference, reducing repeated definitions and decorative print statements.

Move the lengthy CoinGecko/HTTP/Wikipedia helper into optional enrichment or a later data-acquisition lesson. Introduce JSON with a small local example before a remote URL. Stable local examples let students focus on parsing rather than network access and changing services. Web examples can remain useful enrichment.

Keep independent-study exercises, but clarify the album question: a mean of album-level mean track lengths and a track-weighted mean are different quantities. State which is intended and the necessary units. The HTML-table and remote JSON exercises should be explicitly separate from the required in-class activity.

## Implemented revision

Rebuilt the chapter around local files: setup → raw structure → CSV import → inspection → delimiter diagnosis → export and verification. Reduced executable cells to 18, removed repeated pandas introductions, and deferred detailed selection/index manipulation to later chapters. Replaced live web/API demonstrations with optional local JSON and HTML examples and a short explanation of web acquisition.

Corrected the index, dtype inference, delimiter, and HTML attributes explanations. All worked examples and activities use the downloadable kit's lowercase `data/` directory. Generated exports live beside the notebooks, leaving input files intact. The kit now includes a worked `reading_examples.ipynb`, the unfinished `activity03.ipynb`, both movie representations, small JSON/HTML previews, and unchanged album/book practice datasets.

Clarified the album-duration task as a track-weighted mean and retained the books file's extra index columns for diagnosis. The in-class activity remains the final chapter section, with the original stable anchor, A–D task list, rendering instructions, and 16-point upload rubric. The existing four MCQs and 16-point upload remain aligned; question IDs and grading were preserved.

Executed all 18 chapter cells in a fresh pandas 3.0.5 kernel, saved their outputs, and synchronized the downloadable examples. Separately checked the optional HTML parser against the JSON preview and verified the independent-practice datasets. The core notebook requires no network calls or HTML parser. A standalone local preview is available in `teaching-materials/reading-data-review/Reading_data.html`.

## Instructor expected results and validation

- Both local imports: 2,228 rows and 11 data columns; default row index excluded from shape's column count.
- IMDB Rating: 2,228 non-null values; mean about 6.2390; median 6.4 (50% row). Non-null counts do not establish validity.
- Selected rating column: Series with shape (2228,).
- In pandas 3.0.5, the semicolon file imported with default commas raises ParserError; the supplied diagnostic catches it. Accept an explained malformed-table result on other parser versions.
- Correct semicolon import equals the CSV import. Export with index=False preserves dimensions and column names. Default export introduces an extra `Unnamed: 0` column when read back with default settings.
- Checked data parsing and export with pandas 3.0.5, ZIP/source equality, and QTI packaging/scoring with the skill generator. These checks do not constitute an actual Canvas import test.

The quiz links to the newly added chapter anchor, which must be published with the student kit before students use the quiz. Instructor files and the answer-bearing QTI package belong outside the public website and student download ZIP. No publication, push, or Canvas import was performed.
