import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

data=px.data.gapminder()
st.line_chart(data)
