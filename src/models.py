from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Kingdom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kingdom = db.Column(db.String(512), unique=True, nullable=False)

    def __repr__(self):
        return "<Kingdom %r>" % self.kingdom


class Phylum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phylum = db.Column(db.String(512), unique=True, nullable=False)

    def __repr__(self):
        return "<Phylum %r>" % self.phylum


class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(512), unique=True, nullable=False)

    def __repr__(self):
        return "<Class %r>" % self.class_name


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.String(512), unique=True, nullable=False)

    def __repr__(self):
        return "<Order %r>" % self.order


class Family(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    family = db.Column(db.String(512), unique=True, nullable=False)

    def __repr__(self):
        return "<Family %r>" % self.family


class Genus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genus = db.Column(db.String(512), unique=True, nullable=False)

    def __repr__(self):
        return "<Genus %r>" % self.genus


class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(512), unique=True, nullable=False)

    def __repr__(self):
        return "<Species %r>" % self.species


class Organism(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taxonKey = db.Column(db.Integer, nullable=True)
    scientificName = db.Column(db.String(512), nullable=True)
    acceptedTaxonKey = db.Column(db.Integer, nullable=True)
    acceptedscientificName = db.Column(db.String(512), nullable=True)
    numberOfOccurrences = db.Column(db.Integer, nullable=True)
    taxonRank = db.Column(db.String(512), nullable=True)
    taxonomicStatus = db.Column(db.String(512), nullable=True)
    iucnRedListCategory = db.Column(db.String(512), nullable=True)

    kingdomKey = db.Column(db.Integer, db.ForeignKey("kingdom.id"))
    phylumKey = db.Column(db.Integer, db.ForeignKey("phylum.id"))
    classKey = db.Column(db.Integer, db.ForeignKey("class.id"))
    orderKey = db.Column(db.Integer, db.ForeignKey("order.id"))
    familyKey = db.Column(db.Integer, db.ForeignKey("family.id"))
    genusKey = db.Column(db.Integer, db.ForeignKey("genus.id"))
    speciesKey = db.Column(db.Integer, db.ForeignKey("species.id"))
