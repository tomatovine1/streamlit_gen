#using metric, dataframes, tables

import streamlit as st
import pandas as pd

sample_data = {"Mammals": ["Cat", "Dog", "Pig"]}
df = pd.DataFrame(sample_data)

c1, c2, c3, c4 = st.columns(4)

with c1:
	st.markdown("## Metric")
	st.metric(label="Velocity in kilometres per hour", value=75.4, delta=-2)

with c2:
	st.markdown("## Dataframe")
	st.dataframe(df)
	
with c3:
	st.markdown("## Table")
	st.table(df)

with c4:
	st.markdown("## JSON")
	st.json(sample_data)
