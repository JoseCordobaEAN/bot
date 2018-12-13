from pymongo import MongoClient
from pprint import pprint

cliente = MongoClient()

print(cliente)

base = cliente.test

print(base)

coleccion = base.test

print(coleccion)

elemento = coleccion.find({"name": "jose"})
for name in elemento:
    pprint(name)

