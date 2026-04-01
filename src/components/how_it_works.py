import streamlit as st

def render():
    st.markdown("""
    <div style="margin-top:3rem;">
      <div class="sec-lbl">Process</div>
      <div class="sec-title">How It Works</div>
      <p class="sec-sub">Three simple steps to a cleaner, happier you.</p>
      <div class="steps">
        <div class="step"><div class="s-circle">💬</div><div class="s-title">1. Chat with Us</div><div class="s-desc">Reach out on WhatsApp and tell us what you need.</div></div>
        <div class="step"><div class="s-circle">📅</div><div class="s-title">2. Pick a Slot</div><div class="s-desc">Choose a convenient time and we'll be there.</div></div>
        <div class="step"><div class="s-circle">✨</div><div class="s-title">3. Sit Back & Enjoy</div><div class="s-desc">We handle everything. You just relax.</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)
