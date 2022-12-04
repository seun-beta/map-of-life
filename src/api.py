from flask import Blueprint, jsonify

from src.constants.http_status_codes import HTTP_200_OK
from src.models import Species

mol_bp = Blueprint("mol", __name__, url_prefix="/api/v1/mol")


@mol_bp.get("/")
def main():
    return jsonify({"id": "name"}, HTTP_200_OK)


@mol_bp.get("/db")
def db():
    data = Species.query.all()

    return jsonify({"id": data}, HTTP_200_OK)
