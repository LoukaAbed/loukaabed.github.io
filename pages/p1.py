import streamlit as st
import utils.db_utils as db

st.title("Neon Database Connection Test")
st.divider()

query = "SELECT * FROM bp where gender = :gender and age > :age"
st.write(db.db_fetch(query, {"gender": "Male", "age": 25}))
