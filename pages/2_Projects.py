import streamlit as st
import pandas as pd
from utils.data_loader import get_data, get_project_skills, get_project_software, get_project_data

data = get_data()
projects = get_project_skills(data)
projects = get_project_software(projects, data)
projects = get_project_data(projects, data)

st.title("Project Portfolio")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Projects", len(projects))
with col2:
    completed = len(projects[projects['Completion status'] == 'Completed'])
    st.metric("Completed", completed)
with col3:
    ongoing = len(projects[projects['Completion status'] == 'Ongoing'])
    st.metric("Ongoing", ongoing)
with col4:
    clients = projects['Client'].nunique()
    st.metric("Clients", clients)

st.markdown("---")

with st.sidebar:
    st.header("Filters")
    type_filter = st.multiselect("Project Type", options=projects['type'].dropna().unique(), default=projects['type'].dropna().unique())
    status_filter = st.multiselect("Status", options=projects['Completion status'].dropna().unique(), default=projects['Completion status'].dropna().unique())
    location_filter = st.multiselect("Location", options=projects['Location'].dropna().unique(), default=projects['Location'].dropna().unique())

filtered = projects[
    (projects['type'].isin(type_filter)) &
    (projects['Completion status'].isin(status_filter)) &
    (projects['Location'].isin(location_filter))
]

st.subheader(f"Showing {len(filtered)} projects")

for _, row in filtered.iterrows():
    with st.expander(f"{row['Title']} ({row['type']})"):
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Client:** {row['Client']}")
            st.write(f"**Donor:** {row['Donor']}")
            st.write(f"**Location:** {row['Location']}")
            st.write(f"**Duration:** {row['Duration']}")
        with col2:
            st.write(f"**Role:** {row['Role']}")
            st.write(f"**Status:** {row['Completion status']}")
            if pd.notna(row.get('software_list')):
                st.write(f"**Software:** {row['software_list']}")
            if pd.notna(row.get('data_list')):
                st.write(f"**Data:** {row['data_list']}")
            if pd.notna(row.get('expertise_list')):
                st.write(f"**Expertise:** {row['expertise_list']}")
        
        if pd.notna(row.get('Description')):
            st.write(f"**Description:** {row['Description']}")
        if pd.notna(row.get('Responsibilities')):
            st.write(f"**Responsibilities:** {row['Responsibilities']}")
        if pd.notna(row.get('Accomplishments')):
            st.write(f"**Accomplishments:** {row['Accomplishments']}")
