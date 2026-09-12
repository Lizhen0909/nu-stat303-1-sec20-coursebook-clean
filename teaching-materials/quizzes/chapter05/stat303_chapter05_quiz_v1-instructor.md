# Chapter 5 Quiz: NumPy Fundamentals — Instructor Key

Total: 20 points. Instructor-only; do not publish with student materials.

## Question 1: Preserving an axis

Correct answer: **B**. An integer column index removes that axis. A one-column slice preserves its length-one axis; both retain all three stores.

## Question 2: One multiplier per store

Correct answer: **C**. A (3, 1) factor array matches the three store rows and broadcasts along the four product columns. The other expressions have incompatible trailing sizes 4 and 3.

## Question 3: Interpreting totals

Correct answer: **A**. Summing along axis 1 removes the product axis and retains one total for each of the three stores.

## Question 4: Values, positions, and ties

Correct answer: **D**. max returns the value. With no axis, argmax returns the first flattened position at the maximum. argwhere(revenue == revenue.max()) can identify all tied coordinates.

## Final HTML upload — 16 points

Submit `activity05.html`; follow [Chapter 5 Practice Activity](https://lizhen0909.github.io/nu-stat303-1-sec20-coursebook-clean/Numpy.html#practice-activity-shapes-sales-and-search).

- **Shapes and selections (3 points):** 1 point: attributes and axis meanings; 1: predictions and results for integer versus sliced column selection; 1: first-two-store/last-two-product slice, shape, and explanation.

- **Broadcasting and units (4 points):** 1 point: units times prices with operand/result shapes; 1: dollar-unit and per-product explanation; 1: explains why (3, 4) times (3,) fails; 1: correct column-shaped factors, adjusted revenue, and per-store interpretation.

- **Summaries and min/max searches (4 points):** 1 point: unadjusted totals by store and product with names, shapes, and units; 1: minimum/maximum store positions, names, and totals; 1: maximum cell value and first coordinate using argmax/unravel_index; 1: all tied coordinates/names and value-versus-position/tie explanation.

- **Views, copies, and concatenation (4 points):** 1 point: correctly creates view and independent copy before edits and records predictions; 1: displays resulting arrays and explains source sharing versus original preservation; 1: correct row-shaped new-store concatenation from original units; 1: new shape/last row and explanations of matching dimensions and product order.

- **Readable completed HTML (1 points):** 0.5 point: name and readable code, results, and explanations; 0.5: completion note describing restart/run/save and HTML inspection. The report itself does not prove execution history.
