from dotenv import load_dotenv
import os

# parse .env file if exists
load_dotenv()


class Config(object):
    TESTING = False
    ENV = 'development'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    API_URL = os.getenv('API_URL')

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['eadomenech2020@gmail.com']


class DevelpmentConfig(Config):
    DEBUG = True
    DEBUG_TB_ENABLED = True


class TestConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')
