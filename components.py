"""Shared UI pieces: the STAR card and the compact secondary card."""

from html import escape

import streamlit as st


def _tags(tags):
    return "".join(f'<span class="tag">{escape(t)}</span>' for t in tags)


def star_card(item, evidence=None):
    """Render one project or role in STAR layout.

    evidence: optional callable that draws extra content inside the evidence expander.
    """
    badge = item.get("badge")
    badge_cls = "badge award" if badge and "place" in badge.lower() else "badge"
    badge_html = f'<span class="{badge_cls}">{escape(badge)}</span>' if badge else ""

    st.markdown(
        f"""
<div class="star">
  <div class="star-head">
    <div>
      <div class="star-title">{escape(item['title'])}</div>
      <div class="star-meta">{escape(item['org'])} · {escape(item['dates'])}</div>
    </div>
    {badge_html}
  </div>
  <div class="star-grid">
    <div class="q"><div class="q-k">Situation</div><div class="q-v">{escape(item['situation'])}</div></div>
    <div class="q"><div class="q-k">Task</div><div class="q-v">{escape(item['task'])}</div></div>
    <div class="q"><div class="q-k">Action</div><div class="q-v">{escape(item['action'])}</div></div>
    <div class="q q-result"><div class="q-k">Result</div><div class="q-v">{escape(item['result'])}</div></div>
  </div>
  <div class="star-tags">{_tags(item.get('tags', []))}</div>
</div>
        """,
        unsafe_allow_html=True,
    )

    has_more = item.get("extra") or item.get("disclosure") or evidence
    if has_more:
        with st.expander("Evidence and notes"):
            if item.get("extra"):
                st.markdown(item["extra"])
            if evidence:
                evidence()
            if item.get("disclosure"):
                st.markdown(f'<div class="disclosure">{escape(item["disclosure"])}</div>',
                            unsafe_allow_html=True)


def secondary_card(item):
    st.markdown(
        f"""
<div class="star secondary">
  <div class="kind">{escape(item['kind'])}</div>
  <div class="star-title">{escape(item['title'])}</div>
  <div class="star-meta">{escape(item['org'])}</div>
  <p class="sec-body">{escape(item['body'])}</p>
  <div class="star-tags">{_tags(item.get('tags', []))}</div>
</div>
        """,
        unsafe_allow_html=True,
    )


def section(label):
    st.markdown(f'<div class="eyebrow">{escape(label)}</div>', unsafe_allow_html=True)


def divider():
    st.markdown('<div class="route-line"></div>', unsafe_allow_html=True)
