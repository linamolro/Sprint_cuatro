from Modelos.Mesa import Mesa
from Repositorios.repositorioMesa import RepositorioMesa

class MesaControlador():

  def __init__(self):
    self._repositorio_mesa = RepositorioMesa()

  def listar_mesa(self):
    datos_mesa = self._repositorio_mesa.findAll()
    return datos_mesa

  def datos_una_mesa(self,id):
    datos_mesa = Mesa(self._repositorio_mesa.findById(id))
    return datos_mesa.__dict__

  def crear_mesa(self,datos_entrada):
    _mesa = Mesa(datos_entrada)
    return self._repositorio_mesa.save(_mesa)

  def actualizar_mesa(self,id,datos_entrada):
    _mesa_db = self._repositorio_mesa.findById(id)
    _mesa_obj = Mesa(_mesa_db)
    _mesa_obj.numero_mesa = datos_entrada["numero_mesa"]
    _mesa_obj.numero_votantes = datos_entrada["numero_votantes"]
    return self._repositorio_mesa.save(_mesa_obj)
    
  def eliminar_mesa(self,id):
    return self._repositorio_mesa.delete(id)
  