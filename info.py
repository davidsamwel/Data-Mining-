
import streamlit as st
import pandas as pd
def show_data_info(data):
   st.write("## Dataset Information")
   st.write(f"Number of Rows: {data.shape[0]}")
   st.write(f"Number of Columns: {data.shape[1]}") 
   st.write("## Column Information")
   changes = {}
   special_chars_dict = {}
   
   for col in data.columns:
      st.write(f"### Column: {col}")
      st.write(f"Data Type: {data[col].dtype}")
      st.write(f"Number of Numerical Values: {data[col].apply(pd.to_numeric, errors='coerce').notnull().sum()}")
      st.write(f"Number of NaN Values: {data[col].isnull().sum()}")
      st.write(f"Count of Unique Values: {data[col].nunique()}")
            
            # Count special characters
      special_chars = get_special_char_count(data[col], special_chars_dict)
      st.write(f"Count of Special Characters: {special_chars}")
      

      if data[col].nunique() <20:
         st.write(f"Unique Values: {data[col].unique()}")
            
            # Change datatype
      new_type = st.selectbox(
        "Change Data Type for :",
        ["No Change", "int", "float", "str","Date Time"],key=f"{col}_dtype")
      try:
         if new_type=="int":
             data[col] = data[col].astype(new_type)
             st.success(f"Data Type Changed to {new_type}")
         elif new_type=="float": 
             data[col] = data[col].astype(new_type)
             st.success(f"Data Type Changed to {new_type}")
         elif new_type=="str": 
             data[col] = data[col].astype(new_type)
             st.success(f"Data Type Changed to {new_type}")
         elif new_type=="Date Time": 
            data[col]=pd.to_datetime(data[col]) 
            st.success(f"Data Type Changed to {new_type}")    
      except:
          st.error("Error: Unable to change data type")    
      st.write("---")
        
       
       
def get_special_char_count(column, special_chars_dict):
    if column.dtype == "object":
        special_chars = [char for char in column.unique() if not str(char).isalnum()]
        special_chars_dict[column.name] = special_chars
        return len(special_chars)
    return 0

