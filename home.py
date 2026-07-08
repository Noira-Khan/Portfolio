# ==========================================================
# home.py
# AI Product Manager Portfolio
# ==========================================================

from turtle import st

from components.layout import Layout
from components.navbar import navbar
from components.hero import hero
from components.about import about
from components.contact_section import contact_section
import streamlit as st
# ----------------------------------------------------------
# PAGE SETUP
# ----------------------------------------------------------

Layout.setup()

# ----------------------------------------------------------
# PAGE COMPONENTS
# ----------------------------------------------------------

navbar()

hero()

about()

contact_section()




