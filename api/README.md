# 🚀 API Test Automation with `pytest`

## 📌 Introduction
This project contains automated tests for API endpoints, including **user registration** and **login functionality**.  
It uses `pytest` for running tests and `pytest-html` for generating HTML test reports.

---

## 📌 Prerequisites
Before running tests, ensure you have:
- Python **3.8+** installed
- Required dependencies installed:
  ```sh
  pip install -r requirements.txt


📌 Running Tests


✅ Run All Tests

pytest -v

✅ Run Tests and Generate an HTML Report

pytest --html=report.html

🚀 Run All Positive Tests

pytest -m positive -v

❌ Run All Negative Tests

pytest -m negative -v
