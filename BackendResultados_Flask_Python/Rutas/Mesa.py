from flask import jsonify, Blueprint, request
from Controladores.ControladorMesa import ControladorMesa

miControladorMesa = ControladorMesa()

mesa = Blueprint('mesa',__name__)

@mesa.route("/mesas",methods=['GET'])
def getMesas():
    try:
        json=miControladorMesa.index()
        return jsonify(json),200
    except Exception as e:
        strE = format(e)
        return jsonify('Ha ocurrido el siguiente error : ' + strE), 500

@mesa.route("/mesas",methods=['POST'])
def crearMesa():
    try:
        data = request.get_json()
        if "cant_inscritos" in data and "numero" in data:
            json=miControladorMesa.create(data)
            if json.__contains__('error'):
                return jsonify(json), 400
            else:
                return jsonify(json), 201
        else:
            return jsonify('Ha ocurrido el siguiente error : Faltan parametros cant_inscritos y / o numero, en la peticion o estan mal nombrados'), 400
    except Exception as e:
        strE = format(e)
        return jsonify('Ha ocurrido el siguiente error : ' + strE), 500

@mesa.route("/mesas/<string:id>",methods=['GET'])
def getMesa(id):
    try:
        json=miControladorMesa.show(id)
        return jsonify(json),202
    except Exception as e:
        strE = format(e)
        if strE.__contains__('keys'):
            return jsonify('Ha ocurrido el siguiente error : El id de la mesa solicitado no existe'),400
        else:
            return jsonify('Ha ocurrido el siguiente error : ' + strE),500

@mesa.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesa(id):
    try:
        data = request.get_json()
        if ("cant_inscritos" and "numero") in data:
            json=miControladorMesa.update(id,data)
            if json.__contains__('error'):
                return jsonify(json), 400
            else:
                return jsonify(json), 200
        else:
            return jsonify('Ha ocurrido el siguiente error : Faltan parametros cant_inscritos y / o numero, en la peticion o estan mal nombrados'), 400
    except Exception as e:
        strE = format(e)
        if strE.__contains__('keys'):
            return jsonify('Ha ocurrido el siguiente error : El id de la mesa solicitado no existe'), 400
        else:
            return jsonify('Ha ocurrido el siguiente error : ' + strE), 500


@mesa.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    try:
        json=miControladorMesa.delete(id)
        if json['deleted_count'] == 0:
            return jsonify('Ha ocurrido el siguiente error : El id de la mesa solicitado no existe'), 400
        else:
            return jsonify(json), 202
    except Exception as e:
        strE = format(e)
        if strE.__contains__('keys'):
            return jsonify('Ha ocurrido el siguiente error : El id de la mesa solicitado no existe'),400
        else:
            return jsonify('Ha ocurrido el siguiente error : ' + strE),500