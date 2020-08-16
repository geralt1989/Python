import pymongo
from pymongo import MongoClient


#eseguo la connessione con mongodb
client = MongoClient('localhost', 27017)

#creo un database chiamato testdb
db = client.testdb

# creo la collection persone
persone_coll = db.persone

#trova il primo elemento
p = persone_coll.find_one()
print(p)

#trova tutti
print("***")
persone = persone_coll.find({"computer": "lenovo"})
for persona in persone:
    print(persona)

#modifica un parametro
print("---")
res = persone_coll.update_one({"nome": "marco"}, {"$set": {"eta": 50}})
p = persone_coll.find_one({"nome": "marco"})
print(p)

#usa filtro
print("_______")
persona = persone_coll.find_one({"nome": {"$gt": "marco"}})
print(persona)





