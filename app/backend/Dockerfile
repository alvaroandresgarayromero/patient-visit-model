# heroku uses Dockerfile
# local development uses docker-compose
FROM python:3.9-buster

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# CMD runs in container
# Deployment development: Heroku reads Dockerfile only, and environment variables are set inside Heroku
# Local development: Environment variables are set by docker-compose in .env
CMD gunicorn --bind 0.0.0.0:$PORT "flaskr:create_app()"