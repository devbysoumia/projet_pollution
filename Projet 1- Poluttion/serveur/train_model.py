import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np

np.random.seed(42)
X = pd.DataFrame({
    'temperature': np.random.uniform(0, 40, 100),
    'humidity': np.random.uniform(0, 100, 100),
    'pm2_5': np.random.uniform(0, 50, 100),
    'pm10': np.random.uniform(0, 80, 100),
    'co': np.random.uniform(0, 10, 100)
})
y = np.random.randint(0, 2, 100)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)
with open('random_forest_air.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Modèle random_forest_air.pkl créé avec succès !")
