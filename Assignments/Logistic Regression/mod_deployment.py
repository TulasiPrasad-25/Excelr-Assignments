#!/usr/bin/env python
# coding: utf-8

# In[18]:


!pip install streamlit 

# In[19]:


import pandas as pd
import numpy as np
import streamlit as st
import pickle
import warnings
warnings.filterwarnings('ignore')

# In[20]:


model = pickle.load(open('log_reg_model.pkl','rb'))

# In[21]:


#title of the page
st.title("patient data for admit")

# In[22]:


def user_input_data():
    Pregnancies = st.sidebar.slider("enter Pregnancies :",0,17)
    Glucose = st.sidebar.slider("enter Glucose :",0,200)
    BloodPressure = st.sidebar.slider("enter BloodPressure :",0,122)
    SkinThickness = st.sidebar.slider("enter SkinThickness :",0,100)
    Insulin = st.sidebar.slider("enter Insulin :",0,846)
    BMI = st.sidebar.slider("enter BMI :",0,67)
    DiabetesPedigreeFunction = st.sidebar.slider("enter DiabetesPedigreeFunction :",0,2)
    Age = st.sidebar.slider("enter Age :",21,81)
    data = {'Pregnancies':Pregnancies,'Glucose':Glucose,'BloodPressure':BloodPressure,'SkinThickness':SkinThickness,
            'Insulin':Insulin,'BMI':BMI,'DiabetesPedigreeFunction':DiabetesPedigreeFunction,'Age':Age}
    features=pd.DataFrame(data , index=[0])
    return features


# In[23]:


df = user_input_data()

# In[24]:


df = user_input_data()
pred = model.predict(df)
pred_proba = model.predict_proba(df)
button = st.button('Predict')
if button is True:
    st.subheader('Prediction')
    st.write('You are eligible to Adimit' if pred_proba[0][1] >=0.5 else 'Not eligible for admit')
    st.write(pred_proba)

# In[26]:


streamlit run app.py


# In[ ]:



