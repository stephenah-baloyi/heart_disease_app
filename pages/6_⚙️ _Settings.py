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
    page_title="Account",
    page_icon="⚙️",
)

from streamlit_extras.app_logo import add_logo

add_logo("https://img.icons8.com/arcade/2x/hearts.png")

st.subheader('Account')

with st.form(key='myform', clear_on_submit=True):
    if st.session_state['loggedIn'] == "":
        switch_page("Login")
    
    else:
        
        userID = st.session_state['loggedIn']
        users = get_user(userID)
            
        for user in users:
            usrid = user[0]
            usrfname = user[1]
            usrlname = user[2]
            usrgender = user[3]
            usraddress = user[4]
            usrmobile = user[5]
            usrname = user[6]
            usrpsswrd = user[7]
            
            col1, col2 = st.columns(2)
            
            with col1:
                idNo = st.text_input("ID Number", usrid, key="placeholder",)
            with col2:
                name = st.text_input("First Name", usrfname, placeholder=st.session_state.placeholder,)
            with col1:
                surname = st.text_input("Last Name", usrlname,placeholder=st.session_state.placeholder,)
            with col2:
                gender = st.text_input("Gender", usrgender, placeholder=st.session_state.placeholder,)
            with col1:
                address = st.text_input("Address", usraddress, placeholder=st.session_state.placeholder,)
            with col2:
                mobile = st.text_input("Mobile No", usrmobile, placeholder=st.session_state.placeholder,)
            with col1:
                username = st.text_input("Username", usrname, placeholder=st.session_state.placeholder,)
            with col2:
                password = st.text_input("Password", usrpsswrd, placeholder=st.session_state.placeholder, type='password')
            
            with col1:
                if st.form_submit_button("Update User Details"):
                    uid = get_user(idNo)
                    if(uid):
                      edit_user(name, surname, gender, address, mobile, password,username,idNo)
                      st.success("User Successfully Updated")
                    else:
                        st.error("User does not exist")
                   
            
            with col2:
                if st.form_submit_button("Delete Account"):
                    uid = get_user(idNo)
                    if(uid):
                      delete_data(idNo)
                      delete_diagnosis(idNo)
                      delete_sysmptoms(idNo)
                      st.success("User Successfully Deleted")
                    else:
                        st.error("User does not exist")