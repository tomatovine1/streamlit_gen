import streamlit as st

t1, t2, t3 = st.columns([1,3,1])
m1, m2 = st.columns(2)
b1, b2, b3 = st.columns([1,3,1])

with t2:
	st.markdown("`Title`")
	st.title("Exploring Streamlit")
	st.write("------------------------------------------------------")

with m1:
	st.markdown("`Heading`")
	st.header("Introduction")
	st.write("------------------------------------------------------")	
	st.markdown("`Sub Heading`")
	st.subheader("Installation")
	st.write("------------------------------------------------------")
	st.markdown("`Text`")
	st.text("Learn how to install Streamlit")
	st.write("------------------------------------------------------")

with m2:
	st.markdown("`Markdown`")
	st.markdown("Install Streamlit using `pip install streamlit ")
	st.write("------------------------------------------------------")
	st.markdown("`Write`")
	st.write("Once installed, run Streamlit using the command `streamlit hello`")
	st.write("------------------------------------------------------")
	st.markdown("`Latex`")
	st.latex(r"s \left ( t \right ) = ut + \dfrac{1}{2} at^2")
	st.write("------------------------------------------------------")

with b2:
	st.markdown("`Caption`")
	st.caption("Streamlit text options")
