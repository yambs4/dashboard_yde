import streamlit as st
import pandas as pd
from utils.data_loader import get_data

data = get_data()

st.title("Professional Profile")

col1, col2 = st.columns([2, 1])

with col1:
    st.header("Yonatan Desalegn Enaro")
    st.subheader("Data Science and Economic Research")
    st.markdown("📧 yambs4@gmail.com | 📍 Addis Ababa, Ethiopia | 📞 +251 916829485")
    st.markdown("---")
    st.markdown("Economist (Ph.D.) and data scientist with over 15 years of experience in impact evaluations, data science and M&E of development interventions and economic policy research across various sectors, teaching, and research.")
    
    st.subheader("Core Skills")
    for _, row in data['core_skills'].iterrows():
        st.markdown(f"<span class='tag'>{row['Skill']}</span>", unsafe_allow_html=True)

with col2:
    st.subheader("Languages")
    lang_df = data['languages'][['Language', 'Reading', 'Writing', 'Speaking', 'Listening']]
    st.dataframe(lang_df, width='stretch', hide_index=True)
    
    st.subheader("Software Proficiency")
    for _, row in data['software'].iterrows():
        st.progress(row['Proficiency'].lower() == 'advanced' and 1.0 or row['Proficiency'].lower() == 'intermediate' and 0.6 or 0.3)
        st.caption(f"{row['Name']} ({row['Proficiency']})")

st.header("Positions of Trust")
for _, row in data['positions_of_trust'].iterrows():
    with st.expander(f"{row['Position']} - {row['Institution']}"):
        st.write(f"**Duration:** {row['Duration']}")
        st.write(f"**Description:** {row['Description']}")
