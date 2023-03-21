from flask import Blueprint, jsonify, render_template, request, json, redirect, session, send_file
#import request
# from firebase_admin import bd
from firebase import firebase
from werkzeug.utils import secure_filename
import os
app = Blueprint('Permiso', __name__, url_prefix='/permiso')

# app.config["UPLOAD_FOLDER"] = "static/uploads"
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

bd = firebase.FirebaseApplication("https://treecko-c8c52-default-rtdb.firebaseio.com", None)

@app.get('/find')
def alumno_find():
    
    registro = []
    division = session['division']
    carrera = session['carrera']
    usuario = session['username']
    permiso = bd.get(f'/treecko/{division}/alumno/{carrera}/{usuario}/permisos', '')
    
    for permiso in permiso:
        registro.append(bd.get(f'/treecko/{division}/alumno/{carrera}/{usuario}/permisos/{permiso}', '')) 
    print(registro)
    return render_template('find_permiso.html', entries=registro)

@app.route("/add", methods=['POST'])
def permiso():
    file = request.files["inputComprobante"]
    filename = secure_filename(file.filename)
    # file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    file.save(os.path.join("static/uploads", filename))
    

    carrera = session['carrera']
    usuario = session['username']
    division = session['division']
    registro = {
        "motivo": request.form['inputMotivo'],
        "descripcion": request.form['inputDescripcion'],
        "fecha": request.form['inputFechaInicial'],
        "comprobante": filename,
        "aprobacionTutor":"pendiente",
        "aprobacionDirector":"pendiente",
        "carrera": carrera,
        "usuario": usuario,
    }
    resultado = bd.put(f'/treecko/{division}/alumno/{carrera}/{usuario}/permisos', request.form['inputFechaInicial'], registro)
    print(resultado)
    
    
    return redirect('/permiso/find')

@app.route('/ver/<idPermiso>/')
def ver_permiso(idPermiso):
    if 'username' in session:
        if session['rol'] == 'alumno':
            carrera = session['carrera']
            usuario = session['username']
            division = session['division']
            
            resultado = bd.get(f'/treecko/{division}/alumno/{carrera}/{usuario}/permisos/{idPermiso}', '')
            img = bd.get(f'/treecko/{division}/alumno/{carrera}/{usuario}/permisos/{idPermiso}/comprobante', '')
            # print(img)
            
            return render_template('show_permisos.html', entries=resultado)
        else:
            return redirect('/')
    else:
        return redirect('/')
    

@app.route('/tutor/validar/<division>/<carrera>/<usuario>/<idPermiso>/')
def validar_por_tutor(division, carrera, usuario, idPermiso):
    resultado = bd.put(f'/treecko/{division}/alumno/{carrera}/{usuario}/permisos/{idPermiso}', "aprobacionTutor", 'aprobado')
    
    
@app.route('/descargar/comprobante/<comprobante>/')
def descarga_comprobante(comprobante):
    # carrera = session['carrera']
    # usuario = session['username']
    # division = session['division']
    # img = bd.get(f'/treecko/{division}/alumno/{carrera}/{usuario}/permisos/{idPermiso}/{comprobante}', '')
    PATH = f'./static/uploads/{comprobante}'
    
    return send_file(PATH, as_attachment=True)
    
@app.route('/tutor/find')
def tutor_ver_permisos():
    if 'username' in session:
        if session['rol'] == 'alumno':
            division = session['division']
            carrera = session['carrera']
            permi = []
            alumnos = bd.get(f'/treecko/{division}/alumno/{carrera}', '')
            for alumnos in alumnos:
                permisos = bd.get(f'/treecko/{division}/alumno/{carrera}/{alumnos}/permisos', '')
                for permisos in permisos:
                    per = bd.get(f'/treecko/{division}/alumno/{carrera}/{alumnos}/permisos/{permisos}', '')
                    if per != "nada":
                        permi.append(per)

            print(permi)
            return render_template('vistaTutor.html', entries=permi)
        else:
            return redirect('/')
    else:
        return redirect('/')

