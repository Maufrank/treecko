from flask import Blueprint, render_template, request, redirect
# import requests
from firebase_admin import db
from firebase import firebase
app = Blueprint('Sesion', __name__, url_prefix='/sesion')

bd = firebase.FirebaseApplication("https://treecko-c8c52-default-rtdb.firebaseio.com", None)

@app.route('/login', methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form['inputUsername']
        passw = request.form['inputPassw']
        if username == 'Gon' and passw == 'pepe':
            return redirect('/tutor/find')
        elif username == 'Mau' and passw == 'Mau':
            return redirect('/tuto')
            # print('Hola')
        elif username == 'Chino' and passw == 'Chino':
            return redirect('/alumn')
        else:
            return redirect('/')
        

