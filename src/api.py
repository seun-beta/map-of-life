from flasgger import swag_from
from flask import Blueprint, jsonify, request

from src.constants.http_status_codes import HTTP_200_OK, HTTP_404_NOT_FOUND
from src.services import (
    country_summary_service,
    occurences_service,
    species_summary_service,
)

mol_bp = Blueprint("mol", __name__, url_prefix="/api/v1/mol")


@swag_from("./docs/country_summary.yaml")
@mol_bp.get("/country_summary/<string:country_name>/")
def country_summary(country_name):
    data = country_summary_service(country_name=country_name)
    if not data:
        return jsonify({"data": "country found"}), HTTP_404_NOT_FOUND

    return jsonify({"data": data}, HTTP_200_OK)


@swag_from("./docs/species_summary.yaml")
@mol_bp.get("/species_summary/<string:species_name>/")
def species_summary(species_name):
    data = species_summary_service(species_name=species_name)
    if not data:
        return jsonify({"data": "specie not found"}), HTTP_404_NOT_FOUND

    return jsonify({"data": data}, HTTP_200_OK)


@swag_from("./docs/occurrences.yaml")
@mol_bp.get("/occurrences/<string:species_name>/")
def occurrences(species_name):

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per-page", 5, type=int)
    try:
        result_list, meta = occurences_service(
            species_name=species_name, page=page, per_page=per_page
        )
    except TypeError:
        return jsonify({"data": "ocurrence not found"}), HTTP_404_NOT_FOUND

    return jsonify({"data": result_list, "meta": meta}), HTTP_200_OK
