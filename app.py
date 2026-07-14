import streamlit as st
import pandas as pd
from utils.data_loader import load_all_data, get_project_skills, get_project_software, get_project_data

st.set_page_config(
    page_title="Yonatan Desalegn - CV Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

with open("config/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

@st.cache_data
def get_data():
    return load_all_data("CV_data.xlsx")

data = get_data()

st.sidebar.title("Navigation")
st.sidebar.markdown("---")
st.sidebar.info("Yonatan Desalegn Enaro\nData Science & Economic Research")

st.title("Professional Dashboard")
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Projects", len(data['projects']))
with col2:
    st.metric("Publications", len(data['publications']))
with col3:
    st.metric("Skills", len(data['core_skills']))
with col4:
    st.metric("Software", len(data['software']))

st.markdown("---")
st.subheader("Quick Overview")

with st.expander("Core Skills"):
    for _, row in data['core_skills'].iterrows():
        st.markdown(f"<span class='tag'>{row['Skill']}</span>", unsafe_allow_html=True)

with st.expander("Software Proficiency"):
    for _, row in data['software'].iterrows():
        st.markdown(f"**{row['Name']}** ({row['Category']}) - {row['Proficiency']}")

with st.expander("Languages"):
    lang_df = data['languages'][['Language', 'Reading', 'Writing', 'Speaking', 'Listening']]
    st.dataframe(lang_df, use_container_width=True, hide_index=True)
