#import libraries 
import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf
from datetime import datetime
import plotly.express as px

# start dashborad buliding 
st.set_page_config(layout="wide")
st.title('stock price comparison')

#get ticker price
ticker  = ('ASIANPAINT.BO' , 'AXISBANK.BO' , 'BAJAJ-AUTO.BO','BAJAJFINSV.BO','HCLTECH.BO','HDFC.BO','ITC.BO','LT.BO','M&M.BO',
           'MARUTI.BO')

#dropdown menu 
dropdown = st.multiselect("Select Stock" , ticker)
#start date picker
start = st.date_input("start:" , value=pd.to_datetime("2018-01-03"))
#end date picker
end = st.date_input("end:" , value=datetime.today())

#reletive raturn
def reletive(df):
    rel = df.pct_change()
    culmulative = (1+rel).cumprod()
    culmulative = culmulative.fillna(0)
    return culmulative

#line charts
if len(dropdown)> 0:
    df = yf.download(dropdown , start, end , scale=True)['Close']
    df_2 = reletive(yf.download(dropdown , start, end , scale=True)['Close'])
    st.subheader("Time series of Stocks :")
    st.line_chart(df)
    st.subheader("Relative returns of Stocks :")
    st.line_chart(df_2)