import streamlit as st
import pandas as pd

st.title('Excel to JSON Converter')

uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("Excel file content:")
    st.write(df)
    
    json_data = df.to_json(orient='records', force_ascii=False)

    st.download_button(
        label="Download JSON",
        data=json_data,
        file_name='data.json',
        mime='application/json'
    )
