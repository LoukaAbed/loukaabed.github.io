import streamlit as st

st.set_page_config(page_title="My App")

# Define your pages exactly as originally specified
contact = st.Page("contact.py", title="Contact", icon="🏠")
another_page = st.Page("analytics.py", title="Analytics", icon="📊")
third_page = st.Page("hellostreamlit.py", title="Hello Streamlit", icon="👋")

# Run navigation without executing any background connection logic here
nav = st.navigation([contact])
nav.run()
