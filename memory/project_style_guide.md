---
name: Notebook style and formatting guide
description: How ECON 4971 notebooks are structured and formatted — layout, markdown conventions, code style, exercises
type: project
originSessionId: 26ffc79c-4f04-4490-b701-5438f6c9313e
---
## Title cell

Every notebook opens with a centered HTML title block:
```markdown
# <div align="center"> Statistical Learning </div>
# <div align="center"> Machine Learning and Econometrics </div>
## <div align="center"> ECO 4971/6971 </div>
#### <div align="center">Class N — Topic name</div>
<div align="center"> Jonathan Holmes (he/him)</div>
```

## Document structure

- **Road map cell** near the top: states learning objectives and what the class covers, written as prose or a short bulleted list.
- **Part N** headers (`#`) divide the notebook into major sections (e.g. "Part 1: Decision trees for regression", "Part 2: Classification trees").
- `##` for subsections within a part, `###` for finer breakdowns.
- Each Part typically follows: motivating concept → math/theory → code demo → in-class exercise.

## Markdown prose style

- Write in flowing prose, not bullet-point fragments. Bullets are fine for lists of items or comparisons, not for replacing sentences.
- Introduce new concepts with a brief motivating question or real-world analogy before the formal definition.
- Use **bold** for key terms on first use. Use *italics* sparingly for emphasis.
- Connect new material to prior content explicitly (e.g. "Recall from Class 9 that…").
- Avoid slide-break artifacts: do not split one idea across multiple cells just to control pacing.

## Math

- Inline math: `$...$`. Display math: `$$...$$` (centred, own line).
- Use `\hat{f}`, `\mathbf{X}`, `\varepsilon` consistently.
- Label equations and reference them in the surrounding text.
- When defining a new quantity, define every symbol that appears.

## Code cells

- Group all imports into one cell near the top; comment-group them (data, viz, stats):
  ```python
  # data libraries
  import pandas as pd
  import numpy as np
  # visualization
  import matplotlib.pyplot as plt
  import seaborn as sns
  sns.set_theme(style="white")
  # ML / stats
  from sklearn.linear_model import LinearRegression
  import statsmodels.formula.api as smf
  ```
- Use `display()` for DataFrames, not `print()`.
- Add short inline comments on non-obvious lines; avoid over-commenting obvious operations.
- Use `random_state=1706` for all sklearn random seeds (consistent across the course).
- Figure sizing: `figsize=(12, 8)` as the default for single plots; `(14, 8)` for wide trees.
- Set axis labels with `fontsize=12` (axis labels) or `fontsize=20` for primary axes.
- Prefer `sns.lineplot` / `sns.scatterplot` / `sns.histplot` over raw `plt.plot` where seaborn is cleaner.

## In-class exercises

Format exercises as a `#` or `##` level header:
```markdown
# In-Class Exercise #N

Q1: Question text in **bold key terms**.

Q2: …
```
Leave a blank code cell immediately after each exercise block for students to work in.

## Tables

Use markdown tables for pros/cons or method comparisons:
```markdown
| Pros | Cons |
| --- | --- |
| Easy to interpret | High variance |
```

## Figures

Reference local images with `![](filename.png)`. Add a short italic caption in the cell below or as a following line: `*Caption text.*`

## Data loading

Datasets are loaded from Dropbox URLs. Local CSV copies are stored in the class folder and used as fallback references. Always assign to a clearly named DataFrame (`df`, `df2` for a second dataset in the same notebook).

## "Try it" / interactive prompts

Use inline comments to invite students to experiment:
```python
# Interactive: change max_depth to 3, 4, or None — watch in-sample MSE and the number of leaves.
```
Or in a markdown follow-up cell:
```markdown
**Try it (after class or live):** Change `max_depth` from `2` to `3` or `4`. How many regions do you get?
```
