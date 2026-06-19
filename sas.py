import streamlit as st

st.set_page_config(page_title="Credentials - Dr. Louka Abed", layout="wide")

st.title("🎖️ Professional Certifications & Credentials")
st.write("Bridging clinical medicine with industry-standard regulatory programming compliance.")

# Create columns for visual scannability
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("1. Base Programming")
    st.info("Status: In Progress / Targeting Q3")
    st.markdown("""
    **SAS Certified Specialist**
    * Core data manipulation (`DATA` step)
    * Reading raw clinical logs & CSVs
    * Error handling and log debugging
    """)

with col2:
    st.subheader("2. Advanced Programming")
    st.info("Status: Planned Pipeline")
    st.markdown("""
    **SAS Certified Professional**
    * Automation using SAS Macro Facility
    * High-efficiency relational queries via `PROC SQL`
    * Processing performance optimizations (Arrays/Hash)
    """)

with col3:
    st.subheader("3. Clinical Trials Programming")
    st.info("Status: Crown Jewel Goal")
    st.markdown("""
    **SAS Certified Professional**
    * **CDISC Standards Compliance**
    * Data mapping architectures (**SDTM & ADaM**)
    * Submission-ready TFL reporting (`PROC REPORT`)
    """)

st.divider()
st.caption("Verification badges and official certificates will be linked here upon final testing window.")
