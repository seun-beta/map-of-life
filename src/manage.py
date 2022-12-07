# flake8: noqa
import os
import sys

import click
import pandas as pd
import requests
from flask.cli import with_appcontext

from src import db
from src.models import (
    Class,
    Country,
    Data,
    Family,
    Genus,
    Kingdom,
    Order,
    Phylum,
    Species,
)


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


def open_file():
    file_name = input("Input the file name:\n ")
    file_path = os.path.abspath(file_name)
    data = pd.read_csv(
        file_path,
        header=0,
        sep="\t",
    )
    return data


@click.command(name="seed_kingdom")
@with_appcontext
def seed_kingdom():
    sys.stdout.write("=== Importing Organism Kingdom ===")
    data = open_file()
    data = data[["kingdom", "kingdomKey"]].dropna(axis=0).drop_duplicates()
    data.index = [x for x in range(len(data))]

    print(data.head())
    for indx in range(len(data)):
        if not Kingdom.query.filter_by(id=int(data["kingdomKey"][indx])).first():
            db.session.add(
                Kingdom(
                    id=int(data["kingdomKey"][indx]),
                    kingdom=data["kingdom"][indx],
                )
            )

        db.session.commit()
    sys.stdout.write("=== Done seeding Organism Kingdom ===")


@click.command(name="seed_phylum")
@with_appcontext
def seed_phylum():
    sys.stdout.write("=== Importing Organism Phylum ===")

    data = open_file()
    data = data[["phylum", "phylumKey"]].dropna(axis=0).drop_duplicates()
    data.index = [x for x in range(len(data))]

    print(data.head())
    for indx in range(len(data)):
        if not Phylum.query.filter_by(id=int(data["phylumKey"][indx])).first():
            db.session.add(
                Phylum(
                    id=int(data["phylumKey"][indx]),
                    phylum=data["phylum"][indx],
                )
            )

        db.session.commit()
    sys.stdout.write("=== Done seeding Organism Phylum ===")


@click.command(name="seed_class")
@with_appcontext
def seed_class():
    sys.stdout.write("=== Importing Organism Class ===")
    data = open_file()
    data = data[["class", "classKey"]].dropna(axis=0).drop_duplicates()
    data.index = [x for x in range(len(data))]

    print(data.head())
    for indx in range(len(data)):
        if not Class.query.filter_by(id=int(data["classKey"][indx])).first():
            db.session.add(
                Class(
                    id=int(data["classKey"][indx]),
                    class_name=data["class"][indx],
                )
            )

        db.session.commit()
    sys.stdout.write("=== Done seeding Organism Class ===")


@click.command(name="seed_order")
@with_appcontext
def seed_order():
    sys.stdout.write("=== Importing Organism Order ===")

    data = open_file()
    data = data[["order", "orderKey"]].dropna(axis=0).drop_duplicates()
    data.index = [x for x in range(len(data))]

    print(data.head())
    for indx in range(len(data)):
        if not Order.query.filter_by(id=int(data["orderKey"][indx])).first():
            db.session.add(
                Order(
                    id=int(data["orderKey"][indx]),
                    order=data["order"][indx],
                )
            )

        db.session.commit()
    sys.stdout.write("=== Done seeding Organism Order ===")


@click.command(name="seed_family")
@with_appcontext
def seed_family():
    sys.stdout.write("=== Importing Organism Family ===")

    data = open_file()
    data = data[["family", "familyKey"]].dropna(axis=0).drop_duplicates()
    data.index = [x for x in range(len(data))]

    print(data.head())
    for indx in range(len(data)):
        if not Family.query.filter_by(id=int(data["familyKey"][indx])).first():
            db.session.add(
                Family(
                    id=int(data["familyKey"][indx]),
                    family=data["family"][indx],
                )
            )

        db.session.commit()
    sys.stdout.write("=== Done seeding Organism Family ===")


@click.command(name="seed_genus")
@with_appcontext
def seed_genus():
    sys.stdout.write("=== Importing Organism Genus ===")

    data = open_file()
    data = data[["genus", "genusKey"]].dropna(axis=0).drop_duplicates()
    data.index = [x for x in range(len(data))]

    print(data.head())
    for indx in range(len(data)):
        if not Genus.query.filter_by(id=int(data["genusKey"][indx])).first():
            db.session.add(
                Genus(
                    id=int(data["genusKey"][indx]),
                    genus=data["genus"][indx],
                )
            )

        db.session.commit()
    sys.stdout.write("=== Done seeding Organism Genus ===")


