@echo off
setlocal
."%~dp0.venv\Scripts\python.exe" -m streamlit run app\main.py --server.headless true
