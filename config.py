from environs import Env
from secrets import token_hex

env = Env()
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
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = env.str('DATABASE_URL')
    JWT_SECRET_KEY = env.str('JWT_SECRET_KEY')
    SECRET_KEY = env.str('SECRET_KEY')
