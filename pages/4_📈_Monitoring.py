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
    page_title="Monitor",
    page_icon="📈",
)

from streamlit_extras.app_logo import add_logo

add_logo("https://img.icons8.com/arcade/2x/hearts.png")

st.title('Monitoring')

if st.session_state["loggedIn"]== "":
    switch_page("Login")
 
else:
    create_table()
    create_symptoms() 
    create_diagnoses()
    
    userID = st.session_state['loggedIn']
    current_user = get_user(userID)
    
    for user in current_user:
        usrid = user[0]
        usrfname = user[1]
        usrlname = user[2]
        usrgender = user[3]
        usraddress = user[4]
        usrmobile = user[5]
        usrname = user[6]
        usrpsswrd = user[7]
    
    symptomid = get_symptoms_per_id(userID)
    
    for user_symptom in symptomid:
        usrid = user_symptom[0]
        age = user_symptom[1]
        sex = user_symptom[2]
        cp = user_symptom[3]
        trestbps = user_symptom[4]
        chol = user_symptom[5]
        fbs = user_symptom[6]
        restecg = user_symptom[7]
        thalach= user_symptom[8]
        exang= user_symptom[9]
        oldpeak= user_symptom[10]
        slope= user_symptom[11]
        ca= user_symptom[12]
        thal= user_symptom[13]
    
    diagnosisid = get_diagnoses(userID)
    
    for duser in diagnosisid:
        did = duser[0]
        diagnosis = duser[1]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success('Status')
    with col2:
        st.success('Connected')
    with col1:
        st.success('RestingBP')
    if(float(trestbps) >= 139):
        with col2:
            st.warning(trestbps + ' MM Hg')
    else:
        with col2:
            st.success(trestbps + ' MM Hg')
    with col1:
        st.success('Cholesterol')
    if(float(chol) >= 200):
        with col2:
            st.warning(chol + ' MM/dl')
    else:
        with col2:
            st.success(chol + ' MM/dl')
    with col1:
        st.success('MaxHR')
    if(float(thalach) > 150):
        with col2:
            st.warning(thalach +' BPM')
    else:
        with col2:
            st.success(thalach +' BPM')
    with col1:
        st.success('Diagnosis')
    if(diagnosis == 1):
        with col2:
            st.warning('1- Heart Disease')
    else:
        with col2:
            st.success('0- No Heart Disease')
    
    with col1:
         st.button('Call Doctor')