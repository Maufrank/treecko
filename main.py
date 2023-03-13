import os
from flask import Flask, send_from_directory, session, request, redirect
from dotenv import load_dotenv
from flask_wtf import CSRFProtect

from features.tutor import routes_backend as tutor_routes_backend
from features.tutor import routes_frontend as tutor_routes_frontend
from features.rutas import routes_frontend as login

# from features.alumno import routes_backend as alumno_routes_backend
from features.alumno import routes_frontend as alumno_routes_frontend
from features.alumno import routes_backend as alumno_routes_backend
from features.director import routes_frontend as director_routes_frontend
from features.permisos import routes_backend as permisos_backend
from features.permisos import routes_frontend as find_permisos
from features.director import routes_backend as director_routes_backend
from features.sesion import routes_backend as sesion_routes_backend


app = Flask(__name__)
app.secret_key = 'treecko_secret_key'
csrf = CSRFProtect(app)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',mimetype='image/vnd.microsoft.icon')

load_dotenv('.env')

# app.register_blueprint(alumno_routes_backend.app)
app.register_blueprint(tutor_routes_backend.app)
app.register_blueprint(tutor_routes_frontend.app)
app.register_blueprint(login.app)
app.register_blueprint(director_routes_backend.app)
app.register_blueprint(alumno_routes_frontend.app)
app.register_blueprint(alumno_routes_backend.app)
app.register_blueprint(director_routes_frontend.app)
app.register_blueprint(find_permisos.app)
app.register_blueprint(sesion_routes_backend.app)
app.register_blueprint(permisos_backend.app)

# @app.before_request
# def before_request():
#     if 'username' not in session and request.endpoint == '/sesion/ver':
#         return redirect('/')

if __name__ == "__main__":
    app.run()

    

