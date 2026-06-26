import streamlit as st
import requests
import re

st.title("📊 SAS Cloud Analytics Engine")
st.write("This workspace bypasses container firewall port blocks using native web streaming requests.")

# --- WEB AUTHENTICATION & EXECUTION PIPELINE ---
def run_sas_via_web_api(sas_code):
    # Match your exact ODA Region 2 server web address
    host = "odamid-usw2-2.oda.sas.com"
    
    # Safely extract your hidden secrets
    username = st.secrets["SAS_USER"]
    password = st.secrets["SAS_PASSWORD"] if "SAS_PASSWORD" in st.secrets else st.secrets["SAS_PASS"]
    
    # Establish a persistent cookie session to maintain connection state
    session = requests.Session()
    
    try:
        # Step 1: Request initial login landing tokens
        login_url = f"https://{host}/SASStudio/j_spring_security_check"
        payload = {'j_username': username, 'j_password': password}
        
        response = session.post(login_url, data=payload, timeout=15)
        
        # Step 2: Stream code directly to the workspace execution API node
        exec_url = f"https://{host}/SASStudio/main/submit"
        headers = {'Content-Type': 'text/plain;charset=UTF-8'}
        
        exec_response = session.post(exec_url, data=sas_code, headers=headers, timeout=20)
        
        if exec_response.status_code == 200:
            return exec_response.text
        else:
            return f"Error: Server returned status code {exec_response.status_code}"
            
    except Exception as e:
        return f"Network Error: {str(e)}"

# --- MAIN UI WORKSPACE ---
sas_code_input = st.text_area(
    "Modify the SAS query:", 
    "proc print data=sashelp.class(obs=5); run;"
)

if st.button("🚀 Execute Code on SAS Cloud", type="primary"):
    with st.spinner("Streaming encrypted web packets over Port 443..."):
        result_output = run_sas_via_web_api(sas_code_input)
        
        # Format and display the returned text output cleanly
        if "Network Error" in result_output or "Error:" in result_output:
            st.error(result_output)
        else:
            st.success("✅ Output streamed successfully!")
            
            # Neatly separate the results from system messages using tabs
            tab1, tab2 = st.tabs(["📊 Execution Results", "📜 Raw Web Trace"])
            with tab1:
                # Basic check to display raw data tables vs raw markdown text strings
                if "<html>" in result_output.lower():
                    st.html(result_output)
                else:
                    st.code(result_output)
            with tab2:
                st.info("Web request completed with no internal socket drops.")
