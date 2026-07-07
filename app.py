import streamlit as st

st.set_page_config(page_title="My App")

# Define page navigation
contact = st.Page("contact.py", title="Contact", icon="📧")
p1 = st.Page("p1.py", title="Project 1", icon="📈")
# Run navigation without executing any background connection logic here
nav = st.navigation([contact, p1])
nav.run()
