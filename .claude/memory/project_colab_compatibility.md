---
name: Google Colab compatibility — Dropbox URLs for all assets
description: Students run notebooks on Google Colab, so all images and datasets must use Dropbox direct-download URLs, not local paths
type: project
---
Students run ECON 4971 notebooks on **Google Colab**, not locally. This means every file reference must be a URL.

**Why:** Local paths (e.g. `pd.read_csv("USArrests.csv")` or `mpimg.imread("figure.png")`) break on Colab since the files don't exist in the Colab environment.

**How to apply:**
- CSV datasets: use `pd.read_csv("https://www.dropbox.com/...?dl=1", index_col=0)` — Dropbox direct-download links end with `?dl=1`.
- Images displayed inline: use a markdown cell with `![](https://www.dropbox.com/...?dl=1)` rather than a code cell with `mpimg.imread()`.
- Never introduce new local file references. If you spot an existing one, flag it to Jonathan so he can upload the file to Dropbox and provide a link.
- The `dl=1` parameter on Dropbox URLs forces a direct file download rather than a preview page — it is required for Colab to fetch the file correctly.
