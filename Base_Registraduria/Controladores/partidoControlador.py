from Modelos.Partido import Partido
from Repositorios.repositorioPartido import RepositorioPartido
class PartidoControlador():
  def __init__(self):
    self._repositorio_partido = RepositorioPartido()

  def listar_partido(self):
    datos_partido = self._repositorio_partido.findAll()
    return datos_partido
  
  def datos_un_partido(self,id):
    datos_partido = Partido(self._repositorio_partido.findById(id))
    return datos_partido.__dict__

  def crear_partido(self,datos_entrada):
    _partido = Partido(datos_entrada)
    return self._repositorio_partido.save(_partido)

  def actualizar_partido(self,id,datos_entrada):
    _partido_db = self._repositorio_partido.findById(id)
    _partido_obj = Partido(_partido_db)
    _partido_obj.nombre_partido = datos_entrada["nombre_partido"]
    _partido_obj.lema = datos_entrada["lema"]
    return self._repositorio_partido.save(_partido_obj)
    
  def eliminar_partido(self,id):
    return self._repositorio_partido.delete(id)
