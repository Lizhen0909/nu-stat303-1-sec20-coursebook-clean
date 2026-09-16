# Pandas and NumPy Workflow practice kit

Follow [Pandas and NumPy in a Data Science Workflow (Chapter 8)](https://lizhen0909.github.io/nu-stat303-1-sec20-coursebook-clean/pandas_numpy_workflow.html)
and its [complete activity instructions](https://lizhen0909.github.io/nu-stat303-1-sec20-coursebook-clean/pandas_numpy_workflow.html#practice-activity-from-messy-file-to-labeled-report).

Extract this folder inside your stat303-setup project and select its verified
environment. NumPy and pandas are required. Use this folder as the notebook
working directory.

- workflow_examples.ipynb matches the worked chapter stage by stage, with saved outputs. It differs from the published chapter in one place only: it reads `data/store_transactions.csv` directly, where the chapter writes the same table to a temporary folder so it renders anywhere. Its coursebook links open the published textbook.
- activity06.ipynb is an unfinished student starter; complete the chapter's A-E tasks. Its first cell builds every input the activity needs, including writing `inventory_raw.csv` into this folder, so no extra data file ships for it. Activity 6 is the filename/activity label, while Pandas and NumPy in a Data Science Workflow is Chapter 8 in the current book.
- data/store_transactions.csv is the table used by the worked stages. Two records have unusable `units` on purpose: order 1008 is blank and order 1010 reads `unknown`. Both become `NaN`, and the chapter uses them to show why that difference is yours to interpret.

The chapter and this kit deliberately stay within the tools of the earlier
chapters: `.to_numpy()`, `pd.to_numeric()`, `pd.to_datetime()`, `.astype()`,
Boolean masks, `np.where()`, `np.select()`, broadcasting, `axis` aggregations, the
`@` matrix product, and `%timeit`. There is no `groupby` or `pivot_table` here,
since neither has been introduced yet.

Restart the activity kernel, run all cells, save, and run
`quarto render activity06.ipynb --to html`. Inspect the HTML and a copy opened
outside the project folder, then submit activity06.html. The chapter is the
single source of activity and grading instructions.

All stores, orders, warehouses, prices, and discount rules are synthetic teaching
data. The timing numbers saved in workflow_examples.ipynb came from one machine;
your own measurements will differ, which is the reason the chapter asks you to
measure rather than to memorize a ratio.
