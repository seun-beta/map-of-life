import sys

import click
import pandas as pd
from flask.cli import with_appcontext

from src import db
from src.models import Class, Family, Genus, Kingdom, Order, Phylum, Species


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


@click.command(name="seed_kingdom")
@with_appcontext
def seed_kingdom():
    sys.stdout.write("=== Importing Organism Kingdom ===")

    data = pd.read_csv(
        "",
        header=0,
        sep="\t",
    )
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

    data = pd.read_csv(
        "",
        header=0,
        sep="\t",
    )
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

    data = pd.read_csv(
        "",
        header=0,
        sep="\t",
    )
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

    data = pd.read_csv(
        "",
        header=0,
        sep="\t",
    )
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

    data = pd.read_csv(
        "",
        header=0,
        sep="\t",
    )
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

    data = pd.read_csv(
        "",
        header=0,
        sep="\t",
    )
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

    data = pd.read_csv(
        "",
        header=0,
        sep="\t",
    )
    # data = data[["species", "speciesKey"]].dropna(axis=0).drop_duplicates()
    # data.index = [x for x in range(len(data))]

    print(data.head())
    for indx in range(len(data)):
        if not Species.query.filter_by(id=int(data["speciesKey"][indx])).first():
            Kingdom.query.filter_by()

            db.session.add(
                Species(
                    id=int(data["speciesKey"][indx]),
                    species=data["species"][indx] or None,
                    taxonKey=Kingdom.query.get(id=data["taxonKey"][indx]) or None,
                    scientificName=data["scientificName"][indx],
                    acceptedscientificName=data["acceptedscientificName"][indx]
                    or data["scientificName"][indx],
                    numberOfOccurrences=data["numberOfOccurrences"][indx] or None,
                    taxonRank=data["taxonRank"][indx] or None,
                    taxonomicStatus=data["taxonomicStatus"][indx] or None,
                    iucnRedListCategory=data["iucnRedListCategory"][indx] or None,
                    kingdom=Kingdom.query.get(id=data["kingdomKey"][indx]) or None,
                    phylum=Phylum.query.get(id=data["phylumKey"][indx]) or None,
                    classKey=Class.query.get(id=data["classKey"][indx]) or None,
                    orderKey=Order.query.get(id=data["orderKey"][indx]) or None,
                    familyKey=Family.query.get(id=data["familyKey"][indx]) or None,
                    genusKey=Genus.query.get(id=data["genusKey"][indx]) or None,
                )
            )

        db.session.commit()
    sys.stdout.write("=== Done seeding Organism Species ===")
