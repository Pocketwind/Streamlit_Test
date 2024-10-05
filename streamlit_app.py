import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

data=px.data.gapminder().query("year==2007")
st.dataframe(data)
fig=px.treemap(data,path=[px.Constant("World"),"continent","country"],values="pop",color="lifeExp")
