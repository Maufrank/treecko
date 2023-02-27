from flask import Flask
from dotenv import load_dotenv

from features.tutor import routes_backend as tutor_routes_backend
from features.tutor import routes_frontend as tutor_routes_frontend

app = Flask(__name__)

load_dotenv('.env')

app.register_blueprint(tutor_routes_backend.app)
app.register_blueprint(tutor_routes_frontend.app)


if __name__ == "__main__":
    app.run()

