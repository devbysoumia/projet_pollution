import streamlit as st
from datetime import date
from PIL import Image

#-------------Sidebar-----------------
st.sidebar.title('Cours Streamlit')  # Corrigé de st.sidebar('Cours Streamlit')
menu = st.sidebar.selectbox('Navigation', ['Acceuil', 'Les Objets', 'Image'])

if menu == 'Acceuil':
    st.markdown(
        """
        <div style='text-align:center'>
        <h1>Introduction à Streamlit</h1>
        <p style='color:blue'>Ce cours est une introduction à Streamlit</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.caption('Text........................')
    st.button('Ok')

elif menu == 'Les Objets':
    #-------------------Textbox-----------------
    nom = st.text_input("Entrer votre nom :")
    if nom:
        st.write(f'Merci {nom}')
    
    #---------------------ComboBox----------------------
    options = ['Option 1', 'Option 2', 'Option 3']
    Choix = st.selectbox('Veuillez choisir une option :', options)
    st.write(f'Vous avez sélectionné : {Choix}')
    
    #---------RadioButton-------------
    Choix2 = st.radio('Choisissez votre club préféré :', ['GCM', 'FCB', 'JUV', 'RM'])
    st.write(f'Votre club est : {Choix2}')
    
    #-----------Checkbox-----------
    check = st.checkbox("Acceptez-vous les termes du contrat ?")
    if check:
        st.write('Merci')
    
    #-----------Slider------------
    age = st.slider("Votre âge est :", 0, 100, 20)
    st.write(f'Votre âge est : {age}')
    
    #-----------Text Area------------
    tex = st.text_area("Votre commentaire svp :")
    if tex:
        st.write(f'Commentaire : {tex}')
    
    #-------------Date------------------
    dateInput = st.date_input('Choisissez une date :', date.today())
    st.write('La date est :', dateInput)

else:  # Image
    #-------------Image-----------------
    fichier = st.file_uploader('Choisir une image :', type=['jpg', 'jpeg', 'png'])
    if fichier is not None:
        img = Image.open(fichier)
        st.image(img, caption='Image chargée')
