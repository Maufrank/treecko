from flask import Blueprint, render_template, request, json, redirect
#import request
# from firebase_admin import bd
from firebase import firebase
app = Blueprint('Alumno', __name__, url_prefix='/alumno')

bd = firebase.FirebaseApplication("https://treecko-c8c52-default-rtdb.firebaseio.com", None)

@app.get('/find')
def alumno_find():
    alumno = bd.get('/tic/alumno', '')
    registro = []
    for alumno in alumno:
        registro.append(bd.get(f'/tic/alumno/{alumno}', '')) 
    print(registro)
    return render_template('find_alumno.html', entries=registro)

@app.route("/register", methods=['POST'])
def alumno():
    registro = {
        "nombre": request.form['inputNombre'],
        "apellidos": request.form['inputApellidos'],
        "correo": request.form['inputCorreo'],
        "grupo": request.form['inputGrupo'],
        "Contraseña": request.form['inputPassword'],
        "Nombre usuario": request.form['inputUsername'],
        "Repetir contraseña": request.form['inputRepetPassword'],
        "Cuatrimestre": request.form['inputCuatrimestre'],
        "Carrera": request.form['inputCarrera'],
    }

    Carrera = request.form['inputCarrera']
    Cuatrimestre = request.form['inputCuatrimestre']
    Username = request.form['inputUsername']

    resultado = bd.put(f'/tic/alumno/{Carrera}', Username, registro)
    print(resultado)
    return redirect('/alumno/consultar')

@app.get("/update")
def alumno_update():
    bd.put('/tic/1', 'nombre', 'Alan')
    return 'se actualizo'

@app.route('/delete/<id>/')
def tutor_delete(id):
    print(id)
    bd.delete('/tic/alumno/2023-A/DSM', id)
    return redirect('/alumno/consultar')
