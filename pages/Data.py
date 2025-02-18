import pandas as pd
import streamlit as st
df=pd.read_csv("Automobile.csv")
df
st.bar_chart(df["company"])
