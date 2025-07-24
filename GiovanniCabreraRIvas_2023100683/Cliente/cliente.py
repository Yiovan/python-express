# cliente.py

from flask import Blueprint, Flask, jsonify, request

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])
def obtener_cliente():
    ci = request.json.get('ci')
    print("CI recibido:", ci)

    if ci == "5860464":
        return jsonify({
            "accion": "Success",
            "codRes": "SIN_ERROR",
            "menRes": "OK",
            "ci": ci,
            "nombre": "Giovanni",
            "apellidos": "Cabrera Rivas",
        }), 200
    else:
        return jsonify({
            "accion": "Cliente no está en el sistema",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": ci
        }), 404
