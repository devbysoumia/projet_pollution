from flask import Flask, request

# Initialisation du serveur
app=Flask(__name__)

@app.route('/model',methods=['POST'])

def get_info():
    data=request.get_json(force=True)
    message_client=data['cle_message']
    print(f'Le client à envoyer : {message_client}')
    return f'Réponse su serveur : Le client à envoyer : {message_client}'

# Lancement du serveur

if __name__=='__main__':
    app.run(debug=True,port=5000)