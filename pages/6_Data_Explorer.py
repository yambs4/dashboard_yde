import streamlit as st
import pandas as pd
from utils.data_loader import get_data

data = get_data()

st.title("Data Explorer")

sheet = st.sidebar.selectbox("Select Dataset", options=list(data.keys()))

df = data[sheet]
st.subheader(f"{sheet.replace('_', ' ').title()} ({len(df)} rows)")

search = st.text_input("Search")
if search:
    mask = df.astype(str).apply(lambda row: row.str.contains(search, case=False, na=False)).any(axis=1)
    df = df[mask]

st.dataframe(df, width='stretch')
