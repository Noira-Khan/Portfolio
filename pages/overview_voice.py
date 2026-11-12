import streamlit as st

from components.layout import Layout
from components.navbar import navbar
from components.project_card import project_links
from data.projects import by_slug

project = by_slug("voice")

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

st.header("What the prototype actually does")
for item in project["proof"]:
    st.markdown(f"- {item}")

st.header("Screens")
st.markdown(
    """
1. **Chat.** The mic is the existing chat mic. After a long typed prompt, one nudge offers hold-to-talk. Short prompts do not get the nudge.
2. **Hold.** Pointer down starts a listening state. Text stays masked. Sliding up cancels. A hold shorter than the threshold does not continue.
3. **Review.** The sample transcript appears. One word is marked for a tap-to-fix. Send is a separate control.
4. **Done.** The sent line and a reply appear only after Send. A short confirmation says voice worked.
"""
)

st.header("Why speech is simulated")
st.write(
    "This page is an interaction prototype. The transcript is a fixed sentence in the "
    "script, so a reviewer can judge the hold, the cancel, the hidden text, and the "
    "review step without a microphone permission or a speech vendor. A later build "
    "can replace that sentence with a recognizer. The send gate stays."
)

st.header("Stack")
st.write(" · ".join(project["stack"]))

st.divider()
project_links(project)
