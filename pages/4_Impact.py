import streamlit as st
import pandas as pd
from utils.data_loader import get_data

data = get_data()

st.title("Publications & Impact")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Publications", len(data['publications']))
with col2:
    phd = len(data['publications'][data['publications']['Type'] == 'PhD Dissertation'])
    st.metric("PhD Dissertations", phd)
with col3:
    peer_reviewed = len(data['publications'][data['publications']['Type'].str.contains('Journal', case=False, na=False)])
    st.metric("Journal Articles", peer_reviewed)

st.markdown("---")

for _, row in data['publications'].iterrows():
    with st.expander(f"{row['Title']} ({row['Year']})"):
        st.write(f"**Citation:** {row['Citation']}")
        st.write(f"**Publisher/Journal:** {row['Publisher/Journal']}")
        st.write(f"**Type:** {row['Type']}")
