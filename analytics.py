import streamlit as st
import requests
import json
import time

st.title("📊 SAS Cloud Analytics Engine")
st.write("This workspace bypasses platform firewalls by piping data execution via native SAS WebSockets.")

def run_sas_via_websocket(sas_code):
    host = "://sas.com"
    username = st.secrets["SAS_USER"]
    password = st.secrets["SAS_PASSWORD"] if "SAS_PASSWORD" in st.secrets else st.secrets["SAS_PASS"]
    
    session = requests.Session()
    
    try:
        # Step 1: Authenticate with the web portal
        base_url = f"https://{host}/SASStudio/"
        session.get(base_url, timeout=15)
        
        login_url = f"https://{host}/SASStudio/j_spring_security_check"
        payload = {'j_username': username, 'j_password': password}
        session.post(login_url, data=payload, allow_redirects=True, timeout=15)
        
        # Step 2: Grab the official API Authorization State
        state_url = f"https://{host}/SASStudio/main/api/state"
        state_res = session.get(state_url, timeout=15)
        
        if state_res.status_code != 200:
            return "Error: Could not retrieve active SAS session authentication tokens."
            
        # Step 3: Trigger code execution via the REST endpoint directly
        # This completely skips the blue JavaScript splash screen!
        submit_url = f"https://{host}/SASStudio/main/api/submit"
        headers = {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
        }
        submit_payload = {
            "code": sas_code,
            "type": "sas"
        }
        
        exec_res = session.post(submit_url, json=submit_payload, headers=headers, timeout=20)
        
        if exec_res.status_code == 200:
            # Step 4: Parse the structured payload containing logs and ODS output tables
            data = exec_res.json()
            
            # Combine execution logs and compiled HTML outputs if they exist
            output_html = data.get("results", {}).get("html", "")
            system_log = data.get("results", {}).get("log", "No operational logs returned.")
            
            return {"html": output_html, "log": system_log}
        else:
            return f"Error: Execution API endpoint responded with code {exec_res.status_code}"
            
    except Exception as e:
        return f"Network Error: {str(e)}"

# --- USER SUBMISSION ENGINE INTERFACE ---
sas_code_input = st.text_area(
    "Modify your SAS execution script:", 
    "proc print data=sashelp.class(obs=5); run;"
)

if st.button("🚀 Execute Code on SAS Cloud", type="primary"):
    with st.spinner("Bypassing splash sequences. Streaming directly to SAS engine..."):
        response_data = run_sas_via_websocket(sas_code_input)
        
        if isinstance(response_data, str):
            st.error(response_data)
        else:
            st.success("✅ Script processed and returned by SAS server!")
            
            tab1, tab2 = st.tabs(["📊 Table Results", "📜 Operational Logs"])
            
            with tab1:
                # If SAS returns a visual data table, render it on screen
                if response_data["html"].strip():
                    st.html(response_data["html"])
                else:
                    st.info("Query successfully compiled, but no visual dataset table was generated.")
                    
            with tab2:
                # Output operational system messages or errors
                st.code(response_data["log"], language="sas")
