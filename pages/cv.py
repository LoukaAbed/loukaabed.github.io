import streamlit as st
import utils.ui as ui

left, center, right =st.columns(3)
with center:
    st.title("Louka Abed")
st.subheader("Clinical Data Scientist | AI Translational Medicine & Pharma R&D")
st.write("""International Medical Graduate (MD) combining clinical and biochemistry domain expertise with MS in Data Science and Mathematics foundations to validate, 
audit, model, and extract AI insights—accelerating novel drug discovery and building predictive translational medicine pipelines through a systems approach 
that integrates complex healthcare data streams, high-throughput genomic and proteomic registries, and heterogeneous multiomics architectures.""")

st.divider()
ui.message()