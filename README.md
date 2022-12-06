# Map of Life


## Table of Contents

- [About](#about)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

### Map Of Life

### Process Outline:
I inspected the csv file and determined a pattern as regards taxonomy. The data set was then split into various logical table as follows:

1) Kingdom
2) Phylum
3) Clas
4) Order
5) Family
6) Genus
7) Species
8) Data
9) Country

The Species table holds information regarding distinct species. The Data table holds occurrence information about each specie. The data used to populate the Data table is extracted from gbif.org using the REST API service from GBIF. The country model contains country data also extracted from GBIF.

### Technology Stack:
The technology stack used include
- Python 3.10
- Flask 2.2.2
- PostgreSQL
- Flask SQLAlchemy as the Object Relational Mapper (ORM). I used the ORM because of it's easy integration with Flask. The ORM also helped to provide a python layer over raw SQL queries.
- Docker
- Docker Compose. I used Docker Compose to manage multiple containers ( flask server and postgres database)
- Flasgger. The 3 API's were documented according to Open API 2.0
- Pandas and Numpy packages were used for data analysis and data processing. This is so because of the large amount of data being proccessed.

### Challenges working with large datasets.
Some of the challenges I faced working with large datasets is computational power. Processing large datasets takes a large amount of computation power. Anothe challenge I faced was the network overhead from extracting data from the GBIF REST API.



## Prerequisites <a name = "prerequisites"></a>

- Python 3.10
- Docker


## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

 - Run `git clone https://github.com/seun-beta/map-of-life` to clone the project locally.
 - Create a local postgres database locally and add it's url to the DATBASE_URL env variable.
 - Run `pip install -r requirements/development.txt`
 - Create DB models and start server using the command: `flask drop_create_tables && flask seed_kingdom && flask seed_phylum && flask seed_class && flask seed_order && flask seed_family && flask seed_genus && flask seed_species && flask seed_gbif`.

### Run without docker compose
* Start the app with `flask run`
### Run with docker compose
1) Run `make build` to build all the container images
2) Run  `make up` to run the images in seperate containers
3) Run `make seed_all` to seed all data into the database

### Swagger Documentation
* The Swagger documentation can be found here http://127.0.0.1:8000/
