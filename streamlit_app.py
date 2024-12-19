import streamlit as st
import pandas as pd

# Sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 45],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title("Table with Filter")

# Filter input
st.sidebar.header("Filter Options")
filter_city = st.sidebar.text_input("Filter by City (case-sensitive)", "")

# Apply filter
if filter_city:
    filtered_df = df[df["City"].str.contains(filter_city, case=True, na=False)]
else:
    filtered_df = df

# Display table
st.write("### Data Table")
st.dataframe(filtered_df)
