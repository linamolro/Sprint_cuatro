from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from waitress import serve
import datetime
import requests
import re
import json

from flask_jwt_extended import create_access_token, verify_jwt_in_request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app=Flask(__name__)
cors = CORS(app)

#METODO LOGIN
app.config["JWT_SECRET_KEY"]="super-secret"
jwt = JWTManager(app)
@app.route("/login", methods=["POST"])
def create_token():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-security"]+'/usuarios/validar'
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        user = response.json()
        expires = datetime.timedelta(seconds=60 * 60*24)
        access_token = create_access_token(identity=user, expires_delta=expires)
        return jsonify({"token": access_token, "user_id": user["_id"]})
    else:
        return jsonify({"msg": "Bad username or password"}), 401

#IMPLEMENTACION MIDDLEWARE
@app.before_request
def before_request_callback():
    endPoint=limpiarURL(request.path)
    excludedRoutes=["/login"]
    if excludedRoutes.__contains__(request.path):
        pass
    elif verify_jwt_in_request():
        usuario = get_jwt_identity()
        if usuario["rol"]is not None:
            tienePermiso=validarPermiso(endPoint,request.method,usuario["rol"]["id"])
            if not tienePermiso:
                return jsonify({"message": "Permission denied"}), 401
        else:
            return jsonify({"message": "Permission denied"}), 401

def limpiarURL(url):
    partes = url.split("/")
    for laParte in partes:
        if re.search('\\d', laParte):
            url = url.replace(laParte, "?")
    return url

def validarPermiso(endPoint,metodo,idRol):
    url=dataConfig["url-backend-security"]+"/permisos-roles/validar-permiso/rol/"+str(idRol)
    tienePermiso=False
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body={
        "url":endPoint,
        "metodo":metodo
    }
    response = requests.get(url,json=body, headers=headers)
    try:
        data=response.json()
        if("id" in data):
            tienePermiso=True
    except:
        pass
    return tienePermiso

#METODO CONEXION CRUD REGISTRADURIA

#PARTIDOS
#GET
@app.route("/partidos",methods=['GET'])
def getPartido():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/partidos'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

#GET - UN PARTIDO
@app.route("/partidos/<string:id>",methods=['GET'])
def getUnPartido(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/partidos/'+ id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

#POST
@app.route("/partidos",methods=['POST'])
def crearPartido():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/partidos'
    response = requests.post(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)

#PUT
@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/partidos/'+id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

#DELETE
@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/partidos/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

#CANDIDATOS
#GET
@app.route("/candidatos",methods=['GET'])
def getCandidato():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/candidatos'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

#GET - UN CANDIDATO
@app.route("/candidatos/<string:id>",methods=['GET'])
def getUnCandidato(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/candidatos/'+ id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

#POST
@app.route("/candidatos/partido/<string:id_partido>",methods=['POST'])
def crearCandidato(id_partido):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/candidatos/partido/'+id_partido
    response = requests.post(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)

#PUT
@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/candidatos/'+id
    response = requests.put(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)

#DELETE
@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/candidatos/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

#MESAS
#GET
@app.route("/mesas",methods=['GET'])
def getMesa():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/mesas'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

#GET - UNA MESA
@app.route("/mesas/<string:id>",methods=['GET'])
def getUnaMesa(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/mesas/'+ id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

#POST
@app.route("/mesas",methods=['POST'])
def crearMesa():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/mesas'
    response = requests.post(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)

#PUT
@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/mesas/'+id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

#DELETE
@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/mesas/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

#RESULTADOS
#GET
@app.route("/resultados",methods=['GET'])
def getResultado():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/resultados'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

#GET - UN RESULTADO
@app.route("/resultados/<string:id>",methods=['GET'])
def getUnResultado(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/resultados/'+ id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

#POST
@app.route("/resultados/mesa/<string:id_mesa>/candidato/<string:id_candidato>",methods=['POST'])
def crearResultado(id_mesa,id_candidato):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/resultados/mesa/'+id_mesa+'/candidato/'+id_candidato
    response = requests.post(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)

#PUT
@app.route("/resultados/<string:id>",methods=['PUT'])
def modificarResultado(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/resultados/'+id
    response = requests.put(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)

#DELETE
@app.route("/resultados/<string:id>",methods=['DELETE'])
def eliminarResultado(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/resultados/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

#CONSULTAS
#Consulta resultados candidato
@app.route("/resultados/candidatos",methods=['GET'])
def getResultadoCandidato():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/resultados/candidatos'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

#Consulta resultados candidato por mesa
@app.route("/resultados/candidatos/<string:id>",methods=['GET'])
def getResultadoCandidatoPorMesa(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/resultados/candidatos/'+id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

#Consulta resultados por mesa
@app.route("/resultados/mesa",methods=['GET'])
def getResultadoMesa():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/resultados/mesa'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

#Consulta resultados partidos
@app.route("/resultados/partidos",methods=['GET'])
def getResultadoPartido():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/resultados/partidos'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

#Consulta resultados partidos por mesa 
@app.route("/resultados/partidos/<string:id>",methods=['GET'])
def getResultadoPartidoPorMesa(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/resultados/partidos/'+id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

#Consulta distribucion porcentual
@app.route("/resultados/distribucion",methods=['GET'])
def getResultadoDistribucion():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-registraduria"] + '/resultados/distribucion'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

#METODO CONEXION SERVIDOR
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data
if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])