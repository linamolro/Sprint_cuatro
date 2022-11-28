from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.repositorioResultado import RepositorioResultado
from Repositorios.repositorioMesa import RepositorioMesa
from Repositorios.repositorioCandidato import RepositorioCandidato

class ControladorResultado():

    def __init__(self):
        self._repositorio_resultado = RepositorioResultado()
        self._repositorio_mesa = RepositorioMesa()
        self._repositorio_candidato = RepositorioCandidato()
    
    def listar_resultado(self):
        datos_resultado = self._repositorio_resultado.findAll()
        return datos_resultado
    
    def datos_un_resultado(self,id):
        datos_resultado = Resultado(self._repositorio_resultado.findById(id))
        return datos_resultado.__dict__
    
    def crear_resultado(self,datos_entrada,id_mesa,id_candidato):
        _resultado = Resultado(datos_entrada)
        _mesa = Mesa(self._repositorio_mesa.findById(id_mesa))
        _candidato = Candidato(self._repositorio_candidato.findById(id_candidato))
        _resultado.mesa = _mesa
        _resultado.candidato = _candidato
        return self._repositorio_resultado.save(_resultado)
    
    def actualizar_resultado(self,id,datos_entrada):
        _resultado_db = Resultado(self._repositorio_resultado.findById(id))
        _resultado_db.cantidad_votos = datos_entrada["cantidad_votos"]
        return self._repositorio_resultado.save(_resultado_db)

    def eliminar_resultado(self,id):
        return self._repositorio_resultado.delete(id)
    
    #CONSULTAS

    #Obtener votos candidatos general
    def listarResultadoPorCandidato(self):
        return self._repositorio_resultado.getListadoCandidatoGeneral()

    #Obtener votos candidatos por mesa
    def listarResultadoPorCandidatoEnMesa(self,id_mesa):
        return self._repositorio_resultado.getListadoCandidatoPorMesa(id_mesa)
    
    #Obtenes votos por mesa
    def listarResultadoEnMesa(self):
        return self._repositorio_resultado.getListadoVotosPorMesa()
    
    #Obtener votos partidos general
    def listarResultadoPorPartido(self):
        return self._repositorio_resultado.getListadoPartido()  

    #Obtener votos partidos por mesa
    def listarResultadoPorPatidoEnMesa(self,id_mesa):
        return self._repositorio_resultado.getListadoPartidoEnMesa(id_mesa)  
    
    #Obtener Distribucion Porcentual
    def distribucionPartidos(self):
        return self._repositorio_resultado.getDistribucionPorcentual()
