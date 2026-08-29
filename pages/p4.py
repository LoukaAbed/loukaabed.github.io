import streamlit as st
import utils.ui as ui
import pandas as pd
import time

st.title("🛡️ FDA-Compliant Regulatory Data Pipeline")
st.subheader("Clinical ETL Engine: Messy EHR to CDISC SDTM Conversion")
st.markdown("""
This system automates the **SDTM Conversion** process, transforming unstructured, 
real-world hospital electronic health records (MIMIC-IV Demo) into standardized, 
audit-ready datasets required for FDA regulatory submissions.
""")