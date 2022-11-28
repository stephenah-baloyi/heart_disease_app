import pickle
import streamlit as st
import sqlite3
import pandas as pd
from patient_db import * 
import streamlit.components.v1 as stc
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import cufflinks as cf
import plotly.offline
import plotly.graph_objs as go
import plotly.offline as py
from plotly.offline import iplot
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
)

from streamlit_extras.app_logo import add_logo

add_logo("https://img.icons8.com/arcade/2x/hearts.png")

st.subheader('Analytics')

if st.session_state["loggedIn"]== "":
    switch_page("Login")

else:
    df = pd.read_csv("heart.csv")
    # st.dataframe(df)
    #st.dataframe(df.head())
    
    all_columns = df.columns.tolist()
    choices = st.multiselect("Choose Column",all_columns)
    new_df = df[choices]
    
    col1,col2 = st.columns(2)
    with st.expander("Line Chart"):
        st.line_chart(new_df)
        
    with st.expander("Area Chart"):
        st.area_chart(new_df)
        
    # with st.expander("Pie Chart"):
    #     #sum_df = pd.read_csv("data/lang_sum_num_data.csv")
    #     fig = px.pie(df, values=['Age'], names=['Age'], title='Heart Data')
    #     st.plotly_chart(fig)
    
    