import streamlit as st

from components import divider, secondary_card, section, star_card
from data.portfolio import CATEGORIES, PROJECTS, SECONDARY

section("Portfolio")
st.title("Projects")
st.markdown("Filter by area. Every project is laid out as **Situation → Task → Action → Result**.")

choice = st.pills(
    "Filter projects",
    CATEGORIES,
    default="All",
    selection_mode="single",
    label_visibility="collapsed",
    key="project_filter",
) or "All"

divider()


def funnel():
    st.markdown(
        """
<svg viewBox="0 0 560 100" xmlns="http://www.w3.org/2000/svg" role="img"
     aria-label="Screening funnel: 11 candidates to 3 validated isolates"
     style="width:100%;height:auto;max-width:520px;">
  <line x1="18" y1="30" x2="542" y2="30" stroke="#C7D2DE" stroke-width="2" stroke-dasharray="5 4"/>
  <g font-family="Inter, sans-serif" text-anchor="middle">
    <circle cx="46" cy="30" r="20" fill="#fff" stroke="#C7D2DE" stroke-width="1.5"/>
    <text x="46" y="37" font-size="19" font-weight="700" fill="#0F4C81">11</text>
    <text x="46" y="68" font-size="10" font-weight="600" fill="#131C26">Preserved slants</text>
    <text x="140" y="22" font-size="9" fill="#5B6B7C">viability and purity</text>
    <circle cx="234" cy="30" r="20" fill="#fff" stroke="#C7D2DE" stroke-width="1.5"/>
    <text x="234" y="37" font-size="19" font-weight="700" fill="#0F4C81">4</text>
    <text x="234" y="68" font-size="10" font-weight="600" fill="#131C26">Pure cultures</text>
    <text x="234" y="81" font-size="9" fill="#5B6B7C">7 cut</text>
    <text x="328" y="22" font-size="9" fill="#5B6B7C">urease screen</text>
    <circle cx="422" cy="30" r="20" fill="#fff" stroke="#C7D2DE" stroke-width="1.5"/>
    <text x="422" y="37" font-size="19" font-weight="700" fill="#0F4C81">3</text>
    <text x="422" y="68" font-size="10" font-weight="600" fill="#131C26">Urease positive</text>
    <text x="422" y="81" font-size="9" fill="#5B6B7C">1 cut</text>
    <text x="470" y="22" font-size="9" fill="#5B6B7C">verify</text>
    <circle cx="518" cy="30" r="20" fill="#0F4C81"/>
    <text x="518" y="37" font-size="19" font-weight="700" fill="#fff">3</text>
    <text x="518" y="68" font-size="10" font-weight="600" fill="#131C26">Validated</text>
  </g>
</svg>
        """,
        unsafe_allow_html=True,
    )
    c1, c2, _ = st.columns([1, 1, 2])
    c1.image("assets/micp_urease_plate.jpg", caption="Urease screen: agar turns pink.",
             width="stretch")
    c2.image("assets/micp_flame_test.jpg", caption="Flame test: brick-red confirms calcium.",
             width="stretch")


def certificate():
    c, _ = st.columns([2, 1])
    c.image("assets/edl_certificate.jpg", width="stretch")


def evidence_for(p):
    if p.get("lab_evidence"):
        return funnel
    if p.get("certificate"):
        return certificate
    return None


shown = 0
for p in PROJECTS:
    if choice != "All" and p["category"] != choice:
        continue
    star_card(p, evidence=evidence_for(p))
    if p.get("link_live_model"):
        st.page_link("app_pages/bullseye.py", label="▶ Run the live siting model")
    shown += 1

secondaries = [s for s in SECONDARY if choice in ("All", s["category"])]
if secondaries:
    section("Supporting work")
    for s in secondaries:
        secondary_card(s)
        shown += 1

if not shown:
    st.caption("Nothing in this category yet.")
