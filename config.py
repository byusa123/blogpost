import os

class Config:
    
    
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
 
    # DEBUG = True

class ProdConfig(Config):
    SECRET_KEY = os.environ.get('12345')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:gizo@localhost/blog'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:gizo@localhost/blog'
    DEBUG = True

config_options = {
'development':DevConfig,


}