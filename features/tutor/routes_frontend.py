from flask import request, Blueprint, jsonify, session, flash, make_response, redirect, url_for, render_template


app = Blueprint('tutorPages', __name__, url_prefix='/tutor')

@app.get('/agregar')
def add_tutor():
    return render_template('add_tutor.html')

@app.get('/consultar')
def get_tutor():
    return render_template('find_tutor.html')


