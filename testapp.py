import streamlit as st

# ==============================================================================
# 1. PAGE FUNCTIONS (The content for each individual view)
# ==============================================================================

def render_home():
    """Renders the Home page view."""
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        # Placeholder image - replace with "my_photo.jpg" once available locally
        st.image(
            "https://placeholder.com", 
            caption="Dr. — Clinical Data Scientist", 
            use_container_width=True
        )
        st.markdown("### 🎯 Target Role")
        st.info(
            "Senior Clinical Data Scientist / Principal Biostatistician within "
            "Big Pharma (Oncology, Immunology, or Rare Disease pipelines)."
        )

    with col2:
        st.title("Clinical Data Science Portfolio")
        st.subheader("International Medical Graduate & MS Data Science Candidate")
        
        st.markdown("""
        #### 🎓 Academic Profile
        * **Master of Science in Data Science (Accelerated)** | *Eastern University*
        * **Doctor of Medicine (M.D.) / International Medical Graduate**
        
        #### 🔬 Executive Value Proposition
        I bridge the gap between medical insight and scalable machine learning pipelines. 
        By combining clinical domain expertise with rigorous mathematical programming, 
        I transform complex real-world evidence (RWE), electronic health records (EHR), 
        and CDISC clinical trials datasets into actionable clinical trial strategies.
        """)
        st.success("👈 Select a tab from the permanent sidebar to review my projects or download my CV.")


def render_projects():
    """Renders the Projects page view with R and Python tabs."""
    st.title("💡 Clinical Data Science Repository")
    st.write("A professional collection of statistical modeling, analytics, and software tools built for pharma applications.")
    
    tab_python, tab_r = st.tabs(["🐍 Python Ecosystem", "📊 R Statistical Computing"])
    
    with tab_python:
        st.subheader("Python Implementations")
        
        with st.expander("🚀 Interactive: Phase-III Patient Dropout Risk Calculator", expanded=True):
            st.markdown("**Type:** Live Interactive Widget | **Stack:** Scikit-Learn, Streamlit, Pandas")
            st.write("Simulates trial attrition scoring based on demographic data and patient adherence.")
            
            adherence = st.slider("Patient Treatment Adherence Rate (%)", 0, 100, 85, key="py_adherence")
            adverse_events = st.number_input("Reported Adverse Events", 0, 10, 2, key="py_ae")
            
            risk_score = max(0.0, min(100.0, (100 - adherence) * 1.6 + (adverse_events * 11)))
            st.metric(label="Calculated Drop-out Attrition Risk", value=f"{risk_score:.1f}%")
            st.button("View GitHub Source Code", key="btn_py1")

        with st.expander("📉 Static: Survival Analysis on Synthetic Oncology Cohorts", expanded=False):
            st.markdown("**Type:** Jupyter Notebook | **Stack:** Lifelines, Matplotlib")
            st.write("Conducted Kaplan-Meier analysis and Cox Proportional Hazards modeling to assess treatment response metrics.")
            st.image("https://placeholder.com", caption="Output Graph: Survival Probability vs Days")

    with tab_r:
        st.subheader("R Programming Implementations")
        
        with st.expander("🧪 Interactive: CDISC SDTM Data Transformer Simulation", expanded=True):
            st.markdown("**Type:** Interactive Framework | **Stack:** R, Tidyverse")
            st.write("Validates mock spreadsheet fields against standardized regulatory domains.")
            domain = st.selectbox("Select Domain Mapping Target:", ["Demographics (DM)", "Adverse Events (AE)", "Laboratory (LB)"])
            st.code(f"library(tidyverse)\n\n# Dynamic filter query\ntarget_domain_data <- sdtm_raw %>%\n  filter(DOMAIN == '{domain}')", language="r")

        with st.expander("📊 Static: R-Markdown Production Report Automation", expanded=False):
            st.markdown("**Type:** Automated Document Pipeline | **Stack:** knitr, rmarkdown, ggplot2")
            st.write("Automated standard clinical reporting templates into production-ready PDFs.")
            st.button("Download Sample PDF Artifact", key="btn_r2")


def render_cv():
    """Renders the Interactive Curriculum Vitae page."""
    st.title("📄 Curriculum Vitae")
    
    st.download_button(
        label="📥 Download Full Executive CV (PDF)",
        data=b"Placeholder PDF Byte Content", 
        file_name="Dr_Clinical_Data_Scientist_CV.pdf",
        mime="application/pdf"
    )
    st.markdown("---")
    
    st.header("💼 Highlighted Experience")
    st.markdown("""
    **Graduate Researcher / Data Scientist** | *Eastern University* (Expected Graduation: 2026)
    * Developing advanced machine learning applications and survival analysis scripts for clinical trial tracking.
    
    **International Medical Graduate (M.D.)** | *Clinical Medicine Practice*
    * Managed healthcare cohorts, bringing critical clinical reasoning and medical code domain knowledge directly to the data ecosystem.
    """)
    
    st.header("🛠️ Technical Proficiencies")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Biostatistics & ML:** Survival Analysis, Regression, NLP, Scikit-Learn")
    with c2:
        st.markdown("**Languages & Standards:** R, Python, SQL, CDISC (SDTM/ADaM)")


def render_contact():
    """Renders the Contact Page and social media layout."""
    st.title("✉️ Get In Touch")
    st.write("I am actively exploring Clinical Data Scientist opportunities. Let's start a conversation.")
    
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Name / Institution")
        email = st.text_input("Email Address")
        message = st.text_area("Message")
        if st.form_submit_button("Send Message"):
            if name and email and message:
                st.success(f"Thank you, {name}! Your message was sent successfully.")
            else:
                st.error("Please fill out all fields.")
                
    st.markdown("### 🌐 Professional Links")
    st.markdown("- 👔 **LinkedIn:** [://linkedin.com](https://linkedin.com)\n- 💻 **GitHub:** [://github.com](https://github.com)")


# ==============================================================================
# 2. APPLICATION CONFIGURATION & ENGINE ROUTING
# ==============================================================================

# Global setup configurations
st.set_page_config(
    page_title="Dr. Portfolio | Clinical Data Scientist",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded" # Guarantees sidebar starts in an open position
)

# INJECT CUSTOM CSS: Forces sidebar navigation to remain visible and non-collapsible
st.markdown(
    """
    <style>
        /* 1. Hides the collapse arrow button on the top-left sidebar */
        [data-testid="collapsedControl"] {
            display: none !important;
        }
        
        /* 2. Disables the sidebar resize dragging edge to prevent UI breakages */
        [data-testid="stSidebarResizer"] {
            display: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Define the routing architecture using Streamlit Page Objects
home_page = st.Page(render_home, title="Home Page", icon="🏠", default=True)
projects_page = st.Page(render_projects, title="Projects Portfolio", icon="📊")
cv_page = st.Page(render_cv, title="Curriculum Vitae", icon="📄")
contact_page = st.Page(render_contact, title="Contact Details", icon="✉️")

# 4. Initialize navigation rendering block
pg = st.navigation([home_page, projects_page, cv_page, contact_page])
pg.run()
