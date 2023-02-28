from flask import request, Blueprint, jsonify, session, flash, make_response, redirect, url_for, render_template


app = Blueprint('rutas', __name__, url_prefix='/')

@app.get('/')
def login():
    return render_template('login.html')



    