SHELL=/bin/bash
PYTHON=python3

DIST_ROOT=lona_picocss/static/lona-picocss/dist

PYTHON_ENV_ROOT=envs
PYTHON_DEV_ENV=$(PYTHON_ENV_ROOT)/$(PYTHON)-dev
PYTHON_PACKAGING_ENV=$(PYTHON_ENV_ROOT)/$(PYTHON)-packaging
PYTHON_TESTING_ENV=$(PYTHON_ENV_ROOT)/$(PYTHON)-testing


.PHONY: all clean pull-picocss shell python-shell test-script dist _release

all: | test-script

clean:
	rm -rf node_modules
	rm -rf $(PYTHON_ENV_ROOT)

# npm #########################################################################
node_modules: package.json
	npm install

pull-picocss: | node_modules
	rm -rf $(DIST_ROOT)
	mkdir -p $(DIST_ROOT)
	cp node_modules/@picocss/pico/css/pico.min.css $(DIST_ROOT)

# python ######################################################################
$(PYTHON_DEV_ENV): pyproject.toml
	rm -rf $(PYTHON_DEV_ENV) && \
	$(PYTHON) -m venv $(PYTHON_DEV_ENV) && \
	. $(PYTHON_DEV_ENV)/bin/activate && \
	pip install pip --upgrade && \
	pip install -e .

$(PYTHON_PACKAGING_ENV): pyproject.toml
	rm -rf $(PYTHON_PACKAGING_ENV) && \
	$(PYTHON) -m venv $(PYTHON_PACKAGING_ENV) && \
	. $(PYTHON_PACKAGING_ENV)/bin/activate && \
	pip install --upgrade pip && \
	pip install .[packaging]

$(PYTHON_TESTING_ENV): pyproject.toml
	rm -rf $(PYTHON_TESTING_ENV) && \
	$(PYTHON) -m venv $(PYTHON_TESTING_ENV) && \
	. $(PYTHON_TESTING_ENV)/bin/activate && \
	pip install --upgrade pip && \
	pip install .[testing]

# helper
shell: $(PYTHON_DEV_ENV)
	. $(PYTHON_DEV_ENV)/bin/activate && \
	/bin/bash

python-shell: $(PYTHON_DEV_ENV)
	. $(PYTHON_DEV_ENV)/bin/activate && \
	rlpython

# tests
test-script: $(PYTHON_DEV_ENV)
	. $(PYTHON_DEV_ENV)/bin/activate && \
	$(PYTHON) test-script/test_script.py $(args)

# packaging
dist: $(PYTHON_PACKAGING_ENV)
	. $(PYTHON_PACKAGING_ENV)/bin/activate && \
	rm -rf dist *.egg-info && \
	python -m build

_release: all dist
	. $(PYTHON_PACKAGING_ENV)/bin/activate && \
	twine upload --config-file ~/.pypirc.fscherf dist/*

# tests #######################################################################
testclean:
	rm -rf $(PYTHON_ENV)
	rm -rf tests/.tox

pytest: | $(PYTHON_TESTING_ENV)
	. $(PYTHON_TESTING_ENV)/bin/activate && \
	cd tests && \
	tox $(args)

test-docker-build:
	docker-compose \
		-f tests/docker/docker-compose.yml \
		rm -f

	docker-compose \
		-f tests/docker/docker-compose.yml \
		build --no-cache

test:
	DOCKER_USER=$$(id -u):$$(id -g) \
	ARGS=$(args) \
		docker-compose \
			-f tests/docker/docker-compose.yml \
			run lona-picocss-pytest
