from flask import request, Blueprint, jsonify, session, flash, make_response, redirect, url_for, render_template, Request
from firebase import firebase
from datetime import datetime

app = Blueprint('rutas', __name__, url_prefix='/')
bd = firebase.FirebaseApplication("https://treecko-c8c52-default-rtdb.firebaseio.com", None)


@app.get('/')
def login():
    return render_template('login.html')

@app.get('/tuto')
def login_tutor():
    return render_template('vistaTutor.html')

@app.get('/alumn')
def login_alumn():
    return render_template('permissions_alumno.html')

@app.get('/error')
def error():
    return render_template('sin_conexion.html')

@app.get('/respaldo')
def respaldo():
    try:
        respaldo = bd.get('/treecko', '')
        fecha = datetime.now()
        fecha = fecha.strftime("%d-%m-%Y-%H:%M:%S")
        print(fecha)
        resultado = bd.put('/respaldo', fecha, respaldo)
        return 'Respaldo hecho satisfactoriamente'
    except Exception:
        return redirect('/error')
    
@app.route('/prueba')
def prueba():
    return render_template('vistaTutor.html')

@app.route('/admin/panel')
def panel_control():
    return render_template('panel_control.html')

@app.route('/actualizar/periodo')
def actualizar_periodo():
    ahora = datetime.now()
    mes = ahora.month
    año = ahora.year
    print(mes)
    if mes >= 1 and mes <= 4:
        bd.put('treecko', 'periodo', f'{año}-A')
    elif mes >= 5 and mes <= 8:
        bd.put('treecko', 'periodo', f'{año}-B')
    elif mes >= 9 and mes <= 12:
        bd.put('treecko', 'periodo', f'{año}-C')
    return 'Periodo actualizado'

# @app.route('/pruebaA')
# def prueba():
#     return render_template('header_alumno.html')
