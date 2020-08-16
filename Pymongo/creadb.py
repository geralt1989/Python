import pymongo
from pymongo import MongoClient


#eseguo la connessione con mongodb
client = MongoClient('localhost', 27017)

#creo un database chiamato testdb
db = client.testdb

# creo la collection persone
persone_coll = db.persone

persone_coll.create_index([("nome", pymongo.ASCENDING)])
persone_coll.create_index([("cognome", pymongo.ASCENDING)])
persone_coll.create_index([("computer", pymongo.ASCENDING)])

#creo un documento
p1 = {"nome": "raffaele", "cognome":  "immobile", "eta": 31,
        "computer": ["lenovo", "apple"]}

#inseriamo documento nella coll
persone_coll.insert_one(p1)

p2 = {"nome": "marco", "cognome":  "bianchi", "eta": 35,
        "computer": ["lenovo"]}
persone_coll.insert_one(p2)
