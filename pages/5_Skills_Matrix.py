import streamlit as st
import pandas as pd
from utils.data_loader import get_data, get_project_skills, get_project_software

data = get_data()
projects = get_project_skills(data)
projects = get_project_software(projects, data)

st.title("Skills Matrix")

st.subheader("Projects by Expertise")
exp_counts = projects['expertise_list'].dropna().str.split(', ').explode().value_counts().reset_index()
exp_counts.columns = ['Expertise', 'Count']
st.bar_chart(exp_counts.set_index('Expertise'))

st.subheader("Projects by Core Skills")
skill_counts = projects['skills_list'].dropna().str.split(', ').explode().value_counts().reset_index()
skill_counts.columns = ['Skill', 'Count']
st.bar_chart(skill_counts.set_index('Skill'))

st.subheader("Software Usage")
sw_counts = projects['software_list'].dropna().str.split(', ').explode().value_counts().reset_index()
sw_counts.columns = ['Software', 'Count']
st.bar_chart(sw_counts.set_index('Software'))

st.subheader("Detailed Skills Breakdown")
st.dataframe(
    projects[['Title', 'type', 'expertise_list', 'skills_list', 'software_list']],
    width='stretch',
    hide_index=True
)
