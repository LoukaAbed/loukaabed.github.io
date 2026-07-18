import streamlit as st


# set config for all subpages
st.set_page_config(
    page_title='Louka Abed | Portfolio',
    page_icon='assets/Louka_portfolio_tab_icon.png',
    layout='wide'
)

# Define page navigation
cv = st.Page("pages/cv.py", title="CV", icon="📋", url_path='cv')
p1 = st.Page("pages/p1.py", title="Project 1", icon="📈", url_path='Project1')
#p2 = st.Page("pages/p2.py", title="Project 2", icon="📈", url_path='Project2')
p3 = st.Page("pages/p3.py", title="Project 3", icon="📈", url_path='Project3')
# Run navigation 
nav = st.navigation([cv, p1, p3])
nav.run()
