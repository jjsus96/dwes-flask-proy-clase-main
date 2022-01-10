import os

class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), '..', 'data.db')
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/flask_blog'
    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost:3306/flask_blog'
