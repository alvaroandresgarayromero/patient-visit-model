#!/bin/sh

if [ "$FLASK_ENV" = "development" ]
then
  echo "Waiting for postgres container to build..."

  while ! nc -z $POSTGRES_CONTAINER_NAME_APP $POSTGRES_PORT_APP; do
    sleep 0.1
  done

  echo "PostgreSQL container started"
else
  echo "PostgresSQL database is already running in Heroku"
fi

echo "Creating the database tables..."
python3 appserver.py create-db
echo "Tables created"


exec "$@"