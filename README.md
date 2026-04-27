# ECON 4971 / 6971 — Statistical Learning

**Machine Learning and Econometrics — University of Ottawa**
Instructor: Jonathan Holmes

This repository holds the course materials for Introduction to Machine Learning a course I have taught at the University of Ottawa (ECON 4199) and Tulane (ECON 4971 (undergraduate) / 6971 (graduate)). It is designed to teach students who already know at least a bit of econometrics how to use Machine Learning. 
---

## What this course is about

Statistical learning is the bridge between traditional econometrics and modern machine learning. This course covers two sections: 
1. Classes 2-4 are an introduction to using Python. This is mostly useful for students taking my course. If you are learning Python yourself, there are better self-directed sources you can use (see below for textbook examples).
2. Classes 5-14 cover the key topics in statistical learning. 


Inside each class folder you will typically find:

| File | What it is |
|------|-----------|
| `Class N - <Topic>.ipynb` | The lecture notebook — the version we work through together in class. |
| `Class N - Solutions.ipynb` (and `.pdf`) | Worked solutions to the in-class exercises. |
| `*.csv` | Datasets used in that class (Advertising, Credit, Boston, Heart, Hitters, Auto, USArrests, …). |
| `*.png` / `*.pdf` | Figures referenced in the lecture. |

Other top-level folders:

- **`Exams/`** — past midterm and final exam materials (LaTeX source plus compiled PDFs), and a final-exam practice question set with worked solutions.
- **`Term_Paper/`** — the term paper handout describing the end-of-semester project.

---

## Running the notebooks

You have two equally good options.

### Option 1 — Google Colab (recommended; nothing to install)

Every notebook is set up to run on [Google Colab](https://colab.research.google.com/) without any local data files. Datasets are loaded over the internet from public Dropbox links, so as long as you can sign in to Google and open a notebook, you are ready. This is the path I recommend, especially if you have not used Python before.

To open a notebook from this repo on Colab:

1. Go to the notebook's file on GitHub (e.g. `Class 06 - Linear Regressions/Class 6 - Linear Regressions.ipynb`).
2. Click the **Open in Colab** badge at the top, or copy the URL and use *File → Open notebook → GitHub* in Colab.
3. Run the cells with **Shift + Enter**.

### Option 2 — Local Jupyter (Anaconda or VS Code)

If you prefer to work locally:

1. Install [Anaconda](https://www.anaconda.com/download) (which bundles Python and Jupyter) or set up `jupyterlab` with `pip` / `uv`.
2. Clone this repository:
   ```bash
   git clone https://github.com/JonathanAHolmes/Data-Science-for-Social-Scientists.git
   cd <repo>
   ```
3. Launch Jupyter:
   ```bash
   jupyter lab          # or: jupyter notebook
   ```
4. Open any class folder and start with the lecture notebook.



## Textbooks: 
**Python and exploratory data analysis (Classes 2–4, or for self-study):**

- *Think Python: How to Think Like a Computer Scientist* (3rd ed.), Allen B. Downey (O'Reilly / Green Tea Press, 2024). Free at [greenteapress.com/wp/think-python](https://greenteapress.com/wp/think-python/).
- *Think Stats: Exploratory Data Analysis in Python* (3rd ed.), Allen B. Downey (O'Reilly / Green Tea Press, 2024). Free at [greenteapress.com/wp/think-stats](https://greenteapress.com/wp/think-stats/).

**Statistical learning (Classes 5–14):**

- *An Introduction to Statistical Learning with Applications in Python*, James, Witten, Hastie, Tibshirani, Taylor (Springer, 2023). Free at [statlearning.com](https://www.statlearning.com/).
- *The Elements of Statistical Learning*, Hastie, Tibshirani, Friedman (Springer, 2009). Free at [hastie.su.domains/ElemStatLearn](https://hastie.su.domains/ElemStatLearn/).


Thanks to Fabian Forge (https://forgef.github.io/) for providing me the original version of these notes. 