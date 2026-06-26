import os
import streamlit as st
import saspy

st.title("📊 SAS Cloud Analytics Engine")
st.write("This workspace connects to the ODA servers independently via secure web endpoints.")

# --- BACKGROUND SYSTEM WORKER ---
def build_sas_profile_and_connect():
    # Target your specific Region 2 assigned workspace domain
    ODA_SERVER = "odaws01-usw2-2.oda.sas.com" 

    # Safely extract your hidden secrets
    sas_user = st.secrets["SAS_USER"]
    sas_pass = st.secrets["SAS_PASSWORD"] if "SAS_PASSWORD" in st.secrets else st.secrets["SAS_PASS"]

    # NETWORKING FIX: We must pass 'url' with 'https://' over port 443 
    # to punch through Hugging Face's container egress port block. 
    # 'omr': False disables the background metadata server discovery loop.
    config_content = f"""
SAS_config_names = ['oda']
oda = {{
    'iomhost': '{ODA_SERVER}',
    'url': 'https://{ODA_SERVER}:443',
    'user': '{sas_user}',
    'pw': '{sas_pass}',
    'encoding': 'utf-8',
    'omr': False,
    'appname': 'StreamlitApp'
}}
"""
    config_file_path = os.path.abspath("sascfg_personal.py")
    with open(config_file_path, "w") as f:
        f.write(config_content)
        
    # Launch session using the native proxy tunnel settings
    return saspy.SASsession(cfgfile=config_file_path, cfgname="oda")


# --- TIMEOUT PROTECTED CACHE ENGINE ---
@st.cache_resource(show_spinner="Connecting to SAS Cloud Engine...")
def load_subpage_sas_session():
    try:
        sas = build_sas_profile_and_connect()
        return sas
    except Exception as e:
        st.error(f"❌ Internal System Error: {e}")
        return None

# Trigger connection exclusively inside this view state
sas_session = load_subpage_sas_session()

if sas_session:
    st.success("✅ Securely connected to SAS OnDemand for Academics via Web Tunneling.")
    
    # Simple operational testing block
    sas_code = "proc print data=sashelp.class(obs=5); run;"
    res = sas_session.submit(sas_code)
    
    if res.get('LST'):
        st.html(res['LST'])
    else:
        st.code(res.get('LOG', 'No log returned.'), language="sas")
