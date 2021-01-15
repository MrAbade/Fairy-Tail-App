from flask import Flask
from flask_migrate import Migrate

from app.models import config_database
from app.views import config_views

configs = {
    'development': 'DevelopmentConfig',
    'production': 'ProductionConfig',
    'test': 'TestingConfig'
}

def create_app(config='production'):
    app = Flask(__name__)

    app.config.from_object(f'config.{configs[config]}')

    config_database(app)
    config_views(app)
    Migrate(app, app.db)

    return app
