from flask import jsonify, Blueprint, request
from Controladores.ControladorPartido import ControladorPartido

miControladorPartido = ControladorPartido()

partido = Blueprint('partido',__name__)

@partido.route("/partidos",methods=['GET'])
def getPartidos():
    try:
        json=miControladorPartido.index()
        return jsonify(json)
    except Exception as ex:
        return jsonify({'Ha ocurrido el siguiente error':str(ex)}),500
@partido.route("/partidos",methods=['POST'])
def crearPartido():
    try:
        data = request.get_json()
        json=miControladorPartido.create(data)
        return jsonify(json)
    except ValueError as val:
        return jsonify({'Petición fallida':str(val)}),400
    except Exception as ex:
        return jsonify({'Ha ocurrido el siguiente error':str(ex)}),500
@partido.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)
@partido.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    try:
        data = request.get_json()
        json=miControladorPartido.update(id,data)
        return jsonify(json)
    except ValueError as val:
        return jsonify({'Petición fallida':str(val)}),400
    except Exception as ex:
        return jsonify({'Ha ocurrido el siguiente error':str(ex)}),500

@partido.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    try:
        json=miControladorPartido.delete(id)
        return jsonify(json)
    except Exception as ex:
        return jsonify({'Ha ocurrido el siguiente error':str(ex)}),500