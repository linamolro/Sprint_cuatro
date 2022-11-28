from re import U
from flask import request
from flask import Flask
from waitress import serve
from flask import jsonify
import json

from Controladores.candidatoControlador import CandidatoControlador
from Controladores.partidoControlador import PartidoControlador
from Controladores.mesaControlador import MesaControlador
from Controladores.resultadoControlador import ControladorResultado

mi_aplicacion = Flask(__name__)
_controlador_candidato = CandidatoControlador()
_controlador_partido = PartidoControlador()
_controlador_mesa = MesaControlador()
_controlador_resultado = ControladorResultado()

#PARTIDO - CRUD

#get - listar partidos
@mi_aplicacion.route('/partidos', methods = ['GET'])
def listar_partidos():
    datos_salida = _controlador_partido.listar_partido()
    return jsonify(datos_salida)

#get - un partido
@mi_aplicacion.route('/partidos/<string:id>', methods = ['GET'])
def traer_partido(id):
    datos_salida = _controlador_partido.datos_un_partido(id)
    return jsonify(datos_salida)

#post - crear partidos
@mi_aplicacion.route('/partidos', methods = ['POST'])
def crear_partidos():
    datos_entrada = request.get_json()
    datos_salida = _controlador_partido.crear_partido(datos_entrada)
    return jsonify(datos_salida)

#put - actualizar partidos
@mi_aplicacion.route('/partidos/<string:id>', methods = ['PUT'])
def modificar_partidos(id):
    datos_entrada = request.get_json()
    datos_salida = _controlador_partido.actualizar_partido(id,datos_entrada)
    return jsonify(datos_salida)

#delete - eliminar partidos
@mi_aplicacion.route('/partidos/<string:id>', methods = ['DELETE'])
def eliminar_partidos(id):
    datos_salida = _controlador_partido.eliminar_partido(id)
    return jsonify(datos_salida)

#CANDIDATOS - CRUD

#get - listar candidatos
@mi_aplicacion.route('/candidatos', methods = ['GET'])
def listar_candidatos():
    datos_salida = _controlador_candidato.listar_candidato()
    return jsonify(datos_salida)

#get - un candidato
@mi_aplicacion.route('/candidatos/<string:id>', methods = ['GET'])
def traer_candidato(id):
    datos_salida = _controlador_candidato.datos_un_candidato(id)
    return jsonify(datos_salida)

#post - crear candidatos
@mi_aplicacion.route('/candidatos/partido/<string:id_partido>', methods = ['POST'])
def crear_candidatos(id_partido):
    datos_entrada = request.get_json()
    datos_salida = _controlador_candidato.crear_candidato(datos_entrada,id_partido)
    return jsonify(datos_salida)

#put - actualizar candidatos
@mi_aplicacion.route('/candidatos/<string:id>', methods = ['PUT'])
def modificar_candidatos(id):
    datos_entrada = request.get_json()
    datos_salida = _controlador_candidato.actualizar_candidato(id,datos_entrada)
    return jsonify(datos_salida)

#delete - eliminar candidatos
@mi_aplicacion.route('/candidatos/<string:id>', methods = ['DELETE'])
def eliminar_candidatos(id):
    datos_salida = _controlador_candidato.eliminar_candidato(id)
    return jsonify(datos_salida)

#MESA - CRUD

#get - listar mesas
@mi_aplicacion.route('/mesas', methods = ['GET'])
def listar_mesas():
    datos_salida = _controlador_mesa.listar_mesa()
    return jsonify(datos_salida)

#get - una mesa
@mi_aplicacion.route('/mesas/<string:id>', methods = ['GET'])
def traer_mesa(id):
    datos_salida = _controlador_mesa.datos_una_mesa(id)
    return jsonify(datos_salida)

#post - crear mesas
@mi_aplicacion.route('/mesas', methods = ['POST'])
def crear_mesas():
    datos_entrada = request.get_json()
    datos_salida = _controlador_mesa.crear_mesa(datos_entrada)
    return jsonify(datos_salida)

