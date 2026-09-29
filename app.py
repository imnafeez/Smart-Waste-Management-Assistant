import streamlit as st
import requests

# FastAPI Backend Configuration
BACKEND_URL = "http://127.0.0.1:8000"

# Page Configuration
st.set_page_config(
    page_title="Smart Waste Management Assistant",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Dark Navy / Charcoal Theme)
st.markdown("""
    <style>
    /* Dark Charcoal Theme Base */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #1e293b;
        border-right: 1px solid #334155;
    }
    
    /* Headers & Text */
    h1, h2, h3, h4, h5, h6 {
        color: #f8fafc !important;
        font-weight: 600;
    }
    p, span, label {
        color: #cbd5e1 !important;
    }

    /* Cards Styling */
    .feature-card {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }
    .feature-card h3 {
        color: #10b981 !important;
        margin-top: 0;
        margin-bottom: 12px;
    }
    
    .result-card {
        background-color: #1e293b;
        border-left: 4px solid #10b981;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 16px;
    }
    
    .badge-category {
        display: inline-block;
        background-color: #065f46;
        color: #34d399 !important;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.95rem;
        margin-bottom: 15px;
    }

    /* Buttons */
    div.stButton > button {
        background-color: #059669;
        color: #ffffff !important;
        font-weight: 600;
        border-radius: 8px;
        padding: 10px 24px;
        border: none;
        transition: all 0.2s ease-in-out;
    }
    div.stButton > button:hover {
        background-color: #047857;
        border: none;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
    }

    /* Input elements styling */
    .stTextArea textarea, .stSelectbox select {
        background-color: #1e293b !important;
        color: #f8fafc !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
    }

    /* Footer Disclaimer */
    .disclaimer-box {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 14px 20px;
        font-size: 0.85rem;
        color: #94a3b8 !important;
        margin-top: 40px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize navigation session state
if "page" not in st.session_state:
    st.session_state["page"] = "🏠 Home"

def set_page(page_name):
    st.session_state["page"] = page_name

# Sidebar Navigation
st.sidebar.title("♻️ Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "🔍 Identify Waste", "📜 History", "ℹ️ About"],
    index=["🏠 Home", "🔍 Identify Waste", "📜 History", "ℹ️ About"].index(st.session_state["page"])
)
st.session_state["page"] = page


# ==========================================
# HOME PAGE
# ==========================================
if st.session_state["page"] == "🏠 Home":
    st.title("♻️ Smart Waste Management Assistant")
    st.markdown("### *A simple tool to identify waste types and provide basic disposal guidance.*")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="feature-card">
                <h3>🔍 Identify Waste</h3>
                <p>Enter a waste item or select a common waste type to immediately categorize your waste.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="feature-card">
                <h3>🌱 Understand Impact</h3>
                <p>Learn about environmental impacts and why responsible waste handling matters.</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="feature-card">
                <h3>♻️ Get Disposal Guidance</h3>
                <p>View basic handling instructions and recommended disposal actions.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Start Analysis", key="btn_start_home"):
        set_page("🔍 Identify Waste")
        st.rerun()


# ==========================================
# ANALYSIS PAGE
# ==========================================
elif st.session_state["page"] == "🔍 Identify Waste":
    st.title("🔍 Identify & Analyze Waste")
    st.markdown("Enter details about your waste item below or pick from common waste categories.")
    st.markdown("---")

    col_input1, col_input2 = st.columns([2, 1])

    with col_input1:
        user_text = st.text_area(
            "Waste Item Description",
            placeholder="Example: I have an old mobile phone and charger that I no longer use.",
            height=120
        )

    with col_input2:
        common_types = [
            "Select a waste type",
            "Plastic Waste",
            "Paper Waste",
            "Glass Waste",
            "Food Waste",
            "E-Waste",
            "Metal Waste",
            "Medical Waste",
            "Battery Waste",
            "Organic/Garden Waste",
            "Textile Waste"
        ]
        selected_category = st.selectbox("Common Waste Types", options=common_types)

    st.markdown("<br>", unsafe_allow_html=True)
    analyze_click = st.button("🔍 Analyze Waste", key="btn_analyze")

    if analyze_click:
        # Determine effective query
        query = ""
        if selected_category and selected_category != "Select a waste type":
            query = selected_category
        elif user_text.strip():
            query = user_text.strip()

        if not query:
            st.warning("Please enter a waste item description or select a common waste type.")
        else:
            with st.spinner("Analyzing waste details via FastAPI backend..."):
                try:
                    response = requests.post(
                        f"{BACKEND_URL}/api/analyze",
                        json={"waste_type": query},
                        timeout=5
                    )
                    
                    if response.status_code == 200:
                        data = response.json()
                        st.markdown("---")
                        st.subheader("📋 Analysis Result")

                        category = data.get("waste_category", "Unclassified")
                        st.markdown(f'<span class="badge-category">Category: {category}</span>', unsafe_allow_html=True)

                        # Results layout
                        res_col1, res_col2 = st.columns(2)

                        with res_col1:
                            st.markdown(f"""
                                <div class="result-card">
                                    <h4>🗑️ Disposal Method</h4>
                                    <p>{data.get("disposal_method", "N/A")}</p>
                                </div>
                            """, unsafe_allow_html=True)

                            st.markdown(f"""
                                <div class="result-card">
                                    <h4>🌱 Environmental Impact</h4>
                                    <p>{data.get("environmental_impact", "N/A")}</p>
                                </div>
                            """, unsafe_allow_html=True)

                        with res_col2:
                            st.markdown(f"""
                                <div class="result-card">
                                    <h4>📦 Basic Handling</h4>
                                    <p>{data.get("basic_handling", "N/A")}</p>
                                </div>
                            """, unsafe_allow_html=True)

                            st.markdown(f"""
                                <div class="result-card">
                                    <h4>✅ Recommended Action</h4>
                                    <p>{data.get("recommended_action", "N/A")}</p>
                                </div>
                            """, unsafe_allow_html=True)

                    else:
                        st.error("Backend error: Unable to analyze the input. Please try again.")

                except requests.exceptions.ConnectionError:
                    st.error("🔌 Could not connect to FastAPI backend server. Please make sure backend server is running on http://127.0.0.1:8000.")
                except Exception as e:
                    st.error("An unexpected error occurred while contacting the server.")


# ==========================================
# HISTORY PAGE
# ==========================================
elif st.session_state["page"] == "📜 History":
    st.title("📜 Waste Analysis History")
    st.markdown("View past waste analysis queries and recommended disposal methods saved in SQLite.")
    st.markdown("---")

    try:
        response = requests.get(f"{BACKEND_URL}/api/history", timeout=5)
        if response.status_code == 200:
            records = response.json()
            if records:
                # Format records into clean tabular structure
                formatted_records = []
                for rec in records:
                    formatted_records.append({
                        "ID": rec.get("id"),
                        "Date": rec.get("date"),
                        "Waste Item": rec.get("waste_item"),
                        "Category": rec.get("category"),
                        "Disposal Method": rec.get("disposal_method")
                    })
                st.dataframe(formatted_records, use_container_width=True, hide_index=True)
            else:
                st.info("No analysis history recorded yet. Perform an analysis to view saved entries.")
        else:
            st.error("Unable to retrieve history records from backend.")
    except requests.exceptions.ConnectionError:
        st.error("🔌 Could not connect to FastAPI backend. Ensure backend is running.")
    except Exception:
        st.error("An error occurred while loading history data.")


# ==========================================
# ABOUT PAGE
# ==========================================
elif st.session_state["page"] == "ℹ️ About":
    st.title("ℹ️ About the Project")
    st.markdown("---")

    st.markdown("""
        <div class="feature-card">
            <h3>📖 Smart Waste Management Assistant</h3>
            <p>The Smart Waste Management Assistant is a web-based application designed to help users quickly identify common waste materials, learn about their environmental impacts, and apply proper disposal procedures.</p>
        </div>
    """, unsafe_allow_html=True)

    col_ab1, col_ab2 = st.columns(2)

    with col_ab1:
        st.markdown("""
            <div class="feature-card">
                <h3>🎯 Project Objective</h3>
                <p>“To provide a simple and user-friendly tool for basic waste identification and responsible disposal guidance.”</p>
            </div>
        """, unsafe_allow_html=True)

    with col_ab2:
        st.markdown("""
            <div class="feature-card">
                <h3>🛠️ Technologies Used</h3>
                <ul>
                    <li><b>Python</b> — Core logic and processing</li>
                    <li><b>FastAPI</b> — Lightweight backend API framework</li>
                    <li><b>Streamlit</b> — Interactive frontend UI</li>
                    <li><b>SQLite</b> — Built-in relational database storage</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)


# ==========================================
# FOOTER DISCLAIMER
# ==========================================
st.markdown("""
    <div class="disclaimer-box">
        ⚠️ <b>Disclaimer:</b> This is a basic waste-management guidance assistant. Follow local waste-disposal rules and consult the appropriate waste-management authority when required.
    </div>
""", unsafe_allow_html=True)
