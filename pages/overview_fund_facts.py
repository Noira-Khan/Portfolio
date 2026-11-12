import streamlit as st

from components.layout import Layout
from components.navbar import navbar
from components.project_card import project_links
from data.projects import by_slug

project = by_slug("fund-facts")

Layout.setup(page_title=project["title"])
navbar()

st.title(project["title"])
st.markdown(f"### {project['eyebrow']}")
st.write(project["summary"])
project_links(project)

st.divider()
st.header("Problem")
st.write(project["problem"])

st.header("Product decision")
st.write(project["decision"])

st.header("What the repository enforces")
for item in project["proof"]:
    st.markdown(f"- {item}")

st.header("Schemes in the corpus")
st.write(
    "Primary chat schemes are HDFC Large Cap, HDFC Flexi Cap, HDFC Mid Cap, "
    "and HDFC ELSS Tax Saver. The other Groww pages in the list of 15 widen "
    "AMC context. Questions outside that corpus get a not-in-sources response."
)

st.header("Response types")
st.markdown(
    """
| Type | When it is used |
| --- | --- |
| answer | A validated fact, one link, a date, and a proof passage |
| refusal_advice | The question asks for a buy, sell, hold, or recommendation |
| refusal_performance | The question asks for returns, a comparison, or a ranking |
| pii | Personal data was detected. The input is not echoed or stored |
| not_in_sources | The fact is outside the corpus or failed validation |
| clarify | A scheme-sensitive question did not name a scheme |
"""
)

st.header("How a question moves")
st.markdown(
    """
1. PII detection runs in plain code. A match returns a fixed warning and stops.
2. Intent routing sends advice and performance questions to fixed responses.
3. Retrieval pulls only from the curated Groww pages.
4. The model may use that context. Retrieved text is data, not instructions.
5. Validation checks sentence count, the URL, advice and performance phrases, number grounding, verbatim proof, and PII echo.
6. Invalid output gets one repair attempt, then a safe not-in-sources response.
7. Only a validated factual answer is cached. The cache key is a hash of the question and an optional scheme.
"""
)

st.header("Stack")
st.write(" · ".join(project["stack"]))
st.caption(
    "The model id and provider key stay in environment variables or Streamlit secrets. "
    "They are not in the repository."
)

st.divider()
project_links(project)
