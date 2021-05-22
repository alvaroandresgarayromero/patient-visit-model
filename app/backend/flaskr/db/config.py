import os

user = os.environ.get('POSTGRES_USER_APP', None)
password = os.environ.get('POSTGRES_PASSWORD_APP', None)
host = os.environ.get('POSTGRES_CONTAINER_NAME_APP', None)
database = os.environ.get('POSTGRES_DB_APP', None)
port = os.environ.get('POSTGRES_PORT_APP', None)

if host is None:
    # deployment development with Heroku
    DATABASE_URL_HEROKU = os.environ.get('DATABASE_URL', None)

    assert DATABASE_URL_HEROKU is not None, 'DATABASE was not found during initialization routine. ' \
                                            'NOTE that local development such as tests need to be ran ' \
                                            'from a Docker Container. See Local Development README for more info'

    # SQLAlchemy 1.4 removed the deprecated postgres:// dialect name,
    # the postgresql must be used now. However, Heroku hasn't updated this
    # on their end. So let's take care of it here.
    DATABASE_URL = 'postgresql' + DATABASE_URL_HEROKU.replace('postgres', '')

else:
    # local development with docker-compose container
    DATABASE_URL = f'postgresql://{user}:{password}@{host}:{port}/{database}'
