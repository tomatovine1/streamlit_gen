#media
import streamlit as st

c1, c2 = st.columns(2)

with c1:
	st.markdown("## Image")	
	st.image("https://bit.ly/edus3ha")

with c2:
	st.markdown("## Video")
	st.video("https://bit.ly/canibs3")

st.markdown("## Audio")
st.audio("https://bit.ly/rainaws3")