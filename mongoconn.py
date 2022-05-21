import pymongo
import bsonjs
from bson.raw_bson import RawBSONDocument
from bson.json_util import loads
from bson.json_util import dumps
# <-------------------------------------------------------- CONNECTION
from urllib.parse import quote_plus
username = quote_plus('desarrollo')
password = quote_plus('9i4AKtrGBCZZ9gOL')
cluster = 'cluster0'
authSource = 'authSource'
authMechanism = 'authMechanism'
uri = "mongodb+srv://desarrollo:"+password+"@"+cluster+".lgbmw.mongodb.net/?retryWrites=true&w=majority"

conn = pymongo.MongoClient(uri)

# create db
db = conn.fourengine

# create collection users if not exists
collection = db.users
collectionCars = db.cars

# <-------------------------------------------------------- INSERT 
# Funcion para insertar datos users
def insertDatos(post) :
	insertPost = collection.insert_one(post)
	return insertPost
	
# <-------------------------------------------------------- UPDATE
# Funcion para actualizar datos
def updateDatos(id,post):
	updatePost = collection.update({"username":id},post)
	return updatePost
# <-------------------------------------------------------- DELETE
# Funcion para eliminar datos
def deleteDatos(id):
	deletePost = collection.remove({"_id":ObjectId(id)})
	return deletePost
# <-------------------------------------------------------- SELECT
# Funcion para seleccionar datos
def selectDatos(id):
	selectPost = collection.find_one({"_id":ObjectId(id)})
	return selectPost
# <-------------------------------------------------------- SELECT username
# Funcion para seleccionar datos por nombre
def selectDatosUserName(username):
	selectPost = list(collection.find({"username":username}))
	
	 
	return selectPost
# <-------------------------------------------------------- INSERT car
def insertCar(post) :
	insertPost = collectionCars.insert_one(post)
	return insertPost
# <-------------------------------------------------------- SELECT patente
# Funcion para seleccionar datos por patente
def selectDatosPatente(patente):
	selectPost = collectionCars.find({"patente":patente})
	return selectPost
# <-------------------------------------------------------- Delete car
def deleteCar(id):
	deletePost = collectionCars.remove({"_id":ObjectId(id)})
	return deletePost
# <-------------------------------------------------------- Update car
def updateCar(id,post):
	updatePost = collectionCars.update({"_id":ObjectId(id)},post)
	return updatePost
# <-------------------------------------------------------- SELECT ALL
# Funcion para seleccionar todos los datos
def selectAllDatos():
	selectAllPost = collection.find()
	return selectAllPost
