from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
import pymongo
import certifi
from waitress import serve
from Rutas.Partido import partido
from Rutas.Candidato import candidato
from Rutas.Mesa import mesa
from Rutas.Resultado import resultado
from Rutas.Reporte import reporte

app=Flask(__name__)
cors = CORS(app)

app.register_blueprint(partido)
app.register_blueprint(candidato)
app.register_blueprint(mesa)
app.register_blueprint(resultado)
app.register_blueprint(reporte)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
    #app.run(debug=True)
