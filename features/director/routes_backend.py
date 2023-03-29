from flask import Blueprint, render_template, request, redirect, session, jsonify
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
                
                direc = {
                    "apellidos": dire["apellidos"],
                    "contraseña": dire["contraseña"],
                    "correo": dire["correo"],
                    "division": dire["division"],
                    "nombre": dire["nombre"],
                    "usuario": dire["usuario"],
                    "editar": f'<button type="button" class="btn btn-success" onclick="location.href=`/tutor/actualizar/{dire["usuario"]}/`" >Editar</button>',
                    "eliminar": f'''
                    <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#eliminar">Eliminar</button>
                    <div class="modal fade" id="eliminar" tabindex="-1" aria-labelledby="eliminarLabel" aria-hidden="true">
                        <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                            <h1 class="modal-title fs-5" id="eliminarLabel">¿Desea eliminar al director?</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    
                            </div>
                            <div class="modal-body">
                            <P>Si elimina este registro nunca mas podra consultarlo</P>
                            </div>
                            <div class="modal-footer">
                            <button type="button" class="btn btn-warning" data-bs-dismiss="modal">Cancelar</button>
                            <button type="submit" class="btn btn-danger"  onclick="location.href=`/director/delete/{dire["usuario"]}/{dire["division"]}/`">Eliminar</button>
                            </div>
                        </div>
                        </div>
                    </div>

                    '''
                    
                }
                direName = dire["apellidos"]
                registro.append(direc)
            return jsonify({"datos": registro})
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
    
@app.route('/delete/<id>/<division>')
def director_delete_one(id, division):
    if 'username' in session:
        if session['rol'] == 'alumno':
            print(id)
            bd.delete(f'/treecko/{division}/director', id)
            return redirect('/director/consultar')
        else:
            return redirect('/')
    else:
        return redirect('/')
