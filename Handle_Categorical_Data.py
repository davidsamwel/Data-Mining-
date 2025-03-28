import streamlit as st
import pandas as pd

def handle_categorical_data(data):
    st.title("Handle Categorical Data")

    # Ensure data is a DataFrame
    df = pd.DataFrame(data)

    # Identify categorical columns with less than 5 unique values
    categorical_columns = df.select_dtypes(include=["object", "category"]).columns.tolist()
    col = [col for col in categorical_columns if len(df[col].unique()) < 5]

    if not col:
        st.success("No suitable categorical columns found in the dataset (less than 5 unique values)!")
        return

    # Select a column and method for handling
    selected_column = st.selectbox("Select a categorical column", col)
    method = st.selectbox(
        "Select a method to handle categorical data",
        [
            "Fill Missing with Mode",
            "Label Encoding",
            "One-Hot Encoding",
            "Drop Column",
        ]
    )

    # Preview dataset before handling
    st.write("### Dataset Preview (Before Handling)")
    st.dataframe(df.head(10))

    if st.button("Apply"):
        try:
            if method == "Fill Missing with Mode":
                df[selected_column].fillna(df[selected_column].mode()[0], inplace=True)
                st.success(f"Missing values in '{selected_column}' filled with mode.")
            elif method == "Label Encoding":
                df[selected_column] = df[selected_column].astype('category').cat.codes
                st.success(f"Label encoding applied to '{selected_column}'.")
            elif method == "One-Hot Encoding":
                df = pd.get_dummies(df, columns=[selected_column], drop_first=True)
                st.success(f"One-hot encoding applied to '{selected_column}'.")
            elif method == "Drop Column":
                df.drop(columns=[selected_column], inplace=True)
                st.success(f"Column '{selected_column}' has been dropped.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

    # Preview dataset after handling
    st.write("### Dataset Preview (After Handling)")
    st.dataframe(df.head(10))
