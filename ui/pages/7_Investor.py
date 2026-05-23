"""
7_Investor.py — WhollyPaws Investor Brief
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import streamlit as st
import ui.style as style

st.set_page_config(
    page_title="WhollyPaws — Investor Brief",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

style.inject()
style.brand_nav()
style.page_header(
    "Investor Brief",
    "WhollyPaws™ — The four-legged life plan that pays you back."
)

st.html("""
<div style='margin-bottom:1.5rem;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#8C5E1A;margin-bottom:6px;'>The Opportunity</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.7rem;
             color:#5C3A0E;margin:0 0 0.75rem;'>
    Pet households are among the highest<br />discretionary overspenders in retail.
  </h2>
  <p style='color:#6B5240;font-size:0.95rem;max-width:620px;line-height:1.8;'>
    67% of US households own a pet. They overspend on pet food by an estimated $400–$800/year
    through brand loyalty, size-confusion (cost per ounce vs. bag price), and ignoring
    cross-store pricing. Pets also have health constraints — grain-free, breed-specific,
    vet-prescribed diets — that make the constraint engine a hard requirement, not an option.
    No existing pet savings tool handles this combination correctly.
  </p>
</div>
""")

c1, c2, c3, c4 = st.columns(4, gap="medium")
stats = [
    ("$150B+", "US pet industry annual spend — food alone is $65B and growing"),
    ("$600+",  "Average household overspend on pet food vs. optimal unit pricing"),
    ("67%",    "Of US households own at least one pet — 90M+ households addressable"),
    ("$19/mo", "Full Paws tier vs. $600+/yr in recoverable pet supply savings"),
]
for col, (num, label) in zip([c1, c2, c3, c4], stats):
    with col:
        st.html(f"""
        <div class='wp-stat'>
          <div class='wp-stat-num'>{num}</div>
          <div class='wp-stat-label'>{label}</div>
        </div>
        """)

st.html("<div style='height:1.5rem;'></div>")

st.html("""
<div style='background:linear-gradient(135deg,#3D2208 0%,#5C3A0E 100%);
            border-radius:12px;padding:2.25rem;margin-bottom:1.5rem;'>
  <p style='font-size:0.7rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;
            color:#E0A86A;margin-bottom:0.75rem;'>Platform Thesis</p>
  <blockquote style='font-family:Fraunces,serif;font-weight:300;font-size:1.25rem;
                     font-style:italic;color:#FFFFFF;line-height:1.6;margin:0;'>
    "WhollyPaws applies the same Sincere Strategy constraint engine — already validated
     in the food vertical — to pet supply spending. Breed, species, life-stage, and
     ingredient filters run before price comparison. The moat is identical.
     The market is $150B and largely untouched by honest price intelligence."
  </blockquote>
  <p style='color:rgba(255,255,255,0.4);font-size:0.8rem;margin-top:1rem;'>
    — Sentir Solutions® founding thesis
  </p>
</div>
""")

st.html("""
<div style='margin-bottom:1rem;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#8C5E1A;margin-bottom:6px;'>Competitive Landscape</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.5rem;
             color:#5C3A0E;margin:0;'>
    Why no existing tool gets this right.
  </h2>
</div>
""")

m1, m2 = st.columns(2, gap="medium")
moat = [
    ("Chewy Autoship is one store", "Chewy's autoship is convenient but single-store. WhollyPaws is cross-store — and accounts for the delivery fee vs. in-store gas cost math that Autoship never shows."),
    ("No tool filters on breed/ingredient first", "Rakuten, Honey, and price-comparison tools compare whatever is for sale. WhollyPaws removes anything that fails the pet profile constraint before showing a single price."),
    ("Pet food unit pricing is deliberately confusing", "A 40lb bag looks cheaper than a 15lb bag. WhollyPaws normalizes to cost-per-ounce, cost-per-day, and cost-per-calorie across every store — the comparison that actually matters."),
    ("Vet diet support doesn't exist in savings tools", "Prescription and vet-recommended diets are a significant category ($8B+). WhollyPaws flags these and checks availability — no competitor handles this at all."),
]
for i, (title, body) in enumerate(moat):
    col = m1 if i % 2 == 0 else m2
    with col:
        st.html(f"""
        <div style='background:#FFFFFF;border:1px solid #E8D8C4;border-left:3px solid #C47D2E;
                    border-radius:6px;padding:1.25rem 1.5rem;margin-bottom:1rem;'>
          <h4 style='font-size:0.92rem;font-weight:600;color:#5C3A0E;margin-bottom:0.4rem;'>{title}</h4>
          <p style='font-size:0.85rem;color:#6B5240;line-height:1.75;margin:0;'>{body}</p>
        </div>
        """)

st.html("<div style='height:1.5rem;'></div>")

r1, r2, r3 = st.columns(3, gap="medium")
phases = [
    ("Phase 1–2 — Prerequisite", "#E8D8C4",
     "WhollyFare and WhollyWare validate the Sincere Strategy engine. Circular ingestion, constraint logic, Found Money math — proven in two verticals first."),
    ("Phase 3 — WhollyPaws Launch", "#5C3A0E",
     "Same engine, pet-specific constraints added. Chewy API + PetSmart/Petco circular parsing. Breed library, ingredient exclusion database, life-stage logic."),
    ("Phase 4 — Scale", "#8C5E1A",
     "National. Tractor Supply, Costco pet section, Amazon pet. Vet network B2B licensing — practices can recommend WhollyPaws to clients with dietary needs. $1M+ ARR."),
]
for col, (title, color, desc) in zip([r1, r2, r3], phases):
    with col:
        st.html(f"""
        <div style='background:#FFFFFF;border:1px solid #E8D8C4;border-top:4px solid {color};
                    border-radius:10px;padding:1.5rem;'>
          <h4 style='font-size:0.9rem;font-weight:600;color:#5C3A0E;margin-bottom:0.6rem;'>{title}</h4>
          <p style='font-size:0.85rem;color:#6B5240;line-height:1.75;margin:0;'>{desc}</p>
        </div>
        """)

st.html("<div style='height:1.5rem;'></div>")

st.html("""
<div style='background:#FBF6F0;border:1px solid #E8D8C4;border-radius:12px;
            padding:2.25rem;text-align:center;'>
  <h3 style='font-family:Fraunces,serif;font-weight:300;font-size:1.5rem;
             color:#5C3A0E;margin:0 0 0.75rem;'>
    Interested in the WhollyPaws opportunity?
  </h3>
  <p style='color:#6B5240;font-size:0.9rem;max-width:420px;margin:0 auto 1.25rem;'>
    WhollyPaws is part of the Sentir Solutions® portfolio. Investment inquiries
    cover the full platform — WhollyFare, WhollyWare, WhollyPaws, and WhollyCare.
  </p>
  <a href="mailto:tim.hislop@gmail.com?subject=WhollyPaws%20Investor%20Inquiry"
     style='display:inline-block;background:#5C3A0E;color:#FFFFFF;text-decoration:none;
            font-size:0.9rem;font-weight:600;padding:11px 28px;border-radius:8px;'>
    tim.hislop@gmail.com
  </a>
  <p style='color:#A89080;font-size:0.78rem;margin-top:1rem;'>
    See the full portfolio at
    <a href="https://sentir-solutions.com" target="_blank"
       style="color:#8C5E1A;text-decoration:none;">sentir-solutions.com</a>
  </p>
</div>
""")
