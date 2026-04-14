# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

Course materials for **ECON 4971/6971 — Statistical Learning** (Machine Learning and Econometrics) at uOttawa, taught by Jonathan Holmes. Each class is a Jupyter notebook.

## Running notebooks

Launch Jupyter in any class folder:
```
jupyter notebook
```

Run a notebook non-interactively (re-execute all cells):
```
jupyter nbconvert --to notebook --execute "Class 6 - Linear Regressions.ipynb" --output "Class 6 - Linear Regressions.ipynb"
```

The kernel is named `"base"` (conda base environment, Python 3.13).

## Converting slide-format notebooks to documents

Older notebooks were built for the RISE slideshow library, which is no longer used. When editing or creating notebooks, **convert slide-style formatting to flowing document style**:
- Remove or ignore `slideshow` cell metadata (`slide_type` tags)
- Remove the `"celltoolbar": "Slideshow"` entry from notebook metadata
- Rewrite bullet-heavy slide cells into prose or structured markdown sections that read naturally top-to-bottom
- Merge cells that were split purely to control slide breaks

## Notebook formatting conventions

**Title cell** — every notebook opens with a centered HTML block:
```markdown
# <div align="center"> Statistical Learning </div>
# <div align="center"> Machine Learning and Econometrics </div>
## <div align="center"> ECO 4971/6971 </div>
#### <div align="center">Class N — Topic name</div>
<div align="center"> Jonathan Holmes (he/him)</div>
```

**Document structure** — a "Road map" cell near the top states learning objectives. Major sections use `# Part N: Title`. Subsections use `##` and `###`.

**Prose over bullets** — write in flowing sentences. Bullets are fine for enumerated items or comparison lists, not as a substitute for prose.

**Math** — inline `$...$`, display `$$...$$`. Define every symbol. Use `\hat{f}`, `\mathbf{X}`, `\varepsilon` consistently.

**Code conventions**:
- Group imports at the top, commented by category (data / visualization / ML / stats)
- `sns.set_theme(style="white")` at import time
- `random_state=1706` for all sklearn random seeds
- `display()` for DataFrames, not `print()`
- Default figure size `figsize=(12, 8)`; axis label `fontsize=12`

**In-class exercises** — use `# In-Class Exercise #N` as a `#`-level header with numbered questions (`Q1:`, `Q2:`, …). Leave a blank code cell after each exercise block.

**Interactive prompts** — invite students to experiment via inline comments or a bold "Try it" markdown note after a code cell.

## Python stack

Core libraries used across notebooks:
- **Data**: `numpy`, `pandas`
- **Viz**: `matplotlib`, `seaborn`, `plotly`
- **ML**: `sklearn` (linear models, trees, ensemble, clustering, decomposition, model selection)
- **Stats**: `statsmodels` (OLS, formula API, GLM)
- **Deep learning**: `tensorflow` / `keras`

## Repository layout

```
Class 01–14 - <Topic>/      # One folder per lecture
  Class N - <Topic>.ipynb   # Lecture notebook
  *.csv                     # Datasets used in that class
  *.png / *.pdf             # Figures referenced in the notebook
Exams/
  Midterm_Exam/             # LaTeX source + compiled PDFs
Term_Paper/                 # Term paper handout (.tex + .pdf)
Books/                      # Reference PDFs
```

Notable datasets: `Advertising.csv`, `Credit.csv`, `Boston.csv`, `Heart.csv`, `Hitters.csv`, `Auto.csv`, `USArrests.csv`.

## Exam materials

Exam files are LaTeX (`.tex`) compiled with `latexmk`. To recompile:
```
cd Exams && latexmk -pdf Midterm_Spring_2026.tex
```

## Course sequence

Classes follow ISLR (Introduction to Statistical Learning) with Python:
1. What is Statistical Learning
2–4. Python / NumPy / Pandas / Matplotlib basics
5. Statistical Learning Fundamentals
6. Linear Regression
7. KNN Regression
8. Classification (Logistic, LDA, QDA, Naive Bayes)
9. Resampling Methods (CV, Bootstrap)
10. Model Selection (Best Subset, Ridge, Lasso)
11. Tree-Based Methods (Decision Trees, Random Forests, Boosting)
12. Deep Learning (Feedforward networks, TensorFlow)
13. Unsupervised Learning (PCA, K-Means, Hierarchical Clustering)
14. Social Biases and Prediction
