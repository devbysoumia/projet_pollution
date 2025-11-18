import json,requests

url='http://127.0.0.1:5000/model'

data=json.dumps({'cle_message':'Bonjour, Veuillez transmettre le projet IA1 ce soir sinon ....'})

rep=requests.post(url,data)

print(rep.text)

