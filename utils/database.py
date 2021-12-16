from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config

db = SQLAlchemy()
ma = Marshmallow()

def connect_db():
    app = Flask(__name__)
    app.config.from_object(Config())
    db.init_app(app)
    app.app_context().push()