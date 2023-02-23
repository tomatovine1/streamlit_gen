# native charts
import streamlit as st
import numpy as np

df = np.random.randn(5,5)

mygrid = mygrid = [[],[]]
with st.container():
  mygrid[0] = st.columns(2)
  st.markdown("## Line Chart")
  st.line_chart(df)

with st.container():
  mygrid[1] = st.columns(2)
  st.markdown("## Area Chart")
  st.area_chart(df)


