import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle #pickle for saving the model.
import sklearn
import warnings
warnings.filterwarnings("ignore")

st.title('📃Deposit Prediction Web App')
age = st.number_input('Please enter your age',step = 1)

job = st.selectbox(
     'Please select your job',
    ('admin','blue-collar','entrepreneur', 'housemaid','management','retired','self-employed', 'services','student','technician','unemployed','unknown'))

marital = st.selectbox('Please select your marital status',
                       ('married','single','divorced'))

education = st.selectbox('Please select your education',
                          ('basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown'))

default = st.selectbox('Please select your if you have credit in default or not',('yes','no','unknown') )

housing = st.selectbox('Please select your if you have housing loan or not',('yes','no','unknown') )

loan = st.selectbox('Please select your if you have personal loan',('yes','no','unknown') )

contact = st.selectbox('Please select our contact communication type',
                ('cellular','telephone'))

month = st.selectbox('Please select when was our lasst contact',
                      ('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec') )

day_of_week = st.selectbox('Please select your last contact day of the week',('mon','tue','wed','thu','fri'))

duration = st.number_input('Please enter your last contact duration in seconds',step = 1)

campaign = st.number_input('Please enter your number of contacts performed',step = 1)

pdays = st.number_input('Please enter number of days passed after last contacted from a previous campaign',step = 1)
if pdays == 0:
    pdays = 999
    
previous = st.number_input('Please enter the number of contacts performed before this campaign:',step = 1)

poutcome = st.selectbox('Please select outcome of the previous marketing campaign',('success','failure','nonexistent') )

emp_var_rate = st.number_input('Please enter employment variation rate')

cons_price_idx = st.number_input('Please enter consumer price index')

cons_conf_idx = st.number_input('Please enter consumer confidence index')

euribo3m = st.number_input('Please enter euribor 3 month rate')

nr_employed = st.number_input('Please enter number of employees')

#Test single input.
input_data = np.array([age, job, marital,education,default,housing,loan,contact,month,day_of_week,duration,campaign,pdays,previous,poutcome,emp_var_rate,cons_price_idx ,cons_conf_idx,	euribo3m,nr_employed])
input_data = input_data.reshape(1, -1)
columns = ['age', 'job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week', 'duration', 'campaign', 'pdays', 'previous', 'poutcome', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed']
input_data_df = pd.DataFrame(input_data, columns=columns)

#pickled_model = pickle.load(open("C:/Users/Deniz/OneDrive/Belgeler/GitHub/ada442/models/tuned_best_model.pkl", 'rb'))#Load the model.
pickled_model = pickle.load(open("models/tuned_best_model.pkl", 'rb'))#Load the model.


def predict_display():
    input_predictions = pickled_model.predict(input_data_df)
    # Print out the prediction
    if input_predictions == "no":
        st.error(f'No! Client is NOT subscribed to a term deposit.', icon="🚨")
        col1, col2 ,col3, col4, col5, col6, col7 = st.columns(7)
        with col1:
            st.write(' ')
        with col2:
            st.image("Image20230606202918.gif", width = 500 )
        with col3:
            st.write(' ')
        with col4:
            st.write(' ')
        with col5:
            st.write(' ')
        with col6:
            st.write(' ')
        with col7:
            st.write(' ')

    else:
        st.success(f'YES! Client subscribed to a term deposit.', icon="💸")
        # Load and display a GIF image

        col1, col2 ,col3, col4, col5, col6, col7 = st.columns(7)
        with col1:
            st.write(' ')
        with col2:
            st.image("Image20230606202922.gif", width = 500 )
        with col3:
            st.write(' ')
        with col4:
            st.write(' ')
        with col5:
            st.write(' ')
        with col6:
            st.write(' ')
        with col7:
            st.write(' ')
  

if st.button('Press me'):
    predict_display() 


