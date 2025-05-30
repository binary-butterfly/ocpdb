DOCKER_COMPOSE = docker compose
FLASK_RUN = $(DOCKER_COMPOSE) run --rm flask

# Separate environment for running integration tests
TESTING_COMPOSE_PROJECT_NAME = ocpdb_integrationtests
TESTING_DOCKER_COMPOSE = $(DOCKER_COMPOSE) -p $(TESTING_COMPOSE_PROJECT_NAME)

# Default target when running `make`
.PHONY: all
all: docker-up


# Configuration
# -------------

.PHONY: config
config: .env config.yaml

# Create .env file to set the UID/GID for the docker containers to run as to the current user
.env:
	echo "DOCKER_LOCAL_USER=$(shell id -u):$(shell id -g)" >> .env

# Create config file from config_dist_dev.yaml if it does not exist yet
config.yaml:
	cp config_dist_dev.yaml config.yaml


# Container management
# --------------------

.PHONY: first-start
first-start: config docker-build migrate
	$(DOCKER_COMPOSE) down
	@echo
	@echo 'Database is all set up! \o/'
	@echo 'You can now start the project with "make docker-up"'

# Builds and starts all docker containers
.PHONY: docker-up
docker-up: config docker-build
	$(DOCKER_COMPOSE) up

# Start containers in background (or recreate containers while they are running attached to another terminal)
.PHONY: docker-up-detached
docker-up-detached: config docker-build
	$(DOCKER_COMPOSE) up --detach

.PHONY: docker-down
docker-down: .env
	$(DOCKER_COMPOSE) down --remove-orphans
	$(TESTING_DOCKER_COMPOSE) down --remove-orphans

.PHONY: docker-testing-down
docker-testing-down: .env
	$(TESTING_DOCKER_COMPOSE) down --remove-orphans --volumes

# Restart all containers (default) or only the containers specified by SERVICE (e.g. `make docker-restart SERVICE=flask`)
.PHONY: docker-restart
docker-restart: .env
	$(DOCKER_COMPOSE) restart $(SERVICE)

# Tear down all containers and delete all volumes
.PHONY: docker-purge
docker-purge: .env
	$(DOCKER_COMPOSE) down --remove-orphans --volumes
	$(TESTING_DOCKER_COMPOSE) down --remove-orphans --volumes

# Build the Docker image for the flask service
.PHONY: docker-build
docker-build: .env
	$(DOCKER_COMPOSE) build flask

# Force a rebuild of all images (including pulling the base images)
.PHONY: docker-rebuild
docker-rebuild: .env
	$(DOCKER_COMPOSE) build --no-cache --pull flask

# Pull all images except for locally built images
.PHONY: docker-pull
docker-pull: .env
	$(DOCKER_COMPOSE) pull webpack mysql phpmyadmin redis rabbitmq elasticsearch fakemail

# Show application logs, optionally with `make docker-logs SERVICE=flask` only for specified containers
.PHONY: docker-logs
docker-logs: .env
	$(DOCKER_COMPOSE) logs -f $(SERVICE)

# Run arbitrary commands in the flask docker container
.PHONY: docker-run
docker-run: config
	@test -n "$(CMD)" || ( echo 'Usage: make docker-run CMD="insert command here"'; exit 1 )
	$(FLASK_RUN) $(CMD)

# Start a shell (bash) in the flask docker container
.PHONY: docker-shell
docker-shell: config
	$(FLASK_RUN) bash

# Start an interactive Python shell with Flask application context in a docker container
.PHONY: flask-shell
flask-shell: config
	$(FLASK_RUN) flask shell


# Database management
# -------------------

# Updates the database to the current version
.PHONY: migrate
migrate: config
	$(FLASK_RUN) flask db upgrade


# Cleanup
# -------
# Clean up "volatile" files (caches, test reports, venv, generated assets, ...)
.PHONY: clean
clean: docker-down
	rm -rf logs/ venv/  reports/ .pytest_cache .coverage

# Clean up whole environment (like "clean", but also removes config files and database files)
.PHONY: clean-all
clean-all: docker-purge clean
	rm config.yaml .env


# Test suites
# -----------

# Run unit tests only
.PHONY: test
test: test-unit

# Run all test suites (unit and integration tests) in a separate environment
# and generate combined coverage report in HTML format
.PHONY: test-all
test-all: config
	# remove possibly leftover containers from previous integration test runs
	$(TESTING_DOCKER_COMPOSE) down --remove-orphans --volumes
	# run tests
	$(TESTING_DOCKER_COMPOSE) run --rm -e CONFIG_FILE=config_dist_dev.yaml flask python -m pytest tests/unit \
		tests/integration --cov=webapp --cov-report=html:reports/coverage_html/
	$(TESTING_DOCKER_COMPOSE) down


# Run unit tests only and generate coverage report in HTML format
.PHONY: test-unit
test-unit: config
	$(DOCKER_COMPOSE) run --rm -e COVERAGE_FILE=.coverage.unit_test -e CONFIG_FILE=config_dist_dev.yaml flask \
	python -m pytest tests/unit --cov=webapp --cov-report=html:reports/coverage_unit_html/

# Run integration tests in a separate environment and generate coverage report in HTML format
.PHONY: test-integration
test-integration: config
	$(TESTING_DOCKER_COMPOSE) run --rm -e COVERAGE_FILE=.coverage.integration_test -e CONFIG_FILE=config_dist_dev.yaml \
	flask python -m pytest tests/integration --cov=webapp --cov-report=html:reports/coverage_integration_html/
	$(TESTING_DOCKER_COMPOSE) down

# Open combined unit and integration test coverage report in browser
# (determined by BROWSER env variable, defaults to firefox)
.PHONY: open-coverage
open-coverage:
	@test -f ./reports/coverage_html/index.html || make test-all
	$(or $(BROWSER),firefox) ./reports/coverage_html/index.html

# Open unit test coverage report in browser (determined by BROWSER env variable, defaults to firefox)
.PHONY: open-coverage-unit
open-coverage-unit:
	@test -f ./reports/coverage_unit_html/index.html || make test-unit
	$(or $(BROWSER),firefox) ./reports/coverage_unit_html/index.html

# Open integration test coverage report in browser (determined by BROWSER env variable, defaults to firefox)
.PHONY: open-coverage-integration
open-coverage-integration:
	@test -f ./reports/coverage_integration_html/index.html || make test-integration
	$(or $(BROWSER),firefox) ./reports/coverage_integration_html/index.html


# Linting
# -----------

.PHONY: lint-fix
lint-fix:
	$(FLASK_RUN) ruff format ./webapp ./tests ./migrations
	$(FLASK_RUN) ruff check --fix ./webapp ./tests ./migrations

.PHONY: lint-check
lint-check:
	$(FLASK_RUN) ruff format --check ./webapp ./tests ./migrations
	$(FLASK_RUN) ruff check ./webapp ./tests ./migrations
