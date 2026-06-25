import os
import streamlit as st
import saspy

st.title("📊 SAS Cloud Analytics Engine")
st.write("This workspace authenticates and executes queries on-demand via secure web sockets.")

# --- BACKGROUND SYSTEM PROFILE GENERATOR ---
def initialize_sas_profile():
    # Target your specific Region 2 assigned workspace domain
    ODA_SERVER = "odaws01-usw2-2.oda.sas.com" 

    # Safely extract your secrets from Hugging Face settings
    sas_user = st.secrets["SAS_USER"]
    sas_pass = st.secrets["SAS_PASSWORD"] if "SAS_PASSWORD" in st.secrets else st.secrets["SAS_PASS"]

    # FORCE THE HTTP WEB DRIVER PROFILE: Completely removed 'java' and 'iomport' keys.
    # Passing the exact 'url' parameters tells SASPy to bypass local JAR classpaths.
    config_content = f"""
SAS_config_names = ['oda']
oda = {{
    'iomhost': '{ODA_SERVER}',
    'url': 'https://{ODA_SERVER}:443',
    'user': '{sas_user}',
    'pw': '{sas_pass}',
    'encoding': 'utf-8',
    'omr': False,
    'appname': 'StreamlitHF'
}}
"""
    config_file_path = os.path.abspath("sascfg_personal.py")
    with open(config_file_path, "w") as f:
        f.write(config_content)
        
    return config_file_path

# Cache the connection locally within this specific subpage instance
@st.cache_resource
def load_subpage_sas_session():
    try:
        cfg_path = initialize_sas_profile()
        # Launch session using the native python driver config profile
        sas = saspy.SASsession(cfgfile=cfg_path, cfgname="oda")
        return sas
    except Exception as e:
        st.error(f"Engine connection failed: {e}")
        return None

# Trigger connection ONLY when the user is actively visiting this subpage
sas_session = load_subpage_sas_session()

if sas_session:
    st.success("✅ Securely connected to SAS OnDemand for Academics via Web Sockets.")
    
    # Simple operational testing block
    sas_code = "proc print data=sashelp.class(obs=5); run;"
    res = sas_session.submit(sas_code)
    
    if res.get('LST'):
        st.html(res['LST'])
    else:
        st.code(res.get('LOG', 'No log returned.'), language="sas")
else:
    st.error("❌ Failed to initiate underlying SAS cloud connection.")
