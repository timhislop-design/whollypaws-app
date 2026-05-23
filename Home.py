"""
Home.py — WhollyPaws Landing Page
Run with:  streamlit run Home.py
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

import streamlit as st
import ui.style as style

st.set_page_config(
    page_title="WhollyPaws — Smart Pet Savings",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

style.inject()
style.brand_nav()

# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════
st.html("""
<div style='position:relative;overflow:hidden;
            background:linear-gradient(140deg,#3D2208 0%,#5C3A0E 55%,#8C5E1A 100%);
            border-radius:18px;padding:54px 52px 50px;margin-bottom:20px;'>

  <!-- Decorative paw, right side -->
  <svg style='position:absolute;right:60px;top:50%;transform:translateY(-55%);
              opacity:0.10;pointer-events:none;'
       width="200" height="200" viewBox="0 0 48 48" fill="none"
       xmlns="http://www.w3.org/2000/svg">
    <ellipse cx="24" cy="30" rx="10" ry="9" fill="white"/>
    <ellipse cx="12" cy="20" rx="4.5" ry="6" fill="white"/>
    <ellipse cx="20" cy="15" rx="4.5" ry="6" fill="white"/>
    <ellipse cx="28" cy="15" rx="4.5" ry="6" fill="white"/>
    <ellipse cx="36" cy="20" rx="4.5" ry="6" fill="white"/>
  </svg>

  <!-- Badge -->
  <div style='display:inline-flex;align-items:center;gap:7px;
              background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.18);
              border-radius:20px;padding:5px 14px;margin-bottom:20px;'>
    <span style='width:7px;height:7px;background:#C47D2E;border-radius:50%;
                 display:inline-block;'></span>
    <span style='font-size:0.72rem;font-weight:600;letter-spacing:0.1em;
                 text-transform:uppercase;color:rgba(255,255,255,0.85);'>
      Pet price intelligence &nbsp;·&nbsp; Constraint-aware savings
    </span>
  </div>

  <!-- Headline -->
  <h1 style='font-family:Fraunces,serif;font-weight:300;font-size:clamp(1.9rem,3.5vw,2.9rem);
             color:#FFFFFF;line-height:1.2;margin:0 0 14px;max-width:560px;'>
    Your pet has needs.<br />WhollyPaws makes sure<br /><em style='color:#E0A86A;'>savings never override them.</em>
  </h1>

  <p style='font-size:1.05rem;color:rgba(255,255,255,0.75);max-width:500px;
            line-height:1.8;margin-bottom:28px;'>
    WhollyPaws cross-compares pet food, treats, and supply prices across
    Chewy, PetSmart, Petco, and Tractor Supply — filtered by your pet's
    species, breed, age, size, and ingredient sensitivities. Always safe first.
  </p>

  <!-- Tagline -->
  <div style='display:inline-block;background:rgba(232,124,42,0.18);
              border:1px solid rgba(232,124,42,0.35);border-radius:8px;
              padding:10px 20px;margin-bottom:28px;'>
    <span style='font-family:Fraunces,serif;font-style:italic;font-size:1.1rem;
                 color:#F4A96A;font-weight:300;'>
      The four-legged life plan that pays you back.
    </span>
  </div>

  <div style='display:flex;gap:12px;flex-wrap:wrap;'>
    <a href="#" style='display:inline-block;background:#E87C2A;color:#FFFFFF;
                       text-decoration:none;font-size:0.9rem;font-weight:600;
                       padding:12px 28px;border-radius:8px;letter-spacing:0.02em;'>
      Join the Waitlist
    </a>
    <a href="https://sentir-solutions.com" target="_blank"
       style='display:inline-block;background:rgba(255,255,255,0.1);color:#FFFFFF;
              border:1px solid rgba(255,255,255,0.25);text-decoration:none;
              font-size:0.9rem;font-weight:400;padding:12px 24px;border-radius:8px;'>
      About Sentir Solutions →
    </a>
  </div>
</div>
""")

# ══════════════════════════════════════════════════════════════════════════════
# PETS HAVE CONSTRAINTS TOO
# ══════════════════════════════════════════════════════════════════════════════
st.html("""
<div style='margin-bottom:8px;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#8C5E1A;margin-bottom:6px;'>The Constraint Engine</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.8rem;
             color:#5C3A0E;margin:0 0 6px;'>Pets have allergens too.</h2>
  <p style='color:#6B5240;font-size:0.95rem;max-width:520px;'>
    WhollyPaws runs pet-specific constraints before the price optimizer —
    just like WhollyFare does for human households.
  </p>
