import streamlit as st
import pandas as pd
from utils.data_loader import get_data

data = get_data()

st.title("Employment & Education")

tab1, tab2, tab3 = st.tabs(["Employment", "Education", "Certifications"])

with tab1:
    st.subheader("Work Experience")
    for _, row in data['employment'].iterrows():
        with st.expander(f"{row['Job title']} at {row['Institution']}"):
            st.write(f"**Duration:** {row['Duration']}")
            st.write(f"**Responsibilities:** {row['Responsibilities']}")
            st.write(f"**Accomplishments:** {row['Accomplishments']}")

with tab2:
    st.subheader("Education")
    for _, row in data['education'].iterrows():
        with st.expander(f"{row['Level']} - {row['Name of degree']}"):
            st.write(f"**Institution:** {row['Institution']}")
            st.write(f"**Duration:** {row['Duration']}")
            st.write(f"**Issue Date:** {row['Issue date']}")

with tab3:
    st.subheader("Certificates & Training")
    for _, row in data['certifications'].iterrows():
        with st.expander(row['Certificate']):
            st.write(f"**Institution:** {row['Institution']}")
            st.write(f"**Date:** {row['Date']}")
