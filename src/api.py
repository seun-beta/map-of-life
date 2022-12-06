from flask import Blueprint, jsonify, request

from src.constants.http_status_codes import HTTP_200_OK, HTTP_404_NOT_FOUND
from src.models import Country, Data, Species

mol_bp = Blueprint("mol", __name__, url_prefix="/api/v1/mol")


@mol_bp.get("/")
def main():
    return jsonify({"id": "name"}, HTTP_200_OK)


@mol_bp.get("/db")
def db():
    data = Species.query.filter_by(id=1).first()

    return jsonify({"id": data.taxonKey, "kingdom": data.family.family}, HTTP_200_OK)


@mol_bp.get("/country_summary/<string:country_name>/")
def country_summary(country_name):
    country = Country.query.filter_by(country_name=country_name).first()
    if not country:
        return jsonify({"data": "not found"}), HTTP_404_NOT_FOUND

    return jsonify({"id": "data"}, HTTP_200_OK)


@mol_bp.get("/species_summary/<string:species_name>/")
def species_summary(species_name):
    specie = Species.query.filter_by(species=species_name).first()
    if not specie:
        return jsonify({"data": "not found"}), HTTP_404_NOT_FOUND
    data = Data.query.filter_by(speciesKey=specie.id).distinct()
    year_list = []
    count_list = []
    for i in data:
        if i.year:
            count_list.append(
                Data.query.filter_by(year=i.year, speciesKey=specie.id).count()
            )
            year_list.append(i.year)

    country_list = []
    country_count = []
    for i in data:

        if i.country:
            country_count.append(
                Data.query.filter_by(
                    countryKey=i.country.id, speciesKey=specie.id
                ).count()
            )
            country_list.append(i.country.country_name)
    country_records = list(zip(country_list, country_count))
    year_records = list(zip(year_list, count_list))

    result = {
        "number_of_records": Data.query.filter_by(speciesKey=specie.id).count(),
        "years": year_records,
        "country": country_records,
        "kingdom": specie.kingdom.kingdom,
        "phylum": specie.phylum.phylum,
        "class": specie.class_name.class_name,
        "order": specie.order.order,
        "family": specie.family.family,
        "genus": specie.genus.genus,
    }

    return jsonify(result, HTTP_200_OK)


@mol_bp.get("/occurrences/<string:species_name>/")
def occurrences(species_name):

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per-page", 5, type=int)

    specie = Species.query.filter_by(species=species_name).first()
    if not specie:
        return jsonify({"data": "not found"}), HTTP_404_NOT_FOUND

    data_set = Data.query.filter_by(speciesKey=specie.id).paginate(
        page=page, per_page=per_page
    )

    result_list = []

    for data in data_set.items:
        result_list.append(
            {
                "id": data.id,
                "latitude": data.latitude,
                "longitude": data.longitude,
                "date": f"{data.day}-{data.month}-{data.year}",
                "occurrence_stutus": data.occurrenceStatus,
                "basis_of_record": data.basisOfRecord,
                "gbif_id_link": data.gbifIdLink,
            }
        )

    meta = {
        "page": data_set.page,
        "pages": data_set.pages,
        "total_count": data_set.total,
        "prev_page": data_set.prev_num,
        "next_page": data_set.next_num,
        "has_next": data_set.has_next,
        "has_prev": data_set.has_prev,
    }

    return jsonify({"data": result_list, "meta": meta}), HTTP_200_OK
