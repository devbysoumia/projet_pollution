import warnings
warnings.filterwarnings('ignore')

import numpy as np
import streamlit as st
import pandas as pd

def descripteurs_input():
    
    NbGross=st.sidebar.slider('Nb_Grossesse',0.0,17.0,2.0)
    Glucose=st.sidebar.slider('Glucose',0.0,199.0,100.0)
    PresArt=st.sidebar.slider('PresArt',0.0,122.0,80.0)
    EpaissPli=st.sidebar.slider('EpaissPli',0.0,99.0,80.0)
    Insuline=st.sidebar.slider('Insuline',0.0,846.0,20.0)
    IMC=st.sidebar.slider('IMC',0.0,61.0,20.0)
    pedigree=st.sidebar.slider('Pedigree',0.078,2.42,1.0)
    age=st.sidebar.slider('Age',21.0,81.0,20.0)
    data={
        'Nb_Grossesse':NbGross,
        'Glucose':Glucose,
        'PresArt':PresArt,
        'EpaissPli':EpaissPli,
        'Insuline':Insuline,
        'IMC':IMC,
        'pedigree':pedigree,
        'age':age
    }
    features=pd.DataFrame(data,index=[1])
     
    return features





# col=['NbGross','Glucos','PresArt','EpaissPli','Insuline','IMC','Pedigree','age','class']

