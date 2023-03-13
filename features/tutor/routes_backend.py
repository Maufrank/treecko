from flask import Blueprint, render_template, request, json, redirect, jsonify, session
# import requests
from firebase_admin import db
from firebase import firebase
from openpyxl import Workbook

app = Blueprint('Tutor', __name__, url_prefix='/tutor')

bd = firebase.FirebaseApplication(
    "https://treecko-c8c52-default-rtdb.firebaseio.com", None)


@app.get('/find')
def tutor_find():
    if 'username' in session:
        if session['rol'] == 'administrador':
            periodo = bd.get('/treecko/periodo', '')
            tutores = bd.get(f'/treecko/tic/tutor/{periodo}', '')
            registro = []
            for tutores in tutores:
                carrera = bd.get(f'/treecko/tic/tutor/{periodo}/{tutores}', '')
                # return carrera
                for carrera in carrera:
                    # return carrera
                    registro.append(bd.get(f'/treecko/tic/tutor/{periodo}/{tutores}/{carrera}', '')) 
            print(registro)
            # return registro
            return render_template('find_tutor.html', entries=registro)
        else:
            return redirect('/')
    else:
        return redirect('/')


@app.route('/add', methods=['POST'])
def tutor_add():
    if 'username' in session:
        if session['rol'] == 'administrador':
            registro = {
                'nombre': request.form['inputNombre'],
                'apellidos': request.form['inputApellidos'],
                'correo': request.form['inputCorreo'],
                'usuario': request.form['inputUsername'],
                'contraseña': request.form['inputPassword'],
                'grupo': request.form['inputGrupo']
            }
            carrera = request.form['inputCarrera']
            division = request.form['inputDivision']
            usuario = request.form['inputUsername']
            user = {
                'password': request.form['inputUsername'],
                'rol': 'tutor',
                'division': request.form['inputDivision'],
                'carrera': carrera,
            }
            periodo = bd.get('/treecko/periodo', '')
            resultado = bd.put(
                f'/treecko/{division}/tutor/{periodo}/{carrera}', usuario, registro)
            bd.put(f"/treecko/usuarios", usuario, user)
            print(resultado)
            return redirect('/tutor/find')
        else:
            return redirect('/')
    else:
        return redirect('/')


@app.route('/delete/<id>/')
def tutor_delete(id):
    if 'username' in session:
        if session['rol'] == 'administrador':
            print(id)
            bd.delete('/treecko/tic/tutor/2023-A/DSM', id)
            return redirect('/tutor/find')
        else:
            return redirect('/')
    else:
        return redirect('/')


@app.get('/actualizar/<id>/')
def actualizar_tutor(id):
    if 'username' in session:
        if session['rol'] == 'administrador':
            datos = bd.get(f'/treecko/tic/tutor/2023-A/DSM/{id}', '')
            print(datos)
            return render_template('update_tutor.html', entry=datos)
        else:
            return redirect('/')
    else:
        return redirect('/')


@app.route('/find/filter',  methods=['POST'])
def buscar_filtro():
    filtro = request.form['inputFiltro']
    tutores = []
    if filtro == "Division":
        division = request.form['inputDivision']
        consulta = bd.get(f'/{division}/tutor', '')
        # consulta =
        # for consulta in consulta:
        #     periodo = bd.get(f'/{division}/tutor/{consulta}', '')
        #     for periodo in periodo:
        #         carrera = bd.get(f'/{division}/tutor/{consulta}/{periodo}', '')
        #         for carrera in carrera:
        #             # tutor = bd.get(f'/{division}/tutor/{consulta}/{periodo}/{carrera}', '')
        #             tutores.append(bd.get(f'/{division}/tutor/{consulta}/{periodo}/{carrera}', ''))
    return tutores


@app.route('/guardar/xcel')
def excel():
    tutores = bd.get('/tic/tutor/2023-A/DSM', '')
    registro = []
    for tutores in tutores:
        tuto = bd.get(f'/tic/tutor/2023-A/DSM/{tutores}', '')
    # print(registro)
    # tuto = jsonify(tuto)
    # return render_template('find_tutor.html', entries=registro)
    return tuto.apellidos
