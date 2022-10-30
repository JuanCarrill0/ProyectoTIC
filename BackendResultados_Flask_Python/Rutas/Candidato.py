from flask import jsonify, Blueprint, request
from Controladores.ControladorCandidato import ControladorCandidato

miControladorCandidato = ControladorCandidato()

candidato = Blueprint('candidato',__name__)

@candidato.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

@candidato.route("/candidatos",methods=['GET'])
def getCandidatos():
    try:
        json=miControladorCandidato.index()
        return jsonify(json),202
    except Exception as e:
        strE = format(e)
        return jsonify('Ha ocurrido el siguiente error : ' + strE), 500

@candidato.route("/candidatos",methods=['POST'])
def crearCandidato():
    try:
        data = request.get_json()
        if ("cedula" and "num_resolucion" and "nombre" and "apellido") in data:
            json=miControladorCandidato.create(data)
            if json.__contains__('error'):
                return jsonify(json), 400
            else:
                return jsonify(json), 201
        else:
            return jsonify('Ha ocurrido el siguiente error : Faltan parametros cedula, num_resolucion, nombre y / o apellido, en la peticion o esta mal nombrado'), 400
    except Exception as e:
        strE = format(e)
        return jsonify('Ha ocurrido el siguiente error : ' + strE), 500

@candidato.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    try:
        json=miControladorCandidato.show(id)
        return jsonify(json),202
    except Exception as e:
        strE = format(e)
        if strE.__contains__('keys'):
            return jsonify('Ha ocurrido el siguiente error : El id del candidato solicitado no existe'),400
        else:
            return jsonify('Ha ocurrido el siguiente error : ' + strE),500

@candidato.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    try:
        data = request.get_json()
        if ("cedula" and "num_resolucion" and "nombre" and "apellido") in data:
            json=miControladorCandidato.update(id,data)
            if json.__contains__('error'):
                return jsonify(json), 400
            else:
                return jsonify(json), 200
        else:
            return jsonify(
                'Ha ocurrido el siguiente error : Faltan parametros cedula, num_resolucion, nombre y / o apellido, en la peticion o esta mal nombrado'), 400
    except Exception as e:
        strE = format(e)
        if strE.__contains__('keys'):
            return jsonify('Ha ocurrido el siguiente error : El id del candidato solicitado no existe'), 400
        else:
            return jsonify('Ha ocurrido el siguiente error : ' + strE), 500

@candidato.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    try:
        json=miControladorCandidato.delete(id)
        if json['deleted_count'] == 0:
            return jsonify('Ha ocurrido el siguiente error : El id del candidato solicitado no existe'), 400
        else:
            return jsonify(json),202
    except Exception as e:
        strE = format(e)
        if strE.__contains__('keys'):
            return jsonify('Ha ocurrido el siguiente error : El id del candidato solicitado no existe'),400
        else:
            return jsonify('Ha ocurrido el siguiente error : ' + strE),500

@candidato.route("/candidatos/<string:id>/partido/<string:id_partido>",methods=['PUT'])
def asignarPartidoACandidato(id,id_partido):
    try:
        json=miControladorCandidato.asignarPartido(id,id_partido)
        if json.__contains__('error'):
            return jsonify(json), 400
        else:
            return jsonify(json), 202
    except Exception as e:
        strE = format(e)
        if strE.__contains__('keys'):
            return jsonify('Ha ocurrido el siguiente error : El id del candidato y / o el id del partido no existen'), 400
        else:
            return jsonify('Ha ocurrido el siguiente error : ' + strE), 500