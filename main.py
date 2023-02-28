from flask import Flask
from dotenv import load_dotenv

from features.tutor import routes_backend as tutor_routes_backend
from features.tutor import routes_frontend as tutor_routes_frontend
from features.rutas import routes_frontend as login

# from features.alumno import routes_backend as alumno_routes_backend
from features.alumno import routes_fronted as alumno_routes_frontend
from features.director import routes_frontend as director_routes_frontend
from features.permisos import routes_frontend as find_permisos


app = Flask(__name__)

load_dotenv('.env')

app.register_blueprint(tutor_routes_backend.app)
app.register_blueprint(tutor_routes_frontend.app)
app.register_blueprint(login.app)

app.register_blueprint(alumno_routes_frontend.app)
app.register_blueprint(director_routes_frontend.app)
app.register_blueprint(find_permisos.app)




if __name__ == "__main__":
    app.run()
