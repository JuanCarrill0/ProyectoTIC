from flask import jsonify, Blueprint, request, Response
from Controladores.ControladorResultado import ControladorResultado

miControladorResultado = ControladorResultado()

resultado = Blueprint('resultado',__name__)

@resultado.route("/resultados",methods=['GET'])
def getResultados():
    try:
        json=miControladorResultado.index()
        return jsonify(json),200
    except Exception as e:
        strE = format(e)
        return jsonify('Ha ocurrido el siguiente error : ' + strE), 500

@resultado.route("/resultados/candidato/<string:id_candidato>/mesa/<string:id_mesa>",methods=['POST'])
def crearResultado(id_candidato,id_mesa):
    try:
        data = request.get_json()
        if "cant_votos" in data:
            json=miControladorResultado.create(data,id_candidato,id_mesa)
            if json.__contains__('error'):
                return jsonify(json),400
            else:
                return jsonify(json),201
        else:
            return jsonify('Ha ocurrido el siguiente error : Falta parametro cant_votos en la peticion o esta mal nombrado'),400
    except Exception as e:
        strE = format(e)
        if strE.__contains__('keys'):
            return jsonify('Ha ocurrido el siguiente error : Los id de candidato y / o mesa no existen'),400
        else:
            return jsonify('Ha ocurrido el siguiente error : ' + strE),500

@resultado.route("/resultados/<string:id>",methods=['GET'])
def getResultado(id):
    try:
        json=miControladorResultado.show(id)
        return jsonify(json),202
    except Exception as e:
        strE = format(e)
        if strE.__contains__('keys'):
            return jsonify('Ha ocurrido el siguiente error : El id del resultado solicitado no existe'),400
        else:
            return jsonify('Ha ocurrido el siguiente error : ' + strE),500

@resultado.route("/resultados/<string:id>/candidato/<string:id_candidato>/mesa/<string:id_mesa>",methods=['PUT'])
def modificarResultado(id,id_candidato,id_mesa):
    try:
        data = request.get_json()
        if "cant_votos" in data:
            json = miControladorResultado.update(id,data,id_candidato,id_mesa)
            if json.__contains__('error'):
                return jsonify(json), 400
            else:
                return jsonify(json), 200
        else:
            return jsonify('Ha ocurrido el siguiente error : Falta parametro cant_votos en la peticion o esta mal nombrado'), 400
    except Exception as e:
        strE = format(e)
        if strE.__contains__('keys'):
            return jsonify('Ha ocurrido el siguiente error : Los id del resultado, candidato y / o mesa no existen'), 400
        else:
            return jsonify('Ha ocurrido el siguiente error : ' + strE), 500

@resultado.route("/resultados/<string:id>",methods=['DELETE'])
def eliminarResultado(id):
    try:
        json=miControladorResultado.delete(id)
        if json['deleted_count'] == 0:
            return jsonify('Ha ocurrido el siguiente error : El id del resultado solicitado no existe'), 400
        else:
            return jsonify(json),202
    except Exception as e:
        strE = format(e)
        if strE.__contains__('keys'):
            return jsonify('Ha ocurrido el siguiente error : El id del resultado solicitado no existe'),400
        else:
            return jsonify('Ha ocurrido el siguiente error : ' + strE),500
