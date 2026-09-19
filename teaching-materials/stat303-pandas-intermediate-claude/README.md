# Pandas Intermediate Practice Kit

Open this folder inside your existing stat303-setup project and select its verified Python environment. pandas is the only analysis dependency. All inputs are created in Python. Use pandas_intermediate_examples.ipynb for the lesson and activity05.ipynb for your report.

## Practice Activity: Calculate, Align, and Explain {#practice-activity-calculate-align-and-explain}

**Goal:** Build and explain a small store report using labeled transformations. **File:** `activity05.ipynb` from the practice kit. **Submit:** `activity05.html` through the final upload question in the Pandas Intermediate Canvas quiz when assigned.

**This section contains the complete activity instructions.** The starter supplies invented inputs and spaces for your work, without completed solutions. Work in the extracted `stat303-pandas-intermediate-claude` folder with the verified project environment. The worked examples are preparation, not additional submission requirements.

### A. Calculate with Explicit Inputs

- Replace `Your Name` in the opening Raw cell's `author` field. Run the setup check; it must report `True`. Run the supplied input DataFrames and explain what one row of `sales` represents.
- Preserve `sales` and create a working copy named `report`. Calculate `Revenue = Units * Price`, `Cost = Units * Unit_Cost`, and `Gross_Profit = Revenue - Cost`.
- Copy `quarter_sales` to `quarters` and leave `quarter_sales` itself unchanged for Part B. In `quarters`, name the input columns explicitly as `['Q1', 'Q2']` and calculate each product's total and average. Display the result, and explain why calculating the average after adding the total column would give the wrong answer.
- Interpret one gross-profit value in dollars. These inputs exclude other business expenses; explain why the calculated value is not net profit.

### B. Predict and Check Alignment

- Before executing `quarter_sales + adjustments`, predict the row and column labels of the result and the value at row `P10`, column `Q2`.
- Run the addition and explain two cells that came out as `NaN`, using the labels of both input DataFrames.
- For this exercise, assume an absent adjustment means zero and an absent base-sales record means zero recorded sales. Use `.add(..., fill_value=0)` and compare with the ordinary addition. Identify the cells that are still `NaN` and explain why.
- Reverse the rows of `adjustments` and repeat the calculation. Explain why label-matched results stay the same.

### C. Recode and Apply a Rule

- Map `report['Department']` using the supplied `department_labels`. Display the result and say which department came out as `NaN` and why.
- Use the same dictionary with `.replace()` and explain how its result differs from `.map()` for that department.
- Write a named row function returning `Review` if gross profit is negative, `High Volume` if units are at least 20 and profit is nonnegative, and `Standard` otherwise. Apply it with `axis=1`, keep the result as `Status`, and display product, gross profit, and status.
- Use column arithmetic to calculate a price discounted by 10%, and explain why `apply()` is unnecessary for it. Then write a one-line lambda with `apply()` for a rule plain arithmetic cannot express: label each product `Premium` when its price is at least 6 dollars and `Budget` otherwise.

### D. Interpret a Relationship

- Use the supplied six-row `campaigns` DataFrame. Calculate the Pearson correlation between `Advertising` and `Revenue`.
- Interpret its sign and strength as a linear association for these invented observations. Explain why it does not establish that advertising caused revenue to change.
- Finish with one or two sentences about a label check that mattered in your report: a place where you confirmed which rows or columns a calculation matched.

### Render and Submit

Restart the kernel, run all cells in order, resolve errors, and save. Add a short Markdown completion note, then save again. From `stat303-pandas-intermediate-claude` in the terminal, run:

```text
quarto render activity05.ipynb --to html
```

Follow the Quarto refresher: inspect the HTML and a copy opened outside the project folder. Check your name, predictions, code, outputs, and explanations for A–D. When assigned, upload only `activity05.html` to the Pandas Intermediate Canvas quiz; keep your notebook locally.

**HTML grading (16 points):** calculated variables, explicit inputs, and units (4); alignment and justified `fill_value` choices (4); recoding and custom logic (4); correlation and interpretation (3); name, readable report, and completion note (1).
