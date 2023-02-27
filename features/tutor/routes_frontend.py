from flask import request, Blueprint, jsonify, session, flash, make_response, redirect, url_for, render_template


app = Blueprint('tutorPages', __name__, url_prefix='/')

@app.get('/')
def get_tutor():
    return render_template('add_tutor.html')