from flask import Blueprint, render_template, request, json, redirect, session
# import request
# from firebase_admin import bd
from firebase import firebase
from flask_wtf import CSRFProtect
app = Blueprint('Alumno', __name__, url_prefix='/alumno')

bd = firebase.FirebaseApplication(
    "https://treecko-c8c52-default-rtdb.firebaseio.com", None)


@app.get('/find')
def alumno_find():
    alumno = bd.get('/treecko/tic/alumno', '')
    registro = []
    for alumno in alumno:
        al = bd.get(f'/treecko/tic/alumno/{alumno}', '')
        for al in al:
            registro.append(bd.get(f'/treecko/tic/alumno/{alumno}/{al}', ''))
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
        "usuario": request.form['inputUsername'],
        # "Repetir_contraseña": request.form['inputRepetPassword'],
        # "Cuatrimestre": request.form['inputCuatrimestre'],
        "division": request.form['inputDivision'],
        "Carrera": request.form['inputCarrera'],
        "Cuatrimestre_actual": request.form['inputCuatrimestre'],
        "permisos": ["nada"]

    }

    user = {
        "password": request.form['inputPassword'],
        "rol": 'alumno',
        "division": request.form['inputDivision'],
        "carrera": request.form['inputCarrera']
    }

    Carrera = request.form['inputCarrera']
    Cuatrimestre = request.form['inputCuatrimestre']
    Username = request.form['inputUsername']
    division = request.form['inputDivision']

    resultado = bd.put(f'/treecko/{division}/alumno/{Carrera}', Username, registro)
    resultadoUsuario = bd.put(f'/treecko/usuarios', Username, user)

    print(resultado)
    return redirect('/')


@app.get('/actualizar/<carrera>/<id>/')
def actualizar_alumno(carrera, id):
    if 'username' in session:
        if session['rol'] == 'alumno':
            datos = bd.get(f'/treecko/tic/alumno/{carrera}/{id}', '')
            print(datos)
            return render_template('update_alumno.html', entry=datos)
        else:
            return redirect('/')
    else:
        return redirect('/')


@app.route('/delete/<carrera>/<id>/')
def alumno_delete(carrera, id):
    if 'username' in session:
        if session['rol'] == 'alumno':
            print(id)
            bd.delete(f'/treecko/tic/alumno/{carrera}', id)
            return redirect('/alumno/find')
        else:
            return redirect('/')
    else:
        return redirect('/')
