import streamlit as st
import utils.db_utils as db

st.title("Neon Database Connection Test")
st.divider()

query = "SELECT * FROM bp where gender = :gender and age > :age"
st.write(db.fetch_db(query, {"gender": "Male", "age": 25}))

st.divider()
min_age, max_age = st.slider("Age", 0.0, 100.0, value=(0.0, 100.0), key="age")
st.write(f"Selected age range: {min_age} - {max_age}")
