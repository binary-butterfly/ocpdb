CURRENT_UID = $(shell id -u):$(shell id -g)

DOCKER_COMPOSE_FILE = docker-compose.yml
DOCKER_COMPOSE = CURRENT_UID=$(CURRENT_UID) docker-compose -f $(DOCKER_COMPOSE_FILE)
FLASK_RUN = $(DOCKER_COMPOSE) run --rm flask

DOCKER_REGISTRY = registry.git.sectio-aurea.org

DEV_PUSH_TARGET = "$(DEV_PUSH_USER)@$(DEV_PUSH_HOST):$(DEV_PUSH_ROOT_DIR)/backend/"

# Include file with environment variables if it exists
-include Makefile.env

.PHONY: all config docker-login docker-up docker-up-detached docker-down docker-purge docker-rebuild docker-logs flask-run \
        migrate prepare-unittest elasticsearch-index clean test test-unit test-integration dev-push dev-push-docker-compose

# Default target when running `make`
all: docker-up


# Configuration
# -------------

config: webapp/config.py

# Create config file from config_dist_dev.py if it does not exist yet
webapp/config.py:
	cp webapp/config_dist_dev.py webapp/config.py


# Container management
# --------------------

# Login to Docker registry
docker-login:
	docker login $(DOCKER_REGISTRY)

# Builds and starts all docker containers
docker-up: config
	$(DOCKER_COMPOSE) up --build

# Start containers in background (or recreate containers while they are running attached to another terminal)
docker-up-detached: config
	$(DOCKER_COMPOSE) up --build --detach

docker-down:
	$(DOCKER_COMPOSE) down

# Tear down all containers and delete all volumes
docker-purge:
	$(DOCKER_COMPOSE) down --volumes

# Force a rebuild of all images (including pulling the base images)
docker-rebuild:
	$(DOCKER_COMPOSE) build --no-cache --pull

# Show application logs, optionally with `make docker-logs SERVICE=flask` only for specified containers
docker-logs:
	$(DOCKER_COMPOSE) logs -f $(SERVICE)

# Run arbitrary commands in the flask container
flask-run:
	@test -n "$(CMD)" || ( echo 'Usage: make flask-run CMD="flask"' && exit 1 )
	$(FLASK_RUN) $(CMD)


# Database management
# -------------------

# Updates the database to the current version
migrate: config
	$(FLASK_RUN) flask db upgrade


# Cleanup
# -------
clean: docker-down
	rm -f webapp/config.py


# Test suites
# -----------
# Run all test suites (all 'testpaths' in pytest.ini)
test:
	$(FLASK_RUN) python -m pytest

# Run unit tests only
test-unit:
	$(FLASK_RUN) python -m pytest tests/unit

# Run integration tests only
test-integration:
	$(FLASK_RUN) python -m pytest tests/integration


# Development environments
# ------------------------
dev-push:
	rsync -auv --delete-after \
		--exclude-from=.gitignore \
		--exclude={.git,Makefile.env,docker-compose_local.yml} \
		--include=.gitkeep \
		./ $(DEV_PUSH_TARGET)

dev-push-docker-compose:
	scp ./docker-compose_local.yml $(DEV_PUSH_TARGET)
