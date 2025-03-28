import streamlit as st
import pandas as pd
import random

def random_imputation(column):
    """Randomly impute missing values with existing values in the column."""
    non_null_values = column.dropna().values
    return column.apply(lambda x: random.choice(non_null_values) if pd.isnull(x) else x)

def handle_missing_values(data):
    st.title("Handle Missing Values")
    
    # Identify columns with missing values
    missing_counts = data.isnull().sum()
    columns_with_missing = missing_counts[missing_counts > 0].index.tolist()

    if not columns_with_missing:
        st.success("No missing values found in the dataset!")
        return
    
    selected_column = st.selectbox("Select a column with missing values", columns_with_missing)

    method = st.selectbox(
        "Select a method to handle missing values",
        ["Fill with Mean", "Fill with Median", "Fill with Mode", "Drop Rows", "Random Imputation"]
    )

    st.write("### Dataset Preview (Before Handling)")
    st.dataframe(data.head(10))  

    if st.button("Apply"):
        try:
            if method == "Fill with Mean":
                data[selected_column].fillna(data[selected_column].mean(), inplace=True)
                st.success(f"Missing values in '{selected_column}' filled with mean.")
            elif method == "Fill with Median":
                data[selected_column].fillna(data[selected_column].median(), inplace=True)
                st.success(f"Missing values in '{selected_column}' filled with median.")
            elif method == "Fill with Mode":
                data[selected_column].fillna(data[selected_column].mode()[0], inplace=True)
                st.success(f"Missing values in '{selected_column}' filled with mode.")
            elif method == "Drop Rows":
                data.dropna(subset=[selected_column], inplace=True)
                st.success(f"Rows with missing values in '{selected_column}' dropped.")
            elif method == "Random Imputation":
                data[selected_column] = random_imputation(data[selected_column])
                st.success(f"Missing values in '{selected_column}' filled with random imputation.")

        except Exception as e:
            st.error(f"An error occurred: {e}")

    # Show the dataset preview after handling
    st.write("### Dataset Preview (After Handling)")
    st.dataframe(data.head(10))
