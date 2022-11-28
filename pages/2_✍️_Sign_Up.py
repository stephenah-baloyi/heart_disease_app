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
    page_title="Sign Up",
    page_icon="✍️",
)

from streamlit_extras.app_logo import add_logo

add_logo("https://img.icons8.com/arcade/2x/hearts.png")

st.subheader('Sign Up')

with st.form(key='myform', clear_on_submit=True):

    if st.session_state['loggedIn'] == "":
        col1, col2 = st.columns(2)
        with col1:
            idNo = st.text_input(label="", value="", placeholder="Enter your ID Number")
        with col2:
            name = st.text_input(label="", value="", placeholder="Enter your First Name")
        with col1:
            surname = st.text_input(label="", value="", placeholder="Enter your Last Name")
        with col2:
            gender = st.text_input(label="", value="", placeholder="Enter your Gender")
        with col1:
            address = st.text_input(label="", value="", placeholder="Enter your Address")
        with col2:
            mobile = st.text_input(label="", value="", placeholder="Enter your Mobile No")
        with col1:
            username = st.text_input(label="", value="", placeholder="Enter your Username")
        with col2:
            password = st.text_input(label="", value="", placeholder="Enter your Password", type='password')
        create_table()
        result = get_user(idNo)
          
        if st.form_submit_button("Sign Up"):
            
            if(result):
               st.error("User already exist, please login")
               
            else:
                add_data(idNo, name, surname, gender, address, mobile, username, password)
                st.success("User added Successfully")
                st.info("Please navigate to the Menu to Login")
    else:
        switch_page("Home")