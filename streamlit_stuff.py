import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle #pickle for saving the model.
import sklearn


st.title('Deposit Prediction Web App')

age = st.number_input('Age:')

job = st.text_input('Job:', )

marital = st.text_input('marital:', )

education = st.text_input('education:', )

default = st.text_input('default:', )

housing = st.text_input('housing:', )

loan = st.text_input('loan:', )

contact = st.text_input('contact:', )

month = st.text_input('month:', )

day_of_week = st.text_input('day_of_week:',)

duration = st.number_input('duration:')

campaign = st.number_input('campaign:')

pdays = st.number_input('pdays:')

previous = st.number_input('previous:')

poutcome = st.text_input('poutcome:', )

emp_var_rate = st.number_input('emp_var_rate:')

cons_price_idx = st.number_input('cons_price_idx:')

cons_conf_idx = st.number_input('cons_conf_idx:')

euribo3m = st.number_input('euribo3m:')

nr_employed = st.number_input('nr_employed:')

import os
st.write(os.getcwd())


#Test single input.
input_data = np.array([30, "blue-collar", "married",	"basic.9y",	"no",	"yes",	"no",	"cellular",	"may",	"fri",	487,	2,	999,	0,	"nonexistent",	-1.8,	92.893,	-46.2,	1.313,	5099.1])
input_data = input_data.reshape(1, -1)
columns = ['age', 'job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week', 'duration', 'campaign', 'pdays', 'previous', 'poutcome', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed']
input_data_df = pd.DataFrame(input_data, columns=columns)

#pickled_model = pickle.load(open("C:/Users/Deniz/OneDrive/Belgeler/GitHub/ada442/models/tuned_best_model.pkl", 'rb'))#Load the model.
pickled_model = pickle.load(open("models/tuned_best_model.pkl", 'rb'))#Load the model.

input_predictions = pickled_model.predict(input_data_df)

# Print out the prediction
st.write(input_predictions)

