import streamlit as st

from src.styles import CSS_STYLES
from src.components import hero, trust, services, how_it_works, footer

st.set_page_config(page_title="Flabil – Clean. Relax. Repeat.", page_icon="🧺", layout="wide")

st.markdown(CSS_STYLES, unsafe_allow_html=True)

hero.render()
trust.render_trust_banner()
services.render()
how_it_works.render()
footer.render()
