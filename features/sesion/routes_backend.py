from flask import Blueprint, render_template, request, redirect, session
# import requests
from firebase_admin import db
from firebase import firebase
app = Blueprint('Sesion', __name__, url_prefix='/sesion')

bd = firebase.FirebaseApplication("https://treecko-c8c52-default-rtdb.firebaseio.com", None)

@app.route('/login', methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form['inputUsername']
        passw = request.form['inputPassw']
        try:
            usuarios = bd.get(f'/treecko/usuarios', '')
            for usuarios in usuarios:
                if username == usuarios:
                    if passw == (bd.get(f'/treecko/usuarios/{username}/password', '')):
                        rol = bd.get(f'/treecko/usuarios/{username}/rol', '')
                        division = bd.get(f'/treecko/usuarios/{username}/division', '')
                        carrera = bd.get(f'/treecko/usuarios/{username}/carrera', '')
                        
                        if rol == 'administrador':
                            session['username'] = username
                            session['rol'] = 'administrador'
                            return redirect('/tutor/find')
                        elif rol == 'tutor':
                            session['username'] = username
                            session['rol'] = 'tutor'
                            session['division'] = division
                            session['carrera'] = carrera
                            return redirect('/permisos/tutor/find')
                            # print('Hola')
                        elif rol == 'alumno':
                            session['username'] = username
                            session['rol'] = 'alumno'
                            session['division'] = division
                            session['carrera'] = carrera
                            return redirect('/permisos/find')
                        elif rol == 'director':
                            session['username'] = username
                            session['rol'] = 'director'
                            session['division'] = division
                            # session['carrera'] = carrera
                            return redirect('/permisos/director/find')
                    else:
                        # return 'contraseña incorrecta'
                        return redirect('/')
        except Exception:
            return redirect('/error')
        
        # return contraseña
        return 'no se encontro'
        
@app.route('/logout')
def logout():
    if 'username' in session:
        if session['rol'] == 'administrador':
            session.pop('username')
            session.pop('rol')
        else:
            session.pop('username')
            session.pop('rol')
            session.pop('division')
            session.pop('carrera')
        
    return redirect('/')
    
@app.route('/ver')
def ver():
    username = session['username']
    rol = session['rol']
    mensaje = f'usuario: {username}, rol: {rol}'
    return mensaje

@app.route('/validar/usuario')
def validar_usuario():
    if 'username' not in session:
        return redirect('/')
        # return {'hola'}
    elif 'username' in session:
        return True
        return 'no hola'
    

