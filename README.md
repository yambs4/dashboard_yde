# Yonatan Desalegn - CV Dashboard

Interactive dashboard built with Streamlit, visualizing CV data from Excel.

## Local Development

```bash
py -m streamlit run app.py
```

## Deployment

### Option 1: Streamlit Community Cloud (Recommended)

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app", select this repo and branch
5. Set main file: `app.py`
6. Click "Deploy"

### Option 2: Docker

```bash
docker-compose up -d
```

App will be available at `http://localhost:8501`.

### Option 3: Self-hosted

```bash
py -m pip install -r requirements.txt
py -m streamlit run app.py --server.headless true --server.port 8501
```

## Embedding

Use an iframe on your website:

```html
<iframe src="https://your-app-url.streamlit.app" width="100%" height="800" frameborder="0"></iframe>
```