</div>
""")

col1, col2, col3 = st.columns(3, gap="medium")

constraints = [
    ("Species & Breed", "#5C3A0E",
     "Dog vs. cat vs. small animal. Breed-appropriate formulas. Size and weight class. Large-breed puppy calcium ratios. Breed sensitivities (Bulldogs, Westies, etc.)."),
    ("Ingredient Filters", "#8C5E1A",
     "Grain-free, chicken-free, fish-free, beef-free. No-corn/wheat/soy. Single-protein. Limited ingredient. All run as hard rules — never traded for a better price."),
    ("Life Stage", "#C47D2E",
     "Puppy, adult, senior. Kitten, adult cat, senior cat. Prescription diet flags. Dental health formulas. The right food for where your pet is in life."),
]

for col, (title, color, desc) in zip([col1, col2, col3], constraints):
    with col:
        st.html(f"""
        <div class='wp-card' style='background:#FFFFFF;border:1px solid #E8D8C4;
                                    border-top:3px solid {color};border-radius:10px;
                                    padding:1.75rem;height:100%;'>
          <h3 style='font-size:1rem;font-weight:600;color:#5C3A0E;margin-bottom:0.6rem;'>
            {title}
          </h3>
          <p style='font-size:0.87rem;color:#6B5240;line-height:1.75;'>{desc}</p>
        </div>
        """)

st.html("<div style='height:2rem;'></div>")

# ══════════════════════════════════════════════════════════════════════════════
# HOW IT WORKS
# ══════════════════════════════════════════════════════════════════════════════
st.html("""
<div style='margin-bottom:8px;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#8C5E1A;margin-bottom:6px;'>How It Works</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.8rem;
             color:#5C3A0E;margin:0 0 6px;'>Safe first. Savings second.</h2>
</div>
""")

s1, s2, s3, s4 = st.columns(4, gap="medium")

steps = [
    ("01", "Set up your pet", "Species, breed, age, weight, and any ingredient sensitivities or vet-prescribed restrictions."),
    ("02", "We filter first", "Constraint engine removes anything that doesn't fit your pet's profile — before prices are ever compared."),
    ("03", "Cross-store pricing", "What's left is cross-compared across Chewy, PetSmart, Petco, Tractor Supply — by unit weight, not bag size."),
    ("04", "Your savings list", "One list, per store, with net Found Money shown — delivery fees or gas costs included."),
]

for col, (num, title, desc) in zip([s1, s2, s3, s4], steps):
    with col:
        st.html(f"""
        <div class='wp-card' style='background:#FFFFFF;border:1px solid #E8D8C4;
                                    border-top:3px solid #C47D2E;border-radius:10px;
                                    padding:1.5rem;'>
          <div style='font-family:Fraunces,serif;font-size:1.8rem;font-weight:300;
                      color:#E8D8C4;margin-bottom:0.75rem;'>{num}</div>
          <h4 style='font-size:0.92rem;font-weight:600;color:#5C3A0E;
                     margin-bottom:0.4rem;'>{title}</h4>
          <p style='font-size:0.84rem;color:#6B5240;line-height:1.7;'>{desc}</p>
        </div>
        """)

st.html("<div style='height:2rem;'></div>")

# ══════════════════════════════════════════════════════════════════════════════
# PRICING
# ══════════════════════════════════════════════════════════════════════════════
st.html("""
<div style='margin-bottom:8px;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#8C5E1A;margin-bottom:6px;'>Pricing</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.8rem;
             color:#5C3A0E;margin:0 0 6px;'>Start free. Stay honest.</h2>
