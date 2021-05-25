import click
from .db.models import db


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def init_app(app):
    # inits app with new CLI commands
    # For example,
    # once app is running, we can create the db tables
    # within docker web service like:
    # $ python3 appserver.py create-db
    for command in [create_db, drop_db]:
        app.cli.add_command(app.cli.command()(command))

