"""
Generate figures for Final_Exam_Practice_Questions.tex.

Outputs all PDFs into the `figures/` subdirectory next to this script.

Conventions (from CLAUDE.md):
    - random_state = 1706
    - sns.set_theme(style="white")

Functions are kept under their original filenames (e.g. ``ridge_path.pdf``,
``bank2_heart_confusion_matrix.pdf``, ``qbank3_lasso_cv_curve.pdf``) so the
existing ``\\includegraphics`` paths in the tex file keep working.
"""

import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import (
    Ridge,
    Lasso,
    LassoCV,
    LinearRegression,
    LogisticRegression,
)
from sklearn.model_selection import KFold, train_test_split
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import (
    confusion_matrix,
    roc_curve,
    auc,
    mean_squared_error,
)
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import make_pipeline
from scipy.cluster.hierarchy import linkage, dendrogram

sns.set_theme(style="white")
RS = 1706

HERE = Path(__file__).resolve().parent
FIGDIR = HERE / "figures"
FIGDIR.mkdir(exist_ok=True)

COURSE = HERE.parent.parent  # .../Course_Notes
ADVERTISING = COURSE / "Class 06 - Linear Regressions" / "Advertising.csv"
CREDIT = COURSE / "Class 10 - Model Selection" / "Credit.csv"
HITTERS = COURSE / "Class 11 - Tree Based Methods" / "Hitters.csv"
HEART = COURSE / "Class 11 - Tree Based Methods" / "Heart.csv"
BOSTON = COURSE / "Class 11 - Tree Based Methods" / "Boston.csv"
USARRESTS = COURSE / "Class 13 - Unsupervised Learning" / "USArrests.csv"


def save(fig, name):
    path = FIGDIR / name
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"saved {path.name}")


# =============================================================
# Bank-1 figures (Section 2 of practice questions)
# =============================================================

def _credit_xy():
    df = pd.read_csv(CREDIT)
    df = df.copy()
    df["Own"] = (df["Own"] == "Yes").astype(int)
    df["Student"] = (df["Student"] == "Yes").astype(int)
    df["Married"] = (df["Married"] == "Yes").astype(int)
    df = pd.get_dummies(df, columns=["Region"], drop_first=True)
    y = df["Balance"].values
    X = df.drop(columns=["Balance"])
    X = X.astype(float)
    return X, y


def fig_ridge_path():
    X, y = _credit_xy()
    Xs = StandardScaler().fit_transform(X)
    feat = X.columns.tolist()

    key = ["Income", "Limit", "Rating", "Student", "Cards", "Age"]
    key_idx = [feat.index(f) for f in key]

    lambdas = np.logspace(-2, 5, 80)
    coefs = np.zeros((len(lambdas), len(feat)))
    for i, lam in enumerate(lambdas):
        m = Ridge(alpha=lam).fit(Xs, y)
        coefs[i] = m.coef_

    fig, ax = plt.subplots(figsize=(8, 5))
    for j in range(len(feat)):
        if j in key_idx:
            ax.plot(np.log(lambdas), coefs[:, j], label=feat[j], linewidth=2)
        else:
            ax.plot(np.log(lambdas), coefs[:, j], color="lightgrey", linewidth=1)
    ax.axhline(0, color="black", linewidth=0.6)
    ax.set_xlabel(r"$\log(\lambda)$", fontsize=12)
    ax.set_ylabel("Standardized coefficients", fontsize=12)
    ax.set_title("Ridge coefficient path: Credit data", fontsize=13)
    ax.legend(loc="best", fontsize=9)
    save(fig, "ridge_path.pdf")


def fig_lasso_path():
    X, y = _credit_xy()
    Xs = StandardScaler().fit_transform(X)
    feat = X.columns.tolist()

    key = ["Income", "Limit", "Rating", "Student", "Cards", "Age"]
    key_idx = [feat.index(f) for f in key]

    lambdas = np.logspace(-2, 2.5, 80)
    coefs = np.zeros((len(lambdas), len(feat)))
    for i, lam in enumerate(lambdas):
        m = Lasso(alpha=lam, max_iter=50000).fit(Xs, y)
        coefs[i] = m.coef_

    fig, ax = plt.subplots(figsize=(8, 5))
    for j in range(len(feat)):
        if j in key_idx:
            ax.plot(np.log(lambdas), coefs[:, j], label=feat[j], linewidth=2)
        else:
            ax.plot(np.log(lambdas), coefs[:, j], color="lightgrey", linewidth=1)
    ax.axhline(0, color="black", linewidth=0.6)
    ax.set_xlabel(r"$\log(\lambda)$", fontsize=12)
    ax.set_ylabel("Standardized coefficients", fontsize=12)
    ax.set_title("Lasso coefficient path: Credit data", fontsize=13)
    ax.legend(loc="best", fontsize=9)
    save(fig, "lasso_path.pdf")


