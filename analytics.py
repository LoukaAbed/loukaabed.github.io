import streamlit as st

col1, col2 = st.columns([1, 2])
with col1:
    st.image("profile_pic.jpeg", width=200)
with col2:
    st.header("John Doe")
    st.subheader("Data Scientist")
    st.write("📧 john.doe@email.com")

st.markdown("## Experience")
st.write("**Senior Data Analyst** | Tech Corp (2024–Present)")
st.write("- Spearheaded machine learning initiatives...")

st.markdown("## Skills")
st.write("Python, SQL, Streamlit, Machine Learning")
