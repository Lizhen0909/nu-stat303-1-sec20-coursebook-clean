# Pandas chapter coverage after restoration

This map compares the original Pandas Fundamentals chapter (before the focused Chapter 4 revision) with the restored lesson. It records where substantive topics are taught, rather than reproducing every heading or printed output.

| Original material | Current destination |
|---|---|
| Ecosystem, capabilities, external sources | Chapter 4 introduction and constructors; file readers remain in Reading Data |
| Series from lists and dictionaries; DataFrames from columns and records | Chapter 4: Create a Series from a List or Dictionary; Create a DataFrame by Columns or by Records |
| Single/multiple columns, Boolean conditions, negation, membership | Chapter 4: Select Columns and Filter Rows |
| Labels, positions, slices, combined row/column selection | Chapter 4: Distinguish Labels from Positions |
| Extreme values, labels, positions, ties | Chapter 4: Extreme Value Versus Record Containing It |
| Single/multiple sorting keys, index sorting, top/bottom N | Chapter 4: Sort Movies and Find Extremes |
| Basic ranking | Chapter 4: Basic Ranking and Ties |
| All ranking methods and percentile ranks | Chapter 6: Ranking Conventions and Percentiles |
| Custom sorting with functions | Chapter 6: Custom Sorting Keys, after lambda coverage |
| Adding, inserting, renaming, removing columns; removing rows | Chapter 4: Create Columns and Make Reliable Updates |
| Dtype reference, inspection, select_dtypes, astype, conversion | Chapter 4: Convert Text and Dates with Checks |
| String cleaning and matching | Chapter 4 core examples; Chapter 6: Extended Strings, Dates, and Durations |
| Datetime components and elapsed time | Chapter 4 date parsing/year/duration; Chapter 6 quarter, weekday, ISO year/week, and duration examples |
| Numerical summaries, quantiles, standard deviation, axes | Chapter 4: Summarize Values and Define Denominators |
| inplace behavior and retained return values | Chapter 4 core explanation; Chapter 6 copy/alias example and memory interpretation |
| Performance comparisons | Chapter 6: Measure Performance and Understand Copies; blanket speed rankings corrected |
| Album and survey exercises | Chapter 4: Independent Practice, with scaffolding and corrected metrics/denominators |
| In-class assessment | Chapter 4 practice activity and existing Canvas quiz unchanged |

Repeated prose and large repetitive outputs were consolidated. Unsupported performance guarantees, the misleading profit interpretation, and incorrect exercise calculations were not restored. The independent exercises remain student tasks rather than fully worked answers.

Validation: all 41 Chapter 4 code cells and all 7 new Chapter 6 extension code cells executed in fresh kernels with pandas 3.0.5. Existing Chapter 6 examples outside these extensions were not re-executed. The downloadable worked notebook is synchronized with Chapter 4; the activity starter and activity instructions are unchanged.
