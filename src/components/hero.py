import streamlit as st
from src.config import WHATSAPP_URL

def render():
    st.markdown(f"""
    <div class="hero">
      <div class="badge">✦ Home Services</div>
      <div class="h1">Flabil</div>
      <div class="tagline">Clean. Relax. Repeat.</div>
      <div class="sub">We handle your daily needs — so you don't have to.</div>
      <a href="{WHATSAPP_URL}" target="_blank" class="btn" style="display:inline-block;width:auto;padding:.82rem 2.2rem;font-size:.92rem;">💬 &nbsp;Chat on WhatsApp</a>
      <div class="divider"></div>
    </div>
    """, unsafe_allow_html=True)
