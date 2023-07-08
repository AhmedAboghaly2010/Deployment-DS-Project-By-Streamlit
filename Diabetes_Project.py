import pickle
import streamlit as st
import pandas as pd

# Upload Data

data=pickle.load(open(r'C:\Users\Ahmed\Diabetes_prediction.sav','rb'))

# Streamlit Page

st.title('Diabetes Prediction Web App')

st.sidebar.header('Feature selecting')

st.info('Easy Application For Predictiong Diabetes Deseas')


Pregnancies=st.text_input('Pregnancies')
Glucose=st.text_input('Glucose')
BloodPressure=st.text_input('BloodPressure')
SkinThickness=st.text_input('SkinThickness')
BMI=st.text_input('BMI')
DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction')
Age=st.text_input('Age')

df=pd.DataFrame({'Pregnancies':[Pregnancies],'Glucose':[Glucose],'BloodPressure':[BloodPressure],'SkinThickness':[SkinThickness],'BMI':[BMI],
                 'DiabetesPedigreeFunction':[DiabetesPedigreeFunction],'Age':[Age]},index=[0])

Conf=st.sidebar.button('Confirm')
if Conf:
    result=data.predict(df)
    if result == 0:
       st.sidebar.write('The Patiant is Clear')
       st.sidebar.image('https://astrologer.swayamvaralaya.com/wp-content/uploads/2012/08/health1.jpg',width=50)
    else:
        st.sidebar.write('The Patiant Has Deseas')
        st.sidebar.image('https://brghealth.com/brg/wp-content/uploads/2020/01/diabetes.png',width=50)