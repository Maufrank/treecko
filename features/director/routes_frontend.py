from flask import request, Blueprint, jsonify, session, flash, make_response, redirect, url_for, render_template


app = Blueprint('director', __name__, url_prefix='/director')

@app.get('/consultar')
def director_find():
    if 'username' in session:
        if session['rol'] == 'administrador':
            return render_template('find_director.html')
        else:
            return redirect('/')
    else:
        return redirect('/')

@app.get('/agregar')
def director_add():
    if 'username' in session:
        if session['rol'] == 'administrador':
            return render_template('add_director.html')
        else:
            return redirect('/')
    else:
        return redirect('/')