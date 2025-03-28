import numpy as np
import pandas as pd
import streamlit as st
import io
def download_data(data):
    csv = data.to_csv(index=False)
    st.download_button(
    label="Download Dataset as CSV",
    data=csv,
    file_name='Cleaned Data Set',
    mime="text/csv"
    )
