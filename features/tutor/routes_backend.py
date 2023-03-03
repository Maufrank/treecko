from flask import Blueprint, render_template, request, json, redirect
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
    user = {
        'password': request.form['inputUsername'],
        'rol': 'tutor'
    }
    
    resultado = bd.put(f'/tic/tutor/{periodo}/{carrera}', usuario, registro)
    bd.put(f"/usuarios", usuario, user)
    print(resultado)
    return redirect('/tutor/find')
    

@app.get('/update')
def tutor_update():
    bd.put('/tic/-NPK_tfzeVLDtju5qrBq', 'saludo', 'Hola cola')
    return 'se actualizo'
    
@app.route('/delete/<id>/')
def tutor_delete(id):
    print(id)
    bd.delete('/tic/tutor/2023-A/DSM', id)
    return redirect('/tutor/find')

@app.get('/actualizar/<id>/')
def actualizar_tutor(id):
    datos = bd.get(f'/tic/tutor/2023-A/DSM/{id}', '')
    print(datos)
    return render_template('update_tutor.html', entry=datos)

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