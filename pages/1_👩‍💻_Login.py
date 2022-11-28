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
    page_title="Login",
    page_icon="👩‍💻",
)

from streamlit_extras.app_logo import add_logo

add_logo("https://img.icons8.com/arcade/2x/hearts.png")

st.title('Login')

with st.form(key='myform', clear_on_submit=True):
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = ""
        
        
    def LoggedIn_Clicked(userName, password):
        create_table()
        result = login_user(userName,password)
        
        for user in result:
            usrid = user[0]
            usrfname = user[1]
            usrlname = user[2]
            usrgender = user[3]
            usraddress = user[4]
            usrmobile = user[5]
            usrname = user[6]
            usrpsswrd = user[7]
            
        if (result):
            st.session_state['loggedIn'] = usrid
            switch_page("Home")
        else:
            st.session_state['loggedIn'] = "";
            st.error("Invalid user name or password, please try again")
    
    
    if st.session_state['loggedIn'] == "":    
        username = st.text_input(label="", value="", placeholder="Enter your Username")
        password = st.text_input(label="", value="",placeholder="Enter Password", type="password")
        
        st.form_submit_button("Login", on_click=LoggedIn_Clicked, args= (username, password))
    
    else:
        switch_page("Home")