from flask import request, Blueprint, jsonify, session, flash, make_response, redirect, url_for, render_template


app = Blueprint('permisos', __name__, url_prefix='/permiso')

@app.get('/consultar')
def director_find():
    return render_template('find_permisos.html')


@app.get('/registrar')
def permiso_add():
    return render_template('add_permisos.html')

@app.route('/alumno/ver')
def mis_permisos():
    return render_template('find_permiso.html')

@app.route('/tutor/ver')
def tutor_ver_permisos():
    return render_template('vistaTutor.html')

@app.route('/director/ver')
def director_ver_permisos():
    return render_template('vistaDirector.html')