"""Logistics Bullseye — live demonstration model with branded sliders and presets."""

import altair as alt
import pandas as pd
import streamlit as st

from components import divider, section
from data.zones import CRITERIA, DEFAULT_WEIGHTS, ZONE_SCORES

PRESETS = {
    "Expert AHP": DEFAULT_WEIGHTS,
    "Demand-led": {"demand": 0.55, "travel": 0.25, "zoning": 0.12, "energy": 0.08},
    "Speed-led": {"demand": 0.25, "travel": 0.55, "zoning": 0.12, "energy": 0.08},
    "Compliance-led": {"demand": 0.20, "travel": 0.20, "zoning": 0.45, "energy": 0.15},
}

for k in CRITERIA:
    st.session_state.setdefault(f"w_{k}", int(DEFAULT_WEIGHTS[k] * 100))


def apply_preset():
    name = st.session_state.get("preset")
    if name:
        for k, v in PRESETS[name].items():
            st.session_state[f"w_{k}"] = int(round(v * 100))


section("Live demonstration model")
st.title("Logistics Bullseye")
st.markdown(
    "Where should a quick-commerce operator put a micro-fulfilment centre in Dubai? Pick a "
    "priority profile or set the weights yourself, and the zone ranking updates live. The "
    "research version uses expert-validated AHP weights (consistency ratio **0.027**)."
)
st.markdown(
    '<div class="disclosure">Zone scores are illustrative and simulated. The page demonstrates '
    "the method, not real site data.</div>",
    unsafe_allow_html=True,
)

divider()
st.subheader("1 · Set priorities")
st.pills("Preset", list(PRESETS), key="preset", on_change=apply_preset,
         selection_mode="single", default="Expert AHP")

cols = st.columns(len(CRITERIA), gap="large")
for col, (key, meta) in zip(cols, CRITERIA.items()):
    with col:
        st.slider(meta["label"], 0, 100, key=f"w_{key}", format="%d%%", help=meta["help"])

raw = {k: st.session_state[f"w_{k}"] for k in CRITERIA}
total = sum(raw.values())
if total == 0:
    st.warning("Give at least one criterion a non-zero weight.")
    st.stop()
weights = {k: v / total for k, v in raw.items()}
st.caption("Normalised: " + " · ".join(f"{CRITERIA[k]['label']} {weights[k]:.0%}" for k in CRITERIA))

divider()
st.subheader("2 · Ranking")

df = pd.DataFrame(ZONE_SCORES).set_index("zone")
df["Weighted score"] = sum(df[k] * w for k, w in weights.items())
ranked = df.sort_values("Weighted score", ascending=False)

left, right = st.columns([1, 2], gap="large")
with left:
    for i, (label, cls) in enumerate([("Top-ranked zone", "zone-tile top"), ("Runner-up", "zone-tile")]):
        st.markdown(
            f'<div class="{cls}"><div class="k">{label}</div>'
            f'<div class="v">{ranked.index[i]}</div>'
            f'<div class="s">score {ranked["Weighted score"].iloc[i]:.3f}</div></div>',
            unsafe_allow_html=True,
        )
with right:
    chart_df = ranked.reset_index()[["zone", "Weighted score"]]
    chart = (
        alt.Chart(chart_df)
        .mark_bar(color="#0F4C81", cornerRadiusEnd=3)
        .encode(
            x=alt.X("Weighted score:Q", title="Weighted score", scale=alt.Scale(domain=[0, 1])),
            y=alt.Y("zone:N", sort="-x", title=None, axis=alt.Axis(labelLimit=240)),
            tooltip=["zone", alt.Tooltip("Weighted score:Q", format=".3f")],
        )
        .properties(height=260)
    )
    st.altair_chart(chart, width="stretch")

with st.expander("Full score matrix"):
    st.dataframe(ranked.rename(columns={k: CRITERIA[k]["label"] for k in CRITERIA})
                 .style.format("{:.3f}"), width="stretch")

divider()
st.subheader("3 · Research version vs this demo")
st.markdown(
    """
| Stage | Research version | This demo |
|---|---|---|
| Criteria | Four clusters from literature and practitioner interviews | Same four |
| Weighting | AHP pairwise comparisons, CR = 0.027 | Presets or your sliders |
| Zone scores | Assessed per sub-criterion | Simulated |
| Ranking | Weighted sum, cross-checked with TOPSIS and WASPAS | Weighted sum |

In the demonstration model, the optimally sited zone projected up to an **18% delivery-time
improvement** over a rent-first baseline. That is a modelled figure, not a field measurement.
"""
)
