from flask import request
from flask import json
from flask.json import jsonify
from flask.wrappers import Response
from app import app,auth
from werkzeug.security import generate_password_hash, check_password_hash

users = {
    "admin": generate_password_hash("123"),
    "susan": generate_password_hash("bye")
}

@auth.verify_password
def verify_password(username, password):
    print("----------------------------------")
    if username in users and check_password_hash(users.get(username), password):
        return username






@app.route('/endpoint1', methods=['POST'])
@auth.login_required
def endpoint1():
    data= request.json
    respuestaFinal ={}
    if data is not None:
        
        status=200
        if "sin clasificar" in data:
            array= data['sin clasificar']
            try:
                numbers_clasificados=clasficarNumeros(array)
                respuestaFinal['sin clasificar']=array
                respuestaFinal['clasificado']=numbers_clasificados
            except Exception as ex:
                respuestaFinal['error']=str(ex)
                status=400
        else:
            respuestaFinal['error']="KEY NO FOUND"
            status=400
    else:
            respuestaFinal['error']="ENVIAR INFORMACIÓN"
            status=400
        
    return jsonify(respuestaFinal), status


def clasficarNumeros(numbers):
    repetidos=[]
    sinRepetir =[]

    for number in numbers:
        if number not in sinRepetir:
            sinRepetir.append(number)
        else:
            repetidos.append(number)
    
    ordenados=list(sorted(sinRepetir))

    ordenados.extend(repetidos)

    return ordenados


@app.route('/endpoint2',methods=['POST'])
@auth.login_required
def endpoint2():
    data= request.json
    respuestaFinal ={}
    status=200
    if data is not None:
        if "Mes" in data and "Ventas" in data and "Gastos" in data:
            status=200
            if len(data['Mes']) == len(data['Ventas'])== len(data['Gastos']):
                if all(type(i) == int or type(i)==float for i in data['Ventas']) and all(type(i) == int or type(i)==float for i in data['Gastos']):
                    informacion=[]
                    for i in range(len(data["Mes"])):
                        try:
                            informacion.append(Balance(data['Mes'][i],data['Ventas'][i],data['Gastos'][i]))
                        except Exception as ex:
                            respuestaFinal['error']=str(ex)
                            return respuestaFinal,400
                    respuestaFinal=json.dumps([z.__dict__ for z in informacion])
                else:
                    respuestaFinal['error']='Alguno de los valores ingresados en VENTAS o GASTOS no corresponden a un formato numérico'
                    
            else:
                respuestaFinal['error']="Información Incorrecta"
                
        else:
            status=404
            respuestaFinal['error']="Información Incorrecta"
        
    return respuestaFinal

class Balance():
    Mes=''
    Gastos=0
    Ventas=0
    Balance=0
    def __init__(self,mes,ventas,gastos):
        self.Mes=mes
        self.Ventas=ventas
        self.Gastos=gastos
        self.Balance=ventas-gastos











# @app.route('users/<string:id>', methods=[ 'GET' ])
# def updateInformacion():



