# handle_duplicates.py
import streamlit as st

def handle_duplicates(data):
   
    duplicate_count = data.duplicated().sum()
    
    st.write(f"Number of Duplicate Rows: {duplicate_count}")
    if duplicate_count==0 :
     st.warning('No Need to Remove the Duplicates ')
    
        
        
    if st.button("Remove Duplicate Rows"):
        data.drop_duplicates(inplace=True)
        st.success("Duplicate rows removed.")
        
        

    columns = data.columns.tolist()

    if not columns:
        st.error("No columns found in the dataset!")
        return

    # Dropdown for selecting a column
    selected_column = st.selectbox("Select a column to check duplicates", columns)

    # Dropdown for selecting a method to handle duplicates
    method = st.selectbox(
        "Select a method to handle duplicates",
        ["Keep First", "Keep Last", "Drop All"]
    )

    
    st.write("### Dataset Preview (Before Handling)")
    st.dataframe(data[[selected_column]].head(10)) 

    # Button to handle duplicates
    if st.button("Apply"):
        original_count = len(data)

        # Apply the selected method
        if method == "Keep First":
            data.drop_duplicates(subset=[selected_column], keep="first", inplace=True)
            st.success(f"Duplicates in '{selected_column}' kept the first occurrence.")
        elif method == "Keep Last":
            data.drop_duplicates(subset=[selected_column], keep="last", inplace=True)
            st.success(f"Duplicates in '{selected_column}' kept the last occurrence.")
        elif method == "Drop All":
            data.drop_duplicates(subset=[selected_column], keep=False, inplace=True)
            st.success(f"All duplicates in '{selected_column}' dropped.")

        # Show changes
        new_count = len(data)
        st.write(f"Rows before: **{original_count}**, Rows after: **{new_count}**")

        # Display updated dataset preview
        st.write("### Dataset Preview (After Handling)")
        st.dataframe(data[[selected_column]].head(10))
