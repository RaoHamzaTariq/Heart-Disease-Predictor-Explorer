import streamlit as st
import numpy as np
import pandas as pd
import joblib


def load_model():
    loaded_model = joblib.load('Heart_Disease_Prediction_Model.joblib')
    return loaded_model

model_saved = load_model()



def show_predict_page():
    st.title("Heart Disease Prediction")
    st.write("""### We need some information to predict the heart disease""")

    sex = ['Male', 'Female']
    restecg = ['Normal', 'ST-T wave abnormality', 'Probable or definite LVH']
    cp = ['Typical angina', 'Atypical angina', 'Non-anginal pain', 'Asymptomatic']
    exang = ['Yes', 'No']
    slop = ['Upsloping', 'Flat', 'Downsloping']
    thal = ['Normal', 'Fixed defect', 'Reversible defect', 'Other']
    fbs = ['True', 'False']


    name = st.text_input("Name")
    name = name.title()

    sex_input = st.selectbox('Gender', sex)
    cp_input = st.radio("Chest Pain", cp)
    trestbps_input = st.number_input("Resting Blood Pressure in mm Hg", 1)
    chol_input = st.slider("Serum Cholestoral in mg/dl", 0, 700, 1)
    age_input = st.slider("Age in years", 0, 100, 1)
    fbs_input = st.selectbox("Fasting Blood Sugar > 120 mg/dl", fbs)
    restecg_input = st.selectbox("Resting Electrocardiographic Results", restecg)
    thalach_input = st.slider("Maximum Heart Rate Achieved", 0, 300, 1)
    exang_input = st.radio('Exercise Induced Angina', exang)
    ca_input = st.slider("Number of Major Vessels (0-3) Colored by Flourosopy", 0, 3, 1)
    thal_input = st.selectbox("Thalium Stress Result", thal)
    slope_input = st.selectbox("Slope of Peak Exercise ST Segment", slop)
    oldpeak_input = st.number_input("ST depression induced by exercise relative to rest")


    


    # Convert input to numeric using label_encoder
    sex_mapping = {'Male': 1, 'Female': 0}
    cp_mapping = {'Typical angina': 0, 'Atypical angina': 1, 'Non-anginal pain': 2, 'Asymptomatic': 3}
    restecg_mapping = {'Normal': 0, 'ST-T wave abnormality': 1, 'Probable or definite LVH': 2}
    exang_mapping = {'Yes': 1, 'No': 0} 
    slope_mapping = {'Upsloping': 2, 'Flat': 1, 'Downsloping': 0}
    thal_mapping = {'Normal': 0, 'Fixed defect': 1, 'Reversible defect': 2, 'Other': 3}
    fbs_mapping = {'True': 1, 'False': 0}


    data_input = pd.DataFrame({
        'age': [age_input],
        'sex': [sex_input],
        'cp': [cp_input],
        'trestbps': [trestbps_input],
        'chol': [chol_input],
        'fbs': [fbs_input],
        'restecg': [restecg_input],
        'thalach': [thalach_input],
        'exang': [exang_input],
        'oldpeak': [oldpeak_input],
        'slope': [slope_input],
        'ca': [ca_input],
        'thal': [thal_input]})
    
    data_input['sex'] = data_input['sex'].replace(sex_mapping)
    data_input['cp'] = data_input['cp'].replace(cp_mapping)
    data_input['restecg'] = data_input['restecg'].replace(restecg_mapping)
    data_input['fbs'] = data_input['fbs'].replace(fbs_mapping)
    data_input['slope'] = data_input['slope'].replace(slope_mapping)
    data_input['thal'] = data_input['thal'].replace(thal_mapping)
    data_input['exang'] = data_input['exang'].replace(exang_mapping)
    


    # data_input = np.array([[age_input, sex_input, cp_input, trestbps_input, chol_input,
    #                         fbs_input, restecg_input, thalach_input, exang_input,
    #                         oldpeak_input, slope_input, ca_input, thal_input]])

    data_input = data_input.astype(float)

    prediction = model_saved.predict(data_input)

    if st.button("Submit"):
        if prediction == 1:
            st.warning(f"{name} is a Heart Patient")
        else:
            st.success(f"{name} is not a Heart Patient")
