from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Kingdom(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    kingdom = db.Column(db.String(512), unique=True, nullable=False)

    def __repr__(self):
        return "<Kingdom %r>" % self.kingdom


class Phylum(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    phylum = db.Column(db.String(512), unique=True, nullable=False)

    def __repr__(self):
        return "<Phylum %r>" % self.phylum


class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    class_name = db.Column(db.String(512), unique=True, nullable=False)

    def __repr__(self):
        return "<Class %r>" % self.class_name


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    order = db.Column(db.String(512), nullable=False)

    def __repr__(self):
        return "<Order %r>" % self.order


class Family(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    family = db.Column(db.String(512), nullable=False)

    def __repr__(self):
        return "<Family %r>" % self.family


class Genus(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    genus = db.Column(db.String(512), nullable=False)

    def __repr__(self):
        return "<Genus %r>" % self.genus


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    day = db.Column(db.Integer, nullable=True)
    month = db.Column(db.Integer, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    country = db.Column(db.String(512), nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)


class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    species = db.Column(db.String(512), nullable=False)

    taxonKey = db.Column(db.Integer, nullable=True)
    scientificName = db.Column(db.String(512), nullable=True)
    acceptedTaxonKey = db.Column(db.Integer, nullable=True)
    acceptedscientificName = db.Column(db.String(512), nullable=True)
    numberOfOccurrences = db.Column(db.Integer, nullable=True)
    taxonRank = db.Column(db.String(512), nullable=True)
    taxonomicStatus = db.Column(db.String(512), nullable=True)
    iucnRedListCategory = db.Column(db.String(512), nullable=True)

    kingdomKey = db.Column(db.Integer, db.ForeignKey("kingdom.id"), nullable=True)
    kingdom = db.relationship("Kingdom", backref="kingdom_ref")

    phylumKey = db.Column(db.Integer, db.ForeignKey("phylum.id"), nullable=True)
    phylum = db.relationship("Phylum", backref="phylum_ref")

    classKey = db.Column(db.Integer, db.ForeignKey("class.id"), nullable=True)
    class_name = db.relationship("Class", backref="class_ref")

    orderKey = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=True)
    order = db.relationship("Order", backref="order_ref")

    familyKey = db.Column(db.Integer, db.ForeignKey("family.id"), nullable=True)
    family = db.relationship("Family", backref="family_ref")

    genusKey = db.Column(db.Integer, db.ForeignKey("genus.id"), nullable=True)
    genus = db.relationship("Genus", backref="genus_ref")

    speciesKey = db.Column(db.Integer, db.ForeignKey("data.id"), nullable=True)
    data = db.relationship("Data", backref="data_ref")

    def __repr__(self):
        return "<Species %r>" % self.species
