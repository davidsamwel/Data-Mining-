# handle_outliers.py
import streamlit as st
import pandas as pd
import numpy as np

def handle_outliers(data):
    st.title("Handle Outliers")
    
    numeric_columns = data.select_dtypes(include=["number"]).columns.tolist()
    if not numeric_columns:
        st.error("No numerical columns found in the dataset!")
        return

    
    selected_column = st.selectbox("Select a numeric column", numeric_columns)
   
    
    method = st.selectbox(
        "Select a method to handle outliers",
        ["Remove Outliers", "Replace with Mean", "Replace with Median",'Drop Column']
    )

    
    st.write("### Dataset Preview (Before Handling)")
    st.dataframe(data[[selected_column]].describe())

    # Button to apply outlier handling
    if st.button("Apply"):
        q1 = data[selected_column].quantile(0.25)
        q3 = data[selected_column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        original_count = len(data)

        if method == "Remove Outliers":
            data = data[(data[selected_column] >= lower_bound) & (data[selected_column] <= upper_bound)]
            st.success(f"Outliers in '{selected_column}' removed.")
        
        elif method == "Replace with Mean":
            mean_value = data[selected_column].mean()
            data[selected_column] = np.where(
                (data[selected_column] < lower_bound) | (data[selected_column] > upper_bound),
                mean_value,
                data[selected_column],
            )
            st.success(f"Outliers in '{selected_column}' replaced with mean.")

        elif method == "Replace with Median":
            median_value = data[selected_column].median()
            data[selected_column] = np.where(
                (data[selected_column] < lower_bound) | (data[selected_column] > upper_bound),
                median_value,
                data[selected_column],
            )
            st.success(f"Outliers in '{selected_column}' replaced with median.")

        elif method=="Drop Column":
            df=pd.DataFrame(data)
            df = df.drop(columns=[selected_column],axis=1)
            st.success(f"Column '{selected_column}' has been dropped.")
            data = df
            st.write("### Data Description after drop")
            st.dataframe(data.describe())   
            
            

        # Show changes
        if method != "Drop Column":
            new_count = len(data)
            st.write(f"Rows before: **{original_count}**, Rows after: **{new_count}**")

            # Show dataset preview after handling
            st.write("### Dataset Preview (After Handling)")
            st.dataframe(data[[selected_column]].describe())


