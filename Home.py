# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 00:56:52 2022

@author: HP
"""

import pickle
import streamlit as st
import sqlite3
import pandas as pd
from patient_db import * 
import streamlit.components.v1 as stc
import numpy as np
import plotly.express as px
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Home", page_icon="🏚")



def main():

    add_logo("https://img.icons8.com/arcade/2x/hearts.png")
    
    st.write("# Welcome to Heart Doctor! ❤️")


    st.markdown(
        """
        Heart disease often progresses suddenly without any symptoms or forewarning, until a heart attack suddenly strikes. By living a healthy lifestyle and understanding your own health you can prevent heart disease or treat it early before it’s too late.
        ### Want to learn more?
        - Signs of heart attack [heart attack signs](https://www.heartfoundation.co.za/signs-of-a-heart-attack/)
        - Types of heart diseases [Types of heart disease](https://www.heartfoundation.co.za/types-of-heart-disease/)
        - Causes of heart disease [Causes](https://www.heartfoundation.co.za/causes-of-heart-disease/)
        -  Heart Support Directory [Support Community](https://www.heartfoundation.co.za/heart-support-directory/)
    """
    )
#switch_page("Login") 

if __name__ == '__main__':
    main()