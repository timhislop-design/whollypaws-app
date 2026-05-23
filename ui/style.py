"""
style.py — WhollyPaws brand styles
Warm amber palette. inject() must be called on every page after st.set_page_config().
"""

import streamlit as st

DARK    = "#5C3A0E"   # deep amber
MID     = "#8C5E1A"   # mid amber
ACCENT  = "#C47D2E"   # accent amber
LIGHT   = "#E0A86A"   # light amber
BG      = "#FBF6F0"   # warm cream
FOUND   = "#E87C2A"   # Found Money orange

BRAND_NAME   = "WhollyPaws™"
BRAND_DOMAIN = "wholly-paws.com"
TAGLINE      = "The four-legged life plan that pays you back."
PARENT_URL   = "https://sentir-solutions.com"


def inject():
    st.html(f"""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;1,9..144,300&family=Inter:wght@300;400;500;600&display=swap');

      :root {{
        --wp-dark:   {DARK};
        --wp-mid:    {MID};
        --wp-accent: {ACCENT};
        --wp-light:  {LIGHT};
        --wp-bg:     {BG};
        --wp-found:  {FOUND};
      }}

      [data-testid="stAppViewContainer"] > .main {{
        background: var(--wp-bg) !important;
      }}
      .block-container {{ padding-top: 0.5rem !important; }}
      [data-testid="stSidebarNav"] {{ display: none !important; }}
      header[data-testid="stHeader"] {{ display: none !important; }}

      .wp-card {{
        transition: transform 0.18s ease, box-shadow 0.18s ease !important;
      }}
      .wp-card:hover {{
        transform: translateY(-4px) !important;
        box-shadow: 0 14px 40px rgba(92,58,14,0.13) !important;
      }}

      .wp-tier-price {{
        font-family: 'Fraunces', serif;
        font-size: 2.2rem;
        font-weight: 300;
        color: var(--wp-dark);
        line-height: 1;
        margin: 0.5rem 0 0.25rem;
      }}

      .wp-tier-name {{
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: var(--wp-accent);
        margin-bottom: 0.25rem;
      }}

      .wp-stat {{
        background: #FFFFFF;
        border: 1px solid #E8D8C4;
        border-left: 3px solid var(--wp-found);
        padding: 1.25rem 1.5rem;
        border-radius: 6px;
      }}

      .wp-stat-num {{
        font-family: 'Fraunces', serif;
        font-size: 2.2rem;
        font-weight: 300;
        color: var(--wp-dark);
        line-height: 1;
      }}

      .wp-stat-label {{
        font-size: 0.82rem;
        color: #6B5240;
        margin-top: 0.3rem;
        line-height: 1.5;
      }}

      .wp-sincere {{
        display: inline-block;
        background: rgba(255,255,255,0.08);
        color: rgba(255,255,255,0.8);
        font-size: 0.72rem;
        font-weight: 500;
        padding: 4px 12px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.12);
        margin: 2px;
      }}
    </style>
    """)


def page_header(title: str, subtitle: str = ""):
    sub_html = f"<p style='color:{LIGHT};font-size:0.95rem;margin-top:0.5rem;'>{subtitle}</p>" if subtitle else ""
    st.html(f"""
    <div style='background:linear-gradient(135deg,{DARK} 0%,{MID} 100%);
                padding:2.5rem 2rem 2rem;border-radius:12px;margin-bottom:1.5rem;'>
      <p style='font-size:0.7rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;
                color:{LIGHT};margin-bottom:0.5rem;'>WhollyPaws™</p>
      <h1 style='font-family:Fraunces,serif;font-weight:300;font-size:2rem;
                 color:#FFFFFF;margin:0;line-height:1.2;'>{title}</h1>
      {sub_html}
    </div>
    """)


def brand_nav():
    st.html(f"""
    <div style='display:flex;align-items:center;gap:10px;margin-bottom:16px;
                padding:10px 18px;background:#FFFFFF;
                border-radius:10px;border:1px solid #E8D8C4;'>
      <svg width="28" height="28" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <ellipse cx="24" cy="30" rx="8" ry="7" fill="{DARK}" opacity="0.9"/>
        <ellipse cx="14" cy="22" rx="3.5" ry="4.5" fill="{MID}" opacity="0.75"/>
        <ellipse cx="21" cy="18" rx="3.5" ry="4.5" fill="{MID}" opacity="0.75"/>
        <ellipse cx="27" cy="18" rx="3.5" ry="4.5" fill="{MID}" opacity="0.75"/>
        <ellipse cx="34" cy="22" rx="3.5" ry="4.5" fill="{MID}" opacity="0.75"/>
      </svg>
      <span style='font-size:1rem;font-weight:700;color:{DARK};'>WhollyPaws™</span>
      <span style='color:#D8C4A8;margin:0 4px;'>·</span>
      <span style='font-size:0.8rem;color:#666;'>a
        <a href="{PARENT_URL}" target="_blank"
           style="color:{MID};font-weight:600;text-decoration:none;">Sentir Solutions</a>® Company</span>
    </div>
    """)
