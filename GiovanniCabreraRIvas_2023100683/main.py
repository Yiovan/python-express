from flask import Flask
from Cliente.cliente import cliente  

app = Flask(__name__)
app.register_blueprint(cliente)  #

@app.route('/', methods=['GET'])  
def inicio():
    return "Servidor Flask funcionando"

if __name__ == '__main__':
    app.run(debug=True, port=5003)
