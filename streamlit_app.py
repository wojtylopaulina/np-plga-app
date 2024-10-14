import streamlit as st

st.title('PLGA Nanoparticles App ')

st.info("This is app to predict the response variables of PLGA nanoparticles, i.e. particle size and PDI.")


st.subheader("Choose parameters of microfluidic")
factor_A = st.slider("Choose Factor A:", 0, 6)