@click.command(name="seed_species")
@with_appcontext
def seed_species():
    sys.stdout.write("=== Importing Organism Species ===")

    data = open_file()
    # data = data[["species", "speciesKey"]].dropna(axis=0).drop_duplicates()
    # data.index = [x for x in range(len(data))]

    print(data.head())
    for indx in range(len(data)):
        try:
            int(data["speciesKey"][indx])
        except:
            continue

        try:
            species = data["species"][indx]
        except:
            species = None

        try:
            taxonKey = int(data["taxonKey"][indx])
        except:
            taxonKey = None

        try:
            acceptedTaxonKey = int(data["acceptedTaxonKey"][indx])
        except:
            acceptedTaxonKey = None

        try:
            scientificName = data["scientificName"][indx]
        except:
            scientificName = None

        try:
            acceptedscientificName = data["acceptedscientificName"][indx]
        except:
            acceptedscientificName = None

        try:
            numberOfOccurrences = int(data["numberOfOccurrences"][indx])
        except:
            numberOfOccurrences = None

        try:
            taxonRank = data["taxonRank"][indx]
        except:
            taxonRank = None

        try:
            taxonomicStatus = data["taxonomicStatus"][indx]
        except:
            taxonomicStatus = None

        try:
            iucnRedListCategory = data["iucnRedListCategory"][indx]
        except:
            iucnRedListCategory = None

        try:
            kingdomKey = (
                Kingdom.query.filter_by(id=int(data["kingdomKey"][indx])).first().id
            )
        except:
            kingdomKey = None

        try:
            phylumKey = (
                Phylum.query.filter_by(id=int(data["phylumKey"][indx])).first().id
            )
        except:
            phylumKey = None

        try:
            classKey = Class.query.filter_by(id=int(data["classKey"][indx])).first().id
        except:
            classKey = None

        try:
            orderKey = Order.query.filter_by(id=int(data["orderKey"][indx])).first().id
        except:
            orderKey = None

        try:
            familyKey = (
                Family.query.filter_by(id=int(data["familyKey"][indx])).first().id
            )
        except:
            familyKey = None

        try:
            genusKey = Genus.query.filter_by(id=int(data["genusKey"][indx])).first().id
        except:
            genusKey = None

        if not Species.query.filter_by(id=int(data["speciesKey"][indx])).first():

            db.session.add(
                Species(
                    species=species,
                    taxonKey=taxonKey,
                    acceptedTaxonKey=acceptedTaxonKey,
                    scientificName=scientificName,
                    acceptedscientificName=acceptedscientificName,
                    numberOfOccurrences=numberOfOccurrences,
                    taxonRank=taxonRank,
                    taxonomicStatus=taxonomicStatus,
                    iucnRedListCategory=iucnRedListCategory,
                    kingdomKey=kingdomKey,
                    phylumKey=phylumKey,
                    classKey=classKey,
                    orderKey=orderKey,
                    familyKey=familyKey,
                    genusKey=genusKey,
                )
            )

        db.session.commit()
    sys.stdout.write("=== Done seeding Organism Species ===")


@click.command(name="seed_gbif")
@with_appcontext
def fetch_gbif_data():
    sys.stdout.write("=== Seeding Species data from GBIF ===")
    species = Species.query.all()
    for indx in species:
        specie_name = indx.species
        url = f"""https://www.gbif.org/api/occurrence/search?advanced=false&dwca_extension.\
            facetLimit=1000&facetMultiselect=true&issue.facetLimit=1000&locale=en&month.\
                facetLimit=12&q={specie_name}&type_status.facetLimit=1000"""
        response = requests.get(url)

        response = response.json()
        print(len(response["results"]))
        for val in response["results"]:
            try:
                country = val["country"]
            except:
                country = None

            try:
                country_code = val["countryCode"]
            except:
                country_code = None

            try:
                gbifID = val["gbifID"]
            except:
                gbifID = None

            try:
                basisOfRecord = val["basisOfRecord"]
            except:
                basisOfRecord = None

            try:
                occurrenceStatus = val["occurrenceStatus"]
            except:
                occurrenceStatus = None

            try:
                decimalLongitude = val["decimalLongitude"]
            except:
                decimalLongitude = None

            try:
                decimalLatitude = val["decimalLatitude"]
            except:
                decimalLatitude = None

            try:
                year = val["year"]
            except:
                year = None

            try:
                month = val["month"]
            except:
                month = None

            try:
                day = val["day"]
            except:
                day = None

            if country is None:
                country_data = None

            if country_code is None:
                country_data_code = None
            else:
                country_data = Country.query.filter_by(
                    country_name=country, country_code=country_code
                ).first()
            if country_data is None:

                country_data = Country(country_name=country, country_code=country_code)
                db.session.add(country_data)
                db.session.commit()

            if "year" not in val.keys():
                pass
            try:
                country_data = country_data.id
            except:
                country_data = None

            db.session.add(
                Data(
                    day=day,
                    month=month,
                    year=year,
                    latitude=decimalLatitude,
                    longitude=decimalLongitude,
                    speciesKey=indx.id,
                    countryKey=country_data,
                    occurrenceStatus=occurrenceStatus,
                    basisOfRecord=basisOfRecord,
                    gbifId=gbifID,
                    gbifIdLink=f"https://www.gbif.org/occurrence/{gbifID}",
                )
            )

        db.session.commit()
    sys.stdout.write("=== Done seeding Specie data from GBIF ===")
