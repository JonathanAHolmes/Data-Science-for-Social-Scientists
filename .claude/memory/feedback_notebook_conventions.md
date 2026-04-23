---
name: Notebook code and exercise conventions
description: Specific conventions confirmed during Class 13 editing — DataFrame naming, exercise question numbering
type: feedback
---
**Convention 1: Unique DataFrame names per dataset.**
When a notebook uses more than one dataset, give each a distinct short name (e.g. `df_km`, `df_hc`, `df_us`) rather than reusing `df`. Reusing `df` causes length-mismatch errors when cells are re-run out of order because a later cell overwrites the variable with a different-sized dataset.

**Why:** Encountered this bug in Class 13 where the K-means (150 rows), hierarchical (originally 45 rows), and USArrests (50 rows) DataFrames all used `df`, causing crashes on rerun.

**How to apply:** At the start of any notebook with multiple datasets, assign each a unique name. Suffix suggestions: `_km` (K-means), `_hc` (hierarchical clustering), `_us` (USArrests), or just use the dataset name.

---

**Convention 2: Exercise questions numbered sequentially across the whole notebook.**
In-class exercise questions (Q1, Q2, …) should be numbered continuously from 1 to N across all exercise blocks in the notebook — they do not restart at Q1 for each new exercise section.

**Why:** Jonathan confirmed this explicitly during Class 13 editing — he wanted Q1–Q3 in Exercise 1, Q4–Q6 in Exercise 2, Q7–Q9 in Exercise 3.

**How to apply:** When adding or editing exercises, count up from the last question number used in the previous exercise block.
