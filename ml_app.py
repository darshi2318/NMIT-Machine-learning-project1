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
