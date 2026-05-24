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

# ── Hero ──────────────────────────────────────────────────────────────────────
st.html("""
<div style='background:linear-gradient(160deg,#1E0E00 0%,#3D2208 60%,#1E0E00 100%);
            border-radius:16px;padding:52px 44px 44px;color:white;margin-bottom:2rem;'>
  <p style='font-size:0.7rem;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;
            color:#E0A86A;margin-bottom:14px;'>WhollyPaws™ · Sentir Solutions® LLC · Charlottesville, VA</p>
  <h1 style='font-size:2.8rem;font-weight:800;color:#fff;margin:0 0 12px;line-height:1.1;
             letter-spacing:-0.02em;'>$150B. Zero honest<br>price intelligence. Until now.</h1>
  <p style='font-size:1.05rem;color:rgba(255,255,255,0.72);max-width:620px;line-height:1.65;margin-bottom:2rem;'>
    67% of US households own a pet. They overspend by an estimated $400–$800 per year
    through brand loyalty, size confusion, and single-store habit. Pets also have real
    health constraints — grain-free, breed-specific, vet-prescribed diets — that make
    the constraint engine a hard requirement, not a feature. No existing tool handles both.
  </p>
  <div style='display:flex;gap:18px;flex-wrap:wrap;'>
    <div style='background:rgba(255,255,255,0.06);border:1px solid rgba(224,168,106,0.25);
                border-radius:10px;padding:18px 24px;min-width:140px;flex:1;'>
      <div style='font-size:1.9rem;font-weight:800;color:#E87C2A;line-height:1.1;'>$150B+</div>
      <div style='font-size:0.75rem;color:rgba(255,255,255,0.5);margin-top:5px;line-height:1.4;'>
        US pet industry annual spend — food alone is $65B and growing
      </div>
    </div>
    <div style='background:rgba(255,255,255,0.06);border:1px solid rgba(224,168,106,0.25);
                border-radius:10px;padding:18px 24px;min-width:140px;flex:1;'>
      <div style='font-size:1.9rem;font-weight:800;color:#E87C2A;line-height:1.1;'>$600+</div>
      <div style='font-size:0.75rem;color:rgba(255,255,255,0.5);margin-top:5px;line-height:1.4;'>
        Average household overspend on pet food vs. optimal unit pricing
      </div>
    </div>
    <div style='background:rgba(255,255,255,0.06);border:1px solid rgba(224,168,106,0.25);
                border-radius:10px;padding:18px 24px;min-width:140px;flex:1;'>
      <div style='font-size:1.9rem;font-weight:800;color:#E87C2A;line-height:1.1;'>90M+</div>
      <div style='font-size:0.75rem;color:rgba(255,255,255,0.5);margin-top:5px;line-height:1.4;'>
        US pet-owning households — 67% of all households, addressable immediately
      </div>
    </div>
    <div style='background:rgba(255,255,255,0.06);border:1px solid rgba(224,168,106,0.25);
                border-radius:10px;padding:18px 24px;min-width:140px;flex:1;'>
      <div style='font-size:1.9rem;font-weight:800;color:#E87C2A;line-height:1.1;'>$8B+</div>
      <div style='font-size:0.75rem;color:rgba(255,255,255,0.5);margin-top:5px;line-height:1.4;'>
        Prescription and vet-recommended pet diets — a category no savings tool touches
      </div>
    </div>
  </div>
</div>
""")

# ── Platform foundation ───────────────────────────────────────────────────────
st.html("""
<div style='background:linear-gradient(135deg,#3D2208 0%,#5C3A0E 100%);
            border-radius:12px;padding:2.25rem;margin-bottom:1.5rem;'>
  <p style='font-size:0.7rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;
            color:#E0A86A;margin-bottom:0.75rem;'>Platform Foundation</p>
  <blockquote style='font-family:Fraunces,serif;font-weight:300;font-size:1.2rem;
                     font-style:italic;color:#FFFFFF;line-height:1.6;margin:0 0 1rem;'>
    "WhollyPaws applies the same Sincere Strategy constraint engine — already validated
     in the food vertical by WhollyFare — to pet supply spending. Breed, species, life-stage,
     and ingredient filters run before price comparison. The moat is identical.
     The market is $150B and largely untouched by honest price intelligence."
  </blockquote>
  <p style='color:rgba(255,255,255,0.5);font-size:0.82rem;line-height:1.6;margin:0;'>
    WhollyFare is in active pilot — Tim Hislop's family, four Charlottesville grocers, weekly receipts.
    The platform compounds: every vertical that launches is built on a proven, shared foundation.
  </p>
</div>
""")

# ── Why Now ───────────────────────────────────────────────────────────────────
st.html("""
<div style='margin-bottom:1rem;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#8C5E1A;margin-bottom:6px;'>Why Now</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.5rem;
             color:#5C3A0E;margin:0 0 0.5rem;'>
    Three forces converging in the pet market.
  </h2>
</div>
""")

