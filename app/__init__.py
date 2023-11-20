from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

app = Flask(__name__)
jwt = JWTManager(app) # activate JWTManager
app.json.sort_keys = False #cancel sort jsonify
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.model import user, dosen, mahasiswa, gambar #import model
from app import routes