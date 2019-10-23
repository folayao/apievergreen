from flask import Flask, jsonify, request
from db.db import conex 

class tipoSensor():
    global cur
    cur = conex.cursor()

    def list():
        lista = []
        cur.execute("SELECT * FROM tipo_sensores")
        rows = cur.fetchall()
        colums = [i[0] for i in cur.description]

        for row in rows:
            #create a zip object from two list
            registo = zip(colums, row)
            #Create a  dictionary from zip object
            json = dict(registo)
            lista.append(json)
        conex.close
        return jsonify(lista)

    def create(body):
        #campos
        data = (
            body['fecha'],
            body['origen'],
            body['valor'],
            body['codigoSensor'],
            body ['observacion']
        )
        #sentencia SQL
        sql =  "INSERT INTO tipo_sensores (fecha, origen, valor, codigoSensor, observacion) VALUES(%s, %s, %s, %s, %s)"
        cur.execute(sql,data)
        conex.commit()
        return {'estado' : "insertado"}, 200
