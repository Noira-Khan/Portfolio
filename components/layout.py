from pathlib import Path
import streamlit as st


class Layout:

    @staticmethod
    def setup():

        st.set_page_config(
            page_title="Noira Khan | AI Product Manager",
            page_icon="",
            layout="wide",
            initial_sidebar_state="collapsed",
        )

        Layout.load_css()

    @staticmethod
    def load_css():

        base_dir = Path(__file__).resolve().parent.parent
        css_path = base_dir / "assets" / "css" / "styles.css"

        if not css_path.exists():
            raise FileNotFoundError(f"CSS file not found: {css_path}")

        st.markdown(
            f"<style>{css_path.read_text(encoding='utf-8')}</style>",
            unsafe_allow_html=True,
        )

        Layout.hide_streamlit()

    @staticmethod
    def hide_streamlit():

        st.markdown(
            """
            <style>

            #MainMenu{
                visibility:hidden;
            }

            header{
                visibility:hidden;
            }

            footer{
                visibility:hidden;
            }

            [data-testid="collapsedControl"]{
                display:none;
            }

            [data-testid="stSidebar"]{
                display:none;
            }

            </style>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
"""
<style>

header{
visibility:hidden;
}

footer{
visibility:hidden;
}

#MainMenu{
visibility:hidden;
}

</style>
""",
unsafe_allow_html=True
)
        