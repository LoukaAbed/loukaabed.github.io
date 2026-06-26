import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("📊 SAS Cloud Analytics Engine")
st.write("This workspace streams data directly from your SAS OnDemand region node over a secure web protocol.")

# --- COMPACT WEB ACCESS ENGINE ---
def run_sas_via_web_api(sas_code):
    # Your verified SAS ODA US Region 2 host domain
    host = "odamid-usw2-2.oda.sas.com"
    
    # Safely extract your hidden secrets
    username = st.secrets["SAS_USER"]
    password = st.secrets["SAS_PASSWORD"] if "SAS_PASSWORD" in st.secrets else st.secrets["SAS_PASS"]
    
    # Build a persistent session block to carry security credentials
    session = requests.Session()
    
    try:
        # Step 1: Explicitly establish connection to the primary workspace index
        base_url = f"https://{host}/SASStudio/"
        session.get(base_url, timeout=15)
        
        # Step 2: Handle the Spring Security Check gateway challenge
        login_url = f"https://{host}/SASStudio/j_spring_security_check"
        payload = {
            'j_username': username,
            'j_password': password
        }
        
        # Follow redirects strictly to pass the radial loading splash sequence
        login_response = session.post(login_url, data=payload, allow_redirects=True, timeout=15)
        
        # Step 3: Package your analytical script and push to the primary execution vector
        exec_url = f"https://{host}/SASStudio/main/submit"
        headers = {
            'Content-Type': 'text/plain;charset=UTF-8',
            'Referer': f"https://{host}/SASStudio/main"
        }
        
        exec_response = session.post(exec_url, data=sas_code, headers=headers, timeout=25)
        
        if exec_response.status_code == 200:
            return exec_response.text
        else:
            return f"Error: The remote server responded with status flag {exec_response.status_code}"
            
    except Exception as e:
        return f"Network Error Framework Failure: {str(e)}"

# --- INTERACTIVE USER VIEWPORTS ---
sas_code_input = st.text_area(
    "Modify the workspace SAS script query:", 
    "proc print data=sashelp.class(obs=5); run;"
)

if st.button("🚀 Execute Code on SAS Cloud", type="primary"):
    with st.spinner("Streaming encrypted web requests over Port 443..."):
        result_output = run_sas_via_web_api(sas_code_input)
        
        if "Network Error" in result_output or "Error:" in result_output:
            st.error(result_output)
        else:
            st.success("✅ Execution request completed successfully!")
            
            # Neatly distribute logs and dataset tables using interface tabs
            tab1, tab2 = st.tabs(["📊 Compiled Table View", "📜 Raw Response Details"])
            
            with tab1:
                # If the returned payload contains rich HTML data tables, render it visually
                if "<table>" in result_output.lower() or "class=" in result_output.lower():
                    st.html(result_output)
                else:
                    # Parse text if it's returning raw text values
                    soup = BeautifulSoup(result_output, "html.parser")
                    clean_text = soup.get_text()
                    st.code(clean_text if clean_text.strip() else "No printable text returned.")
                    
            with tab2:
                # Show raw code payload for validation checks
                st.code(result_output[:5000], language="html")
