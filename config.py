import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = ''
    UPLOAD_FOLDER = "./hidden-tests"
    PASS='lcv:>?;W5QD<,js8oKyE4q`nN"z$M.?ts4#zd3o^n+9bk%6q$1@1P+P6uD^fY0z.>'
    ALLOWED_EXTENSION = "py"


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
