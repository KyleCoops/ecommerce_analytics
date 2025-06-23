# Orchestrator Demo Project

This project demonstrates how to orchestrate data pipelines using either Apache Airflow, or Dagster.

---

## 🧰 Requirements

- [pyenv](https://github.com/pyenv/pyenv)
- [Poetry](https://python-poetry.org/)
- Docker (optional for future containerization)

---

## 📦 Python Environment Setup

We'll use different Python versions for the components:

| Component | Python Version |
|----------|----------------|
| Flask API | 3.10.x |
| Airflow   | 3.10.x |
| Dagster   | 3.12.x |

### 1. Install Python versions with `pyenv`

```
pyenv install 3.10.14
pyenv install 3.12.3
```