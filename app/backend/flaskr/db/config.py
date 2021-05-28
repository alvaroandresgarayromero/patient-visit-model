import os


class Config(object):
    """Base config """
    DEBUG = False
    TESTING = False

    USER = os.environ.get('POSTGRES_USER_APP', None)
    PASSWORD = os.environ.get('POSTGRES_PASSWORD_APP', None)
    HOST = None
    DATABASE = os.environ.get('POSTGRES_DB_APP', None)
    PORT = None

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return f'postgresql://{self.USER}:{self.PASSWORD}@' \
                           f'{self.HOST}:{self.PORT}/' \
                           f'{self.DATABASE}'


class ProductionConfig(Config):
    """Uses production database server in Heroku."""
    # DATABASE_URL is defined inside Heroku
    DATABASE_URL_HEROKU = os.environ.get('DATABASE_URL', None)

    if DATABASE_URL_HEROKU is not None:
        # SQLAlchemy 1.4 removed the deprecated postgres:// dialect name,
        # the postgresql must be used now. However, Heroku hasn't updated this
        # on their end. So let's take care of it here.
        SQLALCHEMY_DATABASE_URI = 'postgresql' + DATABASE_URL_HEROKU.\
                                                replace('postgres', '')


class DevelopmentConfig(Config):
    """Uses development database server in docker container."""
    HOST = os.environ.get('POSTGRES_CONTAINER_NAME_APP', None)
    PORT = os.environ.get('POSTGRES_PORT_APP', None)
    DEBUG = True


class TestingConfig(Config):
    """Uses test database server in docker container."""
    HOST = os.environ.get('POSTGRES_CONTAINER_NAME_TEST', None)
    PORT = os.environ.get('POSTGRES_PORT_TEST', None)
    DEBUG = True
    TESTING = True


configs = {'development': DevelopmentConfig,
           'test': TestingConfig,
           'production': ProductionConfig,
           'default': ProductionConfig
           }
