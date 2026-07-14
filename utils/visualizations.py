import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def radar_chart_skills(df: pd.DataFrame, skill_col: str, count_col: str, title: str):
    fig = px.line_polar(df, r=count_col, theta=skill_col, line_close=True, title=title)
    fig.update_traces(fill='toself')
    return fig

def bar_chart(df: pd.DataFrame, x: str, y: str, title: str, orientation: str = 'v'):
    if orientation == 'h':
        fig = px.bar(df, x=x, y=y, title=title, orientation='h')
    else:
        fig = px.bar(df, x=x, y=y, title=title)
    fig.update_layout(xaxis_title=x, yaxis_title=y)
    return fig

def pie_chart(df: pd.DataFrame, names: str, values: str, title: str):
    fig = px.pie(df, names=names, values=values, title=title)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

def heatmap(df: pd.DataFrame, x: str, y: str, color: str, title: str):
    fig = px.density_heatmap(df, x=x, y=y, z=color, title=title)
    return fig

def timeline(df: pd.DataFrame, start_col: str, end_col: str, label_col: str, color_col: str = None):
    df = df.copy()
    df[start_col] = pd.to_datetime(df[start_col], errors='coerce')
    df[end_col] = pd.to_datetime(df[end_col], errors='coerce')
    
    fig = go.Figure()
    for _, row in df.iterrows():
        if pd.notna(row[start_col]) and pd.notna(row[end_col]):
            fig.add_trace(go.Bar(
                x=[(row[end_col] - row[start_col]).days],
                y=[row[label_col]],
                orientation='h',
                marker_color=row[color_col] if color_col and color_col in row else None,
                name=row[label_col],
                hovertemplate=f"{row[label_col]}<br>Start: {row[start_col].strftime('%Y-%m-%d')}<br>End: {row[end_col].strftime('%Y-%m-%d')}<extra></extra>"
            ))
    fig.update_layout(barmode='stack', title='Timeline', xaxis_title='Duration (days)', yaxis_title='')
    return fig
