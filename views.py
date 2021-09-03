from flask import request
from flask import json
from flask.json import jsonify
from werkzeug.sansio.response import Response
from app import app,db
from models import *


@app.route('/prueba', methods=['POST'])
def prueba():
    data= request.json
    respuestaFinal ={}
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











# @app.route('users/<string:id>', methods=[ 'GET' ])
# def updateInformacion():



