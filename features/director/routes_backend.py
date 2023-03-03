from flask import Blueprint, render_template, request, redirect
# import requests
from firebase_admin import db
from firebase import firebase
app = Blueprint('Director', __name__, url_prefix='/director')

bd = firebase.FirebaseApplication("https://treecko-c8c52-default-rtdb.firebaseio.com", None)

@app.get('/find')
def director_find():
    director = bd.get('/tic/director/', '')
    registro = []
    for director in director:
        registro.append(bd.get(f'/tic/director/{director}', '')) 
    print(registro)
    return render_template('find_director.html', entries=registro)

@app.route('/add', methods=['POST'])
def director_add():
    registro = {
        'nombre': request.form['inputNombre'],
        'apellidos': request.form['inputApellidos'],
        'correo': request.form['inputCorreo'],
        'usuario': request.form['inputUsername'],
        'contraseña': request.form['inputPassword'],
        'periodo': [{
            'inicio': request.form['inputPeriodo'],
            'final': request.form['inputPeriodof']
        }]
    }
    usuario= request.form['inputUsername']
    print(registro)
    resultado = bd.put(f'/tic/director', usuario ,registro)
    print(resultado)
    return redirect('/director/find')
    

@app.get('/update')
def director_update():
    bd.put('/tic/-NPK_tfzeVLDtju5qrBq', 'saludo', 'Hola cola')
    return 'se actualizo'
    
@app.get('/delete/<id>/')
def director_delete(id):
    print(id)
    bd.delete('/tic/director', id)
    return redirect('/director/find')
