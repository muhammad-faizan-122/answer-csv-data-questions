import streamlit as st
from llm_reader import CSV_READER


st.title("CSV Query Solver 📊")

with st.form("my_form"):
    user_query = st.text_area("Enter text:", "How many rows are in dataset?")
    csv_path = "data/user_data.csv"
    submitted = st.form_submit_button("Submit")
    if submitted:
        llm_resp = CSV_READER(user_query).llm_response
        st.info(llm_resp)
