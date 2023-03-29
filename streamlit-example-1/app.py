import streamlit as st
#basic streamlit 
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)