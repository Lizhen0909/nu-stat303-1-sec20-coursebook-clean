# Pandas Intermediate Practice Kit

Open this folder inside your existing stat303-setup project and select its verified Python environment. pandas is the only analysis dependency. All inputs are created in Python. Use pandas_intermediate_examples.ipynb for the lesson and activity_pandas_intermediate.ipynb for your report.

## Practice Activity: Calculate, Align, and Explain {#practice-activity-calculate-align-and-explain}

**Goal:** Build and explain a small store report using labeled transformations. **Time:** approximately 35–45 minutes. **File:** `activity_pandas_intermediate.ipynb` from the practice kit. **Submit:** `activity_pandas_intermediate.html` through the final upload question in the Pandas Intermediate Canvas quiz when assigned.

**This section contains the complete activity instructions.** The starter supplies invented inputs and spaces for your work, without completed solutions. Work in the extracted `stat303-pandas-intermediate-claude` folder with the verified project environment. The worked examples are preparation, not additional submission requirements.

### A. Calculate with Explicit Inputs

- Replace `Your Name` in the opening Raw cell and Markdown name field. Run the setup check; it must report `True`. Run the supplied input tables and explain what one row of `sales` represents.
- Preserve `sales` and create a working copy named `report`. Calculate `Revenue = Units * Price`, `Cost = Units * Unit_Cost`, and `Gross_Profit = Revenue - Cost`.
- From only `Q1` and `Q2` in `quarter_sales`, calculate each product's total and average. Display the results. Explain why averaging a table after adding its total would give the wrong average.
- Interpret one gross-profit value in dollars. These inputs exclude other business expenses; explain why the calculated value is not net profit.

### B. Predict and Check Alignment

- Before executing `quarter_sales + adjustments`, predict the row and column labels of the result and the value at row `P10`, column `Q2`.
- Run the addition and explain two missing result cells using the labels of both input tables.
- For this exercise, assume an absent adjustment means zero and an absent base-sales record means zero recorded sales. Use `.add(..., fill_value=0)` and compare with the ordinary addition. Identify any cell still missing and explain why.
- Reverse the rows of `adjustments` and repeat the calculation. Explain why label-matched results stay the same.

### C. Recode and Apply a Rule

- Map `report['Department']` using the supplied `department_labels`. Display unmatched departments before deciding what to do with them.
- Use the same dictionary with `.replace()` and explain how its result differs from `.map()` for the unmatched department.
- Write a named row function returning `Review` if gross profit is negative, `High Volume` if units are at least 20 and profit is nonnegative, and `Standard` otherwise. Apply it with `axis=1`, keep the result as `Status`, and display product, gross profit, and status.
- Use column arithmetic to calculate a price discounted by 10%. Explain why a lambda with `apply()` is unnecessary for this calculation.

### D. Interpret a Relationship

- Use the supplied six-row `campaigns` table. Calculate the Pearson correlation between `Advertising` and `Revenue` and report the number of paired observations.
- Interpret its sign and strength as a linear association for these invented observations. Explain why it does not establish that advertising caused revenue to change.
- Finish with a short paragraph describing a label check and a missing-value check that mattered in your report.

### Render and Submit

Restart the kernel, run all cells in order, resolve errors, and save. Add a short Markdown completion note, then save again. From `stat303-pandas-intermediate-claude` in the terminal, run:

```text
quarto render activity_pandas_intermediate.ipynb --to html
```

Follow the Quarto refresher: inspect the HTML and a copy opened outside the project folder. Check your name, predictions, code, outputs, and explanations for A–D. When assigned, upload only `activity_pandas_intermediate.html` to the Pandas Intermediate Canvas quiz; keep your notebook locally.

**HTML grading (16 points):** calculated variables, explicit inputs, and units (4); alignment and justified missing-value handling (4); recoding and custom logic (4); correlation and interpretation (3); name, readable report, and completion note (1).
