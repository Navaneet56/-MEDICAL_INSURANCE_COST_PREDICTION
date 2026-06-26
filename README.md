%%writefile README.md
# 🩺 Medical Insurance AI Premium Predictor

An automated predictive web application built using **Streamlit** and **Scikit-Learn** to forecast annual medical insurance premiums. The system utilizes a trained **Linear Regression** model optimized on historical demographic and biometric health metrics.

---

## 🔗 Live Application Link
You can try the live, interactive web application instantly here:
👉 

## 🚀 Features
- **Premium Dark Cyber Theme:** Features a professional teal/slate UI custom-styled with responsive layout styling.
- **Accurate Predictions:** Inputs are processed instantly through a saved `.sav` model artifact built in a Jupyter Notebook pipeline.
- **Smart Form Processing:** Encodes inputs automatically behind the scenes (categorical values like gender and habits map accurately to metrics expected by your model).

---

## 🛠️ Tech Stack & Requirements
- **Language:** Python 3.8+
- **Framework:** Streamlit (UI Dashboard)
- **ML Engine:** Scikit-Learn (Linear Regression model)
- **Core Processing:** NumPy & Pandas

---

## 📦 Local Installation & Setup

Follow these steps to run the web application locally on your computer:

### 1. Clone or Move to Your Project Directory
Ensure your project directory contains the following core files:
- `app.py` (The main Streamlit interface script)
- `medical_insurance_model.sav` (Your serialized trained model file)
- `requirements.txt` (The list of dependencies)

### 2. Install Dependencies
Open your terminal or command prompt inside the project folder and run:
```bash
pip install -r requirements.txt
