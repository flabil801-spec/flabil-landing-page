CSS_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; background: #fff !important; color: #0a0a0a; }
#MainMenu, footer, header { visibility: hidden !important; display: none !important; }
.stDeployButton, [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stHeader"] { display: none !important; }
[class^="viewerBadge"], [class*="viewerBadge"] { display: none !important; opacity: 0 !important; }
a[href*="streamlit.io/cloud"] { display: none !important; opacity: 0 !important; }
div[data-testid="stAppViewContainer"] > div:last-child { display: none !important; }
@media (max-width: 768px) {
    #MainMenu, footer, header, .stDeployButton, [data-testid="stToolbar"], [class*="viewerBadge"], a[href*="streamlit.io/cloud"] {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
    }
}
.block-container { padding-top: 1.5rem !important; max-width: 1080px !important; }
.hero { text-align: center; padding: 3.5rem 1rem 1rem; }
.badge { display: inline-block; font-size: .72rem; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; border: 1.5px solid #0a0a0a; border-radius: 100px; padding: .28rem .9rem; margin-bottom: 1.2rem; }
.h1 { font-size: clamp(3.2rem,9vw,6.5rem); font-weight: 900; letter-spacing: -.03em; line-height: 1; margin: 0 0 .5rem; }
.tagline { font-size: clamp(1rem,3vw,1.5rem); font-weight: 300; letter-spacing: .05em; color: #444; }
.sub { font-size: .95rem; color: #888; margin: .4rem 0 1.8rem; }
.divider { width: 56px; height: 3px; background: #0a0a0a; border-radius: 2px; margin: 2rem auto; }
.trust { display: flex; justify-content: center; gap: 2.5rem; flex-wrap: wrap; padding: 1.6rem 1rem; border-top: 1.5px solid #f0f0f0; border-bottom: 1.5px solid #f0f0f0; margin: 1.5rem 0 2.5rem; }
.trust-num { font-size: 1.5rem; font-weight: 900; display: block; }
.trust-lbl { font-size: .68rem; color: #888; text-transform: uppercase; letter-spacing: .08em; }
.sec-lbl { text-align: center; font-size: .68rem; font-weight: 700; letter-spacing: .2em; text-transform: uppercase; color: #888; }
.sec-title { text-align: center; font-size: clamp(1.4rem,4vw,2.1rem); font-weight: 800; letter-spacing: -.02em; margin: .2rem 0 .3rem; }
.sec-sub { text-align: center; font-size: .9rem; color: #888; margin-bottom: 2rem; }
.card { border: 1.5px solid #0a0a0a; border-radius: 18px; padding: 1.7rem 1.5rem 1.5rem; display: flex; flex-direction: column; gap: .8rem; height: 100%; transition: box-shadow .2s, transform .2s; }
.card:hover { box-shadow: 6px 6px 0 #0a0a0a; transform: translate(-3px,-3px); }
.c-emoji { font-size: 2rem; }
.c-title { font-size: 1.05rem; font-weight: 700; }
.c-prices { display: flex; align-items: baseline; gap: .5rem; flex-wrap: wrap; }
.p-new { font-size: 1.55rem; font-weight: 900; }
.p-old { font-size: .9rem; color: #aaa; text-decoration: line-through; }
.save { font-size: .66rem; font-weight: 700; background: #0a0a0a; color: #fff; border-radius: 100px; padding: .2rem .6rem; }
.c-note { font-size: .7rem; color: #bbb; font-style: italic; }
.c-desc { font-size: .83rem; color: #666; line-height: 1.55; flex: 1; }
.btn { display: block; width: 100%; padding: .72rem 1rem; font-family: 'Inter',sans-serif; font-size: .85rem; font-weight: 700; letter-spacing: .05em; text-align: center; text-decoration: none; color: #fff; background: #0a0a0a; border: 2px solid #0a0a0a; border-radius: 12px; margin-top: auto; transition: background .2s, color .2s; }
.btn:hover { background: #fff; color: #0a0a0a; }
.steps { display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-top: 1.4rem; }
.step { text-align: center; max-width: 190px; }
.s-circle { width: 50px; height: 50px; border: 2px solid #0a0a0a; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; margin: 0 auto .65rem; }
.s-title { font-size: .88rem; font-weight: 700; margin-bottom: .15rem; }
.s-desc { font-size: .73rem; color: #777; }
.cta { background: #0a0a0a; color: #fff; text-align: center; border-radius: 18px; padding: 2.5rem 1.5rem; margin: 3rem 0 2rem; }
.cta h2 { font-size: clamp(1.3rem,3.5vw,1.9rem); font-weight: 800; margin: 0 0 .5rem; color: #fff; }
.cta p { font-size: .9rem; color: #aaa; margin: 0 0 1.3rem; }
.cta-btn { display: inline-block; padding: .82rem 2rem; font-family: 'Inter',sans-serif; font-size: .9rem; font-weight: 700; letter-spacing: .04em; text-decoration: none; color: #0a0a0a; background: #fff; border-radius: 12px; }
.footer { text-align: center; padding: 2rem 1rem 1rem; font-size: .78rem; color: #bbb; border-top: 1.5px solid #f0f0f0; margin-top: 1.5rem; }
.footer strong { color: #0a0a0a; }
.footer a { color: #0a0a0a; text-decoration: none; }
</style>
"""
