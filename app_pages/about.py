from pathlib import Path

import streamlit as st

from components import divider, section

section("About")
st.title("About")

st.markdown(
        """
        Seeking **logistics and supply chain roles in the UAE**: distribution, operations,
        procurement, and supply chain analytics.

        - 📧 [muhammad.ms25gl109@spjain.org](mailto:muhammad.ms25gl109@spjain.org)
        - 💼 [linkedin.com/in/muhammad-tayseer-wadiwala](https://www.linkedin.com/in/muhammad-tayseer-wadiwala/)
        - 📍 Dubai, United Arab Emirates
        """
)

divider()
c1, c2, c3 = st.columns(3, gap="large")
with c1:
    st.subheader("Methods")
    st.markdown(
        '<span class="tag">AHP</span><span class="tag">TOPSIS</span><span class="tag">WASPAS</span>'
        '<span class="tag">PESTEL</span><span class="tag">Dynamic capabilities</span>'
        '<span class="tag">Landed cost</span><span class="tag">Experimental design</span>',
        unsafe_allow_html=True,
    )
with c2:
    st.subheader("Tools")
    st.markdown(
        '<span class="tag amber">Python</span><span class="tag amber">pandas / scikit-learn</span>'
        '<span class="tag amber">Streamlit</span><span class="tag amber">Excel modelling</span>'
        '<span class="tag amber">SQL</span><span class="tag amber">Google Apps Script</span>',
        unsafe_allow_html=True,
    )
with c3:
    st.subheader("Domains")
    st.markdown(
        '<span class="tag">Last-mile and MFCs</span><span class="tag">Inbound and compliance</span>'
        '<span class="tag">ISO 9001 audit support</span><span class="tag">GCC supply risk</span>'
        '<span class="tag">Circular economy</span>',
        unsafe_allow_html=True,
    )

divider()
st.subheader("Education and involvement")
st.markdown(
    """
| | |
|---|---|
| **Master of Global Business**, Logistics and Supply Chain Management | SP Jain School of Global Management, Dubai |
| **Member, Academic Committee (Acadcom)** | SP Jain School of Global Management, Dubai |
| **Bachelor of Engineering**, Biotechnology | BITS Pilani, Dubai Campus |

**First Place, Business Pitch Presentation**, Entrepreneurship for a Disruptive Launch
Showcase, SP Jain, 2025–26.
"""
)

st.caption("Professional work is described in sanitised form. Modelled figures are labelled as "
           f"projections throughout. · build {Path('VERSION').read_text().splitlines()[0]}")
