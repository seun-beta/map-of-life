import click
from flask.cli import with_appcontext

from src import db


@click.command(name="create_tables")
@with_appcontext
def create_tables():
    db.create_all()


@click.command(name="drop_create_tables")
@with_appcontext
def drop_create():
    db.drop_all()
    db.create_all()
