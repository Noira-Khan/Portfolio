# Architecture

This repository is a Streamlit multipage site. It renders case studies. It does not score payments, retrieve products, or call a fund model.

```
home.py                         entry page
data/projects.py                the only project list
components/layout.py            page config, CSS, hidden Streamlit chrome
components/navbar.py            Home, Products, Case studies, GitHub
components/hero.py              intro and resume download
components/about.py             bio; project names come from the catalog
components/work_strip.py        home cards
components/project_card.py      card and repo/demo links
components/contact_section.py   email, phone, LinkedIn, GitHub, resume
pages/Products_Built.py         catalog grid
pages/Case_Studies.py           short problem / decision index
pages/overview_*.py             one long page per repository
assets/                         CSS, photos, icons, resume, product screenshots
```

Streamlit discovers every `pages/*.py` file. The sidebar is hidden. Navigation is the navbar, which calls `st.switch_page`.

## Request path

There is no backend in this repo.

1. `streamlit run home.py` starts the process.
2. `Layout.setup` sets the wide layout and inlines `assets/css/styles.css`.
3. The navbar switches to another script. That script calls `Layout.setup` again, because each page is its own Streamlit entry.
4. Product pages call `by_slug` and render fields from `data/projects.py`.
5. A GitHub or demo button is a normal link. This app does not proxy those sites.

Fraud screenshots and the retail screenshots are static files under `products/`. Groww Fund Facts and Quiet Push-to-Talk have no screenshots in this repo. Their pages are text, plus the repository link.

## Where the real systems live

```
Portfolio (this repo)
    |
    +-- Finance Shield -------- ML-Fraud-Detection-Project
    |     Streamlit desk, FastAPI POST /predict, saved XGBoost model
    |
    +-- Groww Fund Facts ------ groww-ai-hdfc-mf-facts
    |     PII check -> intent -> retrieval -> generation -> validation -> cache
    |     Streamlit and FastAPI share src/services/chat.py
    |
    +-- Retail assistant ------ multimodal-rag-product-search
    |     Lexical index by default, optional FAISS, Gemini only after retrieval
    |
    +-- Quiet Push-to-Talk ---- voice-input-prototype
          One HTML page. Pointer events. No speech API. GitHub Pages.
```

Details and run commands stay in those repositories. If a number on this site and a number in a product README disagree, the product README wins, and `data/projects.py` should be edited to match it.

## What is intentionally absent

- No second copy of model code, vector indexes, or fund corpora.
- No secrets. The resume PDF is the only personal document, and it was already in `assets/resume/`.
- Placeholder pages for an interview coach and a support agent were removed. Those products are not public repositories.
- `pages/experience.py` and `pages/resume.py` were empty and are removed so Streamlit does not register blank routes.

## Add a project

Change the catalog first. A page that is not listed in `PROJECTS` will not appear on Home, Products, or Case studies. A catalog row whose `page` file is missing will fail when someone opens that card.
