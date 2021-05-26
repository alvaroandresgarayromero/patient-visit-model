# heroku uses web.Dockerfile
# local development uses docker-compose
FROM python:3.9-buster

WORKDIR /app
COPY . /app

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install python dependencies
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt


# ENTRYPOING AND CMD execute once container has completed building
# Deployment development: Heroku reads web.Dockerfile only, and environment variables are set inside Heroku
# Local development: Environment variables are set by docker-compose in .env
CMD gunicorn --bind 0.0.0.0:$PORT "appserver:gunicorn_app"
ENTRYPOINT ["/app/flaskr/web/wait_for_db_container.sh"]
