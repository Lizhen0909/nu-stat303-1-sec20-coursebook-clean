# Reading Data practice kit

Use the [Reading Data chapter](https://lizhen0909.github.io/nu-stat303-1-sec20-coursebook-clean/Reading_data.html) for the lesson and its [complete activity instructions](https://lizhen0909.github.io/nu-stat303-1-sec20-coursebook-clean/Reading_data.html#practice-activity-read-inspect-and-export-movie-data) for the graded task list.

## Open and run

1. Extract this folder and place it inside the existing `stat303-setup` project.
2. Select the project Python environment verified in the setup chapters. The core examples and activity need pandas; no NumPy knowledge or additional package installation is required.
3. Use `stat303-reading-data` as the notebook's working directory. Both notebooks belong beside the lowercase `data/` folder. Use `Path.cwd()` and the supplied file check to verify the location.
4. Run `reading_examples.ipynb` to follow the worked examples. Complete your own `activity03.ipynb` using the chapter's A–D instructions.
5. Restart, run all, and save your activity. From this folder in the terminal, run `quarto render activity03.ipynb --to html`. Inspect the result and upload only `activity03.html` to the Canvas quiz.

The examples write `movies_export.csv` and `movies_with_index.csv` beside the notebooks. Rerunning an export replaces that generated file; the inputs under `data/` are not modified. The activity also writes `movies_export.csv` from the same original dataset.

The HTML-reading extension is optional and needs an HTML parser such as lxml. Its code is shown in Markdown, so running all ordinary example cells does not require that parser or network access. The local JSON example uses pandas alone.

## Included data and provenance

- `movie_ratings.csv`: unchanged copy of the course repository's `Datasets/movie_ratings.csv`, containing 2,228 historical movie records and 11 columns.
- `movie_ratings_semicolon.txt`: the same header and records, serialized with semicolons using Python's csv module.
- `movies_preview.json` and `movies_preview.html`: the first five movie records, restricted to Title, IMDB Rating, and Production Budget. Rating and budget were converted to numerical values when constructing the previews. These files demonstrate equivalent small tables in two formats.
- `Top 10 Albums By Year.csv` and `bestseller_books.txt`: unchanged copies of the corresponding course datasets, provided for independent practice. The books file retains its original extra index columns for diagnosis.

These are historical teaching datasets, not current movie ratings, rankings, or sales figures. Only the two full movie files are required for the in-class activity. The example notebook includes the chapter text; the activity notebook intentionally contains unfinished student work rather than worked solutions.
