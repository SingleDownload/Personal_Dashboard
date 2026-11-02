"""All portfolio content in one place.

Every entry is rendered by components.star_card(). Edit text here, not in the pages.
Rules kept throughout: modelled figures are labelled as projections, estimates as
estimates, and team work says "with the team".
"""

EXPERIENCE = [
    {
        "title": "Analyst Intern",
        "org": "WAFA Biological Laboratory, Dubai",
        "dates": "Jan 2025 – Jul 2025",
        "badge": None,
        "situation": "Certification requests moved through the lab with no shared view of status. "
                     "Some finished reports sat undelivered for months, and clients had not paid "
                     "on accounts still open.",
        "task": "Bring order to the certification and calibration workflow so reports reached "
                "clients on time and open accounts could close.",
        "action": "Built a centralised certification tracker used by 4 people across 2 "
                  "accounts-department teams, matched against the accounts team's records. "
                  "Tested 50+ samples, checked 100+ calibration certificates for accuracy before "
                  "issue, and followed up on certificate delivery.",
        "result": "Turnaround cut from ~10 days to ~3. Reports up to a year old were sent out, "
                  "and clients paid once they received them.",
        "tags": ["Process tracking", "Quality checks", "Calibration", "Accounts follow-up"],
        "extra": "On one client calibration trip, two of us finished in about a week against an "
                 "estimated 10 days for one person.",
        "disclosure": "The calibration-trip comparison is an estimate from a single occasion. "
                      "Client details are withheld.",
    },
    {
        "title": "Auditing Intern",
        "org": "Sanbook Quality Consultancy, Dubai",
        "dates": "Jun 2023 – Aug 2023",
        "badge": None,
        "situation": "The consultancy ran external ISO 9001 compliance audits for client companies "
                     "and briefed its leadership on industry positioning.",
        "task": "Support the audit team on a live client audit and contribute to leadership "
                "communications.",
        "action": "Went with the audit team to a client site. Spotted an unclean waste-disposal "
                  "area during the walk-through. Completed ISO-standard quality management "
                  "training. Wrote the business pitch script for the CEO's opening address at an "
                  "industry conclave.",
        "result": "My waste-disposal observation became a team recommendation for cleaner disposal "
                  "methods. The CEO delivered my script at the conclave.",
        "tags": ["ISO 9001", "Audit support", "Business writing"],
        "extra": None,
        "disclosure": "Audit carried out as part of a team. Client identity withheld.",
    },
]


PROJECTS = [
    # ---------------- Supply chain & logistics
    {
        "id": "bullseye",
        "category": "Supply chain",
        "title": "Logistics Bullseye: siting micro-fulfilment centres in Dubai",
        "org": "Industry Business Research · SP Jain",
        "dates": "Oct 2025 – Jun 2026",
        "badge": None,
        "situation": "E-commerce quick-commerce operators in Dubai often site micro-fulfilment "
                     "centres on rent and instinct, locking in years of delivery-time penalties.",
        "task": "Build a defensible, repeatable framework for choosing MFC locations.",
        "action": "Defined four criterion clusters (demand density, congestion-adjusted travel "
                  "time, zoning feasibility, energy context). Weighted them with AHP, validated "
                  "through interviews with two industry practitioners (consistency ratio 0.027). "
                  "Cross-checked rankings with TOPSIS and WASPAS and shipped a five-tab Streamlit "
                  "dashboard.",
        "result": "Up to 18% faster deliveries for optimally sited MFCs versus a rent-first "
                  "baseline (modelled projection).",
        "tags": ["AHP", "TOPSIS", "WASPAS", "Python", "Streamlit"],
        "disclosure": "The 18% figure is a projection from a model run on simulated data, not a "
                      "measured result.",
        "link_live_model": True,
    },
    {
        "id": "touche",
        "category": "Supply chain",
        "title": "Touché Royale: upstream supply chain readiness for UAE entry",
        "org": "Graduate Industry Project · Team 1 · SP Jain",
        "dates": "Completed Sep 2026",
        "badge": "Completed",
        "situation": "An Indian gemstone-infused luxury fragrance brand planned to enter the UAE. "
                     "Its sourcing, compliance, and inbound logistics had to be ready before launch.",
        "task": "Assess upstream readiness and give the founder a clear view of inbound costs.",
        "action": "Ran an eight-dimension readiness assessment covering raw materials, regulatory "
                  "compliance (CITES, ESMA/MoIAT), and inbound logistics through a dynamic "
                  "capabilities lens, prioritised with TOPSIS. Built a simulated landed-cost "
                  "dashboard for the founder comparing total cost across shipping methods.",
        "result": "Delivered a client-facing research report and presentation with a phased, "
                  "trigger-based growth roadmap and the landed-cost dashboard.",
        "tags": ["Readiness assessment", "TOPSIS", "Landed cost", "Regulatory"],
        "disclosure": "Landed-cost figures in the dashboard are simulated. Client findings are "
                      "summarised, not reproduced.",
    },
    # ---------------- Venture & marketing
    {
        "id": "saharasoil",
        "category": "Venture and marketing",
        "title": "Saharasoil: circular-economy soil amendment venture",
        "org": "Entrepreneurship for a Disruptive Launch · Group 10 · SP Jain",
        "dates": "2025–26",
        "badge": "1st place · pitch",
        "situation": "UAE corporate plantscaping relies on imported growing media, while camel "
                     "manure is a local waste stream.",
        "task": "Design a B2B venture turning that waste into a soil amendment, and pitch it.",
        "action": "Built the business model and the 12-quarter financial model (unit economics, "
                  "ramp, funding), plus the Lean Canvas and stakeholder map. Modelled a peak cash "
                  "trough of ~AED 556K and EBITDA-positive in Year 3 Q4.",
        "result": "First Place in the Business Pitch Presentation, EDL Showcase 2025–26, with a "
                  "validated AED 150K ask for an MVP phase.",
        "tags": ["Venture design", "Financial modelling", "Pitching", "Circular economy"],
        "disclosure": "Financial figures are projections from an academic venture plan.",
        "certificate": True,
    },
    # ---------------- Strategy & research
    {
        "id": "lego",
        "category": "Strategy and research",
        "title": "LEGO and rPET: when the sustainable option isn't",
        "org": "Business Ethics · Group 10 · SP Jain",
        "dates": "2025–26",
        "badge": None,
        "situation": "LEGO dropped its recycled-PET brick programme and drew criticism for it.",
        "task": "Judge whether the decision was ethically defensible.",
        "action": "Compared lifecycle emissions and framed the call as a consequentialist "
                  "resolution between visible sustainability and actual outcomes.",
        "result": "Argued, with lifecycle evidence, that abandoning rPET was the lower-emission "
                  "choice.",
        "tags": ["Sustainability", "Lifecycle thinking", "Ethics"],
    },
    # ---------------- Analytics
    {
        "id": "ml",
        "category": "Analytics",
        "title": "Consumer analytics dashboard: eight ML models compared",
        "org": "Data Analytics coursework · SP Jain",
        "dates": "2025–26",
        "badge": None,
        "situation": "A sustainable leaf-cutlery concept needed evidence on who would buy it.",
        "task": "Turn survey data into a decision-ready view of demand.",
        "action": "Ran the full pipeline: survey design, dataset, eight ML algorithms on one "
                  "prediction task, results shipped as a Streamlit dashboard.",
        "result": "A repeatable survey-to-dashboard pipeline, since reused on other concepts.",
        "tags": ["Python", "scikit-learn", "Streamlit"],
    },
]


