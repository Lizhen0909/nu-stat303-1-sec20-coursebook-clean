# NumPy Fundamentals coverage and validation

The revision preserves the original first figure and all major topic groups: motivation and memory, timed dot product, constructors and file-reader reference, pandas conversion, attributes and dtypes, indexing and slicing (including 3D), Boolean masks, where/select, extrema and top-N selection, arithmetic and broadcasting, reductions, reshape/ravel/flatten/resize/transpose, concatenation and stacking, image arrays, synthetic time series, and capital-distance practice with a spherical-distance bonus.

Added teaching support:

- Pandas-to-NumPy transition with nonconsecutive labels and explicitly ordered numeric columns.
- Views versus copies, dimension-preserving slices, and 1D row/column orientation.
- Meaning-based per-product/per-store broadcasting and axis reductions.
- Explicit maximum/minimum value versus position, flattened coordinates, and all tied maxima.
- Stable tie handling, missing-value discussion, and stack versus concatenate.
- A single authoritative end-of-chapter activity, unfinished activity05 starter, local practice kit, and locally validated instructor-only Canvas QTI package.

Corrections include the previously valid broadcasting example labeled invalid, reshape copy/view guarantees, old dtype names, unsupported speed/contiguity/parallelism claims, an inverted timing explanation, stacking differences for 1D input, and capital-reference exclusion for both minimum and maximum searches. Benchmarks use modest reproducible inputs and equivalent-result checks. No fabricated large-distance sentinel remains. The coordinate-plane metric is explicitly distinguished from spherical distance.

The original first figure is stored unchanged at images/numpy-intro.png, downloaded from the original chapter URL https://i.imgur.com/mg8O3kd.png. It is also included in the student kit for offline rendering. Other shape/broadcasting explanations use text diagrams.

Validation: all 75 worked code cells and starter imports/inputs executed in fresh kernels. Separate checks cover the activity's expected values, broadcast failure and correction, reduction axes, tied maxima, views/copies, concatenation, and reference exclusion in capital searches. Expected activity results and quiz answers remain in teaching-materials/quizzes/chapter05 and are excluded from public publication. A local QTI validation is not a Canvas import test.
