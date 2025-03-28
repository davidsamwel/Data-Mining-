
import streamlit as st

def describe_data(data):
    st.write("### Data Description")
    st.dataframe(data.describe())  