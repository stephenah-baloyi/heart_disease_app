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
    page_title="Database",
    page_icon="🔩",
)

from streamlit_extras.app_logo import add_logo

add_logo("https://img.icons8.com/arcade/2x/hearts.png")

st.subheader('Database') 

if st.session_state['loggedIn'] == "":
    switch_page("Login")   
      
else:
    
    create_table()
    create_symptoms() 
    create_diagnoses()
    
    with st.expander("View All Patients"):
        result = view_all_data()
        #st.write(result)
        clean_df = pd.DataFrame(result,columns=["IDNumber", "Firstname", "Lastname", "Gender", "Address", "Mobile", "Username", "Password"])
        st.dataframe(clean_df)
    
    with st.expander("View Syptoms Table"):
       symptom_result = view_all_symptoms()
       #st.write(result)
       symptom_df = pd.DataFrame(symptom_result,columns=["PID","Age","Sex","ChestPainType","RestingBP","Cholesterol","FastingBS","RestingECG","MaxHR","ExerciseAngina","Oldpeak","ST_Slope","MajorVessels","Thal"])
       st.dataframe(symptom_df)
       
    with st.expander("View Diagnoses Table"):
      diagnosis_result = view_all_diagnoses()
      #st.write(result)
      diagnosis_df = pd.DataFrame(diagnosis_result,columns=["PID","Diagnosis"])
      st.dataframe(diagnosis_df)