import streamlit as st
from src.config import WHATSAPP_URL

def render():
    st.markdown("""
    <div class="sec-lbl">What We Offer</div>
    <div class="sec-title">Our Services</div>
    <p class="sec-sub">First-time customer? Enjoy exclusive introductory prices.</p>
    """, unsafe_allow_html=True)
    
    services = [
        ("🧺", "Clothes Washing",   29, 39, 10, True,  "Fresh, clean laundry picked up and delivered to your door."),
        ("💆", "Body Therapy",      99,149, 50, True,  "Rejuvenating full-body therapy by certified professionals."),
        ("💆‍♂️","Head Massage",    49, 79, 30, True,  "Soothing scalp massage to relieve tension and refresh your mind."),
        ("👔", "Washing + Ironing", 59, 79, 20, False, "Complete laundry — washed, perfectly ironed, ready to wear."),
    ]
    
    cols = st.columns(4, gap="medium")
    for col, (emoji, title, new, old, save, ft, desc) in zip(cols, services):
        note = '<div class="c-note">* First-time customer price</div>' if ft else ""
        col.markdown(f"""
        <div class="card">
          <div class="c-emoji">{emoji}</div>
          <div class="c-title">{title}</div>
          <div class="c-prices">
            <span class="p-new">₹{new}</span>
            <span class="p-old">₹{old}</span>
            <span class="save">Save ₹{save}</span>
          </div>
          {note}
          <div class="c-desc">{desc}</div>
          <a href="{WHATSAPP_URL}" target="_blank" class="btn">Order Now →</a>
        </div>
        """, unsafe_allow_html=True)
