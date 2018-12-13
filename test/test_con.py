from pymongo import MongoClient
from pprint import pprint
from random import randint

cliente = MongoClient()

print(cliente)

base = cliente.test

print(base)

coleccion = base.test

print(coleccion)



elemento = coleccion.find()
seleccionado = randint(0, elemento.count()-1)
print(list(elemento)[seleccionado])


