import streamlit as st
import requests

st.title("📊 SAS Cloud Analytics Engine")
st.write("This workspace communicates with your SAS ODA backend cleanly over secure web APIs.")

def run_sas_via_api_endpoint(sas_code):
    # Your assigned server region domain URL
    host = "odamid-usw2-2.oda.sas.com"
    
    # Extract secrets from your Hugging Face space configuration
    username = st.secrets["SAS_USER"]
    password = st.secrets["SAS_PASSWORD"] if "SAS_PASSWORD" in st.secrets else st.secrets["SAS_PASS"]
    
    session = requests.Session()
    
    try:
        # Step 1: Initialize cookies with the regional server
        base_url = f"https://{host}/SASStudio/"
        session.get(base_url, timeout=15)
        
        # Step 2: Authenticate securely past the login gate
        login_url = f"https://{host}/SASStudio/j_spring_security_check"
        payload = {'j_username': username, 'j_password': password}
        
        # Allow redirection to register session parameters on the server
        session.post(login_url, data=payload, allow_redirects=True, timeout=15)
        
        # Step 3: Direct API Execution Submissions (Bypasses the blue screen!)
        # We target the actual service dispatcher endpoint rather than the user viewport webpage
        submit_url = f"https://{host}/SASStudio/main/api/submit"
        headers = {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
        }
        submit_payload = {
            "code": sas_code,
            "type": "sas"
        }
        
        # Submit payload via json block
        exec_response = session.post(submit_url, json=submit_payload, headers=headers, timeout=25)
        
        if exec_response.status_code == 200:
            return exec_response.text
        else:
            return f"Error: Server rejected submission request with code {exec_response.status_code}"
            
    except Exception as e:
        return f"Network Exception Framework Error: {str(e)}"

# --- INTERACTIVE USER LAYOUT ---
sas_code_input = st.text_area(
    "Modify the SAS query:", 
    "proc print data=sashelp.class(obs=5); run;"
)

if st.button("🚀 Execute Code on SAS Cloud", type="primary"):
    with st.spinner("Streaming calculations directly to the API handler..."):
        result_output = run_sas_via_api_endpoint(sas_code_input)
        
        if "Error" in result_output or "Exception" in result_output:
            st.error(result_output)
        else:
            st.success("✅ Output successfully computed and returned!")
            
            # Neatly group text and logs using application layout tabs
            tab1, tab2 = st.tabs(["📊 Compiled Results", "📜 Raw Technical Response"])
            
            with tab1:
                # If the execution returned native ODS HTML table tags, render them visually
                if "<table>" in result_output.lower() or "class=" in result_output.lower():
                    st.html(result_output)
                else:
                    st.code(result_output)
                    
            with tab2:
                st.text_area("Full Response Dump", value=result_output[:10000], height=300)
