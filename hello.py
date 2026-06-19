import streamlit as st
import smtplib
import os  # Native operating system communications module
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def transmit_pharma_lead(recruiter_name, recruiter_email, lead_subject, lead_body):
    """Establishes a secure connection using Hugging Face Space Environment Variables."""
    try:
        # Hardcode standard Google settings, fetch password securely from Hugging Face
        smtp_target_host = "://gmail.com"
        smtp_target_port = 587
        authenticated_user = "contact@loukaabed.com"
        
        # This line reads your hidden password directly from your Hugging Face settings panel
        app_specific_token = os.environ.get("EMAIL_PASSWORD")

        if not app_specific_token:
            return False, "Configuration Error: EMAIL_PASSWORD secret not found in Hugging Face settings."

        # Formulate email headers
        email_payload = MIMEMultipart()
        email_payload['From'] = authenticated_user
        email_payload['To'] = authenticated_user  
        email_payload['Reply-To'] = recruiter_email
        email_payload['Subject'] = f"💼 Pharma Recruiting: {lead_subject}"

        formatted_message = (
            f"Sender Name / Title: {recruiter_name}\n"
            f"Direct Return Route: {recruiter_email}\n\n"
            f"Message Body:\n{lead_body}"
        )
        email_payload.attach(MIMEText(formatted_message, 'plain', 'utf-8'))

        # Connect to Google SMTP servers
        network_socket = smtplib.SMTP(smtp_target_host, smtp_target_port)
        network_socket.ehlo()      
        network_socket.starttls()  
        network_socket.ehlo()
        
        # Authenticate session
        network_socket.login(authenticated_user, app_specific_token)
        network_socket.sendmail(authenticated_user, authenticated_user, email_payload.as_string())
        network_socket.quit()
        return True, "Transmission deployed safely."
        
    except smtplib.SMTPAuthenticationError:
        return False, "Google Workspace authentication failed. Confirm your 16-character App Password."
    except Exception as network_exception:
        return False, f"Network initialization error: {str(network_exception)}"

# --- STREAMLIT GRAPHICAL RENDERING LAYER ---
st.title("📬 Connect to Dr. Louka Abed's Desk")
st.write("Route strategic pharmaceutical inquiries or trial architecture reviews directly to my enterprise inbox.")

with st.form("secure_contact_gateway", clear_on_submit=True):
    col_left, col_right = st.columns(2)
    
    with col_left:
        input_name = st.text_input("Professional Name / Organization")
        input_subject = st.text_input("Project Objective / Subject Title")
    
    with col_right:
        input_email = st.text_input("Corporate Return Email Address")

    input_message = st.text_area("Pipeline Scope Specifications / Message Context")
    dispatch_trigger = st.form_submit_button("Deploy Encrypted Network Transmission")

    if dispatch_trigger:
        if not input_name or not input_email or not input_message:
            st.warning("All fields are required before deployment.")
        elif "@" not in input_email:
            st.error("Please enter a valid email address.")
        else:
            with st.spinner("Initializing pipeline to Google Workspace..."):
                is_sent, status_log = transmit_pharma_lead(input_name, input_email, input_subject, input_message)
                if is_sent:
                    st.success("Success! Message safely delivered to contact@loukaabed.com.")
                else:
                    st.error(status_log)
