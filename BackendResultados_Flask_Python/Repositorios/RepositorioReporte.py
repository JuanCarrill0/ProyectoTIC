from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado
from bson.son import SON
from bson import ObjectId

class RepositorioReporte(InterfaceRepositorio[Resultado]):

    def ListadoVotosEnMesas(self):
        query1 = {
            "$lookup": {"from": "mesa", "localField": "mesa.$id", "foreignField": "_id", "as": "resultado"}
        }
        query2 = {
            "$unwind": "$resultado"
        }
        query3 = {
            "$group": {
                "_id": {"id": "$resultado._id", "numero": "$resultado.numero"},
                "participacion": {
                    "$sum": "$cant_votos"
                },
            }
        }
        query4 = {
            "$sort": {"participacion": 1}
        }
        pipeline = [query1,query2,query3,query4]
        return self.queryAggregation(pipeline)

    def ListadoVotosCandidatos(self):
        query1 = {
            "$lookup": {"from": "candidato", "localField": "candidato.$id", "foreignField": "_id", "as": "resultado"}
        }
        query2 = {
            "$unwind": "$resultado"
        }
        query3 = {
            "$lookup": {"from": "partido", "localField": "resultado.partido.$id", "foreignField": "_id",
                        "as": "resultado2"}
        }

        query4 = {
            "$unwind": "$resultado2"
        }
        query5 = {
            "$group": {
                "_id": {
                    "id": "$resultado._id",
                    "nombre": "$resultado.nombre",
                    "apellido": "$resultado.apellido",
                    "partido": "$resultado2.nombre"
                },
                "votacion": {
                    "$sum": "$cant_votos"
                },

            }
        }
        query6 = {
            "$sort": {"votacion": -1}
        }
        pipeline = [query1, query2, query3, query4, query5, query6]
        return self.queryAggregation(pipeline)

    def ListadoVotosCandidato(self, id_mesa):
        query = {
            "$match": {"mesa.$id": ObjectId(id_mesa)}
        }
        query1 = {
            "$lookup": {"from": "candidato", "localField": "candidato.$id", "foreignField": "_id", "as": "resultado"}
        }
        query2 = {
            "$unwind": "$resultado"
        }
        query3 = {
            "$lookup": {"from": "partido", "localField": "resultado.partido.$id", "foreignField": "_id",
                        "as": "resultado2"}
        }

        query4 = {
            "$unwind": "$resultado2"
        }
        query5 = {
            "$group": {
                "_id": {
                    "id": "$resultado._id",
                    "nombre": "$resultado.nombre",
                    "apellido": "$resultado.apellido",
                    "partido": "$resultado2.nombre"
                },
                "votacion": {
                    "$sum": "$cant_votos"
                },

            }
        }
        query6 = {
            "$sort": {"votacion": -1}
        }
        pipeline = [query, query1, query2, query3, query4, query5, query6]
        return self.queryAggregation(pipeline)
    
    def ListadoPartidosVotos(self,id_mesa=""):
        query1={
            "$lookup":{"from":"candidato","localField":"candidato.$id","foreignField":"_id","as":"resultado"}
        }
        query2={
           "$unwind":"$resultado"    
        }
        query4={
            "$lookup":{"from":"partido","localField":"resultado.partido.$id","foreignField":"_id","as":"resultado2"}
        }
        query5={
           "$unwind":"$resultado2"    
        }
        query7={
                "$group":{
                "_id": {"id":"$resultado2._id", "nombre":"$resultado2.nombre"},
                "votacion":{
                    "$sum":"$cant_votos"
                },
                

            }
        }
        query8={
            "$sort": {"votacion": -1}
            }

        if (id_mesa != ""):
            query6 ={
            "$match":{"mesa.$id": ObjectId(id_mesa)}
            }
        
            pipeline = [query1,query2,query4,query5,query6,query7,query8]
            return self.queryAggregation(pipeline)
        else :
            pipeline = [query1,query2,query4,query5,query7,query8]
        
        return self.queryAggregation(pipeline)

    def ListadoCongreso(self):
        query1 = {
            "$lookup": {"from": "candidato", "localField": "candidato.$id", "foreignField": "_id", "as": "resultado"}
        }
        query2 = {
            "$unwind": "$resultado"
        }
        query3 = {
            "$lookup": {"from": "partido", "localField": "resultado.partido.$id", "foreignField": "_id",
                        "as": "resultado2"}
        }

        query4 = {
            "$unwind": "$resultado2"
        }
        query5 = {
            "$group": {
                "_id": {
                    "id": "$resultado._id",
                    "partido": "$resultado2.nombre",
                },
                "votacion": {
                    "$sum": "$cant_votos"
                },
            }
        }
        query6 = {
            "$sort": {"votacion": -1}
        }
        query7 = {
            "$limit": 3
        }
        query8 = {
            "$group": {
                "_id": "$_id.partido",
                "cant_senadores": {"$sum": 1},
            },
        }
        pipeline = [query1, query2, query3, query4, query5, query6, query7, query8]
        return self.queryAggregation(pipeline)