def fig_hitters_tree():
    df = pd.read_csv(HITTERS).dropna(subset=["Salary"])
    df["logSalary"] = np.log(df["Salary"])
    X = df[["Years", "Hits"]].values
    y = df["logSalary"].values

    tree = DecisionTreeRegressor(max_depth=2, random_state=RS).fit(X, y)
    fig, ax = plt.subplots(figsize=(10, 6))
    plot_tree(
        tree,
        feature_names=["Years", "Hits"],
        filled=True,
        rounded=True,
        precision=2,
        fontsize=11,
        ax=ax,
    )
    ax.set_title("Regression tree: log(Salary) ~ Years + Hits (Hitters)", fontsize=13)
    save(fig, "hitters_tree.pdf")


def fig_rf_importance():
    df = pd.read_csv(BOSTON)
    y = df["medv"].values
    X = df.drop(columns=["medv"])
    rf = RandomForestRegressor(n_estimators=500, random_state=RS).fit(X, y)
    imp = pd.Series(rf.feature_importances_, index=X.columns).sort_values()

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(imp.index, imp.values, color="steelblue")
    ax.set_xlabel("Feature importance", fontsize=12)
    ax.set_title("Random forest feature importance: Boston (medv)", fontsize=13)
    save(fig, "rf_importance.pdf")


def fig_nn_training_curve():
    # Illustrative curves -- no actual NN training needed for the exam figure.
    rng = np.random.default_rng(RS)
    epochs = np.arange(1, 101)
    train = 1.0 * np.exp(-epochs / 25) + 0.02 + 0.01 * rng.standard_normal(len(epochs))
    val = 1.0 * np.exp(-epochs / 25) + 0.05 + 0.004 * (epochs - 30) ** 2 / 70
    val += 0.02 * rng.standard_normal(len(epochs))
    val = np.clip(val, 0.05, None)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(epochs, train, label="Training loss", color="steelblue", linewidth=2)
    ax.plot(epochs, val, label="Validation loss", color="darkorange", linewidth=2)
    ax.set_xlabel("Epoch", fontsize=12)
    ax.set_ylabel("Loss", fontsize=12)
    ax.set_title("Neural network training vs. validation loss", fontsize=13)
    ax.legend(fontsize=11)
    save(fig, "nn_training_curve.pdf")


def fig_scree_plot():
    df = pd.read_csv(USARRESTS, index_col=0)
    Xs = StandardScaler().fit_transform(df.values)
    pca = PCA().fit(Xs)
    pve = pca.explained_variance_ratio_
    cum = np.cumsum(pve)
    comps = np.arange(1, len(pve) + 1)

    fig, ax1 = plt.subplots(figsize=(8, 5))
    ax1.bar(comps, pve, color="steelblue", alpha=0.8, label="PVE per component")
    ax1.set_xlabel("Principal component", fontsize=12)
    ax1.set_ylabel("Proportion of variance explained", fontsize=12, color="steelblue")
    ax1.set_xticks(comps)
    ax1.set_ylim(0, 1)

    ax2 = ax1.twinx()
    ax2.plot(comps, cum, color="darkorange", marker="o", linewidth=2,
             label="Cumulative PVE")
    ax2.set_ylabel("Cumulative PVE", fontsize=12, color="darkorange")
    ax2.set_ylim(0, 1.05)

    ax1.set_title("Scree plot: USArrests (standardized)", fontsize=13)
    save(fig, "scree_plot.pdf")


def fig_dendrogram():
    df = pd.read_csv(USARRESTS, index_col=0)
    Xs = StandardScaler().fit_transform(df.values)
    Z = linkage(Xs, method="complete")

    fig, ax = plt.subplots(figsize=(12, 6))
    dendrogram(Z, labels=df.index.tolist(), leaf_rotation=90, leaf_font_size=8,
               color_threshold=4.0, ax=ax)
    ax.axhline(4.0, color="red", linestyle="--", linewidth=1.5)
    ax.set_ylabel("Height (distance)", fontsize=12)
    ax.set_title("Hierarchical clustering dendrogram: USArrests (complete linkage)",
                 fontsize=13)
    save(fig, "dendrogram.pdf")


