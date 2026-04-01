import streamlit as st
from src.config import WHATSAPP_URL

def render():
    st.markdown(f"""
    <div class="cta">
      <h2>Ready to Experience Flabil?</h2>
      <p>Join hundreds of happy customers. Your first order comes with a special discount.</p>
      <a href="{WHATSAPP_URL}" target="_blank" class="cta-btn">💬 &nbsp;Order on WhatsApp</a>
    </div>
    <div class="footer">
      <strong>Flabil</strong> &nbsp;·&nbsp; Clean. Relax. Repeat. &nbsp;·&nbsp;
      <a href="{WHATSAPP_URL}" target="_blank">WhatsApp Us</a><br><br>
      © 2026 Flabil. All rights reserved.
    </div>
    """, unsafe_allow_html=True)
