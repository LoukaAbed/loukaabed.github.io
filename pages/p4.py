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
raw_data = {
    'subject_id': ['10001', '10001', '10002', '10002'],
    'charttime': ['2026-08-29 06:00:00', '2026-08-29 12:00:00', '2026-08-29 08:30:00', '2026-08-29 14:15:00'],
    'creatinine': [1.4, 2.1, 0.8, 0.9],   
    'hemoglobin': [13.5, 13.1, 11.2, 11.5]  
}
df_raw = pd.DataFrame(raw_data)

unique_pts = list(df_raw['subject_id'].unique())
if 'unique_patients' not in st.session_state:
    st.session_state['unique_patients'] = unique_pts
if 'active_patient_idx' not in st.session_state:
    st.session_state['active_patient_idx'] = 0
st.session_state['active_patient'] = st.session_state['unique_patients'][st.session_state['active_patient_idx']]

selected_marker = st.radio("Select a lab marker to visualize", options=['creatinine', 'hemoglobin'], horizontal=True)
