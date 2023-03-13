from flask import Blueprint, render_template, request, redirect, session
# import requests
from firebase_admin import db
from firebase import firebase
app = Blueprint('Director', __name__, url_prefix='/director')

bd = firebase.FirebaseApplication("https://treecko-c8c52-default-rtdb.firebaseio.com", None)

@app.get('/find')
def director_find():
    if 'username' in session:
        if session['rol'] == 'administrador':
            director = bd.get('/treecko/tic/director/', '')
            registro = []
            for director in director:
                registro.append(bd.get(f'/treecko/tic/director/{director}', '')) 
            print(registro)
            return render_template('find_director.html', entries=registro)
        else:
            return redirect('/')
    else:
        return redirect('/')
    
@app.route('/add', methods=['POST'])
def director_add():
    if 'username' in session:
        if session['rol'] == 'administrador':
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
            resultado = bd.put(f'/treecko/tic/director', usuario ,registro)
            print(resultado)
            return redirect('/director/find')
        else:
            return redirect('/')
    else:
        return redirect('/')
    

@app.get('/update')
def director_update():
    if 'username' in session:
        if session['rol'] == 'administrador':
            bd.put('/treecko/tic/-NPK_tfzeVLDtju5qrBq', 'saludo', 'Hola cola')
            return 'se actualizo'
        else:
            return redirect('/')
    else:
        return redirect('/')
    
@app.get('/delete/<id>/')
def director_delete(id):
    if 'username' in session:
        if session['rol'] == 'administrador':
            print(id)
            bd.delete('/treecko/tic/director', id)
            return redirect('/director/find')
        else:
            return redirect('/')
    else:
        return redirect('/')
