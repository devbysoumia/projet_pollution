import warnings
warnings.filterwarnings('ignore')

import streamlit as st
from model import pred_proba
from user import descripteurs_input

def main():
    st.set_page_config(page_title='Diagnostique du diabète',page_icon=":hospital:")
    st.title(":red[Diagnostique du diabète en ligne]")
    st.markdown(
        """
        # :orange[Application de prediction du diabète]
        
        """
    )
    st.sidebar.header('Entrer les analyses :')
    analyses=descripteurs_input()
    st.write(analyses)
    pred,proba=pred_proba(analyses)

    if pred==1:
        st.write("# :red[Positif]:cry:")
    else:
        st.write("# :green[Négatif]:smile:")
    st.write(f" # Probabilité : {round(proba*100,2)} %")

if __name__=='__main__':
    main()