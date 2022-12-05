# isort: skip_file

import os

from flask import Flask, jsonify

from src.api import mol_bp
from src.constants.http_status_codes import (
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from src.models import db
from src.manage import (
    create_tables,
    drop_create,
    seed_kingdom,
    seed_phylum,
    seed_class,
    seed_order,
    seed_family,
    seed_genus,
    seed_species,
)


def create_app(test_config=None):
    app: Flask = Flask(__name__, instance_relative_config=True)

    secret_key = os.environ.get("SECRET_KEY")
    if secret_key is None:
        raise Exception("SECRET_KEY does not exist")

    db_url = os.environ.get("DATABASE_URL")
    if db_url is None:
        raise Exception("DATABASE_URL does not exist")

    if not test_config:
        app.config.from_mapping(
            SECRET_KEY=secret_key,
            SQLALCHEMY_DATABASE_URI=db_url,
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JSON_SORT_KEYS=False,
            SWAGGER={"title": "MOL API", "uiversion": 3},
        )
    else:
        app.config.from_mapping(test_config)

    db.app = app
    db.init_app(app)

    app.register_blueprint(mol_bp)

    app.cli.add_command(create_tables)
    app.cli.add_command(drop_create)
    app.cli.add_command(seed_kingdom)
    app.cli.add_command(seed_phylum)
    app.cli.add_command(seed_class)
    app.cli.add_command(seed_order)
    app.cli.add_command(seed_family)
    app.cli.add_command(seed_genus)
    app.cli.add_command(seed_species)

    @app.errorhandler(HTTP_404_NOT_FOUND)
    def handle_404(e):
        return jsonify({"error": "Not Found"}), HTTP_404_NOT_FOUND

    @app.errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
    def handle_500(e):
        return (
            jsonify({"error": "Something went wrong. It's not you, it's us"}),
            HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return app
