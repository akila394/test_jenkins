# Jenkins Practice - Python Test Runner CI

Run locally:
1) python -m venv .venv
2) .\venv\Scripts\pip install -r requirements.txt
3) mkdir reports -Force
3) .\venv\Scripts\pytest -m smoke --junitxml=reports\junit.xml --html=reports\report.html --self-contained-html
