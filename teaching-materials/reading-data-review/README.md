# Reading Data local review

`Reading_data.html` is a standalone preview of the revised chapter, including refreshed outputs. Its practice-kit link targets the local ZIP. Links to other chapters target the published book. This preview is not the public website and does not reproduce full-book chapter numbering or navigation.

## Source and execution

The authoritative chapter is the root `Reading_data.ipynb`. Its code is designed to run with `teaching-materials/stat303-reading-data` as the working directory, matching the downloadable folder students open. Run the notebook with that working directory, or run the synchronized `reading_examples.ipynb` inside the kit. Preserve the source's saved outputs when rendering the book, consistent with the existing `_quarto.yml` configuration.

The worked notebook copy has the same code and outputs as the chapter; it uses absolute links to other published chapters and enables embedded HTML resources for standalone rendering. Its Markdown otherwise follows the source. The activity notebook is unfinished student work. Rebuild `downloads/reading-data-practice.zip` from only `teaching-materials/stat303-reading-data/` after changing any kit files; exclude generated exports and rendered reports.

## Verification

- All 18 executable source cells ran in order in a fresh kernel with pandas 3.0.5.
- Both movie imports and CSV export/reimport checks passed.
- Local JSON and optional HTML previews agree (five rows, three columns).
- Album and book files were read successfully with their documented tasks checked.
- Canvas QTI package validated locally: four MCQs and one manual upload, 20 points.
- No website publication or Canvas import was performed.