#put - actualizar mesas
@mi_aplicacion.route('/mesas/<string:id>', methods = ['PUT'])
def modificar_mesas(id):
    datos_entrada = request.get_json()
    datos_salida = _controlador_mesa.actualizar_mesa(id,datos_entrada)
    return jsonify(datos_salida)

#delete - eliminar mesas
@mi_aplicacion.route('/mesas/<string:id>', methods = ['DELETE'])
def eliminar_mesas(id):
    datos_salida = _controlador_mesa.eliminar_mesa(id)
    return jsonify(datos_salida)

#RESULTADOS - CRUD

#get - listar resultados
@mi_aplicacion.route('/resultados', methods = ['GET'])
def listar_resultados():
    datos_salida = _controlador_resultado.listar_resultado()
    return jsonify(datos_salida)

#get - un resultado
@mi_aplicacion.route('/resultados/<string:id>', methods = ['GET'])
def traer_resultado(id):
    datos_salida = _controlador_resultado.datos_un_resultado(id)
    return jsonify(datos_salida)

#post - crear resultados
@mi_aplicacion.route('/resultados/mesa/<string:id_mesa>/candidato/<string:id_candidato>', methods = ['POST'])
def crear_resultados(id_mesa,id_candidato):
    datos_entrada = request.get_json()
    datos_salida = _controlador_resultado.crear_resultado(datos_entrada,id_mesa,id_candidato)
    return jsonify(datos_salida)

#put - actualizar resultados
@mi_aplicacion.route('/resultados/<string:id>', methods = ['PUT'])
def modificar_resultados(id):
    datos_entrada = request.get_json()
    datos_salida = _controlador_resultado.actualizar_resultado(id,datos_entrada)
    return jsonify(datos_salida)

#delete - eliminar resultados
@mi_aplicacion.route('/resultados/<string:id>', methods = ['DELETE'])
def eliminar_resultados(id):
    datos_salida = _controlador_resultado.eliminar_resultado(id)
    return jsonify(datos_salida)

#CONSULTAS

#Consultar resultado candidatos general
@mi_aplicacion.route('/resultados/candidatos',methods=['GET'])
def resultadosPorCandidato():
    datos_salida = _controlador_resultado.listarResultadoPorCandidato()
    return jsonify(datos_salida)

#Consultar resultado candidatos por mesa
@mi_aplicacion.route('/resultados/candidatos/<string:id_mesa>',methods=['GET'])
def resultadosPorCandidatoEnMesa(id_mesa):
    datos_salida = _controlador_resultado.listarResultadoPorCandidatoEnMesa(id_mesa)
    return jsonify(datos_salida)

#Consultar resultados por mesa
@mi_aplicacion.route('/resultados/mesa',methods=['GET'])
def resultadosPorEnMesa():
    datos_salida = _controlador_resultado.listarResultadoEnMesa()
    return jsonify(datos_salida)

#Consultar resultado partidos general
@mi_aplicacion.route('/resultados/partidos',methods=['GET'])
def resultadosPorPartido():
    datos_salida = _controlador_resultado.listarResultadoPorPartido()
    return jsonify(datos_salida)

#Consultar resultado partidos por mesa
@mi_aplicacion.route('/resultados/partidos/<string:id_mesa>',methods=['GET'])
def resultadosPorPartidoEnMesa(id_mesa):
    datos_salida = _controlador_resultado.listarResultadoPorPatidoEnMesa(id_mesa)
    return jsonify(datos_salida)

#Consultar distribución porcentual
@mi_aplicacion.route('/resultados/distribucion',methods=['GET'])
def resultadosDistribucion():
    datos_salida = _controlador_resultado.distribucionPartidos()
    return jsonify(datos_salida)

#SERVIDOR

def cargar_configuracion():
    with open("config.json") as archivo:
        datos_configuracion = json.load(archivo)
    return datos_configuracion

if __name__ == '__main__':
    datos_configuracion = cargar_configuracion()
    print("Servidor ejecutandose")
    serve(mi_aplicacion, host=datos_configuracion["servidor"], port=datos_configuracion["puerto"])