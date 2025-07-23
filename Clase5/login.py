from flask import Blueprint, Flask, jsonify, request

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def llamarServiciosScet():
    user = request.json.get('user')
    password = request.json.get('password')
    print("user enviado:", user, "Haz enviado:", password)
    return jsonify({"message": "OK"}), 200
