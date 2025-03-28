import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import info,describe,upload,Handle_Missing,Handle_Duplicates,Handle_outliers,Visualization,download,Rename_Columns,Handle_Categorical_Data


st.set_page_config(
    page_title="Data Mining App",
)


st.title("Streamlit Data Mining App")
    # Sidebar with buttons for different tasks
if "data" not in st.session_state:
     st.session_state.data = None
with st.sidebar:
    app=option_menu(
         menu_title='Data Mining',
         options=['Upload The Data','Info','Describe The Data','Rename Columns','Handle Missing','Handle Categorical Data','Handle Duplicates','Handle outliers','Visualization','Download data'],
         icons=['upload','book','table','','','','chat-text-fill','download'],
         menu_icon='chat-text-fill',
         default_index=0,
         styles={
             "container": {"padding": "10!important","background-color":'#383b3e'},
              "icon": {"color": "white", "font-size": "18px"}, 
              "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
               "nav-link-selected": {"background-color": "#02ab21"},}
            )
if app == "Upload The Data":
    upload.file_upload()     
if st.session_state.data is not None:
    if app == "Info":
        info.show_data_info(st.session_state.data)
         
    if app == "Describe The Data":
        describe.describe_data(st.session_state.data)
    if app == "Handle Missing":
        Handle_Missing.handle_missing_values(st.session_state.data) 
    if app == "Handle Duplicates":
        Handle_Duplicates.handle_duplicates(st.session_state.data)  
    if app == "Handle outliers":
        Handle_outliers.handle_outliers(st.session_state.data)  
    if app == "Download data":
        download.download_data(st.session_state.data)
    if app == "Visualization":
        Visualization.visualize(st.session_state.data)     
    if app == "Rename Columns":
        Rename_Columns.rename_columns(st.session_state.data) 
    if app == "Handle Categorical Data":
        Handle_Categorical_Data.handle_categorical_data(st.session_state.data)       
   
            
else:
    st.warning("Please upload a dataset first.")    
        
           
                
