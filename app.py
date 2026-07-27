import streamlit as st
import pickle
import pandas as pd

# Load model
with open("titanic_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load scaler (if used)
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

st.set_page_config(page_title="Titanic Survival Predictor")

st.title("🚢 Titanic Survival Prediction")

st.write("Enter passenger details below:")

# Inputs
pclass = st.selectbox("Passenger Class", [1, 2, 3])

sex = st.selectbox("Sex", ["Male", "Female"])
sex = 1 if sex == "Male" else 0

age = st.number_input("Age", min_value=0, max_value=100, value=25)

sibsp = st.number_input("Number of Siblings/Spouses", min_value=0, max_value=10, value=0)

parch = st.number_input("Number of Parents/Children", min_value=0, max_value=10, value=0)

fare = st.number_input("Fare Paid", min_value=0.0, value=30.0)

embarked = st.selectbox("Embarked", ["C", "Q", "S"])

embarked_map = {
    "C": 0,
    "Q": 1,
    "S": 2
}

embarked = embarked_map[embarked]

# Create FamilySize
family_size = sibsp + parch + 1

# Create DataFrame
data = pd.DataFrame({
    "Pclass": [pclass],
    "Sex": [sex],
    "Age": [age],
    "Fare": [fare],
    "Embarked": [embarked],
    "FamilySize": [family_size]
})

# Scale
data_scaled = scaler.transform(data)

if st.button("Predict"):

    prediction = model.predict(data_scaled)[0]
    probability = model.predict_proba(data_scaled)[0]

    if prediction == 1:
        st.success("🎉 Passenger is likely to Survive")
    else:
        st.error("❌ Passenger is unlikely to Survive")

    st.write(f"Survival Probability : **{probability[1]*100:.2f}%**")
    st.write(f"Death Probability : **{probability[0]*100:.2f}%**")