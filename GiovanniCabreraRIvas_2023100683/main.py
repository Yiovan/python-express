from flask import Flask
from Cliente.cliente import cliente  # Importás el blueprint

app = Flask(__name__)
app.register_blueprint(cliente)  # Lo registrás

@app.route('/', methods=['GET'])  # Solo para testeo
def inicio():
    return "Servidor Flask funcionando"

if __name__ == '__main__':
    app.run(debug=True, port=5003)
