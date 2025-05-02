all:
	docker-compose up -d --build

run:
	docker-compose up -d

build:
	docker-compose up --build

down:
	docker-compose down

prune:
	docker system prune

makemg:
	docker-compose exec webapp python manage.py makemigrations
	
migrate:
	docker-compose exec webapp python manage.py migrate

makemigrations:
	docker-compose exec webapp python manage.py makemigrations

shell:
	docker-compose exec webapp python manage.py shell

createsuperuser:
	docker-compose exec webapp python manage.py createsuperuser