wn1, wn2, wn3 = st.columns(3, gap="medium")
for col, icon, title, body in [
    (wn1, "📈", "Pet food inflation + recall anxiety",
     "Pet food prices rose 17%+ since 2020. Three major recalls since 2022 have made ingredient awareness a priority for pet owners — not a nice-to-have. Constraint-first is exactly what this market needs."),
    (wn2, "🐾", "Pet humanization trend is accelerating",
     "Pet owners increasingly treat pets like family members — same premium health standards, same scrutiny of ingredients. The household that uses Health Guard for their child wants the same engine for their dog."),
    (wn3, "🏪", "Chewy and PetSmart dominate but don't compete on price",
     "Chewy's autoship is convenient. PetSmart's loyalty program is opaque. Neither shows you what the same product costs at Costco, Tractor Supply, or your local grocery. That gap is WhollyPaws."),
]:
    with col:
        st.html(f"""
        <div style='background:#fff;border-radius:10px;padding:1.4rem 1.2rem;
                    border:1px solid #E8D8C4;border-top:4px solid #8C5E1A;
                    box-shadow:0 2px 10px rgba(0,0,0,0.05);'>
          <div style='font-size:1.4rem;margin-bottom:8px;'>{icon}</div>
          <div style='font-size:0.92rem;font-weight:700;color:#5C3A0E;margin-bottom:6px;'>{title}</div>
          <div style='font-size:0.83rem;color:#6B5240;line-height:1.6;'>{body}</div>
        </div>
        """)

st.html("<div style='height:1.5rem;'></div>")

# ── Sincere Strategy ──────────────────────────────────────────────────────────
st.html("""
<div style='margin-bottom:1rem;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#8C5E1A;margin-bottom:6px;'>The Sincere Strategy®</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.5rem;
             color:#5C3A0E;margin:0 0 0.5rem;'>
    Six commitments. Every Wholly brand. No exceptions.
  </h2>
  <p style='color:#6B5240;font-size:0.9rem;max-width:620px;line-height:1.7;'>
    Pet owners who manage grain-free, breed-specific, or vet-prescribed diets have been failed
    by every price-comparison tool that exists. WhollyPaws is built from the ground up to serve
    them first — constraint engine before price engine, always.
  </p>
</div>
""")

s1, s2 = st.columns(2, gap="medium")
sincere = [
    ("🚫 No paid placements",
     "Hill's, Purina, and Royal Canin cannot pay to appear in a recommendation. Chewy's affiliate model is built on exactly this. WhollyPaws cannot adopt it without becoming what it replaced."),
    ("🛡️ Pet health constraints are sacrosanct",
     "If a dog is grain-free, grain appears in zero results. If a cat has a vet-prescribed diet, that constraint is the engine's highest-priority input. Not a filter — a hard wall."),
    ("💰 Net savings, always shown",
     "Delivery fee from Chewy vs. trip cost to Tractor Supply — shown honestly, side by side. No 'you saved $X' without the full picture. The pet owner decides with open eyes."),
    ("🔍 Every rejection logged",
     "If a product was filtered out because of an ingredient flag, the owner can see it. Radical transparency is not just a principle — it is the safety audit trail for households managing recalls."),
    ("📍 Local and national, honestly",
     "WhollyPaws shows what's available at your Petco, your Walmart, your Costco, and Chewy — this week, at actual prices. Not national averages. Not sponsored inventory."),
    ("🔐 Pet health data owned by the household",
     "Breed, diet profile, vet prescription history — this is sensitive data. WhollyPaws does not sell it to Hill's, Purina, or any brand. Subscription revenue only. Ever."),
]
for i, (title, body) in enumerate(sincere):
    col = s1 if i % 2 == 0 else s2
    with col:
        st.html(f"""
        <div style='background:#fff;border:1px solid #E8D8C4;border-left:4px solid #C47D2E;
                    border-radius:6px;padding:1.1rem 1.4rem;margin-bottom:0.85rem;
                    box-shadow:0 2px 8px rgba(0,0,0,0.04);'>
          <div style='font-size:0.92rem;font-weight:700;color:#5C3A0E;margin-bottom:4px;'>{title}</div>
          <div style='font-size:0.83rem;color:#6B5240;line-height:1.65;'>{body}</div>
        </div>
        """)

st.html("""
<div style='background:#FBF6EE;border:1px solid #E0C4A0;border-radius:10px;
            padding:14px 22px;margin-top:4px;font-size:0.88rem;
            color:#5C3A0E;font-weight:600;line-height:1.55;'>
  Chewy's autoship, PetSmart Treats, and pet food affiliate sites cannot adopt the Sincere Strategy
  without eliminating the brand partnership revenue that funds their operations.
  That asymmetry is permanent.
</div>
""")

st.html("<div style='height:1.5rem;'></div>")

