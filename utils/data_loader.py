import pandas as pd
from typing import Dict, Any
import streamlit as st

def load_all_data(excel_path: str) -> Dict[str, Any]:
    xl = pd.ExcelFile(excel_path)
    available = xl.sheet_names
    data = {}

    def safe_sheet(name: str) -> pd.DataFrame:
        return pd.read_excel(excel_path, sheet_name=name) if name in available else pd.DataFrame()

    data['projects'] = safe_sheet('type_of_work')
    data['education'] = safe_sheet('education')
    data['certifications'] = safe_sheet('cert_training')
    data['employment'] = safe_sheet('employment')
    data['publications'] = safe_sheet('publications')
    data['core_skills'] = safe_sheet('core_skills')
    data['software'] = safe_sheet('software')
    data['languages'] = safe_sheet('language')
    data['positions_of_trust'] = safe_sheet('positions_of_trust')
    data['required_expertise'] = safe_sheet('required_expertise')
    data['data_used'] = safe_sheet('data_used')
    data['bridge_project_software'] = safe_sheet('bridge_project_software')
    data['bridge_project_data'] = safe_sheet('bridge_project_data')
    data['bridge_project_expertise'] = safe_sheet('bridge_project_expertise')
    data['bridge_expertise_core_skill'] = safe_sheet('bridge_expertise_core_skill')
    return data

@st.cache_data
def get_data() -> Dict[str, Any]:
    return load_all_data("CV_data.xlsx")

def get_project_skills(data: Dict[str, Any]) -> pd.DataFrame:
    projects = data['projects'].copy()
    skills = data['core_skills'].copy()
    bridge = data['bridge_expertise_core_skill'].copy()
    expertise = data['required_expertise'].copy()
    proj_exp = data['bridge_project_expertise'].copy()
    
    proj_exp = proj_exp.merge(expertise, on='id_exp', how='left')
    proj_exp = proj_exp.merge(bridge, on='id_exp', how='left')
    proj_exp = proj_exp.merge(skills, on='id_skll', how='left')
    
    skill_list = proj_exp.groupby('id_prj')['Skill'].apply(lambda x: ', '.join(x.dropna().astype(str))).reset_index()
    skill_list.columns = ['id_prj', 'skills_list']
    
    exp_list = proj_exp.groupby('id_prj')['Expertise'].apply(lambda x: ', '.join(x.dropna().astype(str))).reset_index()
    exp_list.columns = ['id_prj', 'expertise_list']
    
    result = projects.merge(skill_list, on='id_prj', how='left')
    result = result.merge(exp_list, on='id_prj', how='left')
    return result

def get_project_software(projects: pd.DataFrame, data: Dict[str, Any]) -> pd.DataFrame:
    software = data['software'].copy()
    bridge = data['bridge_project_software'].copy()
    
    merged = bridge.merge(software, on='id_sftwr', how='left')
    sw_list = merged.groupby('id_prj')['Name'].apply(lambda x: ', '.join(x.dropna().astype(str))).reset_index()
    sw_list.columns = ['id_prj', 'software_list']
    
    return projects.merge(sw_list, on='id_prj', how='left')

def get_project_data(projects: pd.DataFrame, data: Dict[str, Any]) -> pd.DataFrame:
    data_used = data['data_used'].copy()
    bridge = data['bridge_project_data'].copy()
    
    merged = bridge.merge(data_used, on='id_data', how='left')
    data_list = merged.groupby('id_prj')['Short name'].apply(lambda x: ', '.join(x.dropna().astype(str))).reset_index()
    data_list.columns = ['id_prj', 'data_list']
    
    return projects.merge(data_list, on='id_prj', how='left')
