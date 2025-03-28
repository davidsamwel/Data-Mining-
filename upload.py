# file_upload.py
import numpy as np
import pandas as pd
import streamlit as st
import io


def file_upload():
     uploaded_file= st.file_uploader("Upload the dataset", type=["csv", "xls", "xlsx"])
     try:
       
       if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1].lower()
        if file_extension == "csv":
             data = pd.read_csv(uploaded_file, encoding='utf-8')
        elif file_extension in ["xls", "xlsx"]:
            data = pd.read_excel(uploaded_file)
        else:
             st.error("Unsupported file format! Please upload a CSV, Excel")
             return None
        st.session_state.data = data
        st.success("File uploaded successfully!")
        st.write("### Preview of the Dataset")
        st.dataframe(data.head())
     except:
         st.error("Unsupported file format! Please upload a CSV, Excel.")

        
        