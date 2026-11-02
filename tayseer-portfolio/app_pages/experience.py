import streamlit as st

from components import divider, section, star_card
from data.portfolio import EXPERIENCE

section("Professional experience")
st.title("Experience")
st.markdown("Each role in the same shape: **Situation → Task → Action → Result**.")
divider()

for role in EXPERIENCE:
    star_card(role)
