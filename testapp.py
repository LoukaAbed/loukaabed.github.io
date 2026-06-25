import os
import streamlit as st
import saspy

st.set_page_config(page_title="My App")

# Define your pages
home_page = st.Page("hello.py", title="Home", icon="🏠")
another_page = st.Page("analytics.py", title="test", icon="📊")
third_page = st.Page("hellostreamlit.py", title="test", icon="👋")
fourth_page = st.Page('sas.py', title='SAS Experience', icon='👋')

# --- BACKEND SAS CONFIGURATION ENGINE ---
JAVA_PATH = "/usr/bin/java"
ODA_SERVER = "odaws01-usw2-2.oda.sas.com" # Region 2 server

# 1. Safely extract credentials from Hugging Face secrets
sas_user_credential = st.secrets["SAS_USER"]
if "SAS_PASSWORD" in st.secrets:
    sas_pass_credential = st.secrets["SAS_PASSWORD"]
else:
    sas_pass_credential = st.secrets["SAS_PASS"]

# 2. WRITE THE SYSTEM AUTHINFO FILE (Fixes the EOF Prompt Engine Error)
# On Linux, SASPy inherently looks for a .authinfo file inside the user's home directory.
home_directory = os.path.expanduser("~")
authinfo_path = os.path.join(home_directory, ".authinfo")

# Create the standard .authinfo file structure required by SAS IOM Java drivers
authinfo_content = f"oda user {sas_user_credential} password {sas_pass_credential}\n"

with open(authinfo_path, "w") as f:
    f.write(authinfo_content)

# Linux security permission rule: .authinfo MUST be user-readable only (600), or SASPy rejects it.
os.chmod(authinfo_path, 0o600)


# 3. GENERATE THE SECURE CONFIGURATION DICTIONARY
# Note that we match 'authkey': 'oda' with the string prefix used inside the .authinfo file.
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


@st.cache_resource
def get_sas_session():
    try:
        # Establish connection using the file-based auth token engine
        sas = saspy.SASsession(cfgfile=config_file_path, cfgname="oda")
        return sas
    except Exception as e:
        # Catch and display exact error trace inside the app sidebar for easy debugging
        st.sidebar.error(f"Internal SASPy Connection Error: {e}")
        return None

# Attempt backend connection and cache it globally
sas_session = get_sas_session()

# --- LANDING PAGE CONTENT & INTERFACE ---
st.title("Welcome to the Portfolio Hub")

if sas_session:
    # Save session state globally so sub-pages can inherit the open connection line
    st.session_state["sas_conn"] = sas_session
    st.success("✅ Backend engine successfully linked to SAS OnDemand for Academics.")
    
    # Navigation link directly targeting the fourth page (SAS Experience)
    st.markdown("---")
    st.subheader("Explore the Cloud Analytical Environment")
    if st.button("👉 View Active SAS Workspace"):
        st.switch_page(fourth_page)
else:
    st.error("❌ Failed to initiate underlying SAS cloud connection. Check Hugging Face Secrets setup logs.")
    st.info("💡 Look closely at your application's left sidebar to inspect the direct error code output from SASPy.")

# Group pages and initialize navigation 
nav = st.navigation([home_page, third_page, fourth_page])
nav.run()
