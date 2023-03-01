from flask import Blueprint, render_template, request
# import requests
from firebase_admin import db
from firebase import firebase
app = Blueprint('Director', __name__, url_prefix='/director')

bd = firebase.FirebaseApplication("https://treecko-c8c52-default-rtdb.firebaseio.com", None)

@app.get('/find')
def director_find():
    leer = bd.get('/tic/director', '')
    return leer

@app.route('/add', methods=['POST'])
def director_add():
    registro = {
        'nombre': request.form['inputNombre'],
        'apellidos': request.form['inputApellidos'],
        'correo': request.form['inputCorreo'],
        'usuario': request.form['inputUsername'],
        'contraseña': request.form['inputPassword'],
        'grupo': request.form['inputGrupo']
    }
    periodo = request.form['inputPeriodo']
    
    resultado = bd.post(f'/tic/director/{periodo}', registro)
    print(resultado)
    return render_template('find_director.html')
    

@app.get('/update')
def director_update():
    bd.put('/tic/-NPK_tfzeVLDtju5qrBq', 'saludo', 'Hola cola')
    return 'se actualizo'
    
@app.get('/delete')
def director_delete():
    bd.delete('/tic', '-NPK_tfzeVLDtju5qrBq')
    return 'se elimino el registro'
