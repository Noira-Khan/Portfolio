"""Single catalog for every public project on github.com/Noira-Khan.

Pages and the README read this list. Add a row here before adding a case-study page.
Facts below are taken from each repository's README. Do not add a project that is not public.
"""

GITHUB = "https://github.com/Noira-Khan"

PROJECTS = [
    {
        "slug": "fraud",
        "title": "Finance Shield",
        "eyebrow": "Card payments",
        "summary": (
            "A card risk desk that scores one payment, or a small file of payments, "
            "and says Allow or Review. A Review case does not decline the card."
        ),
        "problem": (
            "A rare fraud label makes accuracy look excellent even when the model "
            "catches nothing. A banker still needs a cutoff, a queue, and a customer "
            "message that is only a preview."
        ),
        "decision": (
            "Under 95% the payment can go through and the customer gets no message. "
            "At 95% or above the case is filed for review, and the screen shows the "
            "phone alert and the email the customer would get. Nothing is sent, and "
            "the card is not blocked."
        ),
        "proof": [
            "Holdout at a 95% cutoff: about 0.93 fraud precision, 0.82 fraud recall, and 0.87 fraud F1, on 98 fraud cases in the test split.",
            "Accuracy on that file is about 99.8% even for a model that never catches fraud, so the screen does not lead with accuracy.",
            "The model only sees Time, V1–V28, and Amount. It cannot see a merchant, a country, or a cardholder.",
            "POST /predict returns the score and the decision. blocks_payment is always false.",
        ],
        "stack": ["Python", "XGBoost", "FastAPI", "Streamlit"],
        "repo": f"{GITHUB}/ML-Fraud-Detection-Project",
        "demo": "https://financeshieldai.streamlit.app/",
        "page": "pages/overview_fraud.py",
        "image": "products/fraud_detection/fraud_cover.jpeg",
    },
    {
        "slug": "fund-facts",
        "title": "Groww Fund Facts",
        "eyebrow": "Mutual fund facts",
        "summary": (
            "A facts-only assistant for a curated set of HDFC Mutual Fund schemes on Groww. "
            "It cites one allowlisted page, shows the source date, and refuses advice, "
            "performance claims, and personal data."
        ),
        "problem": (
            "A fund chat that can invent a return, compare schemes, or accept a PAN "
            "is not a facts product. The useful version has to stop before the model runs."
        ),
        "decision": (
            "Answers stay inside 15 public Groww.in HDFC pages. Advice, returns, "
            "rankings, and personal data take fixed safe responses. A factual answer "
            "is at most three sentences, with one Groww link, a last-updated date, "
            "and a verbatim proof passage."
        ),
        "proof": [
            "Corpus is 15 curated Groww.in pages. Performance questions link to the HDFC factsheet catalogue and that catalogue is not ingested.",
            "PAN, Aadhaar, phone, email, OTP, and folio numbers are blocked before any model call. They are not logged or cached.",
            "Streamlit and FastAPI both call the same chat service, so the guard order is identical.",
            "Request path: PII check, intent routing, retrieval, generation, deterministic validation, then cache. Only validated factual answers are cached.",
        ],
        "stack": ["Python", "FastAPI", "Streamlit", "Chroma", "Groq"],
        "repo": f"{GITHUB}/groww-ai-hdfc-mf-facts",
        "demo": None,
        "page": "pages/overview_fund_facts.py",
        "image": None,
    },
    {
        "slug": "retail",
        "title": "Multimodal Retail Assistant",
        "eyebrow": "Catalogue search",
        "summary": (
            "A shopping assistant over 44,417 fashion products. Shoppers search with "
            "words or a photo. Retrieval stays on the machine. Gemini writes a caption "
            "or a note only when a key is set, and only about products that were retrieved."
        ),
        "problem": (
            "Keyword search fails when a shopper has a photo, or a description, and "
            "does not know the product name. A generative answer that is not tied to "
            "the catalogue is worse."
        ),
        "decision": (
            "The default path is a local lexical index, so the first search does not "
            "encode 44,000 documents. Semantic FAISS is optional and off until the "
            "index is built. The app runs with no API key. Prices are absent from "
            "the dataset, so the UI does not offer a price filter."
        ),
        "proof": [
            "Catalogue: Fashion Product Images, 44,417 products, in data/styles_cleaned.csv.",
            "Interactive search uses TF–IDF over product text, with extra weight on colour, article type, gender, and name.",
            "A repeat of the same query is served from memory. The first build of the lexical index is about two seconds; later matches are typically well under a second.",
            "Semantic search uses MiniLM and FAISS after scripts/build_index.py. Gemini is limited to image captions and free-form styling notes.",
        ],
        "stack": ["Python", "Streamlit", "TF–IDF", "FAISS", "Gemini"],
        "repo": f"{GITHUB}/multimodal-rag-product-search",
        "demo": "https://multimodal-rag-pro-search.streamlit.app/",
        "page": "pages/overview_retail.py",
        "image": "products/retail_assistant/rag_cover.jpg",
    },
    {
        "slug": "voice",
        "title": "Quiet Push-to-Talk",
        "eyebrow": "Voice input",
        "summary": (
            "A browser prototype of hold-to-talk for a chat app. The person holds "
            "the mic, speaks softly, reviews the words in silence, and only then sends. "
            "Speech on the page is simulated."
        ),
        "problem": (
            "Talking to a phone in public is awkward. A voice button that sends as "
            "soon as you let go leaves no moment to fix a wrong word."
        ),
        "decision": (
            "The mic stays where a chat mic already is. A nudge appears once, and "
            "only after a long or slow typed prompt. Text stays hidden while the "
            "pointer is down and appears on release. Nothing is sent until Send."
        ),
        "proof": [
            "One static page. No server, no speech API, and no audio leaves the browser.",
            "Hold, slide up to cancel, and a short hold is rejected. Those are pointer events, not a recording.",
            "The review line is a fixed sample sentence. One underlined word can be corrected before send.",
            "Published with GitHub Pages from the voice-input-prototype repository.",
        ],
        "stack": ["HTML", "CSS", "JavaScript"],
        "repo": f"{GITHUB}/voice-input-prototype",
        "demo": "https://noira-khan.github.io/voice-input-prototype/",
        "page": "pages/overview_voice.py",
        "image": None,
    },
]


def by_slug(slug: str) -> dict:
    for project in PROJECTS:
        if project["slug"] == slug:
            return project
    raise KeyError(slug)
