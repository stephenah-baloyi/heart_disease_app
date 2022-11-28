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
    page_title="Logout",
    page_icon="👩‍💻",
)


st.session_state['loggedIn'] = ""
    
switch_page("Home")