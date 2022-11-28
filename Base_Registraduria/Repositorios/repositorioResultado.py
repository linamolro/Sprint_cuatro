from Modelos.Resultado import Resultado
from Repositorios.interfazRepositorio import InterfaceRepositorio
from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[Resultado]):

    #Listado candidatos general
    def getListadoCandidatoGeneral(self):
        query_uno = {
            "$group":{
              "_id": "$candidato",
              "total": {
                "$sum": "$cantidad_votos"
                }
            }
        }
        query_dos = {
            "$lookup":{
                "from": "candidato",
                "localField": "_id.$id",
                "foreignField": "_id",
                "as": "candidato"  
            }
        }
        query_tres = {
            "$set":{
                "candidato":{"$first":"$candidato"}
            }
        }
        query_cuatro = {
            "$addFields":{
                "partido_id":"$candidato.partido.$id"
            }
        }
        query_cinco = {
            "$lookup":{
                "from": "partido",
                "localField": "partido_id",
                "foreignField": "_id",
                "as": "partido"  
            }            
        }
        query_seis = {
            "$set":{
                "partido":{"$first":"$partido"}
            }
        }
        query_siete = {
            "$sort":{
                "total": -1
            }
        }
        pipeline = [query_uno,query_dos,query_tres,query_cuatro,query_cinco,query_seis,query_siete]
        return self.queryAggregation(pipeline)    

    #Listado candidatos filtrado por mesa
    def getListadoCandidatoPorMesa(self, id_mesa):
        query_uno = {
            "$match":{"mesa.$id": ObjectId(id_mesa)}
        }
        query_dos = {
            "$group":{
              "_id": "$candidato",
              "total": {
                "$sum": "$cantidad_votos"
                }
            }
        }
        query_tres = {
            "$lookup":{
                "from": "candidato",
                "localField": "_id.$id",
                "foreignField": "_id",
                "as": "candidato"  
            }
        }
        query_cuatro = {
            "$set":{
                "candidato":{"$first":"$candidato"}
            }
        }
        query_cinco = {
            "$addFields":{
                "partido_id":"$candidato.partido.$id"
            }
        }
        query_seis = {
            "$lookup":{
                "from": "partido",
                "localField": "partido_id",
                "foreignField": "_id",
                "as": "partido"  
            }            
        }
        query_siete = {
            "$set":{
                "partido":{"$first":"$partido"}
            }
        }
        query_ocho = {
            "$sort":{
                "total": -1
            }
        }
        pipeline = [query_uno,query_dos,query_tres,query_cuatro,query_cinco,query_seis,query_siete,query_ocho]
        return self.queryAggregation(pipeline)
    
    #Listado votos por mesa
    def getListadoVotosPorMesa(self):
        query_uno = {
            "$group":{
              "_id": "$mesa",
              "total": {
                "$sum": "$cantidad_votos"
                }
            }
        }
        query_dos = {
            "$sort":{
                "total": 1
            }
        }
        pipeline = [query_uno,query_dos]
        return self.queryAggregation(pipeline)
    
    #Listado partidos general
    def getListadoPartido(self):
        query_uno = {
            "$lookup":{
                "from": "candidato",
                "localField": "candidato.$id",
                "foreignField": "_id",
                "as": "candidato"  
            }
        }
        query_dos = {
            "$set":{
                "candidato":{"$first":"$candidato"}
            }
        }
        query_tres = {
            "$group":{
              "_id": "$candidato.partido.$id",
              "total": {
                "$sum": "$cantidad_votos"
                },
                "partido": {"$first":"$candidato.partido"}
            }
        }
        query_cuatro = {
            "$sort":{
                "total": -1
            }
        }
        pipeline = [query_uno,query_dos,query_tres,query_cuatro]
        return self.queryAggregation(pipeline)    

    #Listado partidos por mesa
    def getListadoPartidoEnMesa(self,id_mesa):
        query_uno = {
            "$match":{"mesa.$id": ObjectId(id_mesa)}
        }
        query_dos = {
            "$lookup":{
                "from": "candidato",
                "localField": "candidato.$id",
                "foreignField": "_id",
                "as": "candidato"  
            }
        }
        query_tres = {
            "$set":{
                "candidato":{"$first":"$candidato"}
            }
        }
        query_cuatro = {
            "$group":{
              "_id": "$candidato.partido.$id",
              "total": {
                "$sum": "$cantidad_votos"
                },
                "partido": {"$first":"$candidato.partido"}
            }
        }
        query_cinco = {
            "$sort":{
                "total": -1
            }
        }
        pipeline = [query_uno,query_dos,query_tres,query_cuatro,query_cinco]
        return self.queryAggregation(pipeline)    
    
    #Distribucion porcentual
    def getDistribucionPorcentual(self):
        query_uno = {
            "$group":{
              "_id": "$candidato",
              "total": {
                "$sum": "$cantidad_votos"
                }
            }            
        }
        query_dos = {
            "$lookup":{
                "from": "candidato",
                "localField": "_id.$id",
                "foreignField": "_id",
                "as": "candidato"  
            }
        }
        query_tres = {
            "$set":{
                "candidato":{"$first":"$candidato"}
            }
        }
        query_cuatro = {
            "$lookup":{
                "from": "partido",
                "localField": "candidato.partido.$id",
                "foreignField": "_id",
                "as": "partido"  
            }            
        }
        query_cinco = {
            "$set":{
                "partido":{"$first":"$partido"}
            }
        }
        query_seis = {
            "$sort":{
                "total": -1
            }
        }    
        query_siete = {
            "$limit":15
        }    
        query_ocho = {
            "$group":{
              "_id": "$partido",
              "total_partido": {
                "$count": {}
                }
            }            
        }
        query_nueve = {
            "$addFields":{
                "distribucion":{
                    "$multiply":[
                        {
                            "$divide":["$total_partido",15]
                        }, 100
                    ]
                }
            }
        }      
        pipeline = [query_uno,query_dos,query_tres,query_cuatro,query_cinco,query_seis,query_siete,query_ocho,query_nueve]
        return self.queryAggregation(pipeline)