# ── Competitive landscape ─────────────────────────────────────────────────────
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
    ("Chewy Autoship is one store — and never shows trip cost math",
     "Chewy's autoship is convenient but single-store. WhollyPaws is cross-store — and accounts for the delivery fee vs. in-store trip cost math that Autoship never shows. The honest comparison often favors Costco."),
    ("No tool filters on breed or ingredient first",
     "Rakuten, Honey, and pet deal sites compare whatever is for sale. WhollyPaws removes anything that fails the pet's profile — grain, protein source, life-stage — before showing a single price."),
    ("Pet food unit pricing is deliberately confusing",
     "A 40lb bag looks cheaper than a 15lb bag. WhollyPaws normalizes to cost-per-ounce, cost-per-day, and cost-per-calorie across every store. That is the comparison that actually matters."),
    ("Vet diet support does not exist in any savings tool",
     "Prescription and vet-recommended diets are a $8B+ category. WhollyPaws tracks availability across stores and flags when a vet diet is on sale somewhere the household hasn't checked. No competitor touches this."),
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

# ── Why Tim ───────────────────────────────────────────────────────────────────
st.html("""
<div style='background:linear-gradient(160deg,#1E0E00,#3D2208);border:1px solid #8C5E1A;
            border-radius:12px;padding:2rem 2.25rem;margin-bottom:1.5rem;'>
  <p style='font-size:0.7rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;
            color:#E0A86A;margin-bottom:0.75rem;'>The Founder</p>
  <p style='font-family:Fraunces,serif;font-weight:300;font-size:1.1rem;
            font-style:italic;color:#FFFFFF;line-height:1.6;margin:0 0 1rem;'>
    "The same engine that builds my family's weekly meal plan from real sale circulars
     can build a smarter, safer, more honest shopping plan for every pet household in America.
     The constraint logic is already written. The platform is already proven."
  </p>
  <p style='color:rgba(255,255,255,0.55);font-size:0.83rem;line-height:1.65;margin:0;'>
    Tim Hislop · Founder, Sentir Solutions® LLC · Full-time at ECS · Building nights and weekends ·
    WhollyFare pilot running now in Charlottesville, VA. WhollyPaws is the same codebase applied to
    the $150B pet vertical. The infrastructure investment is already made.
  </p>
</div>
""")

# ── Roadmap ───────────────────────────────────────────────────────────────────
st.html("""
<div style='margin-bottom:1rem;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#8C5E1A;margin-bottom:6px;'>Roadmap</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.5rem;
             color:#5C3A0E;margin:0;'>Built on WhollyFare's proven foundation.</h2>
</div>
""")

r1, r2, r3 = st.columns(3, gap="medium")
phases = [
    ("Phase 1–2 — Prerequisite", "#E8D8C4",
     "WhollyFare and WhollyWare validate the Sincere Strategy engine. Circular ingestion, constraint logic, Found Money math — proven in two verticals before WhollyPaws launches."),
    ("Phase 3 — WhollyPaws Launch", "#5C3A0E",
     "Same engine, pet-specific constraints added. Chewy API + PetSmart/Petco circular parsing. Breed library, ingredient exclusion database, life-stage logic. Vet diet availability tracking."),
    ("Phase 4 — Scale", "#8C5E1A",
     "National. Tractor Supply, Costco pet section, Amazon pet. Vet network B2B licensing — practices recommend WhollyPaws to clients managing dietary needs. $1M+ ARR. The most defensible pet savings tool in the market."),
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

# ── Close ─────────────────────────────────────────────────────────────────────
st.html("""
<div style='background:#FBF6F0;border:1px solid #E8D8C4;border-radius:12px;
            padding:2.25rem;text-align:center;'>
  <h3 style='font-family:Fraunces,serif;font-weight:300;font-size:1.4rem;
             color:#5C3A0E;margin:0 0 0.6rem;'>
    90M pet households. One honest tool. WhollyPaws.
  </h3>
  <p style='color:#6B5240;font-size:0.88rem;max-width:480px;margin:0 auto 1.25rem;line-height:1.7;'>
    WhollyFare is in pilot now. The engine is proven. WhollyPaws is the same engine
    applied to the $150B pet vertical. Investment inquiries cover the full Sentir Solutions® portfolio.
  </p>
  <a href="mailto:tim.hislop@gmail.com?subject=WhollyPaws%20Investor%20Inquiry"
     style='display:inline-block;background:#5C3A0E;color:#FFFFFF;text-decoration:none;
            font-size:0.9rem;font-weight:600;padding:11px 28px;border-radius:8px;'>
    tim.hislop@gmail.com
  </a>
  <p style='color:#A89080;font-size:0.78rem;margin-top:1rem;'>
    Full portfolio at
    <a href="https://sentir-solutions.com" target="_blank"
       style="color:#8C5E1A;text-decoration:none;">sentir-solutions.com</a>
  </p>
</div>
""")
