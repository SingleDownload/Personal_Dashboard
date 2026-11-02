# Muhammad Tayseer Wadiwala — Portfolio

Live portfolio site built on Streamlit. Supply chain analytics, UAE/GCC focus.

**Signature feature:** the Logistics Bullseye micro-fulfilment siting model runs live
on the site — visitors adjust AHP criteria weights and watch the zone ranking respond.

## Structure

```
├── streamlit_app.py        # Router: top navigation, five pages
├── components.py           # STAR card, secondary card, section helpers
├── data/
│   ├── portfolio.py        # ALL page content (edit text here)
│   └── zones.py            # Simulated demo data for the live model
├── app_pages/
│   ├── home.py             # Positioning + headline results
│   ├── experience.py       # WAFA, Sanbook in STAR layout
│   ├── projects.py         # Filterable STAR cards + supporting work
│   ├── bullseye.py         # Live model: presets, sliders, ranking
│   └── about.py            # Contact, skills, education
├── assets/                 # style.css, lab images, certificate
└── .streamlit/config.toml  # Theme
```

## Updating content

Everything a visitor reads lives in `data/portfolio.py`. Add a project by appending a
dict with `situation`, `task`, `action`, `result`; it renders as a STAR card automatically.
Set `category` to one of `CATEGORIES` so the filter picks it up.

## Run locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy (Streamlit Community Cloud)

1. Push this repo to GitHub (public or private).
2. Go to share.streamlit.io → **New app** → select the repo, branch `main`,
   entry point `streamlit_app.py`.
3. Your site goes live at `https://<app-name>.streamlit.app`.
4. Optional: buy a domain and set a redirect to the Streamlit URL for a cleaner
   link on your resume.

**Cold-start note:** free-tier apps sleep after inactivity. The app is kept
deliberately light (no heavy imports at module scope) so wake-up is fast; visiting
your own link the morning of an interview day re-warms it.

## Updating content

- New project → add a `card(...)` block in `app_pages/projects.py`
- New metric → edit the metrics section in `app_pages/home.py`
- Zone data / weights for the demo → `data/zones.py`