# =============================================================
# Bank-2 figures (Section 2 of practice questions)
# =============================================================

def _heart_xy():
    df = pd.read_csv(HEART)
    df = df.replace("?", np.nan).dropna()
    y = (df["AHD"] == "Yes").astype(int).values
    X = df.drop(columns=["AHD"]).copy()
    X = pd.get_dummies(X, drop_first=True)
    X = X.astype(float)
    return X, y


def fig_heart_confusion():
    X, y = _heart_xy()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=RS, stratify=y
    )

    tree = DecisionTreeClassifier(max_depth=3, random_state=RS)
    tree.fit(X_train, y_train)
    y_pred = tree.predict(X_test)

    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False, ax=ax)
    ax.set_xlabel("Predicted label", fontsize=12)
    ax.set_ylabel("Actual label", fontsize=12)
    ax.set_title("Confusion matrix: Heart decision tree (test set)", fontsize=13)
    ax.set_xticklabels(["No AHD", "AHD"], rotation=0)
    ax.set_yticklabels(["No AHD", "AHD"], rotation=0)
    save(fig, "bank2_heart_confusion_matrix.pdf")


def fig_heart_roc_compare():
    X, y = _heart_xy()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=RS, stratify=y
    )

    logit = LogisticRegression(max_iter=2000, random_state=RS)
    rf = RandomForestClassifier(n_estimators=400, random_state=RS)
    logit.fit(X_train, y_train)
    rf.fit(X_train, y_train)

    p_log = logit.predict_proba(X_test)[:, 1]
    p_rf = rf.predict_proba(X_test)[:, 1]

    fpr_l, tpr_l, _ = roc_curve(y_test, p_log)
    fpr_r, tpr_r, _ = roc_curve(y_test, p_rf)
    auc_l = auc(fpr_l, tpr_l)
    auc_r = auc(fpr_r, tpr_r)

    fig, ax = plt.subplots(figsize=(7.5, 5.5))
    ax.plot(fpr_l, tpr_l, linewidth=2, label=f"Logistic regression (AUC={auc_l:.3f})")
    ax.plot(fpr_r, tpr_r, linewidth=2, label=f"Random forest (AUC={auc_r:.3f})")
    ax.plot([0, 1], [0, 1], linestyle="--", color="grey", linewidth=1)
    ax.set_xlabel("False positive rate", fontsize=12)
    ax.set_ylabel("True positive rate", fontsize=12)
    ax.set_title("ROC comparison on Heart test set", fontsize=13)
    ax.legend(loc="lower right", fontsize=10)
    save(fig, "bank2_heart_roc_compare.pdf")


def fig_lasso_cv_path_boston():
    df = pd.read_csv(BOSTON)
    y = df["medv"].values
    X = df.drop(columns=["medv"]).values
    Xs = StandardScaler().fit_transform(X)

    model = LassoCV(
        alphas=np.logspace(-3, 1, 80),
        cv=10,
        max_iter=50000,
        random_state=RS,
    ).fit(Xs, y)

    mean_mse = model.mse_path_.mean(axis=1)
    std_mse = model.mse_path_.std(axis=1)
    alphas = model.alphas_
    best_alpha = model.alpha_

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(np.log(alphas), mean_mse, color="steelblue", linewidth=2)
    ax.fill_between(
        np.log(alphas), mean_mse - std_mse, mean_mse + std_mse, alpha=0.2, color="steelblue"
    )
    ax.axvline(np.log(best_alpha), color="darkorange", linestyle="--", linewidth=2)
    ax.text(
        np.log(best_alpha) + 0.05,
        mean_mse.min() + 0.2,
        "Chosen alpha",
        color="darkorange",
        fontsize=10,
    )
    ax.set_xlabel(r"$\log(\lambda)$", fontsize=12)
    ax.set_ylabel("10-fold CV MSE", fontsize=12)
    ax.set_title("Lasso CV curve: Boston housing", fontsize=13)
    save(fig, "bank2_lasso_cv_curve.pdf")


