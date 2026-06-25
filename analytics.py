import os
import streamlit as st
import saspy

st.title("📊 SAS Cloud Analytics Engine")
st.write("This workspace authenticates and executes queries on-demand.")

# --- BACKGROUND SYSTEM PROFILE GENERATOR ---
def initialize_sas_profile():
    JAVA_PATH = "/usr/bin/java"
    ODA_SERVER = "odaws01-usw2-2.oda.sas.com" # Region 2 server

    # Fetch secrets cleanly
    sas_user = st.secrets["SAS_USER"]
    sas_pass = st.secrets["SAS_PASSWORD"] if "SAS_PASSWORD" in st.secrets else st.secrets["SAS_PASS"]

    # Generate a headless profile file directly in the container home directory
    home_directory = os.path.expanduser("~")
    authinfo_path = os.path.join(home_directory, ".authinfo")
    
    with open(authinfo_path, "w") as f:
        f.write(f"oda user {sas_user} password {sas_pass}\n")
    os.chmod(authinfo_path, 0o600)

    # Write localized personal configuration mapping block
    config_content = f"""
SAS_config_names = ['oda']
oda = {{
    'java': '{JAVA_PATH}',
    'iomhost': '{ODA_SERVER}',
    'iomport': 8591,
    'authkey': 'oda',
    'encoding': 'utf-8'
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
        sas = saspy.SASsession(cfgfile=cfg_path, cfgname="oda")
        return sas
    except Exception as e:
        st.error(f"Engine connection failed: {e}")
        return None

# Trigger connection ONLY when the user is actively visiting this subpage
sas_session = load_subpage_sas_session()

if sas_session:
    st.success("✅ Securely connected to SAS OnDemand for Academics.")
    
    # Simple operational testing block
    sas_code = "proc print data=sashelp.class(obs=5); run;"
    res = sas_session.submit(sas_code)
    st.html(res['LST'])
else:
    st.error("❌ Failed to initiate underlying SAS cloud connection.")
