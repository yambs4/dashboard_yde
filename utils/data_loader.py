import pandas as pd
from typing import Dict, Any

def load_all_data(excel_path: str) -> Dict[str, Any]:
    """Load all sheets from the Excel workbook"""
    data = {}
    data['projects'] = pd.read_excel(excel_path, sheet_name='type_of_work')
    data['education'] = pd.read_excel(excel_path, sheet_name='education')
    data['certifications'] = pd.read_excel(excel_path, sheet_name='cert_training')
    data['employment'] = pd.read_excel(excel_path, sheet_name='employment')
    data['publications'] = pd.read_excel(excel_path, sheet_name='publications')
    data['core_skills'] = pd.read_excel(excel_path, sheet_name='core_skills')
    data['software'] = pd.read_excel(excel_path, sheet_name='software')
    data['languages'] = pd.read_excel(excel_path, sheet_name='language')
    return data