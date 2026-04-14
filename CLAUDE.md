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

## Python stack

Core libraries used across notebooks:
- **Data**: `numpy`, `pandas`
- **Viz**: `matplotlib`, `seaborn`, `plotly`
- **ML**: `sklearn` (linear models, trees, ensemble, clustering, decomposition, model selection)
- **Stats**: `statsmodels` (OLS, formula API, GLM)
- **Deep learning**: `tensorflow` / `keras`

## Repository layout

```
Class 01–14 - <Topic>/   # One folder per lecture
  Class N - <Topic>.ipynb  # Lecture notebook / slides
  *.csv                    # Datasets used in that class
  *.png / *.pdf            # Figures referenced in slides
Exams/                     # LaTeX source + compiled PDFs for midterm
Class XX - Term Paper/     # Term paper handout (Markdown)
Books/                     # Reference PDFs
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
