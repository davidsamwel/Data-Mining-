import streamlit as st 
import pandas as pd
import plotly.express as px
import numpy as np
from matplotlib import pyplot as plt

import seaborn as sns
pd.options.display.max_columns=None
pd.options.display.max_rows=None
pd.options.display.float_format= '{:,.2f}'.format
sns.set()

def visualize(data):
    st.title("Histograms of Numeric Columns")
    numeric_columns = list(data.select_dtypes(include=np.number).columns)
    fig, ax = plt.subplots(figsize=(12, 10))
    data[numeric_columns].hist(ax=ax, bins=30, edgecolor='black')
    plt.tight_layout()
    st.pyplot(fig)
    
    st.title("Categorical Data Visualization")
    categorical_columns = data.select_dtypes(include=['object', 'category']).columns

    if len(categorical_columns) == 0:
        st.write("No categorical columns found in the dataset.")
    else:
        for col in categorical_columns:
            value_counts = data[col].value_counts()

            # Check if the number of unique values is greater than 10
            if len(value_counts) > 10:
                
                continue

            st.write(f"### Bar Chart for '{col}'")

            # Create a bar chart
            fig, ax = plt.subplots()
            value_counts.plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')
            ax.set_title(f"Distribution of {col}")
            ax.set_xlabel(col)
            ax.set_ylabel("Count")
            st.pyplot(fig)

