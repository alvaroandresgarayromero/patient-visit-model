from flaskr import create_app
from flask.cli import FlaskGroup

# Running the server via Gunicorn (dockerfile looks for this file)
gunicorn_app = create_app()


if __name__ == "__main__":
    # DockerFile will execute our own CLI command to create db tables
    # This is done once the web service flask container
    # and postgres container have completing building.
    # NOTE: cli() will call create_app()
    # to generate the app commands
    # $ python3 appserver.py create-db
    cli = FlaskGroup(gunicorn_app)
    cli()

