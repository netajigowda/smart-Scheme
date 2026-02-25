import streamlit as st
from engine import EligibilityEngine
from schemes_data import SCHEMES_DATA

# Set Page Config
st.set_page_config(
    page_title="Smart Scheme Predictor",
    page_icon="🏛️",
    layout="centered",
)

# Custom CSS for Premium Design System (Replicating the original Glassmorphism)
st.markdown("""
<style>
    /* Base styling */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    .main {
        background: radial-gradient(circle at 50% 0%, #1e293b 0%, #0f172a 100%);
        color: #f8fafc;
    }
    
    /* Header styling */
    .header-container {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .title-text {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff 0%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .subtitle-text {
        color: #94a3b8;
        font-size: 1.2rem;
    }
    
    /* Card design */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(24px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 2rem;
        box-shadow: 0 20px 50px -12px rgba(0, 0, 0, 0.5);
        margin-bottom: 2rem;
    }
    
    /* Result card styling */
    .scheme-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: transform 0.3s ease;
    }
    
    .scheme-card:hover {
        transform: translateY(-5px);
        border-color: #6366f1;
    }
    
    .category-badge {
        font-size: 0.7rem;
        font-weight: 800;
        text-transform: uppercase;
        color: #6366f1;
        background: rgba(99, 102, 241, 0.15);
        padding: 4px 10px;
        border-radius: 100px;
        letter-spacing: 0.1em;
    }
    
    .fit-badge {
        font-size: 0.8rem;
        font-weight: 800;
        color: #10b981;
        background: rgba(16, 185, 129, 0.1);
        padding: 4px 10px;
        border-radius: 100px;
        float: right;
    }
    
    .scheme-name {
        font-size: 1.4rem;
        font-weight: 800;
        margin-top: 0.75rem;
        color: #ffffff;
    }
    
    .scheme-desc {
        color: #94a3b8;
        font-size: 1rem;
        margin-top: 0.5rem;
    }
    
    .doc-tag {
        display: inline-block;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 0.75rem;
        margin-top: 0.5rem;
        margin-right: 0.5rem;
        color: #cbd5e1;
    }

    /* Buttons */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
        color: white !important;
        border-radius: 16px !important;
        padding: 0.75rem 1rem !important;
        font-weight: 800 !important;
        border: none !important;
        box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.4) !important;
    }
</style>
""", unsafe_allow_html=True)

# Application Header
st.markdown("""
<div class="header-container">
    <div style="font-size: 3.5rem;">🏛️</div>
    <div class="title-text">Smart Scheme Predictor</div>
    <p class="subtitle-text">Find personalized government benefits based on your profile.</p>
</div>
""", unsafe_allow_html=True)

# Initialize Session State for results
if 'results' not in st.session_state:
    st.session_state.results = None

# Input Form
with st.container():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=1, max_value=110, value=25)
        income = st.number_input("Annual Income (₹)", min_value=0, value=50000)
        occupation = st.selectbox("Occupation", ["Farmer", "Laborer", "Unskilled Laborer", "Small Business", "Student", "Homemaker", "Other"])
    
    with col2:
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        caste = st.selectbox("Category", ["General", "OBC", "SC", "ST", "BPL"])
        location = st.selectbox("Location Type", ["Rural", "Urban"])
        disability = st.selectbox("Disability Status", ["No", "Yes"])

    find_schemes = st.button("Find Schemes ✨")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Prediction Logic
if find_schemes:
    user_data = {
        "age": age,
        "income": income,
        "occupation": occupation,
        "gender": gender,
        "caste": caste,
        "location": location,
        "disability": disability
    }
    
    engine = EligibilityEngine(SCHEMES_DATA)
    st.session_state.results = engine.predict(user_data)
    st.rerun()

# Display Results
if st.session_state.results is not None:
    st.markdown("## Your Eligible Schemes")
    
    if not st.session_state.results:
        st.info("No matching schemes found. Try adjusting your profile (e.g., lower income or different category).")
    else:
        for result in st.session_state.results:
            st.markdown(f"""
            <div class="scheme-card">
                <span class="category-badge">{result['category']}</span>
                <span class="fit-badge">Fit {result['priorityScore']}%</span>
                <div class="scheme-name">{result['name']}</div>
                <p class="scheme-desc">{result['description']}</p>
                <div style="margin-top: 1rem;">
                    {"".join(f'<span class="doc-tag">{doc}</span>' for doc in result['documents'])}
                </div>
                <div style="margin-top: 1rem; font-size: 0.9rem; color: #6366f1; font-weight: 600;">
                    How to Apply:
                    <p style="color: #94a3b8; font-weight: 400; font-size: 0.85rem;">{result['how_to_apply']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

# Reset Button
if st.session_state.results is not None:
    if st.button("← Reset Profile"):
        st.session_state.results = None
        st.rerun()
