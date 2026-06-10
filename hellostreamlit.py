import streamlit as st

tab1, tab2, tab3 = st.tabs(["Overview", "Data", "Settings"])

with tab1:
    st.write("Welcome to the overview tab!")
    st.line_chart([1, 5, 3, 2])

with tab2:
    st.write("Here is the raw data.")

with tab3:
    st.write("Adjust your settings here.")
