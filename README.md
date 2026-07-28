# 🚢 Titanic Survival Prediction

A simple and interactive machine learning web app that predicts whether a Titanic passenger is likely to survive based on selected input features such as passenger class, sex, age, fare, embarkation point, and family size.

## ✨ Features

- Interactive form for entering passenger details
- Real-time survival prediction using a trained model
- Displays both survival and death probabilities
- Clean and user-friendly interface built with Streamlit

## 🛠️ Tech Stack

- Python
- Streamlit
- pandas
- scikit-learn
- NumPy

## 📂 Project Structure

- app.py - Main Streamlit application
- titanic_model.pkl - Trained machine learning model
- scaler.pkl - Saved scaler used for preprocessing
- requirements.txt - Project dependencies

## ▶️ How to Run

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Start the app:

```bash
streamlit run app.py
```

3. Open the local URL shown in the terminal in your browser.

## 🧠 How It Works

The app collects passenger information from the user, preprocesses the input values, and sends them to a pre-trained model to estimate the chance of survival.

This project is a great example of combining machine learning with a simple web interface for real-world prediction.

## 📌 Note

This is a beginner-friendly ML project designed to showcase a basic end-to-end prediction workflow.
