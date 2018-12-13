from pymongo import MongoClient

cliente = MongoClient()
base = cliente.preguntas
coleccion = base.preguntas

while True:
    entrada = input('Ingrese su pregunta o s para salir ')
    if entrada == 's':
        break
    respuesta = coleccion.find_one({'pregunta':entrada})
    if respuesta:
        print(respuesta['respuesta'])
    else:
        respuesta = input('Que debo aprender? ')
        coleccion.insert({'pregunta': entrada,
                          'respuesta': respuesta}
                         )