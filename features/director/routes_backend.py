from flask import Blueprint, render_template, request, redirect, session
# import requests
from firebase_admin import db
from firebase import firebase
app = Blueprint('Director', __name__, url_prefix='/director')

bd = firebase.FirebaseApplication("https://treecko-c8c52-default-rtdb.firebaseio.com", None)

@app.get('/find')
def director_find():
    if 'username' in session:
        if session['rol'] == 'alumno':
            directores = bd.get('/treecko/tic/director/', '')
            registro = []
            # return directores
            for director in directores:
                dire = directores[director]
                registro.append(dire)
            return registro
            print(director)
            for director in director:
                registro.append(bd.get(f'/treecko/tic/director/{director}', '')) 
            print(registro)
            # return render_template('find_director.html', entries=registro)
            return registro
        else:
            return redirect('/')
    else:
        return redirect('/')




@app.route('/add', methods=['POST'])
def director_add():
    if 'username' in session:
        if session['rol'] == 'alumno':
            registro = {
                'nombre': request.form['inputNombre'],
                'apellidos': request.form['inputApellidos'],
                'correo': request.form['inputCorreo'],
                'usuario': request.form['inputUsername'],
                'contraseña': request.form['inputPassword'],
                "division": request.form['inputDivision'],
                
            }
            
            user = {
                "password": request.form['inputPassword'],
                "rol": 'director',
                "division": request.form['inputDivision'],
            }
            division = request.form['inputDivision'];
            
            usuario= request.form['inputUsername']
            print(registro)
            resultado = bd.put(f'/treecko/{division}/director', usuario ,registro)
            print(resultado)
            resultadoUsuario = bd.put(f'/treecko/usuarios', usuario, user)
            
            return redirect('/director/consultar')
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