@app.route('/tutor/show/<usuario>/<idPermiso>/')
def permisos_mis_alumnos(usuario, idPermiso):
    if 'username' in session:
        if session['rol'] == 'alumno':
            division = session['division']
            carrera = session['carrera']
            resultado = bd.get(f'/treecko/{division}/alumno/{carrera}/{usuario}/permisos/{idPermiso}', '')
            return render_template('show_permisos.html', entries=resultado)
        else:
            return redirect('/')
    else:
        return redirect('/')
    
    
@app.route('/tutor/show/<usuario>/<idPermiso>/<rev>/')
def aprobar_permiso(usuario, idPermiso, rev):
    if 'username' in session:
        if session['rol'] == 'alumno':
            division = session['division']
            carrera = session['carrera']
            bd.put(f'/treecko/{division}/alumno/{carrera}/{usuario}/permisos/{idPermiso}', 'aprobacionTutor', rev)
            return redirect('/permiso/tutor/ver')
        else:
            return redirect('/')
    else:
        return redirect('/')
    
    
@app.route('/director/find')
def director_ver_permisos():
    if 'username' in session:
        if session['rol'] == 'alumno':
            print('hola mundo')
            # return jsonify({"datos": 'holas'})
            division = session['division']
            permi = []
            carrera = bd.get(f'/treecko/{division}/alumno', '')
            for carrera in carrera:
                alumnos = bd.get(f'/treecko/{division}/alumno/{carrera}', '')
                for alumnos in alumnos:
                    permisos = bd.get(f'/treecko/{division}/alumno/{carrera}/{alumnos}/permisos', '')
                    for permisos in permisos:
                        per = bd.get(f'/treecko/{division}/alumno/{carrera}/{alumnos}/permisos/{permisos}', '')
                        if per != "nada":
                            aprobacion = bd.get(f'/treecko/{division}/alumno/{carrera}/{alumnos}/permisos/{permisos}/aprobacionTutor', '')
                            if aprobacion == 'Revisado':
                                print(per)
                                permiso = {
                                    "aprobacionDirector": per["aprobacionDirector"],
                                    "aprobacionTutor": per["aprobacionTutor"],
                                    "carrera": per["carrera"],
                                    "comprobante": per["comprobante"],
                                    "descripcion": per["descripcion"],
                                    "fecha": per["fecha"],
                                    "motivo": per["motivo"],
                                    "usuario": per["usuario"],
                                    "aprobar": f'''<button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#eliminar">Ver permiso</button>
                                    <div class="modal fade" id="eliminar" tabindex="-1" aria-labelledby="eliminarLabel" aria-hidden="true">
                                    <div class="modal-dialog">
                                        <div class="modal-content">
                                        <div class="modal-header">
                                            <h1 class="modal-title fs-5" id="eliminarLabel">Permiso de {per["usuario"]}</h1>
                                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                        </div>
                                        <div class="modal-body">
                                            <P>Motivo: {per["motivo"]}</P><br>
                                            <p>Descripcion: {per["descripcion"]}</p><br>
                                            <p>Fecha solicitada: {per["fecha"]}</p><br>
                                            <p>Carrera: {per["carrera"]}</p><br>
                                            <p>Vista del tutor: {per["aprobacionTutor"]}</p><br>
                                            <button type="submit" class="btn btn-success"  onclick="location.href=`/permiso/descargar/comprobante/{per["comprobante"]}/`">Descargar comprobante</button> 
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-warning" data-bs-dismiss="modal"  onclick="location.href=`/permiso/director/show/{per["carrera"]}/{per["usuario"]}/{per["fecha"]}/Rechazado`">Rechazar</button>
                                            <button type="submit" class="btn btn-success"  onclick="location.href=`/permiso/director/show/{per["carrera"]}/{per["usuario"]}/{per["fecha"]}/Aprobado`">Dar visto bueno</button>
                                        </div>
                                        </div>
                                    </div>
                                    </div>
                                    '''
                                }                 
                                permi.append(permiso)
            # return permi
            # return render_template('vistaDirector.html', entries=permi)
            print(permi)
            return jsonify({"datos": permi})
        
        else:
            return redirect('/')
    else:
        return redirect('/')


