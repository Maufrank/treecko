from flask import request, Blueprint, jsonify, session, flash, make_response, redirect, url_for, render_template


app = Blueprint('director', __name__, url_prefix='/director')

@app.get('/consultar')
def director_find_todos():
    if 'username' in session:
        if session['rol'] == 'alumno':
            return render_template('find_director.html')
        else:
            return redirect('/')
    else:
        return redirect('/')

@app.get('/agregar')
def director_add_nuevo():
    if 'username' in session:
        if session['rol'] == 'alumno':
            return render_template('add_director.html')
        else:
            return redirect('/')
    else:
        return redirect('/')