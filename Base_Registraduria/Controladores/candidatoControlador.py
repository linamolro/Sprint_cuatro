from Modelos.Candidato import Candidato
from Repositorios.repositorioCandidato import RepositorioCandidato
from Modelos.Partido import Partido
from Repositorios.repositorioPartido import RepositorioPartido

class CandidatoControlador():
  def __init__(self):
    self._repositorio_candidato = RepositorioCandidato()
    self._repositorio_partido = RepositorioPartido()
  
  #CRUD

  def listar_candidato(self):
    datos_candidato = self._repositorio_candidato.findAll()
    return datos_candidato

  def datos_un_candidato(self,id):
    datos_candidato = Candidato(self._repositorio_candidato.findById(id))
    return datos_candidato.__dict__

  def crear_candidato(self,datos_entrada,id_partido):
    _candidato = Candidato(datos_entrada)
    _partido = Partido(self._repositorio_partido.findById(id_partido))
    _candidato.partido = _partido
    return self._repositorio_candidato.save(_candidato)

  def actualizar_candidato(self,id,datos_entrada):
    _candidato_db = self._repositorio_candidato.findById(id)
    _candidato_obj = Candidato(_candidato_db)
    _candidato_obj.numero_candidato = datos_entrada["numero_candidato"]
    _candidato_obj.cedula = datos_entrada["cedula"]
    _candidato_obj.nombre = datos_entrada["nombre"]
    _candidato_obj.apellido = datos_entrada["apellido"]
    return self._repositorio_candidato.save(_candidato_obj)
    
  def eliminar_candidato(self,id):
    return self._repositorio_candidato.delete(id)