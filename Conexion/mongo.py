import pymongo

def collection_config(nombre):
    # Conectarse a un servidor de MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # Seleccionar una base de datos
    db = client["Noticias"]
    # Seleccionar una colección
    collection = db[nombre]
    return collection
