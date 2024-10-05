import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

data=px.data.gapminder()
st.dataframe(data)
st.bar_chart(data)
