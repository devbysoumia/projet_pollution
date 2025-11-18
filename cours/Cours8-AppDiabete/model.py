import warnings
warnings.filterwarnings('ignore')

import pickle
import numpy as np

# Chargement du model
model_name='diabete_RL.pkl'
model=pickle.load(open(model_name,'rb'))

def pred_proba(data):
    #data=data.values
    pred=int(model.predict(data))
    prob=model.predict_proba(data)
    prob=prob[0][pred]
    return pred,prob
