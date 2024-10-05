import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

data=px.data.gapminder()
st.dataframe(data)

data1=px.data.tips()
fig1=px.treemap(data1,path=[px.Constant("All"),"day","time","sex"],values="tip")
st.plotly_chart(fig1)
