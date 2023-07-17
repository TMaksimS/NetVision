start:
	docker compose -f docker-compose-local.yaml up -d
migrations: start
	sleep 1 && alembic upgrade head
up: migrations
	python3 main.py
down:
	docker compose -f docker-compose-local.yaml down --remove-orphans
up_ci:
	docker compose -f docker-compose-ci.yaml up -d && docker logs app && docker logs client_app --follow
down_ci:
	docker compose -f docker-compose-ci.yaml down --remove-orphans && docker rmi myapp
