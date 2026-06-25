import os
import streamlit as st
import saspy
import concurrent.futures

st.title("📊 SAS Cloud Analytics Engine")
st.write("This workspace connects to the ODA servers independently without impacting your home page.")

# --- BACKGROUND SYSTEM WORKER ---
def build_sas_profile_and_connect():
    JAVA_PATH = "/usr/bin/java"
    ODA_SERVER = "odaws01-usw2-2.oda.sas.com" # Region 2 server

    # Safely extract your hidden secrets
    sas_user = st.secrets["SAS_USER"]
    sas_pass = st.secrets["SAS_PASSWORD"] if "SAS_PASSWORD" in st.secrets else st.secrets["SAS_PASS"]

    # Generate a headless profile file directly in the container home directory to stop EOF prompts
    home_directory = os.path.expanduser("~")
    authinfo_path = os.path.join(home_directory, ".authinfo")
    with open(authinfo_path, "w") as f:
        f.write(f"oda user {sas_user} password {sas_pass}\n")
    os.chmod(authinfo_path, 0o600)

    # Re-apply the stable Java connection mapping block
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
        
    # Return the opened session directly
    return saspy.SASsession(cfgfile=config_file_path, cfgname="oda")


# --- TIMEOUT PROTECTED CACHE ENGINE ---
@st.cache_resource(show_spinner="Connecting to SAS Cloud Engine...")
def load_subpage_sas_session():
    # Force connection process into a separate thread to break infinite loading loops
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(build_sas_profile_and_connect)
        try:
            # Cut the loop off if it takes longer than 15 seconds to reply
            sas_instance = future.result(timeout=15)
            return sas_instance
        except concurrent.futures.TimeoutError:
            st.error("⌛ The SAS Cloud connection timed out (Server took too long to reply).")
            return "TIMEOUT"
        except Exception as e:
            st.error(f"❌ Internal System Error: {e}")
            return None

# Trigger connection exclusively inside this view state
sas_session = load_subpage_sas_session()

if sas_session and sas_session != "TIMEOUT":
    st.success("✅ Securely connected to SAS OnDemand for Academics.")
    
    # Simple operational testing block
    sas_code = "proc print data=sashelp.class(obs=5); run;"
    res = sas_session.submit(sas_code)
    
    if res.get('LST'):
        st.html(res['LST'])
    else:
        st.code(res.get('LOG', 'No log returned.'), language="sas")
elif sas_session == "TIMEOUT":
    st.info("💡 The SAS server did not acknowledge the container handshake. Try clicking another tab and returning here to re-trigger.")
