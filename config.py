from os import environ
from secrets import token_hex


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = token_hex(32)
    SECRET_KEY = token_hex(32)


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://mrabade:pain321123@localhost/FairyTail'
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/FairyTail.db'
    TESTING = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = environ.get('POSTGRES_URL')
    # JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
    # SECRET_KEY = environ.get('SECRET_KEY')
