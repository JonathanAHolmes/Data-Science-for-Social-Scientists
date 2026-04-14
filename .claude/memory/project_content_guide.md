---
name: Course content and pedagogical style guide
description: What ECON 4971 covers, how concepts connect, and Jonathan's teaching philosophy
type: project
originSessionId: 26ffc79c-4f04-4490-b701-5438f6c9313e
---
## Course identity

ECON 4971/6971 is a **prediction-focused** machine learning course for economics students. The unifying frame is:
$$x \rightarrow \hat{f}(x) \rightarrow \hat{y}$$
Every method is introduced as a different way to design $\hat{f}$, and every evaluation tool is a different way to judge whether $\hat{f}$ is good. Students are assumed to have econometrics background; ML concepts are explicitly connected to that prior knowledge (e.g. "linear regression re-interpreted as a prediction problem").

The course closely follows *Introduction to Statistical Learning* (ISLR) with Python implementations.

---

## Concept arc

### Unit 1: Foundations (Classes 1–5)
- What ML is and why it works (data, models, compute).
- The prediction framework: reducible vs. irreducible error, MSE, bias–variance tradeoff.
- Key notation established early: $Y = f(X) + \varepsilon$, $\hat{f}$, training vs. test error.
- Motivating examples are deliberately simple (fire alarm, advertising).

### Unit 2: Core supervised methods (Classes 6–8)
- **Linear regression** (Class 6): OLS reframed as a prediction tool; advertising dataset; interpreting coefficients as prediction weights rather than causal estimates.
- **KNN Regression** (Class 7): Nonparametric baseline; intuition for bias–variance via $K$.
- **Classification** (Class 8): Logistic regression, LDA, QDA, Naive Bayes; confusion matrix, ROC curve, AUC; connects to Class 5's fire alarm (Type I/II error trade-off).

### Unit 3: Model evaluation and selection (Classes 9–10)
- **Resampling** (Class 9): Validation set, LOOCV, k-fold CV, bootstrap; Auto dataset (mpg ~ horsepower polynomial); tuning parameters vs. model parameters.
- **Model selection** (Class 10): Best subset selection; Ridge and Lasso as shrinkage; Credit dataset; the bias–variance interpretation of the penalty $\lambda$.

### Unit 4: Flexible and ensemble methods (Classes 11–12)
- **Tree-based methods** (Class 11): Regression and classification trees; bagging; random forests; boosting; Hitters and Heart datasets; feature importance.
- **Deep learning** (Class 12): Feedforward networks; activation functions; TensorFlow/Keras; connects to linear regression as a special (no hidden layer) case.

### Unit 5: Unsupervised learning (Class 13)
- PCA; K-means; hierarchical clustering; USArrests dataset.
- Framed as "no $Y$" — we are describing structure, not predicting an outcome.

### Unit 6: Ethics and critique (Class 14)
- Algorithmic bias and fairness; face depixelation example (Obama image); when optimizing accuracy harms groups; connects prediction to policy consequences.
- Intentionally placed last — students evaluate methods they've already learned.

---

## Pedagogical style

**Motivating examples first.** Every major concept is introduced through a concrete, accessible scenario before formal notation (fire alarms → MSE; baseball salaries → decision trees; advertising → linear regression).

**Econometrics as the baseline.** Students are reminded what they already know from econometrics, then shown how ML reframes or extends it. This is explicit (e.g. "your econometrics class re-interpreted").

**Bias–variance is the spine.** The bias–variance tradeoff is introduced in Class 5 and returned to explicitly in almost every subsequent class. Method choices (flexible vs. rigid, deep vs. shallow) are always framed through this lens.

**In-class exercises throughout.** Each notebook has 3–6 numbered exercises interspersed at natural breakpoints — not just at the end. Questions are conceptual ("why do we use Gini and not RSS for classification trees?") as well as computational ("change `max_depth` and observe the effect").

**Code illustrates intuition, it doesn't replace it.** Students are told "most of the code will be provided to you." Code demos show the concept visually (RSS vs. cutpoint curves, train/test MSE vs. polynomial degree) rather than asking students to build models from scratch.

**Real datasets from ISLR.** Advertising, Auto, Hitters, Heart, Credit, Boston, USArrests — the same datasets used in the textbook, making it easy for students to cross-reference.

**Prediction, not causation.** The course explicitly and repeatedly scopes itself to prediction. Causal language is flagged and avoided. The term paper guide states: "full causal policy evaluation is usually beyond scope—stick to prediction."

**Visualize everything possible.** Key concepts should be illustrated with simple, effective graphs wherever possible. A well-chosen plot is preferred over a verbal description alone.

**3Blue1Brown narrative arc.** Each class should feel like a well-constructed mathematical explainer: open with a compelling question that creates genuine curiosity, build intuition graphically before (or alongside) formal equations, and use equations only where they are necessary to understand the concept — not as a substitute for intuition.

**Code that students can actually use.** Code blocks are designed for interactivity and accessibility, not completeness. This means: concise but effective inline comments that explain the *why* not just the *what*; parameters and cutpoints exposed as easy-to-change variables; and complexity kept low so students focus on the concept being illustrated rather than decoding the code itself.

---

## Recurring datasets and what they're used for

| Dataset | Class | Task |
| --- | --- | --- |
| Advertising.csv | 6 | Linear regression (sales ~ TV/radio/newspaper) |
| Auto.csv | 9 | Polynomial regression, CV (mpg ~ horsepower) |
| Credit.csv | 10 | Ridge/Lasso/best subset (balance prediction) |
| Hitters.csv | 11 | Regression tree (log salary ~ years + hits) |
| Heart.csv | 11 | Classification tree (AHD yes/no) |
| Boston.csv | 10–11 | Various regression demos |
| USArrests.csv | 13 | PCA, clustering |
