from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def config_database(app: Flask):
    db.init_app(app)
    app.db = db

    from .guild import Guild
    from .sorcerer import Sorcerer