def fig_rf_oob_curve():
    """OOB error vs ensemble size using warm_start so the forest grows in place.

    Retraining a brand-new forest at each n gives nearly independent OOB estimates
    that often look flat or jagged on small tabular problems. Growing one forest
    with shallow trees yields the usual textbook pattern: high error with few
    weak learners, then a decline toward a stable plateau.
    """
    df = pd.read_csv(BOSTON)
    y = (df["medv"] > df["medv"].median()).astype(int).values
    X = df.drop(columns=["medv"]).values

    n_trees = [1, 2, 3, 5, 8, 10, 15, 20, 30, 50, 75, 100, 150, 200, 250, 300, 400]
    oob_err = []

    rf = RandomForestClassifier(
        n_estimators=1,
        oob_score=True,
        bootstrap=True,
        warm_start=True,
        max_depth=4,
        min_samples_leaf=4,
        max_features="sqrt",
        random_state=RS,
        n_jobs=-1,
    )
    for n in n_trees:
        rf.set_params(n_estimators=n)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=UserWarning)
            rf.fit(X, y)
        oob_err.append(1.0 - float(rf.oob_score_))

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(n_trees, oob_err, marker="o", linewidth=2, color="steelblue", markersize=5)
    ax.set_xlabel("Number of trees", fontsize=12)
    ax.set_ylabel("OOB classification error", fontsize=12)
    ax.set_title("Random forest OOB error vs number of trees", fontsize=13)
    save(fig, "bank2_rf_oob_curve.pdf")


# =============================================================
# Bank-3 figures (Section 2 of practice questions)
# =============================================================

def fig_bias_variance_degrees():
    rng = np.random.default_rng(RS)
    x_train = np.linspace(0, 1, 70)
    y_train = np.sin(2 * np.pi * x_train) + 0.35 * x_train + rng.normal(0, 0.25, len(x_train))
    x_test = np.linspace(0, 1, 500)
    y_test = np.sin(2 * np.pi * x_test) + 0.35 * x_test + rng.normal(0, 0.25, len(x_test))

    degrees = np.arange(1, 16)
    train_mse, test_mse = [], []
    for degree in degrees:
        model = make_pipeline(PolynomialFeatures(degree=degree, include_bias=False), LinearRegression())
        model.fit(x_train.reshape(-1, 1), y_train)
        train_mse.append(mean_squared_error(y_train, model.predict(x_train.reshape(-1, 1))))
        test_mse.append(mean_squared_error(y_test, model.predict(x_test.reshape(-1, 1))))

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(degrees, train_mse, marker="o", label="Training MSE", color="steelblue")
    ax.plot(degrees, test_mse, marker="o", label="Test MSE", color="darkorange")
    ax.set_xlabel("Polynomial degree", fontsize=12)
    ax.set_ylabel("MSE", fontsize=12)
    ax.set_xticks(degrees)
    ax.set_title("Training and test error as flexibility increases", fontsize=13)
    ax.legend(fontsize=11)
    save(fig, "qbank3_bias_variance_degrees.pdf")
    print(f"bias/test min degree: {degrees[int(np.argmin(test_mse))]}, test mse: {min(test_mse):.3f}")


def fig_knn_k_curve():
    ads = pd.read_csv(ADVERTISING, usecols=["TV", "Radio", "Newspaper", "Sales"])
    X = ads[["TV", "Radio", "Newspaper"]]
    y = ads["Sales"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=RS)
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    ks = np.arange(1, 41)
    test_mse = []
    for k in ks:
        model = KNeighborsRegressor(n_neighbors=k)
        model.fit(X_train_s, y_train)
        test_mse.append(mean_squared_error(y_test, model.predict(X_test_s)))

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(ks, test_mse, marker="o", color="steelblue")
    ax.axvline(ks[int(np.argmin(test_mse))], color="darkorange", linestyle="--", linewidth=1.5)
    ax.set_xlabel(r"$K$ nearest neighbors", fontsize=12)
    ax.set_ylabel("Test MSE", fontsize=12)
    ax.set_title("KNN regression on Advertising: choosing K", fontsize=13)
    save(fig, "qbank3_knn_k_curve.pdf")
    print(f"knn best K: {ks[int(np.argmin(test_mse))]}, mse: {min(test_mse):.3f}")


