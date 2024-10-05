import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

data=px.data.gapminder().query("year==2007")
st.dataframe(data)

fig1=px.treemap(data,path=[px.Constant("World"),"continent","country"],values="pop",color="lifeExp")
st.plotly_chart(fig1)

data_german=px.data.gapminder().quary("country=='German'")
data_italy=px.data.gapminder().quary("country=='Italy'")
fig2=px.line(data,x="year",y="pop",color="country")
st.plotly_chart(fig2)
