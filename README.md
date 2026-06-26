%%writefile README.md
# 🩺 Medical Insurance AI Premium Predictor

An automated predictive web application built using **Streamlit** and **Scikit-Learn** to forecast annual medical insurance premiums. The system utilizes a trained **Linear Regression** model optimized on historical demographic and biometric health metrics.

---

## 🔗 Live Application Link
You can access the live, interactive web application instantly here:
👉 https://oxzgdvpxiu6dxprwnhx8qk.streamlit.app/

---

## 🚀 Features
- **Premium Dark Cyber Theme:** Features a professional teal/slate UI custom-styled with responsive layout configurations.
- **Accurate Model Inference:** Input data points are processed instantly through a saved `.sav` model artifact built in a Jupyter Notebook pipeline.
- **Automated Parameter Mapping:** Encodes drop-down input categories automatically behind the scenes (categorical values like gender and habits map accurately to features expected by the regression matrix).

---

## 🛠️ Tech Stack & Requirements
- **Language:** Python 3.8+
- **Framework:** Streamlit (UI Dashboard Framework)
- **ML Engine:** Scikit-Learn (Linear Regression Engine)
- **Core Processing:** NumPy & Pandas

---

## 📦 Local Installation & Setup

Follow these steps to run the web application locally on your computer:

### 1. Project Directory Configuration
Ensure your project directory contains the following core files in the same folder level:
- `app.py` (The main Streamlit interface script)
- `medical_insurance.sav` (Your serialized trained model file)
- `requirements.txt` (The list of project dependencies)

### 2. Install Dependencies
Open your terminal or command prompt inside the project folder and install the library packages:
```bash
pip install -r requirements.txt
