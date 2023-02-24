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


import matplotlib.pyplot as plt
import seaborn as sns

arr1, arr2 = np.random.randn(100), np.random.rand(100)
arr3 = np.random.randint(1,1001,100)

c1, c2 = st.columns(2)

with c1:
	fig, ax = plt.subplots()
	ax.set_title("Matplotlib Scatter Plot")
	ax.scatter(arr1, arr2, s = arr3, c = arr3, alpha = 0.6)
	st.pyplot(fig)

with c2:
	fig, ax = plt.subplots()
	ax.set_title("Seaborn Scatter Plot")
	ax = sns.scatterplot(x = arr1, y = arr2)
	st.pyplot(fig)
