import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

data=px.data.gapminder().query("year==2007")
st.dataframe(data)

fig1=px.treemap(data,path=[px.Constant("World"),"continent","country"],values="pop",color="lifeExp")
st.plotly_chart(fig1)

data_german=px.data.gapminder().query("country=='German'")
data_italy=px.data.gapminder().query("country=='Italy'")
fig2=px.line(pd.concat(data_german,data_italy),x="year",y="pop",color="country")
st.plotly_chart(fig2)