# Compact secondary cards (no forced STAR grid)
SECONDARY = [
    {
        "category": "Strategy and research",
        "kind": "Coursework · group project",
        "title": "Middle East 2035: Almarai and the Hormuz question",
        "org": "Adaptability Challenge PBL · SP Jain",
        "body": "Scenario: the Strait of Hormuz reopens but below full capacity. Our team chose "
                "Almarai and built a board presentation and CEO Adaptability Dashboard on routing "
                "and sourcing alternatives that cut dependence on Hormuz, using only official or "
                "high-reliability public data.",
        "tags": ["GCC supply risk", "Scenario planning", "Dashboard"],
    },
    {
        "category": "Engineering",
        "kind": "Secondary research · literature review",
        "title": "Type 1 collagen and its role in wound healing",
        "org": "Design Project (BIOT F376) · BITS Pilani, Dubai · Dec 2024",
        "body": "A structured review of ten sources covering collagen structure, synthesis and "
                "MMP/TIMP-regulated turnover, its role across the four healing phases, and "
                "collagen-nanoparticle scaffolds for chronic wounds. No original data.",
        "tags": ["Literature review", "Technical synthesis"],
    },
]


# Bio-cement is original lab work, so it gets a full STAR card in Engineering.
PROJECTS.append({
    "id": "biocement",
    "category": "Engineering",
    "title": "Screening ureolytic bacteria for bio-cement",
    "org": "Lab Project (BIOT F366) · BITS Pilani, Dubai",
    "dates": "Feb – Jun 2024",
    "badge": None,
    "situation": "Portland cement is carbon-intensive. Bio-cement via microbially induced calcite "
                 "precipitation only works with an organism proven to do it.",
    "task": "Find and validate calcite-precipitating bacteria from 11 preserved cultures.",
    "action": "Ran a gated screen: viability and purity, urease activity on Christensen's agar, "
              "precipitation in liquid medium, then two independent checks (phenol red, flame "
              "test). Tested 2% vs 8% urea and logged the shaking-vs-static incubator confound "
              "rather than claiming a clean result.",
    "result": "11 candidates narrowed to 3 validated isolates, banked in duplicate storage "
              "(slants at −4 °C, triplicate glycerol vials at −80 °C).",
    "tags": ["Screening funnel", "Experimental design", "Protocol and traceability"],
    "disclosure": "Faculty-supervised. Characterisation was qualitative.",
    "lab_evidence": True,
})


CATEGORIES = ["All", "Supply chain", "Venture and marketing", "Strategy and research",
              "Analytics", "Engineering"]
