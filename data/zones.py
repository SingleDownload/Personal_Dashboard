"""Illustrative data for the live Bullseye demo.

Scores are synthetic values on a 0–1 scale, chosen to be plausible for the
zone archetypes but NOT drawn from the research dataset. Higher is better
on every criterion (travel time and regulatory friction are inverted).
"""

CRITERIA = {
    "demand": {
        "label": "Demand density",
        "help": "Residential + commercial order-generation intensity in the zone's catchment.",
    },
    "travel": {
        "label": "Travel-time reach",
        "help": "Congestion-adjusted 15-minute delivery reach (higher = better reach).",
    },
    "zoning": {
        "label": "Zoning & regulatory",
        "help": "Land-use fit and licensing pathway ease (higher = fewer barriers).",
    },
    "energy": {
        "label": "Energy & sustainability",
        "help": "Grid access, tariff context, and operating-energy profile.",
    },
}

# Expert-validated AHP weights from the research version (rounded).
DEFAULT_WEIGHTS = {
    "demand": 0.38,
    "travel": 0.32,
    "zoning": 0.18,
    "energy": 0.12,
}

# Zone archetypes — illustrative, not assessed research scores.
ZONE_SCORES = [
    {"zone": "Al Barsha (mixed-use core)", "demand": 0.86, "travel": 0.72, "zoning": 0.55, "energy": 0.60},
    {"zone": "JLT / Marina fringe", "demand": 0.90, "travel": 0.58, "zoning": 0.48, "energy": 0.62},
    {"zone": "Al Quoz (industrial)", "demand": 0.52, "travel": 0.66, "zoning": 0.92, "energy": 0.70},
    {"zone": "Deira (dense legacy urban)", "demand": 0.88, "travel": 0.49, "zoning": 0.51, "energy": 0.55},
    {"zone": "Dubai South (planned logistics)", "demand": 0.34, "travel": 0.61, "zoning": 0.95, "energy": 0.85},
    {"zone": "Business Bay edge", "demand": 0.81, "travel": 0.63, "zoning": 0.57, "energy": 0.58},
]
