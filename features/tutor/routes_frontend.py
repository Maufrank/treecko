from flask import request, Blueprint, jsonify, session, flash, make_response, redirect, url_for, render_template
from flask_wtf import CSRFProtect

app = Blueprint('tutorPages', __name__, url_prefix='/tutor')


@app.get('/agregar')
def add_tutor():
    if 'username' in session:
        if session['rol'] == 'administrador':
            return render_template('add_tutor.html')
        else:
            return redirect('/')
    else:
        return redirect('/')


@app.get('/consultar')
def get_tutor():
    if 'username' in session:
        if session['rol'] == 'alumno':
            custom_cookie = request.cookies.get('custome_cookie')
            print(custom_cookie)
            return render_template('find_tutor.html')
        else:
            return redirect('/')
    else:
        return redirect('/')
        


@app.route('/cookies')
def coockies():
    response = make_response(render_template('find_tutor.html'))
    response.set_cookie('custome_cookie', 'pinche gon')
    return response

