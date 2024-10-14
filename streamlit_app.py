import streamlit as st

st.title('PLGA Nanoparticles App ')

st.info("This is app to predict the response variables of PLGA nanoparticles, i.e. particle size and PDI.")


st.subheader("Choose parameters of microfluidic")
temp_options = [3, 3.5, 4, 5]
temp = st.select_slider("Choose Factor A:", options=temp_options)
