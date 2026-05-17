import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    
    # Database
    # Use SQLite for development, Postgres for production
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Store Configuration
    STORE_NAME = os.environ.get('STORE_NAME') or 'Ottoman Time'
    CURRENCY = os.environ.get('CURRENCY') or 'PKR'
    CURRENCY_SYMBOL = os.environ.get('CURRENCY_SYMBOL') or 'Rs.'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    
    # Ensure production uses Postgres
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
