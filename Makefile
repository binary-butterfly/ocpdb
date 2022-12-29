CURRENT_UID = $(shell id -u):$(shell id -g)

DOCKER_COMPOSE_FILE = docker-compose.yml
DOCKER_COMPOSE = CURRENT_UID=$(CURRENT_UID) docker-compose -f $(DOCKER_COMPOSE_FILE)

TESTING_COMPOSE_PROJECT_NAME = ocpdb_tests
TESTING_DOCKER_COMPOSE = $(DOCKER_COMPOSE) -p $(TESTING_COMPOSE_PROJECT_NAME)
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

config: config.yaml

# Create config file from config_dist_dev.py if it does not exist yet
config.yaml:
	cp config_dist_dev.yaml config.yaml


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
	rm -f config.yaml


# Test suites
# -----------
# Run unit tests only
test: test-unit

# Run all test suites (unit and integration tests)
test-all: test-unit test-integration

# Run unit tests only and generate coverage report in HTML format
test-unit:
	$(FLASK_RUN) python -m pytest tests/unit --cov=webapp --cov-report=html

# Run integration tests in a separate environment
test-integration:
	$(TESTING_DOCKER_COMPOSE) run --rm flask ./wait_for_services.sh python -m pytest tests/integration
	$(TESTING_DOCKER_COMPOSE) down

# Open coverage report in browser (determined by BROWSER env variable, defaults to firefox)
open-coverage:
	@test -f ./reports/coverage_html/index.html || make test-unit
	$(or $(BROWSER),firefox) ./reports/coverage_html/index.html


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