def fig_logistic_threshold():
    credit = pd.read_csv(CREDIT)
    threshold = credit["Balance"].quantile(0.75)
    credit["HighBalance"] = (credit["Balance"] >= threshold).astype(int)
    X = credit[["Limit"]]
    y = credit["HighBalance"]
    model = LogisticRegression().fit(X, y)
    grid = np.linspace(credit["Limit"].min(), credit["Limit"].max(), 300)
    probs = model.predict_proba(pd.DataFrame({"Limit": grid}))[:, 1]
    limit_at_half = grid[np.argmin(np.abs(probs - 0.5))]

    fig, ax = plt.subplots(figsize=(8, 5))
    jitter = np.random.default_rng(RS).normal(0, 0.015, len(y))
    ax.scatter(credit["Limit"], y + jitter, alpha=0.35, color="grey", label="Observed class")
    ax.plot(grid, probs, color="steelblue", linewidth=2.5, label="Predicted probability")
    ax.axhline(0.5, color="black", linestyle="--", linewidth=1)
    ax.axvline(limit_at_half, color="darkorange", linestyle="--", linewidth=1.5)
    ax.set_xlabel("Credit limit", fontsize=12)
    ax.set_ylabel("Pr(HighBalance = 1)", fontsize=12)
    ax.set_ylim(-0.08, 1.08)
    ax.set_title("Logistic regression probability curve", fontsize=13)
    ax.legend(fontsize=10)
    save(fig, "qbank3_logistic_threshold.pdf")
    print(f"logit 0.5 limit: {limit_at_half:.0f}")


def fig_lasso_cv_curve_credit():
    credit = pd.read_csv(CREDIT)
    credit = credit.copy()
    for col in ["Own", "Student", "Married"]:
        credit[col] = (credit[col] == "Yes").astype(int)
    credit = pd.get_dummies(credit, columns=["Region"], drop_first=True)
    y = credit["Balance"].values
    X = credit.drop(columns=["Balance"]).astype(float)
    cv = KFold(n_splits=10, shuffle=True, random_state=RS)
    model = make_pipeline(StandardScaler(), LassoCV(cv=cv, random_state=RS, max_iter=50000, alphas=120))
    model.fit(X, y)
    lasso = model.named_steps["lassocv"]
    mse_mean = lasso.mse_path_.mean(axis=1)
    mse_se = lasso.mse_path_.std(axis=1) / np.sqrt(lasso.mse_path_.shape[1])
    best_idx = int(np.argmin(mse_mean))

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.errorbar(np.log(lasso.alphas_), mse_mean, yerr=mse_se, color="steelblue", marker="o", markersize=3, capsize=2)
    ax.axvline(np.log(lasso.alpha_), color="darkorange", linestyle="--", linewidth=1.5, label=r"Selected $\lambda$")
    ax.set_xlabel(r"$\log(\lambda)$", fontsize=12)
    ax.set_ylabel("10-fold CV MSE", fontsize=12)
    ax.set_title("Lasso tuning by cross-validation: Credit", fontsize=13)
    ax.legend(fontsize=10)
    save(fig, "qbank3_lasso_cv_curve.pdf")
    print(f"lasso selected alpha: {lasso.alpha_:.3f}, log alpha: {np.log(lasso.alpha_):.2f}, min mse: {mse_mean[best_idx]:.1f}")


def fig_hitters_tree_depth3():
    hitters = pd.read_csv(HITTERS).dropna(subset=["Salary"])
    hitters["logSalary"] = np.log(hitters["Salary"])
    X = hitters[["Years", "Hits"]]
    y = hitters["logSalary"]
    tree = DecisionTreeRegressor(max_depth=3, min_samples_leaf=20, random_state=RS).fit(X, y)

    fig, ax = plt.subplots(figsize=(12, 7))
    plot_tree(
        tree,
        feature_names=["Years", "Hits"],
        filled=True,
        rounded=True,
        precision=2,
        fontsize=10,
        ax=ax,
    )
    ax.set_title("Regression tree: log(Salary) ~ Years + Hits", fontsize=13)
    save(fig, "qbank3_hitters_tree_depth3.pdf")
    pred = tree.predict(pd.DataFrame({"Years": [8], "Hits": [90]}))[0]
    print(f"tree prediction years=8 hits=90: {pred:.2f}")


if __name__ == "__main__":
    # Bank-1 figures
    fig_ridge_path()
    fig_lasso_path()
    fig_hitters_tree()
    fig_rf_importance()
    fig_nn_training_curve()
    fig_scree_plot()
    fig_dendrogram()
    # Bank-2 figures
    fig_heart_confusion()
    fig_heart_roc_compare()
    fig_lasso_cv_path_boston()
    fig_rf_oob_curve()
    # Bank-3 figures
    fig_bias_variance_degrees()
    fig_knn_k_curve()
    fig_logistic_threshold()
    fig_lasso_cv_curve_credit()
    fig_hitters_tree_depth3()
    print(f"\nAll practice-question figures written to: {FIGDIR}")
