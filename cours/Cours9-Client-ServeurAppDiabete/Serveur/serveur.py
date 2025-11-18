from flask import Flask, request,jsonify
import pandas as pd
from model import pred_proba

# Initialisation du serveur
app=Flask(__name__)

@app.route('/model',methods=['POST'])

def get_info():
    data=request.get_json(force=True)
    new_date=pd.DataFrame(data=data,index=[1])
    pred,proba=pred_proba(new_date)
    print(f'pred={pred},-->proba = {proba}')
    dict_resultat={'class':pred,'proba':proba}
        
    return jsonify(dict_resultat)

# Lancement du serveur

if __name__=='__main__':
    app.run(debug=True,port=5000)