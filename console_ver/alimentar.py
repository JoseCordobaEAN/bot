from pymongo import MongoClient

cliente = MongoClient()
base = cliente.preguntas
coleccion = base.preguntas

while True:
    entrada = input('Ingrese su pregunta o s para salir ')
    if entrada.lower() == 's':
        break
    respuesta = input('Que debo aprender? ')
    coleccion.insert({'pregunta': entrada,
                      'respuesta': respuesta}
                     )