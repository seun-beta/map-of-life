build:
	docker-compose -f docker-compose.yaml build
up:
	docker-compose -f docker-compose.yaml up
down:
	docker-compose -f docker-compose.yaml down
create_tables:
	docker-compose exec api flask create_tables
drop_create_tables:
	docker-compose exec api flask drop_create_tables
