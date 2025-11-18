import streamlit as st
from pandas import read_csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import scipy as sc
import seaborn as sns
from pandas.plotting import scatter_matrix

# Chargement ---------------------
try:
    fichier = 'pima.csv'
    col = ['NbGross','Glucos','PresArt','EpaissPli','Insuline','IMC','Pedigree','Age','Class']
    patient = [f'Patient_{i}' for i in range(1, 768)]  # correction de la syntaxe
    data = pd.read_csv(fichier, names=col)
    data.index = patient
except:
    st.write('Erreur de lecture ....')

st.sidebar.title('Navigation')
menu = st.sidebar.selectbox('Choisir un volet', ['Accueil', 'Peak at the data', 'Visualisation', 'Etude de correlation'])

if menu == 'Accueil':
    st.markdown(
        """
        <div style='text-align:center'>
        <h1>Analyse des données sur le Diabète</h1>
        </div>
        """, unsafe_allow_html=True
    )
    st.subheader('Afficher les données')
    st.dataframe(data)  # correction : st.dataframe au lieu de st.dataFrame('data')

# Menu Peak at the data
elif menu == 'Peak at the data':
    st.header('Peak at the data')
    st.subheader('Afficher les 10 premières patientes:')
    st.dataframe(data.head(10))
    st.subheader('Afficher les 10 dernières patientes:')
    st.dataframe(data.tail(10))
    st.subheader('Statistiques descriptives:')
    st.write(data.describe())
    st.subheader('Les dimensions:')
    st.write(data.shape)  # correction : data.Shape() -> data.shape
    st.subheader('Les types des données:')
    st.write(data.dtypes)
    st.subheader('Distribution de la classe:')
    count_class = data['Class'].value_counts()  # correction : data.grouphy -> value_counts()
    st.write(count_class)
    
    # Distribution
    figure, ax = plt.subplots()
    data['Class'].value_counts().plot(kind='bar', color=['green','red'], ax=ax)
    ax.set_xlabel('Classe (0=Non Diabétique, 1=Diabétique)')
    ax.set_ylabel('Nombre de patientes')
    st.pyplot(figure)

# Menu Etude de corrélation
elif menu == 'Etude de correlation':
    st.header('Etude de corrélation')
    corr = data.corr()
    figure, ax = plt.subplots(figsize=(15,10))
    sns.heatmap(corr, annot=True, fmt='.3f', cmap='pink', ax=ax)
    st.pyplot(figure)

# Menu Visualisation
else:
    st.header('Techniques de visualisation')
    st.subheader('Histogrammes')
    data.hist(bins=20, figsize=(15,10), layout=(3,3), grid=True)
    st.pyplot(plt.gcf())
    
    st.subheader('Histogramme pour Glucos')  # "INC" remplacé par "Glucos"
    figure, ax = plt.subplots()
    ax.hist(data['Glucos'], bins=20, edgecolor='black')
    ax.set_xlabel('Valeur des masses')
    ax.set_ylabel('Fréquences')
    st.pyplot(figure)
    
    st.subheader('Graphes de densités')
    data.plot(kind='density', layout=(3,3), sharex=False, sharey=False, figsize=(15,20))
    st.pyplot(plt.gcf())
    
    # Boite à moustaches
    st.subheader('Boite à moustaches')
    data.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False, figsize=(15,20))
    st.pyplot(plt.gcf())
    
    st.subheader('Scatter Matrix')
    scatter_matrix(data, figsize=(25,25))
    st.pyplot(plt.gcf())
    
    st.subheader('PairPlot')
    sns.pairplot(data, hue='Class')
    st.pyplot(plt.gcf())
    
    st.subheader('PairPlot (Glucos/IMC/Insuline)')
    sns.pairplot(data, hue='Class', vars=['Glucos','IMC','Insuline'])
    st.pyplot(plt.gcf())
