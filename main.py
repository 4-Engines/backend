from unicodedata import name
from flask import Flask, jsonify, url_for,request
from requests import delete
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import mongoconn
app = Flask(__name__)
app.config['SECRET_KEY'] = 'wefiwuefhrgfhhyuewiokldapsodjfjaksdjkjekfjsd'


@app.route('/login',methods=['GET', 'POST'])
def login():
    msj='Bienvenido a la aplicacion'
    if request.method == 'POST':
        username = request.json['username']
        password = request.json['password']
        user = mongoconn.selectDatosUserName(username)
        for i in user:
            print(i)
            if check_password_hash(i['password'], password):
                return jsonify({'status':'ok','msj':'Bienvenido'},200)
            else:
                return jsonify({'status':'error','message':'Usuario o contraseña incorrectos'},401)
        return jsonify(user)
        
    return jsonify({'msj':msj})
@app.route('/create_user',methods=['GET', 'POST'])
def comandoUrl():
    if request.method == 'POST':
        username = request.json['username']
        password = request.json['password']
        email = request.json['email']
        name = request.json['name']
        lastname = request.json['lastname']
        phone = request.json['phone']
        rol=request.json['rol']

    
        post = {
            'username': username,
            'password': generate_password_hash(password),
            'email': email,
            'name': name,
            'lastname': lastname,
            'phone': phone,
            'rol':rol,
            'created_at': datetime.utcnow()
        }
        insertPost = mongoconn.insertDatos(post)
        
        return jsonify({'status':'ok','msj':'Usuario creado'},200)
    return jsonify({'status':'error','msj':'No se pudo crear el usuario'} ,401)
@app.route('/update_user',methods=[ 'PUT'])
def updateUser():
    if request.method == 'PUT':
        id = request.json['id']
        username = request.json['username']
        password = request.json['password']
        email = request.json['email']
        name = request.json['name']
        lastname = request.json['lastname']
        phone = request.json['phone']
        rol=request.json['rol']
        post = {
            'username': username,
            'password': generate_password_hash(password),
            'email': email,
            'name': name,
            'lastname': lastname,
            'phone': phone,
            'rol':rol,
            'created_at': datetime.utcnow()
        }
        updatePost = mongoconn.selectDatosUserName(username)
        for i in updatePost:
            if i['_id']==id:
                updatePost = mongoconn.updateDatos(id,post)
                return jsonify({'status':'ok','msj':'Usuario actualizado'},200)
            else:
                return jsonify({'status':'error' ,'msj':'Usuario no existe'} ,401)
    return jsonify({'status':'error','msj':'No se pudo actualizar el usuario'} ,401)
@app.route('/delete_user',methods=['GET', 'POST'])
def deleteUser():
    if request.method == 'POST':
        id = request.json['id']
        msj=mongoconn.deleteDatos(id)
    return jsonify(msj=msj)
@app.route('/newcar',methods=['GET', 'POST'])
def newcar():
    if request.method == 'POST':
        cardId = request.json['cardId']
        marca = request.json['marca']
        model = request.json['model']
        year = request.json['year']
        id_user = request.json['id_user']
        post = {
            'cardId': cardId,
            'marca': marca,
            'model': model,
            'year': year,
            'id_user': id_user,
            'created_at': datetime.utcnow()
        }
        try:
            insertPost = mongoconn.insertCar(post)
            return jsonify({'status':'ok','msj':'Auto creado'},200)
        except:
            return jsonify({'status':'error','msj':'No se pudo Cargar'},401)
    return jsonify({'msj':'No se pudo crear el auto', 'status':'error'},401)
@app.route('/updatecar',methods=['PUT'])
def updatecar():
    if request.method == 'POST':
        id = request.json['id']
        carId = request.json['carId']
        marca = request.json['marca']
        model = request.json['model']
        year = request.json['year']
        id_user = request.json['id_user']
        post = {
            'cardId': carId,
            'marca': marca,
            'model': model,
            'year': year,
            'id_user': id_user,
            'created_at': datetime.utcnow()
        }
        try:
            updatePost = mongoconn.updateCar(id,post)
            return jsonify({'msj':'Auto actualizado'},200)
        except:
            return jsonify({'status':'error','msj':'No se pudo actualizar'},401)
@app.route('/deletecar',methods=['GET', 'POST'])
def deletecar():
    if request.method == 'POST':
        cardId = request.json['cardId']
        try:
            deletePost = mongoconn.deleteCar(cardId)
            return jsonify({'status':'ok','msj':'Auto eliminado'},200)
        except:
            return jsonify({'status':'error','msj':'No se pudo eliminar'},401)
@app.route('/altataller',methods=['GET', 'POST'])
def admin():
    msj="Admin"
    
    return jsonify(msj=msj)

@app.route('/updatetaller',methods=['GET', 'POST'])
def exito():
    msj="exito"
    
    return jsonify(msj=msj)
    
if __name__ == '__main__':
    app.run(port=3000,debug=True)
