"""Muhammad Tayseer Wadiwala — portfolio. Router and global config only."""

from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Muhammad Tayseer Wadiwala — Supply Chain Analytics",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(f"<style>{Path('assets/style.css').read_text()}</style>", unsafe_allow_html=True)

pages = st.navigation(
    [
        st.Page("app_pages/home.py", title="Home", default=True),
        st.Page("app_pages/experience.py", title="Experience"),
        st.Page("app_pages/projects.py", title="Projects"),
        st.Page("app_pages/bullseye.py", title="Live model"),
        st.Page("app_pages/about.py", title="About"),
    ],
    position="top",
)

pages.run()
