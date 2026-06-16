import streamlit as st

st.set_page_config(
    page_title="Maple Media - GTM Engine",
    page_icon="🍁",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&family=JetBrains+Mono:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background: #ffffff;
    color: #000000;
}

.block-container { padding: 2rem 2.5rem 4rem; max-width: 1100px; }

h1 { font-weight: 900; font-size: 2rem; text-transform: uppercase; letter-spacing: -0.02em; border-bottom: 3px solid #000; padding-bottom: 0.5rem; }
h2 { font-weight: 700; font-size: 1.15rem; text-transform: uppercase; letter-spacing: 0.08em; margin-top: 2rem; }
h3 { font-weight: 700; font-size: 0.95rem; text-transform: uppercase; letter-spacing: 0.06em; color: #FF3000; }

.accent { color: #FF3000; }
.mono { font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; }

.phase-header {
    background: #000;
    color: #fff;
    padding: 0.6rem 1rem;
    font-weight: 700;
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin: 1.5rem 0 1rem;
}

.signal-badge {
    display: inline-block;
    background: #FF3000;
    color: #fff;
    font-size: 0.7rem;
    font-weight: 700;
    padding: 2px 8px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin: 2px;
}

.channel-card {
    border: 2px solid #000;
    padding: 1.2rem;
    margin: 0.75rem 0;
}

.email-preview {
    border-left: 3px solid #FF3000;
    padding: 1rem 1.2rem;
    background: #f8f8f8;
    font-size: 0.88rem;
    line-height: 1.7;
    margin: 0.75rem 0;
}

.email-subject {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    color: #FF3000;
    font-weight: 700;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

.tool-row {
    border-bottom: 1px solid #e5e5e5;
    padding: 0.5rem 0;
    font-size: 0.88rem;
}

.wiring-line {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    color: #555;
    background: #f4f4f4;
    padding: 0.5rem 0.75rem;
    border-left: 2px solid #FF3000;
    margin: 0.5rem 0;
}

.metric-box {
    border: 2px solid #000;
    padding: 1rem;
    text-align: center;
}
.metric-val { font-size: 1.6rem; font-weight: 900; color: #FF3000; }
.metric-lbl { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em; color: #555; margin-top: 2px; }

.price-card {
    border: 2px solid #000;
    padding: 1.2rem;
    margin: 0.5rem 0;
}
.price-val { font-size: 1.4rem; font-weight: 900; }
.price-lbl { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em; color: #555; }

div[data-testid="stSidebar"] {
    background: #000;
    color: #fff;
}
div[data-testid="stSidebar"] h1,
div[data-testid="stSidebar"] h2,
div[data-testid="stSidebar"] h3,
div[data-testid="stSidebar"] p,
div[data-testid="stSidebar"] li { color: #fff !important; }
div[data-testid="stSidebar"] a { color: #FF3000 !important; }

.stTabs [data-baseweb="tab-list"] { gap: 0; border-bottom: 2px solid #000; }
.stTabs [data-baseweb="tab"] {
    background: #fff;
    border: 2px solid #000;
    border-bottom: none;
    border-radius: 0;
    font-weight: 700;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    padding: 0.5rem 1rem;
    margin-right: 2px;
}
.stTabs [aria-selected="true"] { background: #000 !important; color: #fff !important; }

.stExpander { border: 1px solid #ddd !important; border-radius: 0 !important; }

footer { visibility: hidden; }
#MainMenu { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### RASUL SHAIKH")
    st.markdown("GTM Engineer")
    st.markdown("---")
    st.markdown("**PRICING**")
    st.markdown("$30 / hr")
    st.markdown("$4,000 / month")
    st.markdown("**$10,000 / quarter** (recommended)")
    st.markdown("---")
    st.markdown("**CASE STUDIES**")
    st.markdown("RemoteState - $180K ARR in 6 months")
    st.markdown("FalconWise - 10+ SQLs/mo, 30% engagement")
    st.markdown("Omnibound AI - 1.5%+ reply rate, 300+ mailboxes")
    st.markdown("---")
    st.markdown("**PORTFOLIO**")
    st.markdown("[rasulshaikh.github.io/gtm-portfolio](https://rasulshaikh.github.io/gtm-portfolio/)")
    st.markdown("[github.com/rasulshaikh](https://github.com/rasulshaikh)")
    st.markdown("---")
    st.markdown("**CONTACT**")
    st.markdown("Rasul Shaikh")

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown("""
<h1><span class="accent">MAPLE MEDIA</span> GTM ENGINE</h1>
<p style="font-size:0.85rem;color:#555;text-transform:uppercase;letter-spacing:0.1em;">
North America - DTC / E-commerce - Startups to Enterprise
</p>
""", unsafe_allow_html=True)

# Metrics row
m1, m2, m3, m4, m5 = st.columns(5)
metrics = [
    ("3", "Channels"),
    ("6", "Signal Types"),
    ("50+", "Sending Domains"),
    ("85%+", "Email Coverage"),
    ("$180K", "ARR in 6 Months"),
]
for col, (val, lbl) in zip([m1, m2, m3, m4, m5], metrics):
    with col:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-val">{val}</div>
            <div class="metric-lbl">{lbl}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Overview ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="phase-header">WHAT GETS BUILT</div>
<p style="font-size:0.95rem;line-height:1.8;">
A three-layer GTM engine that runs continuously and compounds over time.
Not a campaign - a system. Every layer feeds the next: intelligence drives outreach,
outreach generates data, data sharpens targeting. After 60 days the system knows exactly
which DTC founder profile, at which growth stage, responding to which signal, converts.
That intelligence lives in HubSpot - not in a spreadsheet.
</p>
""", unsafe_allow_html=True)

# ── Tabs ─────────────────────────────────────────────────────────────────────
tabs = st.tabs(["PHASE 1: INTELLIGENCE", "PHASE 2: OUTBOUND", "PHASE 3: ATTRIBUTION", "TOOL STACK", "PORTFOLIO WIRING", "EMAIL"])

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 1: INTELLIGENCE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tabs[0]:
    st.markdown("<div class='phase-header'>PHASE 1 - INTELLIGENCE LAYER - WEEKS 1-2</div>", unsafe_allow_html=True)
    st.markdown("*Who to reach, when, and why - before anything sends.*")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ICP SCORING")
        st.markdown("""
| Dimension | How Scored |
|---|---|
| GMV tier | Seed / Growth / Enterprise |
| Ad spend | Meta-heavy, TikTok-native, Google-first |
| Tech stack | Shopify, Klaviyo, Triple Whale, Northbeam |
| Headcount | Solo founder to 200+ |
| Growth signal | Live trigger - hire, raise, review, expansion |
""")

        st.markdown("### PRE-SEND LIST GATE")
        st.markdown("Every list graded A+ to F across 8 dimensions before upload. Below grade B = blocked + Slack alert.")
        gate_items = [
            "Email validity rate",
            "Domain diversity",
            "Role relevance to ICP",
            "Seniority match",
            "Company size match",
            "Signal match rate",
            "Duplicate rate",
            "Bounce history",
        ]
        for i, item in enumerate(gate_items, 1):
            st.markdown(f"**{i}.** {item}")

    with col2:
        st.markdown("### SIGNAL STACK")
        signals = [
            ("New CMO / head of growth hired", "Trigify + LinkedIn", "Last 30 days"),
            ("Funding round raised", "Crunchbase + Trigify", "Last 30 days"),
            ("Attribution tool switch", "BuiltWith + Trigify", "Last 14 days"),
            ("Negative agency review on G2 / Clutch", "Apify scrape", "Last 14 days"),
            ("North American market expansion", "LinkedIn + Crunchbase", "Last 60 days"),
            ("LinkedIn post on creative / ROAS / scaling", "PhantomBuster", "Last 7 days"),
        ]
        for signal, source, window in signals:
            st.markdown(f"""
<div class="channel-card" style="padding:0.6rem 0.8rem;margin:0.4rem 0;">
<span class="signal-badge">{window}</span><br>
<strong style="font-size:0.85rem;">{signal}</strong><br>
<span style="font-size:0.75rem;color:#555;">{source}</span>
</div>
""", unsafe_allow_html=True)

    st.markdown("### ENRICHMENT PIPELINE (CLAY 9-STEP)")
    st.markdown("""
<div class="wiring-line">
Upload → Company Enrich → People Enrich → Email Waterfall (Findymail > Prospeo > BetterContact) → ZeroBounce Verify → Phone (T1 only) → Claygent Custom Data → AI Lead Score 0-100 → HubSpot Export with Tier Tag
</div>
""", unsafe_allow_html=True)

    ecol1, ecol2, ecol3 = st.columns(3)
    with ecol1:
        st.markdown("""<div class="metric-box"><div class="metric-val">85%+</div><div class="metric-lbl">Email Coverage</div></div>""", unsafe_allow_html=True)
    with ecol2:
        st.markdown("""<div class="metric-box"><div class="metric-val">40%</div><div class="metric-lbl">Single-Finder Avg</div></div>""", unsafe_allow_html=True)
    with ecol3:
        st.markdown("""<div class="metric-box"><div class="metric-val">0-100</div><div class="metric-lbl">AI Lead Score</div></div>""", unsafe_allow_html=True)

    st.markdown("### DOMAIN FLEET + DELIVERABILITY")
    st.markdown("""
- 50+ sending domains, SPF / DKIM / DMARC on every domain
- 3-4 week inbox warm-up before campaign launch
- 50-domain rotation per campaign run
- Weekly deliverability audit every Monday: bounce rate, spam rate, domain health, reply rate flags - Slack report
""")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 2: OUTBOUND
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tabs[1]:
    st.markdown("<div class='phase-header'>PHASE 2 - OUTBOUND ENGINE - WEEKS 3-5</div>", unsafe_allow_html=True)
    st.markdown("*Three channels running in parallel, each firing on a specific signal.*")

    st.markdown("""
| Channel | Tool | Tier | Volume |
|---|---|---|---|
| Cold Email | Smartlead | T1 + T2 | 500-2,000 / week |
| LinkedIn | HeyReach | T1 | 50-100 / week |
| Personalized Video | Loom | T1 top 50 | 20-50 / month |
""")

    # Channel 1
    st.markdown("""<div class="channel-card">
<h3 style="color:#FF3000;font-size:0.85rem;text-transform:uppercase;letter-spacing:0.08em;margin:0 0 0.5rem;">
CHANNEL 1 - COLD EMAIL (SMARTLEAD)
</h3>
</div>""", unsafe_allow_html=True)

    st.markdown("**Wiring:**")
    st.markdown("""<div class="wiring-line">
Clay scored list - pre-send gate - Smartlead upload - sequence runs - reply detected - n8n webhook - HubSpot deal created + Slack alert
</div>""", unsafe_allow_html=True)

    st.markdown("**3 Copy Angles for DTC Brands:**")
    a1, a2, a3 = st.columns(3)
    with a1:
        st.markdown("""<div class="channel-card">
<strong style="color:#FF3000;">ANGLE 1</strong><br>Creative Attribution Gap<br>
<span style="font-size:0.82rem;color:#444;">Spending on creative but can't prove which concepts drive pipeline vs impressions. Maple Media closes that gap.</span>
</div>""", unsafe_allow_html=True)
    with a2:
        st.markdown("""<div class="channel-card">
<strong style="color:#FF3000;">ANGLE 2</strong><br>Competitor Visibility<br>
<span style="font-size:0.82rem;color:#444;">Competitor showing up in buyer shortlists before they do. Maple Media gets them into those answers.</span>
</div>""", unsafe_allow_html=True)
    with a3:
        st.markdown("""<div class="channel-card">
<strong style="color:#FF3000;">ANGLE 3</strong><br>North American Market Entry<br>
<span style="font-size:0.82rem;color:#444;">Expanding from UK / EU / MENA. Needs a creative partner who knows the channel dynamics, not just the product.</span>
</div>""", unsafe_allow_html=True)

    st.markdown("**Variant Matrix:** E1 x 3 (signal-led hooks) | E2 x 2 (social proof) | 10 subject lines rotated by company hash | 80-word gate on every send")

    with st.expander("VIEW EMAIL COPY EXAMPLES"):
        st.markdown("""<div class="email-subject">SIGNAL: NEW HEAD OF GROWTH HIRED</div>
<div class="email-preview">
<strong>Subject:</strong> scaling creative at [Company] - the system behind it<br><br>
Hey [First Name],<br><br>
Saw [Company] just brought on a head of growth. The first 90 days usually come down to one question: is the creative engine producing enough signal to know what's working, or are you still guessing?<br><br>
Most DTC brands at [Company]'s stage are spending on creative without a system to know which concepts drive pipeline versus impressions.<br><br>
Maple Media builds the repeatable engine behind that: research, structure, testing, and iteration so your head of growth can optimize from real data.<br><br>
3 brands in [industry] saw a measurable lift in pipeline-attributed creative within 60 days.<br><br>
Worth 20 minutes to see what that looks like for [Company]?
</div>""", unsafe_allow_html=True)

        st.markdown("""<div class="email-subject">SIGNAL: NEGATIVE G2 / CLUTCH REVIEW</div>
<div class="email-preview">
<strong>Subject:</strong> [Company] just left a review - here's what that usually means<br><br>
Hey [First Name],<br><br>
[Company] posted a review about their last creative agency. The feedback was about consistency and results, not quality.<br><br>
That gap is almost always a system problem, not a talent problem. The agency was producing creative without a repeatable engine behind the testing and iteration.<br><br>
Maple Media's model is built the other way: research and framework first, then creative output from a structured process. Creative that compounds instead of resets every quarter.<br><br>
Happy to show you what that looks like in 20 minutes.
</div>""", unsafe_allow_html=True)

        st.markdown("""<div class="email-subject">SIGNAL: FUNDING ROUND RAISED</div>
<div class="email-preview">
<strong>Subject:</strong> saw the raise - pipeline velocity matters now<br><br>
Hey [First Name],<br><br>
Saw [Company] closed [round]. Post-raise, the pipeline target just got bigger. Most teams respond by scaling content. The ones building pipeline aren't just publishing more - they're building from the exact prompts buyers use when evaluating [category] brands.<br><br>
Maple Media builds from that intelligence. The result is creative that earns pipeline, not just impressions.<br><br>
Worth a 30-minute conversation?
</div>""", unsafe_allow_html=True)

        st.markdown("""<div class="email-subject">FOLLOW-UP - DAY 5 (CASE STUDY)</div>
<div class="email-preview">
<strong>Subject:</strong> re: scaling creative at [Company]<br><br>
Hey [First Name],<br><br>
Following up on the note about creative attribution.<br><br>
RemoteState went from zero GTM infrastructure to $180K ARR in 6 months. The first thing we fixed was knowing which campaigns were driving pipeline versus burning budget. Everything else followed from that.<br><br>
Case study is here if useful: [link]<br><br>
Happy to show you what that first 30 days looks like for [Company].
</div>""", unsafe_allow_html=True)

        st.markdown("""<div class="email-subject">FOLLOW-UP - DAY 14 (SOFT CLOSE)</div>
<div class="email-preview">
<strong>Subject:</strong> last one from me<br><br>
Hey [First Name],<br><br>
Dropping this one last note in case the timing wasn't right earlier.<br><br>
If creative attribution - knowing which concepts drive pipeline versus impressions - is something you're thinking about this quarter, worth 20 minutes.<br><br>
If not, no worries at all.
</div>""", unsafe_allow_html=True)

    # Channel 2
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""<div class="channel-card">
<h3 style="color:#FF3000;font-size:0.85rem;text-transform:uppercase;letter-spacing:0.08em;margin:0 0 0.5rem;">
CHANNEL 2 - LINKEDIN (HEYREACH)
</h3>
</div>""", unsafe_allow_html=True)

    st.markdown("**Wiring:**")
    st.markdown("""<div class="wiring-line">
PhantomBuster (post engagers / followers) - Clay ICP filter - HeyReach sequence - reply - HubSpot tag + Slack
</div>""", unsafe_allow_html=True)

    st.markdown("""
| Day | Action |
|---|---|
| D1 | Engage with target's most recent post - genuine comment |
| D3 | Connection request with light context, no pitch |
| D5 | DM if accepted - references their post, one question, no CTA |
| D8 | Cold email lands (coordinated with email sequence) |
""")
    st.markdown("**Follower play:** Daily follower export - Clay ICP filter within 24h - warm outreach same day")

    with st.expander("VIEW LINKEDIN DM EXAMPLES"):
        st.markdown("""<div class="email-subject">AFTER CONNECTION ACCEPTED</div>
<div class="email-preview">
Hey [First Name], appreciate the connect.<br><br>
Saw your post on [creative testing / ROAS / scaling DTC] last week. One thing that keeps coming up with the brands I talk to at your stage: the creative is good, but there is no system behind knowing which concepts drive actual pipeline versus impressions.<br><br>
Curious - is that something you're solving internally right now, or still a bit of a black box?
</div>""", unsafe_allow_html=True)

        st.markdown("""<div class="email-subject">FOLLOWER PLAY - WARM INTENT</div>
<div class="email-preview">
Hey [First Name], noticed you followed - appreciate it.<br><br>
Looks like you're working on [growth / creative / performance] at [Company]. I've been building GTM engines for DTC brands - mostly the infrastructure behind knowing which creative actually drives pipeline.<br><br>
Happy to share what's been working if that's useful.
</div>""", unsafe_allow_html=True)

    # Channel 3
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""<div class="channel-card">
<h3 style="color:#FF3000;font-size:0.85rem;text-transform:uppercase;letter-spacing:0.08em;margin:0 0 0.5rem;">
CHANNEL 3 - VIDEO / LOOM (T1 TOP 50 ONLY)
</h3>
</div>""", unsafe_allow_html=True)

    st.markdown("**Fires on:** New CMO hire | Round raised | 3+ touches without reply (high intent, no conversion)")
    st.markdown("**Wiring:**")
    st.markdown("""<div class="wiring-line">
Clay flags T1 - Loom recorded per account - linked in email as P.S. - Loom watch event triggers HubSpot deal update
</div>""", unsafe_allow_html=True)

    with st.expander("VIEW LOOM SCRIPT"):
        st.markdown("""<div class="email-preview">
<em>Format: 60-90 seconds, screen share of their website, specific to their creative stack. Not generic.</em><br><br>
"Hey [First Name] - I pulled [Company]'s site before recording this. You're running [product category] creatives focused on [angle - social proof / founder story / UGC]. The creative is strong.<br><br>
What I don't see is a testing framework behind it - a way to know which angles are driving pipeline for your new [CMO / head of growth] in the first 90 days.<br><br>
That's exactly what Maple Media builds. Not a one-off audit. A repeatable system: research, concept structure, testing cadence, and iteration loop. So your team can optimize from signal, not guesswork.<br><br>
I'll drop two case study links in the email below. Happy to walk you through what the first 30 days looks like for [Company] - 20 minutes, no pitch deck."
</div>""", unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 3: ATTRIBUTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tabs[2]:
    st.markdown("<div class='phase-header'>PHASE 3 - ATTRIBUTION + ITERATION - ONGOING</div>", unsafe_allow_html=True)
    st.markdown("*Close the loop. Every touch tracked. Every winner doubled down on.*")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### WHAT GETS TRACKED")
        touches = [
            ("Email sent", "Outbound campaign touch"),
            ("Email opened", "Engagement flag"),
            ("Email replied", "Deal created + signal tag + Slack alert"),
            ("LinkedIn DM sent", "LinkedIn touch"),
            ("LinkedIn DM replied", "LinkedIn conversion tag"),
            ("Loom watched", "Video engagement flag"),
            ("Site visit post-email (RB2B)", "Silent conversion tag"),
            ("Signed up without replying", "Outbound-influenced signup"),
        ]
        for touch, log in touches:
            st.markdown(f"""
<div class="tool-row">
<strong>{touch}</strong><br>
<span style="font-size:0.78rem;color:#FF3000;">{log}</span>
</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown("### WEEKLY ITERATION LOOP")
        st.markdown("Every Monday:")
        steps = [
            "Which signal types generated meetings last week",
            "Which copy angles got replies",
            "Which channel made first contact on converted accounts",
            "Underperformers flagged and paused",
            "Winners get additional variants built",
        ]
        for i, step in enumerate(steps, 1):
            st.markdown(f"**{i}.** {step}")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### FULL-FUNNEL REPORTING")
        st.markdown("""<div class="wiring-line">
Outbound touch - reply - meeting booked - deal created - revenue closed
</div>""", unsafe_allow_html=True)
        st.markdown("Outbound-influenced signups captured even when the contact did not reply to the cold email.")
        st.markdown("Silent conversions: prospect visited site after email without replying - still tracked and tagged.")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### WHAT MAKES IT SCALABLE")
        st.markdown("""
- Month 1: 500 contacts/week, 3 email variants, LinkedIn on T1 only
- Month 3: 2,000 contacts/week, 9 variants optimized from reply data, full multichannel on T1 + T2
- Month 6: System self-corrects. Underperforming signals deprioritized automatically. Winning angles get more variants.

Infrastructure cost stays flat. Output scales.
""")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 4: TOOL STACK
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tabs[3]:
    st.markdown("<div class='phase-header'>FULL TOOL STACK</div>", unsafe_allow_html=True)

    tools = [
        ("LIST BUILDING", "Apollo", "ICP pull by title, industry, headcount, geo"),
        ("ENRICHMENT", "Clay", "9-step enrichment table, IIFE scoring formulas, Claygent custom data"),
        ("EMAIL FINDING", "Findymail + Prospeo + BetterContact", "Waterfall email discovery - 85%+ coverage"),
        ("EMAIL VERIFICATION", "ZeroBounce", "Removes invalid + risky contacts before send"),
        ("AI SCORING", "Claude via Clay", "0-100 lead score, copy hook generation per contact"),
        ("SIGNAL DETECTION", "Trigify", "Job changes, funding rounds, expansion signals"),
        ("TECH STACK DETECTION", "BuiltWith", "Attribution tool switch, Shopify / Klaviyo detection"),
        ("WEBSITE VISITORS", "RB2B", "Anonymous visitor identification post-email"),
        ("LINKEDIN SCRAPING", "PhantomBuster", "Post engagers, follower export, profile data"),
        ("EMAIL SEQUENCING", "Smartlead", "50+ domain fleet, A/B testing, bounce monitoring"),
        ("LINKEDIN OUTREACH", "HeyReach", "Connection requests, DM sequences, comment engagement"),
        ("VIDEO", "Loom", "Personalized 60-90s videos for T1 accounts"),
        ("ORCHESTRATION", "n8n", "Webhooks, routing logic, CRM sync, dead letter queue"),
        ("CRM", "HubSpot", "Contact management, deal creation, attribution, reporting"),
        ("ALERTS", "Slack", "Real-time reply alerts, deliverability flags, weekly report"),
    ]

    for layer, tool, description in tools:
        c1, c2, c3 = st.columns([1.2, 1.5, 3])
        with c1:
            st.markdown(f"<span style='font-size:0.7rem;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;color:#FF3000;'>{layer}</span>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"**{tool}**")
        with c3:
            st.markdown(f"<span style='font-size:0.85rem;color:#444;'>{description}</span>", unsafe_allow_html=True)
        st.markdown("<hr style='margin:0.3rem 0;border:none;border-top:1px solid #eee;'>", unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 5: PORTFOLIO WIRING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tabs[4]:
    st.markdown("<div class='phase-header'>PORTFOLIO WIRING MAP</div>", unsafe_allow_html=True)
    st.markdown("Every component of this build is live on the portfolio with steps, metrics, and copy examples.")

    portfolio_base = "https://rasulshaikh.github.io/gtm-portfolio/"

    workflows = [
        ("Omnibound v12 Signal-Led Outbound", "Phase 2 - Email", "Signal classification, email variants, 14 subject lines, reply routing"),
        ("Volume-Based Outbound Campaign", "Phase 2 - Email", "High-volume layer, 250+ domain fleet, deliverability-gated upload"),
        ("Hyper-Personalised Campaign", "Phase 2 - Email", "T1 per-account research, 7-stage LLM pipeline, custom first line"),
        ("Relevance-Based Campaign", "Phase 2 - Email", "Content engagement trigger, relevance scoring, same-day T1 send"),
        ("Clay Webhook to HubSpot Enrichment", "Phase 1 - Enrichment", "Real-time enrich, email classify, lead score, HubSpot sync"),
        ("Pre-Send List Quality Gate", "Phase 1 - Gate", "8-dimension grading, grade B+ forward, below B blocked"),
        ("Weekly Deliverability Audit", "Phase 1 - Infra", "SPF/DKIM/DMARC, inbox health, bounce/spam flags - Monday cron"),
        ("Founder-Led Content Loop", "Phase 2 - LinkedIn", "LinkedIn engager capture, hot/warm/nurture scoring, warm outbound"),
        ("AI Lead Scorer", "Phase 1 - Scoring", "0-100 composite, firmographic + technographic + behavioral"),
        ("Clay 9-Step Enrichment", "Phase 1 - Enrichment", "85%+ email coverage, waterfall, verify, score, CRM export"),
        ("6 Buying Signals", "Phase 1 - Signals", "Signal ranking by conversion correlation, timing windows, routing"),
        ("Signal Sourcer Master Workflow", "Phase 1 - Signals", "9 signal sub-skills, multi-signal compound scoring"),
        ("Cold Email Master Skill", "Phase 2 - Email", "ATL/BTL persona, first touch, follow-up, subject line A/B"),
        ("Cold Outreach Message Framework", "Phase 2 - Email", "First line framework, body components, 80-word gate"),
        ("Email Cadence Library", "Phase 2 - Email", "23 YAML cadences by signal, vertical, stage"),
        ("Inbound Followers Play", "Phase 2 - LinkedIn", "Daily follower export, ICP filter, 48h outreach"),
        ("Signal Activation (Context Engine)", "Phase 2 - Wiring", "11-step capture-to-activate engine, tier scoring, HubSpot sync"),
        ("GTM Flywheel 2026 (Context Engine)", "All Phases", "Full traffic-to-retention loop, all repos wired"),
        ("Outbound Attribution 2026", "Phase 3 - Attribution", "Every touch logged, outbound-influenced signups, revenue reporting"),
        ("RemoteState Greenfield GTM Engine", "Case Study", "Zero to $180K ARR in 6 months - closest parallel to this build"),
    ]

    phase_colors = {
        "Phase 1": "#f0f0f0",
        "Phase 2": "#fff0ee",
        "Phase 3": "#f0fff0",
        "All": "#fffff0",
        "Case": "#f0f0ff",
    }

    for name, phase, description in workflows:
        phase_key = phase.split(" - ")[0].replace("Phase 1", "Phase 1").replace("Phase 2", "Phase 2").replace("Phase 3", "Phase 3")
        c1, c2, c3 = st.columns([2.5, 1.2, 3])
        with c1:
            st.markdown(f"**[{name}]({portfolio_base})**")
        with c2:
            color = "#FF3000" if "Phase 2" in phase else ("#000" if "Phase 1" in phase else ("#555" if "Phase 3" in phase else "#888"))
            st.markdown(f"<span style='font-size:0.72rem;font-weight:700;text-transform:uppercase;letter-spacing:0.06em;color:{color};'>{phase}</span>", unsafe_allow_html=True)
        with c3:
            st.markdown(f"<span style='font-size:0.82rem;color:#444;'>{description}</span>", unsafe_allow_html=True)
        st.markdown("<hr style='margin:0.3rem 0;border:none;border-top:1px solid #eee;'>", unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 6: EMAIL
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tabs[5]:
    st.markdown("<div class='phase-header'>THE EMAIL - FOLLOW-UP VERSION</div>", unsafe_allow_html=True)
    st.markdown("*Send this after an initial call or intro. This is the full written breakdown.*")

    st.markdown("""<div class="email-subject">SUBJECT: GTM PLAN FOR MAPLE MEDIA - TOOLS, CHANNELS, AND WIRING</div>""", unsafe_allow_html=True)

    st.markdown("""<div class="email-preview">
Hey [Name],<br><br>
Good talking. Here's the full GTM plan - tool stack, channel selection, copy examples, and how everything is wired together.<br><br>
<strong>What I'd build for you - 3 phases:</strong><br><br>
<strong>Phase 1: Intelligence (Weeks 1-2)</strong><br>
ICP scoring table in Clay across 5 dimensions: GMV tier, ad spend category, tech stack (Shopify, Klaviyo, Triple Whale detection), headcount, and live growth signal. Every contact gets a 0-100 AI lead score before anything sends. Anything below a grade B is blocked from ever touching your sending domains.<br><br>
Signals I'd track for your ICP: new CMO / head of growth hired (last 30 days), round raised, attribution tool switch, negative agency review on G2 or Clutch, North American market expansion, and LinkedIn content engagement on creative or ROAS posts.<br><br>
<strong>Phase 2: Outbound on 3 channels (Weeks 3-5)</strong><br><br>
Cold email via Smartlead (50+ sending domain fleet):<br>
- Signal-led sequences - every email references the specific trigger that fired it<br>
- 3 copy angles: creative attribution gap, competitor visibility, North American market entry<br>
- E1 x 3 variants, E2 x 2 variants, 10 subject lines rotated by company hash<br>
- 80-word gate - nothing sends over 80 words<br><br>
LinkedIn via HeyReach (T1 accounts): post engagement Day 1, connection request Day 3, DM Day 5 (one question, no pitch), email lands Day 8. Follower play runs daily.<br><br>
Video / Loom (top 50 T1 accounts per month): 60-90 seconds, specific to their website and creative stack. Fires on new CMO hire, round raised, or 3+ touches without reply. Linked in email as P.S.<br><br>
<strong>Phase 3: Attribution and iteration (ongoing)</strong><br>
Every touch across all 3 channels logged in HubSpot. Weekly loop: which signals and copy angles generated meetings, feed back into ICP scoring weights. The system gets sharper every cycle. Infrastructure cost stays flat. Output scales.<br><br>
<strong>Full tool stack:</strong><br>
Clay (enrichment + scoring) | Apollo (list pull) | Findymail + Prospeo (email waterfall) | ZeroBounce (verify) | Smartlead (email, 50-domain fleet) | HeyReach (LinkedIn) | Loom (video) | n8n (webhooks, routing) | HubSpot (CRM, attribution) | Trigify (signals) | RB2B (visitor ID) | Slack (alerts)<br><br>
All 20 workflows that map to this build are live on the portfolio with steps, metrics, and copy examples:<br>
<a href="https://rasulshaikh.github.io/gtm-portfolio/">rasulshaikh.github.io/gtm-portfolio/</a><br><br>
RemoteState case study (greenfield GTM, $180K ARR in 6 months) and FalconWise case study (ABM engine, 10+ SQLs/mo) are both downloadable from the portfolio.<br><br>
<strong>Pricing:</strong> $30/hr | $4,000/mo | $10,000/quarter (full Phase 1-3 build + documented playbook you own at the end)<br><br>
Happy to walk through the specific workflows that map to your setup in 30 minutes, or send a scoped Phase 1 proposal to start with infrastructure.<br><br>
Rasul
</div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### SEND ORDER")
    st.markdown("""
1. Send the cold version (Option B) if no prior contact
2. After they respond, send this full follow-up with the plan link
3. Attach this page as a link - share the URL directly
4. Record a 90-second Loom of their website before the call - it will get a reply on its own
""")
