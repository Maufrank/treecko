from flask import request, Blueprint, jsonify, session, flash, make_response, redirect, url_for
import requests
from firebase_admin import db
app = Blueprint('Tutor', __name__, url_prefix='/tutor')

@app.get('/find')
def tutor_add():
    response = requests.get("https://treecko-c8c52-default-rtdb.firebaseio.com/tic/alumno.json")
    data = response.json()
    print(data)
    return data

