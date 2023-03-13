from flask import Blueprint, render_template, request, json, redirect, session, send_file
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
    carrera = session['carrera']
    usuario = session['username']
    division = session['division']
    
    resultado = bd.get(f'/treecko/{division}/alumno/{carrera}/{usuario}/permisos/{idPermiso}', '')
    img = bd.get(f'/treecko/{division}/alumno/{carrera}/{usuario}/permisos/{idPermiso}/comprobante', '')
    # print(img)
    
    return render_template('show_permisos.html', entries=resultado)

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

@app.route('/tutor/show/<usuario>/<idPermiso>/')
def permisos_mis_alumnos(usuario, idPermiso):
    division = session['division']
    carrera = session['carrera']
    resultado = bd.get(f'/treecko/{division}/alumno/{carrera}/{usuario}/permisos/{idPermiso}', '')
    return render_template('show_permisos.html', entries=resultado)
    
@app.route('/tutor/show/<usuario>/<idPermiso>/<rev>/')
def aprobar_permiso(usuario, idPermiso, rev):
    division = session['division']
    carrera = session['carrera']
    bd.put(f'/treecko/{division}/alumno/{carrera}/{usuario}/permisos/{idPermiso}', 'aprobacionTutor', rev)
    return redirect('/permiso/tutor/find')
    
@app.route('/director/find')
def director_ver_permisos():
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
                        permi.append(per)
    # return permi
    return render_template('vistaDirector.html', entries=permi)


@app.route('/director/show/<carrera>/<usuario>/<idPermiso>/<rev>/')
def liberar_permiso(carrera, usuario, idPermiso, rev):
    division = session['division']
    # carrera = session['carrera']
    bd.put(f'/treecko/{division}/alumno/{carrera}/{usuario}/permisos/{idPermiso}', 'aprobacionDirector', rev)
    return redirect('/permiso/director/find')


