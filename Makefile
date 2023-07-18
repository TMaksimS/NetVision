start:
	docker compose -f docker-compose-local.yaml up -d
migrations: start
	sleep 5 && alembic upgrade head
up: migrations
	python3 main.py
down:
	docker compose -f docker-compose-local.yaml down --remove-orphans
docker_compose_up:
	docker compose -f docker-compose-ci.yaml up -d
logs_server_app: docker_compose_up
	sleep 5 && docker logs app
up_ci: logs_server_app
	sleep 3 && docker logs client_app --follow
down_ci:
	docker compose -f docker-compose-ci.yaml down --remove-orphans && docker rmi myapp
