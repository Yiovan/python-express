#-*- Coding utf-8 -*-
#caracteres especiales


from flask import Blueprint,Flask, jsonify, request
from login import login 
app = Flask(__name__)
app.register_blueprint(login)

@app.route('/', methods=['GET'])

def unida():
    return "Server Flask running on port 5000!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)