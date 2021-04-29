# heroku uses Dockerfile
# local development uses docker-compose
FROM python:3.9-buster

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Deployment development: $PORT is set by Heroku
# Local development: $PORT is set by docker-compose
CMD gunicorn --bind 0.0.0.0:$PORT "flaskr:create_app()"