@app.route('/director/show/<carrera>/<usuario>/<idPermiso>/<rev>/')
def liberar_permiso(carrera, usuario, idPermiso, rev):
    if 'username' in session:
        if session['rol'] == 'alumno':
            division = session['division']
            # carrera = session['carrera']
            bd.put(f'/treecko/{division}/alumno/{carrera}/{usuario}/permisos/{idPermiso}', 'aprobacionDirector', rev)
            return redirect('/permiso/director/find')
        else:
            return redirect('/')
    else:
        return redirect('/')
    


@app.get('/findRep')
def alumno_permiso_find():
    registro = []
    division = session['division']
    carrera = session['carrera']
    usuario = session['username']
    permiso = bd.get(f'/treecko/{division}/alumno/{carrera}/{usuario}/permisos', '')
    
    for permiso in permiso:
        permi = bd.get(f'/treecko/{division}/alumno/{carrera}/{usuario}/permisos/{permiso}', '')
        
            
        print(permi)
        if permi != 'nada':
            # permi = json.loads(permi)
            # for dato in permi:
            #     print(permi[dato])
            per = {'aprobacionDirector': permi['aprobacionDirector'],
                   'aprobacionTutor': permi['aprobacionTutor'],
                   'carrera': permi['carrera'],
                   'comprobante': permi['comprobante'],
                   'descripcion': permi['descripcion'],
                   'fecha': permi['fecha'],
                   'motivo': permi['motivo'],
                   'usuario': permi['usuario'],
                   'permiso': f'<button type="submit" class="btn btn-success" onclick="location.href=`/permiso/descargar/comprobante/{permi["comprobante"]}/`">Ver permiso</button>'}
            print(per)
            registro.append(per) 
        # print(permi)
        
    return jsonify({"datos": registro})

@app.route('/tutor/misalumnos')
def method_name():
    division = session['division']
    carrera = session['carrera']
    permis = []
    alumnos = bd.get(f'/treecko/{division}/alumno/{carrera}', '')
    for alumnos in alumnos:
        permisos = bd.get(f'/treecko/{division}/alumno/{carrera}/{alumnos}/permisos', '')
        for permisos in permisos:
            permi = bd.get(f'/treecko/{division}/alumno/{carrera}/{alumnos}/permisos/{permisos}', '')
            if permi != "nada":
                per = {'aprobacionDirector': permi['aprobacionDirector'],
                   'aprobacionTutor': permi['aprobacionTutor'],
                   'carrera': permi['carrera'],
                   'comprobante': permi['comprobante'],
                   'descripcion': permi['descripcion'],
                   'fecha': permi['fecha'],
                   'motivo': permi['motivo'],
                   'usuario': permi['usuario'],
                   'permiso': f'''<button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#eliminar">Ver permiso</button>
                                    <div class="modal fade" id="eliminar" tabindex="-1" aria-labelledby="eliminarLabel" aria-hidden="true">
                                    <div class="modal-dialog">
                                        <div class="modal-content">
                                        <div class="modal-header">
                                            <h1 class="modal-title fs-5" id="eliminarLabel">Permiso de {permi["usuario"]}</h1>
                                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                        </div>
                                        <div class="modal-body">
                                            <P>Motivo: {permi["motivo"]}</P><br>
                                            <p>Descripcion: {permi["descripcion"]}</p><br>
                                            <p>Fecha solicitada: {permi["fecha"]}</p><br>
                                            <p>Carrera: {permi["carrera"]}</p><br>
                                            <p>Vista del tutor: {permi["aprobacionTutor"]}</p><br>
                                            <button type="submit" class="btn btn-success"  onclick="location.href=`/permiso/descargar/comprobante/{permi["comprobante"]}/`">Descargar comprobante</button> 
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-warning" data-bs-dismiss="modal"  onclick="location.href=`/permiso/tutor/show/{permi["usuario"]}/{permi["fecha"]}/Rechazado`">Rechazar</button>
                                            <button type="submit" class="btn btn-success"  onclick="location.href=`/permiso/tutor/show/{permi["usuario"]}/{permi["fecha"]}/Aprobado`">Dar visto bueno</button>
                                        </div>
                                        </div>
                                    </div>
                                    </div>
                                    '''
                   }
                permis.append(per)
                
    return jsonify({"datos": permis})
    