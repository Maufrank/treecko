from flask import request, Blueprint, jsonify, session, flash, make_response, redirect, url_for, render_template


app = Blueprint('director', __name__, url_prefix='/director')

@app.get('/consultar')
def director_find():
    return render_template('find_director.html')

@app.get('/agregar')
def director_add():
    return render_template('add_director.html')
