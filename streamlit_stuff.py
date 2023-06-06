import streamlit as st

st.title('My first Streamlit app')
st.write('Hello, world!')

age = st.number_input('Age:')
st.write('The current number is ', age)

job = st.text_input('Job:', )
st.write('The current movie title is', job)

marital = st.text_input('marital:', )
st.write('The current movie title is', marital)

education = st.text_input('education:', )
st.write('The current movie title is', education)

default = st.text_input('default:', )
st.write('The current movie title is', default)

housing = st.text_input('housing:', )
st.write('The current movie title is', housing)

loan = st.text_input('loan:', )
st.write('The current movie title is', loan)

contact = st.text_input('contact:', )
st.write('The current movie title is', contact)

month = st.text_input('month:', )
st.write('The current movie title is', month)

day_of_week = st.text_input('day_of_week:',)
st.write('The current number is ', day_of_week)

duration = st.number_input('duration:')
st.write('The current number is ', duration)

campaign = st.number_input('campaign:')
st.write('The current number is ', campaign)

pdays = st.number_input('pdays:')
st.write('The current number is ', pdays)

previous = st.number_input('previous:')
st.write('The current number is ', previous)

poutcome = st.text_input('poutcome:', )
st.write('The current movie title is', poutcome)

emp_var_rate = st.number_input('emp_var_rate:')
st.write('The current number is ', emp_var_rate)

cons_price_idx = st.number_input('cons_price_idx:')
st.write('The current number is ', cons_price_idx)

cons_conf_idx = st.number_input('cons_conf_idx:')
st.write('The current number is ', cons_conf_idx)

euribo3m = st.number_input('euribo3m:')
st.write('The current number is ', euribo3m)

nr_employed = st.number_input('nr_employed:')
st.write('The current number is ', nr_employed)

