from flask import request, Blueprint, jsonify, session, flash, make_response, redirect, url_for, render_template

app = Blueprint('alumnopages', __name__, url_prefix='/alumno')

@app.get('/registrar')
def alumno():
    return render_template('add_alumno.html')

@app.get('/consultar')
def con_alumno():
    return render_template('find_alumno.html')

@app.get('/permiso')
def add_permiso():
    return render_template('add_permisos.html')

