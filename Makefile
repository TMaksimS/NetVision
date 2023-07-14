up:
	docker compose -f docker-compose-local.yaml up -d
down:
	docker compose -f docker-compose-local.yaml down --remove-orphans
up_ci:
	docker compose -f docker-compose-ci.yaml up -d
down_ci:
	docker compose -f docker-compose-ci.yaml down --remove-orphans
