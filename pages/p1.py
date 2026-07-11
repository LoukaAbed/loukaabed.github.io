import streamlit as st
import utils.db_utils as db

st.title("Neon Database Connection Test")
st.divider()

query = "SELECT * FROM bp where gender = :gender and age > :age"
st.write(db.fetch_db(query, {"gender": "Male", "age": 25}))

st.divider()
min_age, max_age = st.slider("Age", 0.0, 100.0, value=(0.0, 100.0), key="age")
query_age = "SELECT * FROM bp where gender = :gender and age between :min_age and :max_age"
gender = st.radio(label="Gender", options=["Male", "Female"], horizontal=True)
st.write(db.fetch_db(query_age, {"gender": gender, "min_age": min_age, "max_age": max_age}))
