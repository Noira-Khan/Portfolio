# Noira Khan — portfolio

Streamlit site for the public work on [github.com/Noira-Khan](https://github.com/Noira-Khan).

The site is a case-study layer. Each product still lives in its own repository. This repo does not vendor that code.

## Projects on the site

| Project | What it decides | Repository |
| --- | --- | --- |
| Finance Shield | Allow a card payment, or send it to review. Review does not decline the card. | [ML-Fraud-Detection-Project](https://github.com/Noira-Khan/ML-Fraud-Detection-Project) |
| Groww Fund Facts | Answer a fund fact from 15 Groww pages, or refuse. | [groww-ai-hdfc-mf-facts](https://github.com/Noira-Khan/groww-ai-hdfc-mf-facts) |
| Multimodal Retail Assistant | Retrieve fashion products on the machine before any generated sentence. | [multimodal-rag-product-search](https://github.com/Noira-Khan/multimodal-rag-product-search) |
| Quiet Push-to-Talk | Hold, review, then send. Speech on the page is simulated. | [voice-input-prototype](https://github.com/Noira-Khan/voice-input-prototype) |

Copy for titles, problems, and proof lines lives in [`data/projects.py`](data/projects.py). The home page, the products page, and the case-study index all read that list.

## Run

```bash
pip install -r requirements.txt
streamlit run home.py
```

Open `http://localhost:8501`.

Pages:

- `home.py` — intro, about, the four projects, contact
- `pages/Products_Built.py` — the same four, as cards
- `pages/Case_Studies.py` — problem and decision for each
- `pages/overview_fraud.py`, `overview_fund_facts.py`, `overview_retail.py`, `overview_voice.py` — full pages

## Add a repository

1. Add one dict to `PROJECTS` in `data/projects.py`. Use claims that are already in that repo's README.
2. Add `pages/overview_<slug>.py` and set the dict's `page` to that path.
3. Run `python -m pytest`.

## Tests

```bash
pip install pytest
python -m pytest
```

The test checks that the catalog has the four public repos, that each GitHub URL is under `Noira-Khan`, and that each case page path is unique.

## Docs

[Architecture](docs/ARCHITECTURE.md)
