import streamlit as st

st.title('My first Streamlit app')
st.write('Hello, world!')

number = st.number_input('Insert a number')
st.write('The current number is ', number)