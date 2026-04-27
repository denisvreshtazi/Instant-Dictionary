# 📚 Instant-Dictionary

> A multi-page **web application** for instant word lookup, built with [JustPy](https://justpy.io/) and a shared `Page` base class. Sister project of [Instant-Dictionary-API](https://github.com/denisvreshtazi/Instant-Dictionary-API).

[![Python](https://img.shields.io/badge/python-3.7%2B-blue)]()
[![JustPy](https://img.shields.io/badge/framework-justpy-purple)]()
[![Pandas](https://img.shields.io/badge/data-pandas-yellow)]()

---

## 📌 Overview

Where the API project exposes a single JSON endpoint, this repo wraps the same dictionary data in a **full web application** with:
- A **home page** explaining what the app does
- A **dictionary lookup page** with a search input and live results
- An **about page**
- A shared layout with reusable navbar and page scaffolding

It demonstrates a more polished JustPy pattern: an OOP-based router that **auto-discovers any subclass of `Page`** and registers its route — no explicit `jp.Route(...)` needed per page.

## 🛣️ Pages & Routes

| Class | Path | Description |
|---|---|---|
| `Home` | `/` | Landing page |
| `Dictionary` | `/dictionary` | Word lookup form + results |
| `About` | `/about` | Project info |

## 🧱 Architecture

```
main.py
  │
  │  introspects globals(), finds every subclass of Page,
  │  and auto-registers jp.Route(obj.path, obj.serve)
  │
  ▼
webapp/
├── page.py        # Page base class — defines `path` + `serve()`
├── layout.py      # Shared layout wrapper
├── navbar.py      # Top navigation
├── home.py        # Home page
├── dictionary.py  # Lookup page (uses definition.py)
└── about.py       # About page

definition.py      # pandas CSV lookup (shared with API project)
data.csv           # word,definition dataset
```

## 🚀 Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the server
```bash
python main.py
```
The app starts on **http://localhost:8001** (configurable via `jp.justpy(port=...)` in `main.py`).

### 3. Open in your browser
- http://localhost:8001/ — Home
- http://localhost:8001/dictionary — Lookup
- http://localhost:8001/about — About

## 🧩 Core Pattern: Auto-Routing via Reflection

The cleanest part of this project is in `main.py`:

```python
imports = list(globals().values())
for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)
```

Every page just needs to inherit `Page` and declare a `path` attribute — no manual route registration. Adding a new page is a 3-step task:
1. Create `webapp/new_page.py` with a class extending `Page`
2. Set `path = '/new'`
3. Import it in `main.py`

## 🗂️ Project Structure

```
Instant-Dictionary/
├── main.py
├── definition.py
├── data.csv
├── requirements.txt
├── design/                  # Mock-ups & screenshots
│   ├── home.png
│   ├── dictionary.png
│   ├── about.png
│   └── design.txt
├── examples/
│   └── file.html
└── webapp/
    ├── page.py
    ├── layout.py
    ├── navbar.py
    ├── home.py
    ├── dictionary.py
    └── about.py
```

## 📦 Key Dependencies

```
justpy==0.1.5
pandas==1.2.0
uvicorn==0.13.3
starlette==0.14.1
```

(Full list in `requirements.txt`.)

## 💡 Possible Extensions

- Replace the CSV with a real database
- Add fuzzy search (e.g. via `rapidfuzz`) for misspelled words
- Add user accounts and bookmarked words
- Containerize with Docker for easy deployment
- Add a public REST API (already exists in [Instant-Dictionary-API](https://github.com/denisvreshtazi/Instant-Dictionary-API))

## 👤 Author

**Denis Vreshtazi** — [GitHub](https://github.com/denisvreshtazi)
