import streamlit as st

def render_trust_banner():
    st.markdown("""
    <div class="trust">
      <div><span class="trust-num">500+</span><span class="trust-lbl">Happy Customers</span></div>
      <div><span class="trust-num">4.9 ★</span><span class="trust-lbl">Average Rating</span></div>
      <div><span class="trust-num">₹29</span><span class="trust-lbl">Starting Price</span></div>
      <div><span class="trust-num">2 hrs</span><span class="trust-lbl">Avg Service Time</span></div>
    </div>
    """, unsafe_allow_html=True)
