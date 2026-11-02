import streamlit as st

from components import divider, section

section("Supply chain analytics · UAE / GCC")
st.title("Muhammad Tayseer Wadiwala")

col_text, _ = st.columns([3, 1], gap="large")
with col_text:
    st.markdown(
        """
        I build **decision frameworks and analytics tools for logistics problems**:
        facility siting, inbound cost, compliance, and last-mile operations, grounded in
        the UAE and wider GCC market.

        Master of Global Business (Logistics and Supply Chain Management) at **SP Jain
        School of Global Management**, where I serve on the **Academic Committee**.
        Engineering degree from **BITS Pilani, Dubai**. I pair multi-criteria methods
        (AHP, TOPSIS, WASPAS) with Python and Streamlit, and ship analysis as tools people
        can use rather than slides they skim.
        """
    )
    b1, b2, _ = st.columns([1, 1, 2])
    b1.page_link("app_pages/projects.py", label="See projects →")
    b2.page_link("app_pages/bullseye.py", label="Try the live model →")

divider()
section("Selected results")
m1, m2, m3 = st.columns(3)
m1.metric("Certification turnaround", "10 → 3 days", "WAFA Biological Laboratory", delta_color="off")
m2.metric("Business pitch", "1st place", "SP Jain EDL Showcase 2025–26", delta_color="off")
m3.metric("Projected delivery-time gain*", "18%", "Logistics Bullseye siting model", delta_color="off")
st.markdown(
    '<div class="disclosure">* Modelled output of the Logistics Bullseye demonstration model on '
    "simulated data. A projection, not a realised result.</div>",
    unsafe_allow_html=True,
)
