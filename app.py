import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Mark Brown | Security Contracts & Operations",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #09090b; color: #f4f4f5; }
    .stApp { background-color: #09090b; }
    h1, h2, h3 { color: #fafafa !important; }
    .card { background-color: #18181b; padding: 20px; border-radius: 10px; border: 1px solid #27272a; margin-bottom: 15px; }
    .metric-card { background-color: #18181b; border: 1px solid #3f3f46; padding: 15px; border-radius: 8px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# Session State for Contract Applications
if 'applications' not in st.session_state:
    st.session_state['applications'] = []

# Sidebar Navigation
st.sidebar.markdown("## 🛡️ MARK BROWN")
st.sidebar.markdown("**Independent Security Operations & Supervisor**")
st.sidebar.markdown("---")
nav = st.sidebar.radio("Navigation", ["Home / Overview", "Verified Credentials Index", "Active Contract Board", "Submit Subcontract Inquiry"])

if nav == "Home / Overview":
    st.markdown("# Elite Physical Security Command & Contract Supervision")
    st.markdown("### National Deployment | Travel Ready | Executive Protection & Government Contracting")
    
st.markdown("""<div class="metric-card"><h3>6'6" / 360 lbs</h3><p>Physical Command</p></div>""", unsafe_allow_html=True)

  
    
  
    with col_a:
        st.markdown("### 🎯 Core Capabilities")
        st.markdown("- **Executive Protection & Armed Guarding:** High-visibility deterrence, asset protection, and crowd management.")
        st.markdown("- **Contract Supervision & Site Management:** Managing security personnel, post orders, and compliance for corporate and municipal facilities.")
        st.markdown("- **Physical & Digital Convergence:** Bridging physical security guards with cybersecurity (Mesa CC CCL / ASU) and web infrastructure oversight.")
    
    with col_b:
        st.markdown("### 📞 Direct Contact Dispatch")
        st.markdown("- **Phone:** 408-453-1965")
        st.markdown("- **Email:** info@creativemindedsolutions.com")
        st.markdown("- **Base:** Fort Wayne, Indiana (Ready for nationwide travel & TDY assignments)")

elif nav == "Verified Credentials Index":
    st.markdown("# 📜 Verified Licenses & Credentials Index")
    st.markdown("Complete repository of state licensing, tactical training, and academic transcripts.")
    
    data = {
        "Credential / License": [
            "Private Investigator (PI) License",
            "Armed & Unarmed Security Guard License",
            "Indiana Concealed Carry License (CCW)",
            "Cannabis Dispensary & Retail Health License",
            "California Police Reserve (Level 3 & 2)",
            "Cybersecurity Certificate of Completion (CCL)",
            "Fingerprint Clearance Card",
            "CPR / First Aid & Active Shooter Response"
        ],
        "Issuing Authority": [
            "Arizona Department of Public Safety (DPS)",
            "Arizona DPS / State Compliance",
            "State of Indiana",
            "State / Local Health Authority",
            "California POST / Reserve Standards",
            "Mesa Community College / ASU Cohort",
            "Arizona DPS",
            "National Safety Council / ALERT Academy"
        ],
        "Status": ["Active", "Active", "Active", "Verified", "Completed", "Graduated", "Cleared", "Certified"]
    }
    
    df = pd.DataFrame(data)
    st.table(df)
    
    st.markdown("### 🎓 Higher Education & Honors")
    st.markdown("- **Associate of Arts (AA) in Commercial Art** – Modesto Junior College")
    st.markdown("- **Associate of Science (AS) / AA in Child Development** – Modesto Junior College")
    st.markdown("- **Phi Theta Kappa Honor Society** – Academic Honor Recognition")

elif nav == "Active Contract Board":
    st.markdown("# 📋 Active Contract & Subcontract Opportunities")
    st.markdown("Browse current security supervisory and contract opportunities available for subcontracting or direct placement.")
    
    contracts = [
        {"Company": "Allied Universal", "Role": "Custom Protection Officer / Data Center Supervisor", "Location": "Midwest / Regional", "Rate": "$24 - $28/hr", "Status": "Open"},
        {"Company": "P4 Security Solutions", "Role": "Executive Protection & Flex Supervisor", "Location": "Chicago / Midwest", "Rate": "$25 - $40/hr", "Status": "Active"},
        {"Company": "GardaWorld", "Role": "Remote Security Operations & Site Evaluator", "Location": "Nationwide / Travel", "Rate": "Contract / DOE", "Status": "Open"},
        {"Company": "SAM.gov / Municipal", "Role": "Government Facility Security Supervisor", "Location": "Indiana / Regional", "Rate": "Federal Scale", "Status": "Accepting Bids"}
    ]
    
    for c in contracts:
        st.markdown(f"""
            <div class="card">
                <h3>{c['Company']} — {c['Role']}</h3>
                <p><strong>Location:</strong> {c['Location']} &nbsp;|&nbsp; <strong>Compensation:</strong> {c['Rate']} &nbsp;|&nbsp; <strong>Status:</strong> {c['Status']}</p>
            </div>
        """, unsafe_allow_html=True)

elif nav == "Submit Subcontract Inquiry":
    st.markdown("# 📝 Submit Subcontract / Contract Inquiry")
    st.markdown("Corporate procurement officers and security directors can submit placement or subcontract inquiries directly.")
    
    with st.form("contract_form"):
        company = st.text_input("Company / Agency Name")
        contact_name = st.text_input("Contact Person")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        details = st.text_area("Contract Scope, Location & Requirements")
        submitted = st.form_submit_button("Submit Contract Dispatch")
        
        if submitted:
            if company and email and details:
                st.session_state['applications'].append({
                    "company": company,
                    "contact": contact_name,
                    "email": email,
                    "phone": phone,
                    "details": details,
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                st.success("✅ Inquiry submitted successfully! Mark Brown's operations desk has been notified.")
            else:
                st.error("Please fill in all required fields (Company, Email, Details).")

    if st.session_state['applications']:
        st.markdown("---")
        st.markdown("### Recent Submitted Inquiries")
        for app in st.session_state['applications']:
            st.info(f"**{app['company']}** ({app['contact']} - {app['email']}): {app['details']} [{app['time']}]")
