from flask import Blueprint, render_template, request, json
# import requests
from firebase_admin import db
from firebase import firebase
app = Blueprint('Tutor', __name__, url_prefix='/tutor')

bd = firebase.FirebaseApplication("https://treecko-c8c52-default-rtdb.firebaseio.com", None)

@app.get('/find')
def tutor_find():
    tutores = bd.get('/tic/tutor/2023-A/DSM', '')
    registro = []
    for tutores in tutores:
        registro.append(bd.get(f'/tic/tutor/2023-A/DSM/{tutores}', '')) 
        
    # registro = json(registro)
    print(registro)
    return render_template('find_tutor.html', entries=registro)

@app.route('/add', methods=['POST'])
def tutor_add():
    registro = {
        'nombre': request.form['inputNombre'],
        'apellidos': request.form['inputApellidos'],
        'correo': request.form['inputCorreo'],
        'usuario': request.form['inputUsername'],
        'contraseña': request.form['inputPassword'],
        'grupo': request.form['inputGrupo']
    }
    carrera = request.form['inputCarrera']
    periodo = request.form['inputPeriodo']
    usuario = request.form['inputUsername']
    
    resultado = bd.put(f'/tic/tutor/{periodo}/{carrera}', usuario, registro)
    print(resultado)
    return render_template('find_tutor.html')
    

@app.get('/update')
def tutor_update():
    bd.put('/tic/-NPK_tfzeVLDtju5qrBq', 'saludo', 'Hola cola')
    return 'se actualizo'
    
@app.route('/delete/<id>/')
def tutor_delete(id):
    print(id)
    bd.delete('/tic/tutor/2023-A/DSM', id)
    return render_template('find_tutor.html')

