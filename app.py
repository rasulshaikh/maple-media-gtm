import streamlit as st

st.set_page_config(
    page_title="Maple Media — GTM Engine",
    page_icon="▣",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700;800&display=swap');

/* ── RESET ── */
html, body, [class*="css"], p, span, div, li, td, th, label {
    font-family: 'JetBrains Mono', monospace !important;
    background-color: #FFFFFF;
    color: #000000;
}

.block-container { padding: 2.5rem 2.5rem 5rem; max-width: 1080px; }

/* ── TYPE SCALE ── */
h1, h2, h3, h4 {
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #000000;
    border-radius: 0 !important;
}
h1 { font-size: 2rem; border-bottom: 4px solid #000; padding-bottom: 0.6rem; margin-bottom: 0.5rem; }
h2 { font-size: 1.1rem; letter-spacing: 0.12em; margin: 2rem 0 0.8rem; }
h3 { font-size: 0.82rem; letter-spacing: 0.14em; margin: 1.5rem 0 0.6rem; }

/* ── TOKENS AS CLASSES ── */
.ph {
    background: #000;
    color: #FFF !important;
    padding: 0.55rem 1rem;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.72rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.16em;
    margin: 1.8rem 0 1rem;
    border: 2px solid #000;
}

.badge {
    display: inline-block;
    background: #000;
    color: #FFF !important;
    font-size: 0.62rem;
    font-weight: 700;
    padding: 2px 7px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    border: 2px solid #000;
    margin: 2px 2px 2px 0;
}

.badge-outline {
    display: inline-block;
    background: #FFF;
    color: #000 !important;
    font-size: 0.62rem;
    font-weight: 700;
    padding: 2px 7px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    border: 2px solid #000;
    margin: 2px 2px 2px 0;
}

.card {
    border: 2px solid #000;
    padding: 1.2rem;
    margin: 0.6rem 0;
    background: #FFF;
    box-shadow: 4px 4px 0 0 #000;
    border-radius: 0;
}

.card-compact {
    border: 2px solid #000;
    padding: 0.6rem 0.8rem;
    margin: 0.4rem 0;
    background: #FFF;
    border-radius: 0;
}

.wiring {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.72rem;
    font-weight: 500;
    color: #000 !important;
    background: #FFF;
    padding: 0.65rem 0.9rem;
    border: 2px dashed #000;
    margin: 0.5rem 0;
    line-height: 1.7;
    letter-spacing: 0.02em;
}

.sig-label {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.68rem;
    font-weight: 800;
    color: #000 !important;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    display: block;
    margin: 1.2rem 0 0.3rem;
    border-left: 4px solid #000;
    padding-left: 0.6rem;
}

.email-body {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.82rem;
    line-height: 1.85;
    color: #000 !important;
    background: #FFF;
    padding: 1rem 1.2rem;
    border: 2px solid #000;
    box-shadow: 4px 4px 0 0 #000;
    margin: 0.4rem 0 1.2rem;
    white-space: pre-wrap;
}

.metric-box {
    border: 2px solid #000;
    padding: 1.1rem;
    text-align: center;
    box-shadow: 4px 4px 0 0 #000;
    background: #FFF;
}
.metric-val {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 1.8rem;
    font-weight: 800;
    color: #000 !important;
    letter-spacing: -0.02em;
}
.metric-lbl {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.62rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #555 !important;
    margin-top: 4px;
}

.tool-lbl {
    font-size: 0.65rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #555 !important;
}

/* ── SIDEBAR ── */
div[data-testid="stSidebar"] { background: #000 !important; }
div[data-testid="stSidebar"] * {
    color: #FFF !important;
    font-family: 'JetBrains Mono', monospace !important;
    background-color: transparent !important;
}
div[data-testid="stSidebar"] a { color: #FFF !important; text-decoration: underline; }
div[data-testid="stSidebar"] hr { border-color: #333 !important; margin: 0.8rem 0; }
div[data-testid="stSidebar"] h3 { color: #FFF !important; border: none; font-size: 0.78rem; }

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
    gap: 0;
    border-bottom: 2px solid #000;
    background: #FFF;
}
.stTabs [data-baseweb="tab"] {
    background: #FFF !important;
    border: 2px solid #000 !important;
    border-bottom: none !important;
    border-radius: 0 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 700 !important;
    font-size: 0.65rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
    padding: 0.5rem 0.85rem !important;
    margin-right: 2px !important;
    color: #000 !important;
    transition: none !important;
}
.stTabs [data-baseweb="tab"] * {
    color: #000 !important;
    background: transparent !important;
}
.stTabs [data-baseweb="tab"]:hover {
    background: #E5E5E5 !important;
    color: #000 !important;
}
.stTabs [data-baseweb="tab"]:hover * {
    color: #000 !important;
    background: transparent !important;
}
/* ACTIVE TAB — black background, white text — applied to the tab AND every child */
.stTabs [aria-selected="true"],
.stTabs [aria-selected="true"] *,
.stTabs [aria-selected="true"] p,
.stTabs [aria-selected="true"] span,
.stTabs [aria-selected="true"] div,
.stTabs [aria-selected="true"] button {
    background: #000 !important;
    color: #FFF !important;
}
.stTabs [aria-selected="true"]:hover {
    background: #000 !important;
    color: #FFF !important;
}
.stTabs [aria-selected="true"]:hover * {
    background: #000 !important;
    color: #FFF !important;
}

/* ── EXPANDER ── */
.stExpander {
    border: 2px solid #000 !important;
    border-radius: 0 !important;
    box-shadow: none !important;
}
.stExpander > div:first-child {
    border-radius: 0 !important;
    background: #FFF !important;
}
.stExpander summary {
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 700;
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #000 !important;
}

/* ── TABLES ── */
table { border-collapse: collapse; width: 100%; }
th {
    background: #000 !important;
    color: #FFF !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.7rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    padding: 0.5rem 0.7rem;
    border: 2px solid #000;
}
td {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.8rem;
    padding: 0.45rem 0.7rem;
    border: 1px solid #000;
    color: #000 !important;
    background: #FFF !important;
}
tr:nth-child(even) td { background: #f9f9f9 !important; }

/* ── MISC ── */
hr { border: none; border-top: 2px solid #000; margin: 1.2rem 0; }
a { color: #000 !important; text-decoration: underline; }
/* inline code only (not inside pre) — for short tags like `clay` in body text */
p code, li code, td code, span code, div:not([data-testid="stText"]):not([data-testid="stCode"]) code {
    background: #000 !important;
    color: #FFF !important;
    font-family: 'JetBrains Mono', monospace !important;
    padding: 1px 5px;
}
blockquote { border-left: 4px solid #000; padding: 0.5em 1em; margin: 0.8em 0; color: #000 !important; }

/* ── NATIVE TEXT BLOCKS (st.text, st.code) ── */
[data-testid="stText"], [data-testid="stCode"] {
    border: 2px solid #000 !important;
    box-shadow: 4px 4px 0 0 #000 !important;
    background: #FFF !important;
    padding: 0 !important;
    border-radius: 0 !important;
}
[data-testid="stText"] pre, [data-testid="stCode"] pre,
[data-testid="stText"] code, [data-testid="stCode"] code,
[data-testid="stText"] p, [data-testid="stCode"] p,
[data-testid="stText"] div, [data-testid="stCode"] div,
[data-testid="stText"] *, [data-testid="stCode"] * {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.82rem !important;
    line-height: 1.85 !important;
    color: #000 !important;
    background: #FFF !important;
    padding: 1rem 1.2rem !important;
    white-space: pre-wrap !important;
    border-radius: 0 !important;
    margin: 0 !important;
    word-wrap: break-word !important;
    opacity: 1 !important;
    filter: none !important;
}

footer { visibility: hidden; }
#MainMenu { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### RASUL SHAIKH")
    st.markdown("GTM ENGINEER")
    st.markdown("---")
    st.markdown("**PRICING**")
    st.markdown("$30 / HR")
    st.markdown("$4,000 / MONTH")
    st.markdown("**$10,000 / QUARTER**")
    st.markdown("*(recommended)*")
    st.markdown("---")
    st.markdown("**MY CASE STUDIES**")
    st.markdown("REMOTESTATE")
    st.markdown("$180K ARR / 6 MONTHS")
    st.markdown("FALCONWISE")
    st.markdown("10+ SQLS/MO, 30% ENGAGE")
    st.markdown("OMNIBOUND AI")
    st.markdown("1.5%+ REPLY, 300+ MAILBOXES")
    st.markdown("---")
    st.markdown("**MAPLE MEDIA PROOF**")
    st.markdown("$250M+ REVENUE")
    st.markdown("150+ BRANDS")
    st.markdown("07 PUBLIC CASES")
    st.markdown("10 BLOG POSTS")
    st.markdown("[wearemaplemedia.com](https://wearemaplemedia.com)")
    st.markdown("---")
    st.markdown("**PORTFOLIO**")
    st.markdown("[rasulshaikh.github.io/gtm-portfolio](https://rasulshaikh.github.io/gtm-portfolio/)")
    st.markdown("[github.com/rasulshaikh](https://github.com/rasulshaikh)")
    st.markdown("---")
    st.markdown("RASUL SHAIKH")

# ── HEADER ────────────────────────────────────────────────────────────────────
st.markdown("<h1>MAPLE MEDIA GTM ENGINE</h1>", unsafe_allow_html=True)
st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:0.72rem;font-weight:500;color:#555;text-transform:uppercase;letter-spacing:0.14em;margin-top:-0.3rem;">NORTH AMERICA / DTC / E-COMMERCE / STARTUPS TO ENTERPRISE</p>', unsafe_allow_html=True)

m1, m2, m3, m4, m5 = st.columns(5)
for col, val, lbl in zip(
    [m1, m2, m3, m4, m5],
    ["$250M+", "150+", "07", "16", "10"],
    ["MAPLE REVENUE", "MAPLE BRANDS", "MAPLE CASE STUDIES", "TOOLS WIRED", "BLOG POSTS TO LINK"],
):
    with col:
        st.markdown(f'<div class="metric-box"><div class="metric-val">{val}</div><div class="metric-lbl">{lbl}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="ph">WHAT GETS BUILT</div>', unsafe_allow_html=True)
st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:0.85rem;line-height:1.85;color:#000;max-width:72ch;">A three-layer GTM engine that runs continuously and compounds over time. Not a campaign — a system. Every layer feeds the next: intelligence drives outreach, outreach generates data, data sharpens targeting. After 60 days the system knows exactly which DTC founder profile, at which growth stage, responding to which signal, converts. That intelligence lives in HubSpot — not in a spreadsheet.</p>', unsafe_allow_html=True)

tabs = st.tabs([
    "01 INTELLIGENCE",
    "02 OUTBOUND",
    "03 ATTRIBUTION",
    "04 TOOL STACK",
    "05 MAPLE MEDIA FIT",
    "06 PORTFOLIO WIRING",
])

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 01 INTELLIGENCE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tabs[0]:
    st.markdown('<div class="ph">PHASE 01 - INTELLIGENCE LAYER - WEEKS 1-2</div>', unsafe_allow_html=True)
    st.markdown("*Who to reach, when, and why — before anything sends.*")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### ICP SCORING")
        st.markdown("""
| DIMENSION | HOW SCORED |
|---|---|
| GMV TIER | SEED / GROWTH / ENTERPRISE |
| AD SPEND | META-HEAVY, TIKTOK-NATIVE, GOOGLE-FIRST |
| TECH STACK | SHOPIFY, KLAVIYO, TRIPLE WHALE, NORTHBEAM |
| HEADCOUNT | SOLO FOUNDER TO 200+ |
| GROWTH SIGNAL | LIVE TRIGGER - HIRE, RAISE, REVIEW, EXPANSION |
""")
        st.markdown("### PRE-SEND LIST GATE")
        st.markdown("Every list graded A+ to F across 8 dimensions. Below grade B = blocked + Slack alert.")
        for i, item in enumerate([
            "EMAIL VALIDITY RATE", "DOMAIN DIVERSITY", "ROLE RELEVANCE TO ICP",
            "SENIORITY MATCH", "COMPANY SIZE MATCH", "SIGNAL MATCH RATE",
            "DUPLICATE RATE", "BOUNCE HISTORY",
        ], 1):
            st.markdown(f'<div style="font-family:\'JetBrains Mono\',monospace;font-size:0.8rem;padding:0.3rem 0;border-bottom:1px solid #ddd;color:#000;"><span style="font-weight:800;color:#000;">{str(i).zfill(2)}</span>  {item}</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("### SIGNAL STACK")
        signals = [
            ("NEW CMO / HEAD OF GROWTH HIRED", "TRIGIFY + LINKEDIN", "LAST 30 DAYS"),
            ("FUNDING ROUND RAISED (SEED → SERIES B+)", "CRUNCHBASE + TRIGIFY", "LAST 30 DAYS"),
            ("ATTRIBUTION TOOL SWITCH (TRIPLE WHALE / NORTHBEAM / ROCKERBOX / MOTION)", "THEIRSTACK + TRIGIFY", "LAST 14 DAYS"),
            ("NEGATIVE AGENCY REVIEW ON G2 / CLUTCH", "APIFY SCRAPE", "LAST 14 DAYS"),
            ("HIRING CREATIVE / PERFORMANCE ROLES (3+ OPEN)", "LINKEDIN JOB CHANGES", "LAST 14 DAYS"),
            ("AD ACCOUNT FLAGGED / RESTRICTED ON META / TIKTOK", "META ADS LIBRARY + SUPPORT", "LAST 7 DAYS"),
            ("NEW PRODUCT LAUNCH / SKU EXPANSION", "SHOPIFY MONITOR + LINKEDIN", "LAST 30 DAYS"),
            ("iOS 18+ TRACKING / ATTRIBUTION ISSUES MENTIONED", "TECH NEWS MONITOR", "LAST 14 DAYS"),
            ("LINKEDIN POST ON CREATIVE / ROAS / SCALING / FATIGUE", "PHANTOMBUSTER", "LAST 7 DAYS"),
            ("NORTH AMERICAN MARKET EXPANSION (UK / EU / MENA → NA)", "LINKEDIN + CRUNCHBASE", "LAST 60 DAYS"),
        ]
        for signal, source, window in signals:
            st.markdown(f"""
<div class="card-compact">
<span class="badge">{window}</span><br>
<span style="font-family:'JetBrains Mono',monospace;font-size:0.82rem;font-weight:700;color:#000;">{signal}</span><br>
<span style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#555;">SRC: {source}</span>
</div>""", unsafe_allow_html=True)

    st.markdown("### ENRICHMENT PIPELINE (CLAY 9-STEP)")
    st.markdown('<div class="wiring">UPLOAD → COMPANY ENRICH → PEOPLE ENRICH → EMAIL WATERFALL (FINDYMAIL > PROSPEO > BETTERCONTACT) → ZEROBOUNCE VERIFY → PHONE [T1 ONLY] → CLAYGENT CUSTOM DATA → AI LEAD SCORE 0-100 → HUBSPOT EXPORT + TIER TAG</div>', unsafe_allow_html=True)

    ecol1, ecol2, ecol3 = st.columns(3)
    for col, val, lbl in zip([ecol1, ecol2, ecol3], ["85%+", "40%", "0-100"], ["EMAIL COVERAGE", "SINGLE-FINDER AVG", "AI LEAD SCORE RANGE"]):
        with col:
            st.markdown(f'<div class="metric-box"><div class="metric-val">{val}</div><div class="metric-lbl">{lbl}</div></div>', unsafe_allow_html=True)

    st.markdown("### DOMAIN FLEET + DELIVERABILITY")
    for item in [
        "50+ SENDING DOMAINS — SPF / DKIM / DMARC ON EVERY DOMAIN",
        "3-4 WEEK INBOX WARM-UP BEFORE CAMPAIGN LAUNCH",
        "50-DOMAIN ROTATION PER CAMPAIGN RUN",
        "WEEKLY DELIVERABILITY AUDIT — MONDAY — BOUNCE RATE, SPAM RATE, DOMAIN HEALTH — SLACK REPORT",
    ]:
        st.markdown(f'<div style="font-family:\'JetBrains Mono\',monospace;font-size:0.78rem;padding:0.35rem 0;border-bottom:1px solid #ddd;color:#000;">▸  {item}</div>', unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 02 OUTBOUND
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tabs[1]:
    st.markdown('<div class="ph">PHASE 02 - OUTBOUND ENGINE - WEEKS 3-5</div>', unsafe_allow_html=True)
    st.markdown("*Three channels running in parallel. Each fires on a specific signal.*")

    st.markdown("""
| CHANNEL | TOOL | TIER | VOLUME |
|---|---|---|---|
| COLD EMAIL | SMARTLEAD | T1 + T2 | 500-2,000 / WEEK |
| LINKEDIN | HEYREACH | T1 | 50-100 / WEEK |
| PERSONALIZED VIDEO | LOOM | T1 TOP 50 | 20-50 / MONTH |
""")

    # Channel 1
    st.markdown('<div class="ph" style="margin-top:1.5rem;">CH-01 / COLD EMAIL / SMARTLEAD</div>', unsafe_allow_html=True)
    st.markdown("**WIRING:**")
    st.markdown('<div class="wiring">CLAY SCORED LIST → PRE-SEND GATE → SMARTLEAD UPLOAD → SEQUENCE RUNS → REPLY DETECTED → N8N WEBHOOK → HUBSPOT DEAL CREATED + SLACK ALERT</div>', unsafe_allow_html=True)

    st.markdown("**3 COPY ANGLES — DTC-NATIVE PAIN:**")
    a1, a2, a3 = st.columns(3)
    angles = [
        ("A1", "ROAS PLATEAU AT SCALE", "Spend is growing but ROAS is decaying — same 5 creatives rotating, frequency caps, CPM inflation. Maple Media's engine ships 30–50 fresh concepts per month so spend can scale without ROAS dropping."),
        ("A2", "CREATIVE VELOCITY GAP", "Brief-to-ship cycle is 3–4 weeks. Ads fatigue in 5 days. Maple Media generates 50+ concepts per brand per month with a research and testing framework behind every angle — kill-or-scale decisions in 7 days, not 30."),
        ("A3", "ATTRIBUTION FRACTURE", "Just switched from Triple Whale to Northbeam (or iOS 18 broke their tracking). They can't tell which creative actually drove the sale. Maple Media's research-led system identifies winners in 7-day test windows — they know which concept drove the purchase, not just which ad got the click."),
    ]
    for col, (tag, title, body) in zip([a1, a2, a3], angles):
        with col:
            st.markdown(f'<div class="card"><span class="badge">{tag}</span><br><span style="font-family:\'JetBrains Mono\',monospace;font-size:0.8rem;font-weight:800;color:#000;text-transform:uppercase;letter-spacing:0.06em;display:block;margin:0.5rem 0 0.4rem;">{title}</span><span style="font-family:\'JetBrains Mono\',monospace;font-size:0.76rem;color:#555;line-height:1.7;">{body}</span></div>', unsafe_allow_html=True)

    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:0.75rem;color:#555;margin-top:0.5rem;">VARIANT MATRIX: E1 x 3 (SIGNAL-LED) | E2 x 2 (SOCIAL PROOF) | 10 SUBJECT LINES ROTATED BY COMPANY HASH | 80-WORD GATE ON EVERY SEND</p>', unsafe_allow_html=True)

    # Merge tag legend
    st.markdown("""
<div style="border:2px dashed #000;padding:0.6rem 0.9rem;margin:0.5rem 0 0.9rem;background:#FFF;">
<span style="font-family:'JetBrains Mono',monospace;font-size:0.68rem;font-weight:800;color:#000;text-transform:uppercase;letter-spacing:0.14em;display:block;margin-bottom:0.4rem;">MERGE TAGS (SMARTLEAD / CLAY FORMAT)</span>
<span style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#000;line-height:1.9;">
{{first_name}} &nbsp; {{last_name}} &nbsp; {{company}} &nbsp; {{industry}} &nbsp; {{product_category}} &nbsp; {{funding_round}} &nbsp; {{post_topic}} &nbsp; {{department}} &nbsp; {{creative_angle}} &nbsp; {{new_hire_role}} &nbsp; {{case_study_link}}
</span>
</div>
""", unsafe_allow_html=True)

    with st.expander("VIEW EMAIL COPY EXAMPLES"):
        emails = [
            (
                "E-01 / NEW HEAD OF GROWTH HIRED",
                "scaling creative at {{company}} — the velocity question",
                (
                    "<p style='margin:0 0 0.6rem 0;'>Hey {{first_name}},</p>"
                    "<p style='margin:0 0 0.6rem 0;'>Saw {{company}} just brought on a head of growth. The first 90 days usually come down to one question: is the creative engine shipping 30–50 fresh concepts per month, or is the team still running 3–5 ads on rotation and watching them fatigue in 5 days?</p>"
                    "<p style='margin:0 0 0.6rem 0;'>Most DTC brands at {{company}}'s stage are scaling ad spend on a creative engine that breaks the moment CPMs go up. Same concepts, higher frequency, ROAS decays — and the new CMO inherits the plateau.</p>"
                    "<p style='margin:0 0 0.6rem 0;'>Maple Media's model is built the other way: research-led concept generation, 30–50 fresh ads per brand per month, kill-or-scale decisions in 7-day test windows. Budget grows and ROAS holds.</p>"
                    "<p style='margin:0 0 0.6rem 0;'>3 brands in {{industry}} just shipped 50+ concepts in their first 60 days and saw blended ROAS hold through a 3x spend increase.</p>"
                    "<p style='margin:0;'>Worth 20 minutes to see what the first 30 days looks like for {{company}}?</p>"
                ),
            ),
            (
                "E-02 / NEGATIVE G2 / CLUTCH REVIEW",
                "{{company}} just left a review — here's what that usually means",
                (
                    "<p style='margin:0 0 0.6rem 0;'>Hey {{first_name}},</p>"
                    "<p style='margin:0 0 0.6rem 0;'>{{company}} posted a review about their last creative agency. The feedback was about consistency and results, not quality.</p>"
                    "<p style='margin:0 0 0.6rem 0;'>That gap is almost always a system problem, not a talent problem. The agency was producing creative without a repeatable research and testing engine behind it — so every month started from zero, every winning concept burned out before the next one shipped, and ROAS drifted down quarter after quarter.</p>"
                    "<p style='margin:0 0 0.6rem 0;'>Maple Media's model is built the other way: research and concept framework first, then creative output from a structured process. 50+ concepts per brand per month, every one grounded in customer research and tested against the live ad set. Creative that compounds instead of resetting every quarter.</p>"
                    "<p style='margin:0;'>Happy to show you what that looks like in 20 minutes.</p>"
                ),
            ),
            (
                "E-03 / FUNDING ROUND RAISED",
                "saw the raise — your creative engine needs to scale with you",
                (
                    "<p style='margin:0 0 0.6rem 0;'>Hey {{first_name}},</p>"
                    "<p style='margin:0 0 0.6rem 0;'>Saw {{company}} closed {{funding_round}}. Post-raise, the ad budget just got bigger — and so did the pressure on the creative engine to keep ROAS flat while spend grows 3x.</p>"
                    "<p style='margin:0 0 0.6rem 0;'>Most teams respond by scaling the same 3–5 winning creatives. That works for a month, then frequency caps, ad fatigue, and CPM inflation kick in — and ROAS drops right when the target got bigger.</p>"
                    "<p style='margin:0 0 0.6rem 0;'>Maple Media scales differently. Research-led concept generation, 30–50 fresh ads per month, kill-or-scale decisions every 7 days. Budget grows, ROAS holds. {{product_category}} brands in your stage are running this exact playbook right now.</p>"
                    "<p style='margin:0;'>Worth a 30-minute conversation?</p>"
                ),
            ),
            (
                "FU-01 / DAY 5 / CASE STUDY",
                "re: creative velocity at {{company}}",
                (
                    "<p style='margin:0 0 0.6rem 0;'>Hey {{first_name}},</p>"
                    "<p style='margin:0 0 0.6rem 0;'>Following up on the note about creative velocity.</p>"
                    "<p style='margin:0 0 0.6rem 0;'>Ancient Remedies went from 3 concepts per month and unprofitable paid social to 50+ concepts per month and $1M+ in ad spend at a 1.8x blended ROAS — 20,000+ purchases at a $45 cost per purchase. The first thing we changed was the cadence and the testing framework. Everything else followed.</p>"
                    "<p style='margin:0 0 0.6rem 0;'>Case study here if useful: {{case_study_link}}</p>"
                    "<p style='margin:0;'>Happy to show you what the first 30 days looks like for {{company}}.</p>"
                ),
            ),
            (
                "FU-02 / DAY 14 / SOFT CLOSE",
                "last one from me",
                (
                    "<p style='margin:0 0 0.6rem 0;'>Hey {{first_name}},</p>"
                    "<p style='margin:0 0 0.6rem 0;'>Dropping this one last note in case the timing wasn't right earlier.</p>"
                    "<p style='margin:0 0 0.6rem 0;'>If creative velocity — shipping 30–50 fresh concepts per month and knowing which ones kill CPA in 7 days — is something you're solving this quarter, worth 20 minutes.</p>"
                    "<p style='margin:0;'>If not, no worries at all.</p>"
                ),
            ),
        ]
        for label, subject, body in emails:
            st.markdown(f'<span class="sig-label">{label}</span>', unsafe_allow_html=True)
            st.markdown(f"**SUBJECT:** {subject}")
            # Inline-styled div with explicit color/background — bypasses any CSS specificity conflict
            st.markdown(
                f'<div style="color:#000000;background:#FFFFFF;'
                f'font-family:\'JetBrains Mono\',monospace;font-size:0.82rem;line-height:1.55;'
                f'padding:1rem 1.2rem;margin:0.4rem 0 1.2rem;'
                f'border:2px solid #000000;box-shadow:4px 4px 0 0 #000000;'
                f'opacity:1;">{body}</div>',
                unsafe_allow_html=True
            )

    # Channel 2
    st.markdown('<div class="ph" style="margin-top:1.5rem;">CH-02 / LINKEDIN / HEYREACH</div>', unsafe_allow_html=True)
    st.markdown("**WIRING:**")
    st.markdown('<div class="wiring">PHANTOMBUSTER (POST ENGAGERS / FOLLOWERS) → CLAY ICP FILTER → HEYREACH SEQUENCE → REPLY → HUBSPOT TAG + SLACK</div>', unsafe_allow_html=True)

    st.markdown("""
| DAY | ACTION |
|---|---|
| D1 | ENGAGE WITH TARGET'S MOST RECENT POST — GENUINE COMMENT |
| D3 | CONNECTION REQUEST WITH LIGHT CONTEXT — NO PITCH |
| D5 | DM IF ACCEPTED — ONE QUESTION REFERENCING THEIR POST — NO CTA |
| D8 | COLD EMAIL LANDS — COORDINATED WITH EMAIL SEQUENCE |
""")
    st.markdown("**FOLLOWER PLAY:** DAILY FOLLOWER EXPORT → CLAY ICP FILTER WITHIN 24H → WARM OUTREACH SAME DAY")

    with st.expander("VIEW LINKEDIN DM EXAMPLES"):
        dms = [
            ("LI-01 / AFTER CONNECTION ACCEPTED",
             (
                 "<p style='margin:0 0 0.6rem 0;'>Hey {{first_name}}, appreciate the connect.</p>"
                 "<p style='margin:0 0 0.6rem 0;'>Saw your post on {{post_topic}} last week. One thing that keeps coming up with the DTC brands I talk to at your stage: the creative is solid, but there's no system for shipping 30–50 fresh concepts per month and knowing which ones actually hold ROAS at scale.</p>"
                 "<p style='margin:0;'>Curious — is creative velocity something you're solving with an in-house team right now, or still mostly gut feel on what to brief next?</p>"
             )),
            ("LI-02 / FOLLOWER PLAY — WARM INTENT",
             (
                 "<p style='margin:0 0 0.6rem 0;'>Hey {{first_name}}, noticed you followed — appreciate it.</p>"
                 "<p style='margin:0 0 0.6rem 0;'>Looks like you're working on {{department}} at {{company}}. I work with DTC brands on the creative engine behind scaling — research, concept generation, testing cadence, iteration loop. The brands I work with ship 30–50 fresh concepts per month and kill or scale each one in a 7-day test window.</p>"
                 "<p style='margin:0;'>Happy to share what's been working if that's useful.</p>"
             )),
        ]
        for label, body in dms:
            st.markdown(f'<span class="sig-label">{label}</span>', unsafe_allow_html=True)
            st.markdown(
                f'<div style="color:#000000;background:#FFFFFF;'
                f'font-family:\'JetBrains Mono\',monospace;font-size:0.82rem;line-height:1.55;'
                f'padding:1rem 1.2rem;margin:0.4rem 0 1.2rem;'
                f'border:2px solid #000000;box-shadow:4px 4px 0 0 #000000;'
                f'opacity:1;">{body}</div>',
                unsafe_allow_html=True
            )

    # Channel 3
    st.markdown('<div class="ph" style="margin-top:1.5rem;">CH-03 / VIDEO / LOOM / T1 TOP 50</div>', unsafe_allow_html=True)
    st.markdown("**FIRES ON:** NEW CMO HIRE | ROUND RAISED | 3+ TOUCHES WITHOUT REPLY")
    st.markdown('<div class="wiring">CLAY FLAGS T1 → LOOM RECORDED PER ACCOUNT → LINKED IN EMAIL AS P.S. → LOOM WATCH EVENT → HUBSPOT DEAL UPDATE</div>', unsafe_allow_html=True)

    with st.expander("VIEW LOOM SCRIPT"):
        st.markdown("*FORMAT: 60-90 SECONDS. SCREEN SHARE OF THEIR WEBSITE + META AD LIBRARY. SPECIFIC TO THEIR CREATIVE STACK.*")
        loom_script = (
            "<p style='margin:0 0 0.6rem 0;'>Hey {{first_name}} — I pulled {{company}}'s site and your Meta ad library before recording this.</p>"
            "<p style='margin:0 0 0.6rem 0;'>You're running {{product_category}} creatives focused on {{creative_angle}}. The creative is strong.</p>"
            "<p style='margin:0 0 0.6rem 0;'>What I don't see is the testing framework behind it — no system to ship 30–50 fresh concepts per month, kill the ones that fatigue in 5 days, and scale the ones that hold ROAS. Right now it looks like you're rotating maybe 5–8 ads — which works at $20K/mo spend but breaks the moment you try to scale to $200K.</p>"
            "<p style='margin:0 0 0.6rem 0;'>That's exactly what Maple Media builds. Not a one-off audit. A repeatable system: research, concept structure, testing cadence, iteration loop. So your new {{new_hire_role}} inherits a creative engine that ships at the velocity your ad budget demands.</p>"
            "<p style='margin:0;'>I'll drop two case study links in the email below — one in your category, one a stretch. Happy to walk you through what the first 30 days looks like for {{company}} — 20 minutes, no pitch deck.</p>"
        )
        st.markdown(
            f'<div style="color:#000000;background:#FFFFFF;'
            f'font-family:\'JetBrains Mono\',monospace;font-size:0.82rem;line-height:1.55;'
            f'padding:1rem 1.2rem;margin:0.4rem 0 1.2rem;'
            f'border:2px solid #000000;box-shadow:4px 4px 0 0 #000000;'
            f'opacity:1;">{loom_script}</div>',
            unsafe_allow_html=True
        )

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 03 ATTRIBUTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tabs[2]:
    st.markdown('<div class="ph">PHASE 03 - ATTRIBUTION + ITERATION - ONGOING</div>', unsafe_allow_html=True)
    st.markdown("*Close the loop. Every touch tracked. Every winner doubled down on.*")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### WHAT GETS TRACKED")
        touches = [
            ("EMAIL SENT", "OUTBOUND CAMPAIGN TOUCH"),
            ("EMAIL OPENED", "ENGAGEMENT FLAG"),
            ("EMAIL REPLIED", "DEAL CREATED + SIGNAL TAG + SLACK ALERT"),
            ("LINKEDIN DM SENT", "LINKEDIN TOUCH"),
            ("LINKEDIN DM REPLIED", "LINKEDIN CONVERSION TAG"),
            ("LOOM WATCHED", "VIDEO ENGAGEMENT FLAG"),
            ("SITE VISIT VIA RB2B POST-EMAIL", "SILENT CONVERSION TAG"),
            ("SIGNED UP WITHOUT REPLYING", "OUTBOUND-INFLUENCED SIGNUP"),
        ]
        for touch, log in touches:
            st.markdown(f"""<div style="border-bottom:1px solid #ddd;padding:0.45rem 0;">
<span style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;font-weight:700;color:#000;">{touch}</span><br>
<span style="font-family:'JetBrains Mono',monospace;font-size:0.68rem;font-weight:500;color:#555;">→ {log}</span>
</div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("### WEEKLY ITERATION LOOP")
        st.markdown("**EVERY MONDAY:**")
        for i, step in enumerate([
            "WHICH SIGNAL TYPES GENERATED MEETINGS LAST WEEK",
            "WHICH COPY ANGLES GOT REPLIES",
            "WHICH CHANNEL MADE FIRST CONTACT ON CONVERTED ACCOUNTS",
            "UNDERPERFORMERS FLAGGED AND PAUSED",
            "WINNERS GET ADDITIONAL VARIANTS BUILT",
        ], 1):
            st.markdown(f'<div style="font-family:\'JetBrains Mono\',monospace;font-size:0.78rem;padding:0.35rem 0;border-bottom:1px solid #ddd;color:#000;"><span style="font-weight:800;">{str(i).zfill(2)}</span>  {step}</div>', unsafe_allow_html=True)

        st.markdown("### FULL-FUNNEL REPORTING")
        st.markdown('<div class="wiring">OUTBOUND TOUCH → REPLY → DISCOVERY CALL BOOKED → PROPOSAL → ENGAGEMENT SIGNED → CASE STUDY WON</div>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:0.78rem;color:#555;line-height:1.7;">Outbound-influenced signups captured even when the contact did not reply. Silent conversions tracked via RB2B post-email site visit.</p>', unsafe_allow_html=True)

        st.markdown("### SCALABILITY")
        for month, detail in [
            ("MONTH 01", "500 CONTACTS/WK — 3 EMAIL VARIANTS — LINKEDIN ON T1 ONLY"),
            ("MONTH 03", "2,000 CONTACTS/WK — 9 VARIANTS FROM REPLY DATA — FULL MULTICHANNEL T1 + T2"),
            ("MONTH 06", "SYSTEM SELF-CORRECTS — UNDERPERFORMING SIGNALS DEPRIORITIZED — WINNING ANGLES GET MORE VARIANTS"),
        ]:
            st.markdown(f'<div class="card-compact"><span class="badge">{month}</span> <span style="font-family:\'JetBrains Mono\',monospace;font-size:0.76rem;color:#000;">{detail}</span></div>', unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 04 TOOL STACK
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tabs[3]:
    st.markdown('<div class="ph">TOOL STACK — 16 TOOLS WIRED END TO END</div>', unsafe_allow_html=True)

    tools = [
        ("LIST BUILDING",         "APOLLO",                              "ICP PULL BY TITLE, INDUSTRY, HEADCOUNT, GEO"),
        ("ENRICHMENT",            "CLAY",                                "9-STEP ENRICHMENT TABLE, IIFE SCORING FORMULAS, CLAYGENT CUSTOM DATA"),
        ("EMAIL FINDING",         "FINDYMAIL + PROSPEO + BETTERCONTACT", "WATERFALL EMAIL DISCOVERY — 85%+ COVERAGE"),
        ("EMAIL VERIFICATION",    "ZEROBOUNCE",                          "REMOVES INVALID + RISKY CONTACTS BEFORE SEND"),
        ("AI SCORING",            "CLAUDE VIA CLAY",                     "0-100 LEAD SCORE, COPY HOOK GENERATION PER CONTACT"),
        ("SIGNAL DETECTION",      "TRIGIFY",                             "JOB CHANGES, FUNDING ROUNDS, EXPANSION SIGNALS"),
        ("TECH STACK DETECTION",  "THEIRSTACK",                          "ATTRIBUTION TOOL SWITCH, SHOPIFY / KLAVIYO / TRIPLE WHALE DETECTION"),
        ("WEBSITE VISITORS",      "RB2B",                                "ANONYMOUS VISITOR IDENTIFICATION POST-EMAIL"),
        ("LINKEDIN SCRAPING",     "PHANTOMBUSTER",                       "POST ENGAGERS, FOLLOWER EXPORT, PROFILE DATA"),
        ("EMAIL SEQUENCING",      "SMARTLEAD",                           "50+ DOMAIN FLEET, A/B TESTING, BOUNCE MONITORING"),
        ("LINKEDIN OUTREACH",     "HEYREACH",                            "CONNECTION REQUESTS, DM SEQUENCES, COMMENT ENGAGEMENT"),
        ("VIDEO",                 "LOOM",                                "PERSONALIZED 60-90S VIDEOS FOR T1 ACCOUNTS"),
        ("ORCHESTRATION",         "N8N",                                 "WEBHOOKS, ROUTING LOGIC, CRM SYNC, DEAD LETTER QUEUE"),
        ("GTM ANALYTICS",         "DEEPLINE CLI",                        "OUTBOUND ANALYTICS, SEQUENCE PERFORMANCE, REPLY → MEETING ATTRIBUTION"),
        ("CRM",                   "HUBSPOT",                             "CONTACT MANAGEMENT, DEAL CREATION, ATTRIBUTION, REPORTING"),
        ("ALERTS",                "SLACK",                               "REAL-TIME REPLY ALERTS, DELIVERABILITY FLAGS, WEEKLY MONDAY REPORT"),
    ]

    for i, (layer, tool, desc) in enumerate(tools):
        c1, c2, c3 = st.columns([1.3, 1.7, 3.0])
        with c1:
            st.markdown(f'<span class="tool-lbl">{layer}</span>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.82rem;font-weight:800;color:#000;">{tool}</span>', unsafe_allow_html=True)
        with c3:
            st.markdown(f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.78rem;color:#555;">{desc}</span>', unsafe_allow_html=True)
        st.markdown("<hr style='margin:0.2rem 0;border:none;border-top:1px solid #ddd;'>", unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 05 MAPLE MEDIA FIT — THEIR CUSTOMERS, THEIR SYSTEM, THEIR CONTENT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tabs[4]:
    st.markdown('<div class="ph">MAPLE MEDIA FIT — WHY THIS PLAN WORKS FOR YOU SPECIFICALLY</div>', unsafe_allow_html=True)
    st.markdown("*This engine is reverse-engineered from your actual customer base, your own creative system, and the content you already have live. Every outreach references proof that exists on your site today.*")

    # ── YOUR SYSTEM ──
    st.markdown("### HOW YOUR SYSTEM WORKS")
    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:0.78rem;color:#000;line-height:1.7;margin:0.4rem 0;">Your repeatable creative engine: <strong>Research → Concept → Structured Planning → Scalable Iteration</strong>. Skipping steps kills performance — you don\'t skip steps. 50+ ad concepts per brand per month. $250M+ revenue driven across 150+ brands.</p>', unsafe_allow_html=True)
    st.markdown("""
<div class="wiring">RESEARCH → CONCEPT → STRUCTURED PLANNING → SCALABLE ITERATION → TESTING → WINNING ANGLE EXTRAPOLATION → REPEAT</div>
""", unsafe_allow_html=True)
    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:0.75rem;margin:0.4rem 0;"><a href="https://wearemaplemedia.com/#system" target="_blank" rel="noopener" style="color:#000;font-weight:800;">→ VIEW FULL SYSTEM ON YOUR SITE</a></p>', unsafe_allow_html=True)

    # ── YOUR CUSTOMERS (LIVE PROOF) ──
    st.markdown("### YOUR CUSTOMERS (LIVE PROOF)")
    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:0.75rem;color:#555;margin:0.4rem 0 0.8rem;">These 7 brands are your public case studies. I use them as named social proof in cold email P.S. lines, in Loom intros, and in LinkedIn DMs — the prospect reads their own peer set, not a generic claim.</p>', unsafe_allow_html=True)

    customers = [
        ("ANCIENT REMEDIES", "Natural healing book collection", "1.8+ ROAS", "$1M+", "20,000+", "https://wearemaplemedia.com/case-study/ancient-remedies-2-7x-roas-271-return-on-ad-spend/"),
        ("CALLIXE", "Neck therapy traction pillow", "1.9+ ROAS", "$100K+", "1,000+", "https://wearemaplemedia.com/case-study/callixe-2-7x-roas-48-purchase-to-initiate-checkout-rate/"),
        ("SAINT EYEWEAR", "Fit-over polarized sunglasses", "1.9+ ROAS", "$450K+", "15,000+", "https://wearemaplemedia.com/case-study/saint-eyewear-2-5x-roas-150-growth-in-new-customer-acquisition/"),
        ("PRIMAL QUEEN", "Grass-fed beef organ supplements", "1.9+ ROAS", "$250K+", "4,000+", "https://wearemaplemedia.com/case-study/primal-queen-2x-roas-25-reduction-in-cost-per-acquisition/"),
        ("CALVRIS", "Scalp & skin care line", "1.7+ ROAS", "$150K+", "1,000+", "https://wearemaplemedia.com/case-study/calvris-2-2x-roas-scaled-0-month-over-month/"),
        ("JEVI SUPPLEMENTS", "Cortisol / stress supplements", "1.7+ ROAS", "$350K+", "7,000+", "https://wearemaplemedia.com/case-study/jevi-supplements-2-3x-roas-cpm-67-below-category-average/"),
        ("CURVANI", "Plant-based booty drops", "1.6+ ROAS", "$200K+", "2,000+", "https://wearemaplemedia.com/case-study/2-2x-roas-on-200000-in-spend-for-curvani/"),
    ]

    for name, product, roas, spend, purchases, url in customers:
        st.markdown(
            f'<div class="card-compact" style="padding:0.7rem 0.9rem;">'
            f'<a href="{url}" target="_blank" rel="noopener" style="font-family:\'JetBrains Mono\',monospace;font-size:0.82rem;font-weight:800;color:#000;text-transform:uppercase;letter-spacing:0.06em;text-decoration:underline;">{name} ↗</a>'
            f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.7rem;color:#555;display:block;margin-top:2px;">{product}</span>'
            f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.7rem;color:#000;margin-top:4px;display:inline-block;"><strong>ROAS:</strong> {roas} &nbsp;·&nbsp; <strong>SPEND:</strong> {spend} &nbsp;·&nbsp; <strong>PURCHASES:</strong> {purchases}</span>'
            f'</div>',
            unsafe_allow_html=True
        )

    # ── BLOG & INSIGHTS ──
    st.markdown("### YOUR BLOG & INSIGHTS (LINKED IN OUTREACH)")
    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:0.75rem;color:#555;margin:0.4rem 0 0.8rem;">These 10 posts are your proof of thought leadership. I link the relevant one in the cold email P.S. based on the prospect\'s category — the prospect reads your framework, not mine.</p>', unsafe_allow_html=True)

    blog_posts = [
        ("From $100K to $1M Monthly Spend: A Creative Strategy Roadmap", "The DTC Playbook", "https://wearemaplemedia.com/the-dtc-playbook/from-100k-to-1m-monthly-spend-a-creative-strategy-roadmap/"),
        ("The DTC Playbook for 2026: What Works When Everything Changed", "The DTC Playbook", "https://wearemaplemedia.com/the-dtc-playbook/the-dtc-playbook-for-2026-what-works-when-everything-changed/"),
        ("The Avatar-First Approach: Why Customer Research Is Your Real Creative Advantage", "The Creative Lab", "https://wearemaplemedia.com/the-creative-lab/the-avatar-first-approach-why-customer-research-is-your-real-creative-advantage/"),
        ("Inside the Maple Media Creative Lab: How We Generate 50+ Ad Concepts Per Brand Per Month", "The Creative Lab", "https://wearemaplemedia.com/the-creative-lab/inside-the-maple-media-creative-lab-how-we-generate-50-ad-concepts-per-brand-per-month/"),
        ("The Anatomy of a Winning Meta Ad: Seven Patterns From Eight-Figure Spend", "Performance Creative", "https://wearemaplemedia.com/performance-creative/the-anatomy-of-a-winning-meta-ad-seven-patterns-from-eight-figure-spend/"),
        ("Why Most Performance Creative Fails (and the Framework That Actually Works)", "Performance Creative", "https://wearemaplemedia.com/performance-creative/why-most-performance-creative-fails-and-the-framework-that-actually-works/"),
        ("How to Build a Profitable Acquisition Engine in a Privacy-First World", "Growth Strategy", "https://wearemaplemedia.com/growth-strategy/how-to-build-a-profitable-acquisition-engine-in-a-privacy-first-world/"),
        ("The 90-Day Creative Velocity System for Scaling DTC Brands", "Growth Strategy", "https://wearemaplemedia.com/growth-strategy/the-90-day-creative-velocity-system-for-scaling-dtc-brands/"),
        ("The Agency Model Is Broken. Here's What Maple Media Is Building Instead.", "Founder's Notes", "https://wearemaplemedia.com/founders-notes/the-agency-model-is-broken-heres-what-maple-media-is-building-instead/"),
        ("Why We Built Maple Media Around Creative Velocity, Not Creative Vanity", "Founder's Notes", "https://wearemaplemedia.com/founders-notes/why-we-built-maple-media-around-creative-velocity-not-creative-vanity/"),
    ]

    for title, category, url in blog_posts:
        st.markdown(
            f'<div class="card-compact" style="padding:0.5rem 0.8rem;">'
            f'<a href="{url}" target="_blank" rel="noopener" style="font-family:\'JetBrains Mono\',monospace;font-size:0.78rem;font-weight:700;color:#000;text-decoration:underline;">{title} ↗</a>'
            f'<span class="badge-outline" style="margin-left:8px;font-size:0.55rem;padding:1px 5px;">{category}</span>'
            f'</div>',
            unsafe_allow_html=True
        )

    # ── VIDEO / YOUTUBE ──
    st.markdown("### VIDEO / YOUTUBE")
    st.markdown(
        f'<div class="card-compact" style="padding:0.7rem 0.9rem;">'
        f'<a href="https://www.youtube.com/@maplemediallc" target="_blank" rel="noopener" style="font-family:\'JetBrains Mono\',monospace;font-size:0.85rem;font-weight:800;color:#000;text-decoration:underline;">MAPLE MEDIA YOUTUBE CHANNEL ↗</a>'
        f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.7rem;color:#555;display:block;margin-top:4px;">@maplemediallc — channel live, video library being built out. Linked in the Loom script intro and the cold email P.S. once you have 2-3 flagship videos.</span>'
        f'</div>',
        unsafe_allow_html=True
    )

    # ── OUTREACH WIRING (HOW I USE YOUR CONTENT) ──
    st.markdown("### HOW THIS CONTENT WIRES INTO OUTREACH")
    st.markdown("""
<div class="wiring" style="line-height:1.9;">
COLD EMAIL E1 (SIGNAL-LED) — OPENS WITH A {{case_study}} PEER REFERENCE → P.S. LINKS A RELEVANT BLOG POST BY CATEGORY<br>
COLD EMAIL FU-01 (DAY 5) — DROPS THE {{case_study_link}} THAT MAPS TO THE PROSPECT'S CATEGORY<br>
LINKEDIN DM — USES THE PROSPECT'S POST TOPIC TO PIVOT INTO THE RELEVANT BLOG POST (NOT A GENERIC LINK)<br>
LOOM SCRIPT — OPENS WITH "I PULLED YOUR SITE + READ YOUR CREATIVE LAB POST" → NAMES 2 CASE STUDIES IN THE P.S.<br>
FOLLOW-UP EMAIL — REPLACES "VIEW CASE STUDIES" WITH A DIRECT CATEGORY-MATCHED CASE STUDY LINK
</div>
""", unsafe_allow_html=True)

    # ── PROOF LINE (for the email P.S.) ──
    st.markdown("### PROOF LINE FOR THE EMAIL P.S.")
    st.markdown(
        f'<div style="border:2px solid #000;background:#FFF;padding:1rem 1.2rem;'
        f'box-shadow:4px 4px 0 0 #000;margin:0.4rem 0 1.2rem;font-family:\'JetBrains Mono\',monospace;'
        f'font-size:0.82rem;line-height:1.55;color:#000;opacity:1;">'
        f'<p style="margin:0 0 0.6rem 0;">P.S. — 7 DTC brands (Ancient Remedies, Callixe, SAINT Eyewear, Primal Queen, Calvris, Jevi, Curvani) saw 1.6–2.7x ROAS on $1.5M+ in combined ad spend. Full case studies here: <a href="https://wearemaplemedia.com/case-studies/" target="_blank" rel="noopener" style="color:#000;">wearemaplemedia.com/case-studies</a></p>'
        f'<p style="margin:0;">P.P.S. — your Creative Lab breakdown on the avatar-first approach is the closest thing to what I\'d build for {{company}}: <a href="https://wearemaplemedia.com/the-creative-lab/the-avatar-first-approach-why-customer-research-is-your-real-creative-advantage/" target="_blank" rel="noopener" style="color:#000;">read it here</a>.</p>'
        f'</div>',
        unsafe_allow_html=True
    )

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 06 PORTFOLIO WIRING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tabs[5]:
    st.markdown('<div class="ph">PORTFOLIO WIRING MAP — 20 PRODUCTION WORKFLOWS</div>', unsafe_allow_html=True)
    st.markdown("Every component of this build is live on the portfolio with steps, metrics, and copy examples.")

    base = "https://rasulshaikh.github.io/gtm-portfolio/"
    workflows = [
        ("OMNIBOUND V12 SIGNAL-LED OUTBOUND",         "PH-02 / EMAIL",       "Signal classification, email variants, 14 subject lines, reply routing"),
        ("VOLUME-BASED OUTBOUND CAMPAIGN",             "PH-02 / EMAIL",       "High-volume layer, 250+ domain fleet, deliverability-gated upload"),
        ("HYPER-PERSONALISED CAMPAIGN",                "PH-02 / EMAIL",       "T1 per-account research, 7-stage LLM pipeline, custom first line"),
        ("RELEVANCE-BASED CAMPAIGN",                   "PH-02 / EMAIL",       "Content engagement trigger, relevance scoring, same-day T1 send"),
        ("CLAY WEBHOOK TO HUBSPOT ENRICHMENT",         "PH-01 / ENRICHMENT",  "Real-time enrich, email classify, lead score, HubSpot sync"),
        ("PRE-SEND LIST QUALITY GATE",                 "PH-01 / GATE",        "8-dimension grading, grade B+ forward, below B blocked"),
        ("WEEKLY DELIVERABILITY AUDIT",                "PH-01 / INFRA",       "SPF/DKIM/DMARC, inbox health, bounce/spam flags — Monday cron"),
        ("FOUNDER-LED CONTENT LOOP",                   "PH-02 / LINKEDIN",    "LinkedIn engager capture, hot/warm/nurture scoring, warm outbound"),
        ("AI LEAD SCORER",                             "PH-01 / SCORING",     "0-100 composite, firmographic + technographic + behavioral"),
        ("CLAY 9-STEP ENRICHMENT",                     "PH-01 / ENRICHMENT",  "85%+ email coverage, waterfall, verify, score, CRM export"),
        ("6 BUYING SIGNALS",                           "PH-01 / SIGNALS",     "Signal ranking by conversion correlation, timing windows, routing"),
        ("SIGNAL SOURCER MASTER WORKFLOW",             "PH-01 / SIGNALS",     "9 signal sub-skills, multi-signal compound scoring"),
        ("COLD EMAIL MASTER SKILL",                    "PH-02 / EMAIL",       "ATL/BTL persona, first touch, follow-up, subject line A/B"),
        ("COLD OUTREACH MESSAGE FRAMEWORK",            "PH-02 / EMAIL",       "First line framework, body components, 80-word gate"),
        ("EMAIL CADENCE LIBRARY",                      "PH-02 / EMAIL",       "23 YAML cadences by signal, vertical, stage"),
        ("INBOUND FOLLOWERS PLAY",                     "PH-02 / LINKEDIN",    "Daily follower export, ICP filter, 48h outreach"),
        ("SIGNAL ACTIVATION (CONTEXT ENGINE)",         "PH-02 / WIRING",      "11-step capture-to-activate engine, tier scoring, HubSpot sync"),
        ("GTM FLYWHEEL 2026 (CONTEXT ENGINE)",         "ALL PHASES",          "Full traffic-to-retention loop, all repos wired"),
        ("OUTBOUND ATTRIBUTION 2026",                  "PH-03 / ATTRIBUTION", "Every touch logged, outbound-influenced signups, revenue reporting"),
        ("REMOTESTATE GTM ENGINE",                     "CASE STUDY",          "Forward Deployed GTM Engineer — $180K ARR in 6 months — worked with existing clients on GTM opportunities"),
    ]

    for name, phase, description in workflows:
        c1, c2, c3 = st.columns([2.6, 1.3, 3.1])
        with c1:
            st.markdown(f'<a href="{base}" style="font-family:\'JetBrains Mono\',monospace;font-size:0.8rem;font-weight:700;color:#000;">{name}</a>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<span class="badge-outline">{phase}</span>', unsafe_allow_html=True)
        with c3:
            st.markdown(f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.75rem;color:#555;">{description}</span>', unsafe_allow_html=True)
        st.markdown("<hr style='margin:0.2rem 0;border:none;border-top:1px solid #ddd;'>", unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# END — Email follow-up template is sent via email, not shown in the app.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
