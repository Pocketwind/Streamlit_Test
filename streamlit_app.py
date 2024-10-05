import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

data=px.data.gapminder().query("year==2007")
st.dataframe(data)

fig1=px.treemap(data,path=[px.Constant("World"),"continent","country"],values="pop",color="lifeExp")
st.plotly_chart(fig1)

data=px.data.gapminder().quary("iso_alpha=='JPN' and iso_alpha=='KOR')
fig2=px.line(data,x="year",y="pop",color="country")
st.plotly_chart(fig2)