</div>
""")

p1, p2, p3, p4 = st.columns(4, gap="medium")

tiers = [
    ("Price Finder",    "Free",   "forever",
     "Cross-store unit-price comparison for pet food and supplies. Always free."),
    ("Paws Tracker",    "$5/mo",  "per household",
     "Auto-track your regular brands. Buy-off alerts when your pet's food goes on sale."),
    ("Health Guard",    "$12/mo", "per household",
     "Hard constraint engine — breed, ingredient, life-stage filters. Safety before savings, always."),
    ("Full Paws",       "$19/mo", "per household",
     "Multi-pet profiles, supply history, vet diet tracking, Chewy Autoship optimizer."),
]

for col, (name, price, period, desc) in zip([p1, p2, p3, p4], tiers):
    with col:
        st.html(f"""
        <div class='wp-card' style='background:#FFFFFF;border:1px solid #E8D8C4;
                                    border-top:3px solid #C47D2E;border-radius:10px;
                                    padding:1.75rem;'>
          <p class='wp-tier-name'>{name}</p>
          <div class='wp-tier-price'>{price}</div>
          <p style='font-size:0.78rem;color:#A89080;'>{period}</p>
          <p style='font-size:0.87rem;color:#6B5240;line-height:1.7;margin-top:0.75rem;'>{desc}</p>
        </div>
        """)

st.html("<div style='height:2rem;'></div>")

# ══════════════════════════════════════════════════════════════════════════════
# SINCERE STRATEGY
# ══════════════════════════════════════════════════════════════════════════════
st.html("""
<div style='background:linear-gradient(135deg,#3D2208 0%,#5C3A0E 100%);
            border-radius:14px;padding:2.5rem;margin-bottom:20px;'>
  <p style='font-size:0.7rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;
            color:#E0A86A;margin-bottom:1rem;'>The Sincere Strategy®</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.6rem;
             color:#FFFFFF;margin:0 0 1rem;line-height:1.3;'>
    No brand can pay to appear in your pet's food plan.<br />
    <em style='color:#E0A86A;'>Not one. Ever.</em>
  </h2>
  <div style='display:flex;flex-wrap:wrap;gap:8px;margin-top:1.25rem;'>
    <span class='wp-sincere'>Zero paid placements — ever</span>
    <span class='wp-sincere'>Health & ingredient filters are hard rules</span>
    <span class='wp-sincere'>Net savings shown — delivery fees included</span>
    <span class='wp-sincere'>Your pet data is never sold or targeted</span>
    <span class='wp-sincere'>Subscription-only revenue</span>
  </div>
  <p style='color:rgba(255,255,255,0.4);font-size:0.8rem;margin-top:1.5rem;'>
    A <a href="https://sentir-solutions.com" target="_blank"
         style="color:#E0A86A;text-decoration:none;font-weight:500;">Sentir Solutions®</a> company ·
    wholly-paws.com · Coming 2026
  </p>
</div>
""")

# ══════════════════════════════════════════════════════════════════════════════
# CTA
# ══════════════════════════════════════════════════════════════════════════════
st.html("""
<div style='background:#FFFFFF;border:1px solid #E8D8C4;border-radius:14px;
            padding:2.5rem;text-align:center;margin-bottom:20px;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.16em;text-transform:uppercase;
            color:#8C5E1A;margin-bottom:0.75rem;'>Coming Soon — 2026</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.8rem;
             color:#5C3A0E;margin:0 0 0.75rem;'>
    Be first to know when WhollyPaws launches.
  </h2>
  <p style='color:#6B5240;font-size:0.95rem;max-width:460px;margin:0 auto 1.5rem;'>
    We're building WhollyPaws after WhollyFare and WhollyWare prove the Sincere Strategy
    platform. Join the waitlist and we'll reach out when your area goes live.
  </p>
  <a href="mailto:tim.hislop@gmail.com?subject=WhollyPaws%20Waitlist"
     style='display:inline-block;background:#E87C2A;color:#FFFFFF;text-decoration:none;
            font-size:0.9rem;font-weight:600;padding:12px 32px;border-radius:8px;'>
    Join the Waitlist →
  </a>
</div>
""")

st.html("""
<div style='text-align:center;padding:1.5rem;color:#A89080;font-size:0.8rem;'>
  WhollyPaws™ · A <a href="https://sentir-solutions.com" target="_blank"
  style="color:#8C5E1A;text-decoration:none;">Sentir Solutions®</a> Company ·
  Charlottesville, VA ·
  <a href="mailto:tim.hislop@gmail.com" style="color:#8C5E1A;text-decoration:none;">
    tim.hislop@gmail.com
  </a>
</div>
""")
