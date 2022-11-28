import pickle
import streamlit as st
import sqlite3
import pandas as pd
from patient_db import * 
import streamlit.components.v1 as stc
import numpy as np
import plotly.express as px
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(
    page_title="Predict",
    page_icon="❤️",
)

from streamlit_extras.app_logo import add_logo

add_logo("https://img.icons8.com/arcade/2x/hearts.png")

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
#heart_disease_model = 'https://heart-disease-ml-api.herokuapp.com/heart_disease_predict'
st.title('Heart Disease Prediction ApP')

with st.form(key='myform', clear_on_submit=True):

    if st.session_state["loggedIn"]== "":
        switch_page("Login")
     
    else: 
        #st.write(st.session_state["loggedIn"])
        col1, col2, col3 = st.columns(3)
        
        with col1:
            age = st.number_input('Age')
               
        with col2:
            sex = st.number_input('Sex: 0-Male and 1-Female')
               
        with col3:
            cp = st.number_input('Chest Pain types')
               
        with col1:
            trestbps = st.number_input('Resting Blood Pressure')
               
        with col2:
            chol = st.number_input('Serum Cholestoral in mg/dl')
               
        with col3:
            fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
               
        with col1:
            restecg = st.number_input('Resting Electrocardiographic results')
               
        with col2:
            thalach = st.number_input('Maximum Heart Rate')
               
        with col3:
            exang = st.number_input('Exercise Induced Angina')
              
        with col1:
            oldpeak = st.number_input('ST depression induced by exercise')
               
        with col2:
            slope = st.number_input('ST Slope exercise segment')
               
        with col3:
            ca = st.number_input('Major vessels colored by flourosopy')
               
        with col1:
            thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        create_symptoms() 
        create_diagnoses()
        
        # code for Prediction
        heart_diagnosis = ''
        pid = st.session_state['loggedIn']
           
        # creating a button for Prediction
           
        if st.form_submit_button('Predict Heart Disease'):
            
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
               
            if (heart_prediction[0] == 1):
                 heart_diagnosis = 'You have Heart Disease'
                 diagnosis = 1
                 st.error(heart_diagnosis)
            else:
                 heart_diagnosis = 'You don\'t have any Heart Disease'
                 diagnosis = 0 
                 st.success(heart_diagnosis)
            
                   
            patientid = get_symptoms_per_id(pid)
            #st.write(pid)
            if (patientid):
                edit_symptoms(age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal,pid)
            else:
                add_sysmptoms(pid,age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal)
            
           
            diagnosisid = get_diagnoses(pid)
            if (diagnosisid):
               edit_diagnoses(diagnosis, pid)
              
            else:
                add_diagnoses(pid,diagnosis)
                