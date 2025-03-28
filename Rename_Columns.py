import streamlit as st
import time
def rename_columns(df):
    st.header("Rename Columns")
    #st.session_state.rename_columns_clicked = True
    new_names = {}

    # Create two columns layout with better spacing
    col1, spacer, col2 = st.columns([2, 0.2, 2])

    with col1:
        st.markdown("""
        <div style='padding: 15px; border-radius: 5px;'>
            <h3 style='margin-bottom: 15px;'>Current Names</h3>
        """, unsafe_allow_html=True)
        
        # Display current column names in a more styled way
        for i, col in enumerate(df.columns):
            st.markdown(f"""
                <div style='
                    background-color: #0E1117
                    color: #FFFFFF;
                    padding: 8px; 
                    margin: 5px 0; 
                    border-radius: 4px;
                    display: flex;
                    align-items: center;'>
                        <span style='
                    background-color: #D3D3D3; 
                    color: #000000; 
                    padding: 2px 8px; 
                    border-radius: 3px; 
                    margin-right: 8px;
                    font-size: 0.8em;'>
                    {i + 1}
                    </span>
                        <span>
                        {col}
                        </span>
                    </div>
                    """, unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)        
    with col2:
        st.markdown("""
        <div style='padding: 15px; border-radius: 5px;'>
            <h3 style='margin-bottom: 15px;'>New Names</h3>
        """, unsafe_allow_html=True)
        st.write("Enter new names for the columns you want to rename:")
        # Create text inputs for each column
        for col in df.columns:
            # Use session state to maintain input values
            if f"new_name_{col}" not in st.session_state:
                st.session_state[f"new_name_{col}"] = col
                
            new_name = st.text_input(
                f"New name for '{col}'",
                value=st.session_state[f"new_name_{col}"],
                key=f"input_new_name_{col}",
                label_visibility="collapsed"  # Hide the label for cleaner UI
            )
            new_names[col] = new_name
        
        st.markdown("</div>", unsafe_allow_html=True)

    # Add some spacing before the buttons
    st.markdown("<br>", unsafe_allow_html=True)

    # Create a container for buttons with better styling
    button_col1, button_col2 = st.columns(2)

    with button_col1:
        apply_changes = st.button(
            "Apply Changes",
            type="primary"
        )

    with button_col2:
        cancel = st.button(
            " ❌ Cancel",
        )

    if apply_changes:
        try:
            # Create a mapping of old to new column names
            rename_dict = {
                old_name: new_name 
                for old_name, new_name in new_names.items() 
                if new_name != old_name  # Only include changed names
            }
            
            if rename_dict:  # If there are columns to rename
                # Rename the columns
                st.session_state.df = df.rename(columns=rename_dict)
                
                # Show success message with better styling
                st.success("✅ Columns renamed successfully!")
                time.sleep(2)
                
                # Clear the stored new names from session state
                for col in new_names:
                    if f"new_name_{col}" in st.session_state:
                        del st.session_state[f"new_name_{col}"]
                st.rerun()
                
            else:
                st.info("No columns were renamed.")
                
        except Exception as e:
            st.error(f"Error renaming columns: {str(e)}")

    if cancel:
        # Clear the stored new names from session state
        for col in new_names:
            if f"new_name_{col}" in st.session_state:
                del st.session_state[f"new_name_{col}"]
        st.error("Columns renaming has been cancelled")
        time.sleep(2)
        st.rerun()