from src.models import Country, Data, Species


def country_summary_service(country_name: str) -> list:
    country = Country.query.filter_by(country_name=country_name).first()
    if not country:
        return False
    data = Data.query.filter_by(countryKey=country.id).distinct()
    specie_list = []
    for i in data:
        specie_list.append(
            {
                "specie": i.species.species,
                "no_of_occurrences": i.species.numberOfOccurrences,
            }
        )
    return specie_list


def year_data(specie, data):
    year_list = []
    count_list = []
    for i in data:
        if i.year:
            count_list.append(
                Data.query.filter_by(year=i.year, speciesKey=specie.id).count()
            )
            year_list.append(i.year)
    return list(zip(year_list, count_list))


def country_data(specie, data):
    country_list = []
    country_count = []
    country_code_list = []
    for i in data:

        if i.country:
            country_count.append(
                Data.query.filter_by(
                    countryKey=i.country.id, speciesKey=specie.id
                ).count()
            )
            country_list.append(i.country.country_name)
            country_code_list.append(i.country.country_code)

    return list(zip(country_list, country_code_list, country_count))


def species_summary_service(species_name: str) -> list:
    specie = Species.query.filter_by(species=species_name).first()
    if not specie:
        return False
    data = Data.query.filter_by(speciesKey=specie.id).distinct()
    country_records = country_data(specie=specie, data=data)
    year_records = year_data(specie=specie, data=data)

    result = {
        "number_of_records": Data.query.filter_by(speciesKey=specie.id).count(),
        "taxonomy": {
            "kingdom": specie.kingdom.kingdom,
            "phylum": specie.phylum.phylum,
            "class": specie.class_name.class_name,
            "order": specie.order.order,
            "family": specie.family.family,
            "genus": specie.genus.genus,
        },
        "countries": country_records,
        "years": year_records,
    }
    return result


def occurences_service(species_name, page, per_page):

    specie = Species.query.filter_by(species=species_name).first()
    if not specie:
        return False

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

    return result_list, meta
