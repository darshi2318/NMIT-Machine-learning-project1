import streamlit as st
import pandas as pd
import numpy as np
import joblib

from sklearn.tree import DecisionTreeClassifier
#loading up the classification model we create
model=DecisionTreeClassifier(criterion='entropy', max_depth=10, min_samples_leaf=2,
                       random_state=0)
model=joblib.load('finalized_model.joblib')
#caching the model for faster loading
@st.cache
#Define the prediction function
def predict(Buying,Maint,Doors,Persons,Lug_boots,Safety):
  if Safety=='med':
    safety=1
  elif safety=='high':
    safety=2
  elif safety=='low':
    safety=3
  df=pd.DataFrame([[Buying,Maint,Doors,Persons,Lug_boots,Safety]],
        columns=['Buying','Maint','Doors','Persons','Lug_boots','Safety'])
  prediction=model.predict([[Buying,Maint,Doors,Persons,Lug_boots,Safety]])
  return prediction
st.title('car Evaluation Classification')
st.image("""https://www.hindustantimes.com/ht-img/img/2024/04/17/550x309/CRICKET-IND-AFG-T20-62_1709207374217_1713331028912.jpg""")
st.header('Enter the information of the car:')
Buying=st.number_input('maint:',min_value=1,max_value=4, value=1)
st.txt("vhigh=1 high=2 med=3 low=4")
Main=st.number_input('maint:',min_value=1,max_value=4, value=1)
st.txt("2-Doors=1 3-Doors=2 4-Doors=3 5more=4")
Doors=st.number_input('doors:',min_value=1,max_value=4, value=1)
st.txt("2-persons=1 4-persons=2 more=3")
Persons=st.number_input('persons:',min_value=1,max_value=4, value=1)
st.txt("small=1 med=2 big=3")
Lug_boot=st.number_input('lug_boot:',min_value=1,max_value=4, value=1)
Safety=st.radio('safety:',('med','high','low'))

if st.button('Submit_Car_Infos'):
  cal_eval=predict(Buying,Maint,Doors,Persons,Lug_boots,Safety)
  st.success(f'The Evaluation of car :{cal_eval[0]}')
