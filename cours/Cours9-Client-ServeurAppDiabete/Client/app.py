import warnings
warnings.filterwarnings('ignore')
import streamlit as st
from user import descripteurs_input
import requests,json

url='http://127.0.0.1:5000/model'

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
    data=json.dumps(analyses)
    rep=requests.post(url,data)
    dict_rep=rep.json()
    pred,proba=dict_rep['class'],dict_rep['proba']

    if pred==1:
        st.write("# :red[Positif]:cry:")
    else:
        st.write("# :green[Négatif]:smile:")
    st.write(f" # Probabilité : {round(proba*100,2)} %")

if __name__=='__main__':
    main()