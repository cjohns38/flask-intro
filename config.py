import os

# default config


class BaseConfig(object): 
    DEBUG = False
    SECRET_KEY = '\x84{\x80K\xe6i\xbd`\xb1\xa0\x0f9\x84%s\xc9\xe7\xf5c\xb6C\xa6\xf2\xd3'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False 
