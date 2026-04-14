---
name: Notebook format — documents not slides
description: Notebooks were slide-based (RISE) but that library broke; convert to document style when editing or creating
type: feedback
originSessionId: 26ffc79c-4f04-4490-b701-5438f6c9313e
---
Do not treat or maintain the slideshow structure in notebooks. The RISE slide library is broken and no longer used.

**Why:** The slideshow library that powered interactive slides stopped working; notebooks are now read as plain documents.

**How to apply:** When editing existing notebooks, strip out `slideshow` cell metadata and the `"celltoolbar": "Slideshow"` notebook metadata entry. Rewrite bullet-heavy slide cells into flowing prose or well-structured markdown. Merge cells that were split only for slide-break purposes. When creating new notebooks, write them as documents from the start.
