import streamlit as st
import numpy as np
import joblib

# Load the pre-trained model
model_path = r"C:\Users\Public\PycharmProjects\sustainloadingFRPs\xgb\xgboost_model1.pkl"
model = joblib.load(model_path)

# Custom CSS to change the font to Times New Roman, set the font size, and make all text bold
st.markdown("""
    <style>
    body, p, div, input, label, select, textarea {
        font-family: 'Times New Roman', Times, serif;
        font-size: 14px;
        font-weight: bold;
    }
    .title {
        font-family: 'Times New Roman', Times, serif;
        font-size: 16px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit app
st.markdown('<h1 class="title">Prediction Application</h1>', unsafe_allow_html=True)

# Create two columns
col1, col2 = st.columns(2)

# Column 1 for dropdown menus (categorical features)
with col1:
    feature_1 = st.selectbox('Resin type', options=[1, 2, 3], format_func=lambda x: {1: 'VE', 2: 'UPE', 3: 'PE*'}.get(x))
    feature_3 = st.selectbox('Production method', options=[1, 2], format_func=lambda x: {1: 'Pultrusion', 2: 'Vacuum Infusion'}.get(x))
    feature_4 = st.selectbox('Exposure environment', options=[1, 2, 3, 4, 5], format_func=lambda x: {1: 'Distilled water', 2: 'Tap water immersion', 3: 'Saltwater immersion', 4: 'Indoor controlled environment', 5: 'Continuous condensation'}.get(x))
    feature_7 = st.selectbox('Mechanical Property', options=[1, 2, 3, 4], format_func=lambda x: {1: 'TS', 2: 'ILSS', 3: 'TM', 4: 'FS'}.get(x))
    feature_8 = st.selectbox('Sustain loading type', options=[1, 2, 3], format_func=lambda x: {1: 'No load', 2: 'Pure tension', 3: 'Bending'}.get(x))

# Column 2 for number inputs (continuous features)
with col2:
    st.write("**Thickness**: 1.4 to 7.1")
    feature_2 = st.number_input('Thickness', min_value=1.4, max_value=7.1)
    st.write("**Temperature**: 20.0 to 66.0")
    feature_5 = st.number_input('Temperature', min_value=20.0, max_value=66.0)
    st.write("**Sustained loading**: 0.0 to 58.0")
    feature_6 = st.number_input('Sustained loading', min_value=0.0, max_value=58.0)
    st.write("**Time**: 0.0 to 1097.5")
    feature_9 = st.number_input('Time', min_value=0.0, max_value=1097.5)

# Create a button for prediction
if st.button('Predict Property Retention'):
    # Prepare the feature vector for prediction
    input_features = np.array([[feature_1, feature_2, feature_3, feature_4, feature_5, feature_6, feature_7, feature_8, feature_9]])

    # Make a prediction
    prediction = model.predict(input_features)

    # Display the prediction, limited to three decimal places
    st.write(f'Predicted value: {prediction[0]:.3f}')
