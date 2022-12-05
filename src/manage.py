import sys

import click
from flask.cli import with_appcontext

from src import db


@click.command(name="create_tables")
@with_appcontext
def create_tables():
    sys.stdout.write("creating tables...")
    db.create_all()


@click.command(name="drop_create_tables")
@with_appcontext
def drop_create():
    sys.stdout.write("dropping tables...")
    db.drop_all()
    sys.stdout.write("creating tables...")
    db.create_all()
