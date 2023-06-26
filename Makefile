SHELL=/bin/bash
PYTHON=python3
PYTHON_ENV=env

DJANGO_SETTINGS_MODULE=test_django_project._django.settings
DJANGO_DATABASE_NAME=test-django-project/db.sqlite3

.PHONY: all clean npm-dependencies dist _release \
	test-script test-project test-django-project


all: | test-script

clean:
	rm -rf node_modules
	rm -rf $(PYTHON_ENV)

# python ######################################################################
$(PYTHON_ENV): pyproject.toml
	rm -rf $(PYTHON_ENV) && \
	$(PYTHON) -m venv $(PYTHON_ENV) && \
	. $(PYTHON_ENV)/bin/activate && \
	pip install pip --upgrade && \
	pip install -e .[packaging,test] \
	pip install -e test-django-project

# npm #########################################################################
node_modules: package.json
	npm install

npm-dependencies: | node_modules
	rm -rf $(DIST_ROOT)
	mkdir -p $(DIST_ROOT)

	# picocss
	mkdir -p $(DIST_ROOT)/pico
	cp node_modules/@picocss/pico/LICENSE.md $(DIST_ROOT)/pico
	cp -r node_modules/@picocss/pico/css $(DIST_ROOT)/pico/css
	cp -r node_modules/@picocss/pico/scss $(DIST_ROOT)/pico/scss

	# feather icons
	mkdir -p $(DIST_ROOT)/feather-icons
	cp node_modules/feather-icons/LICENSE $(DIST_ROOT)/feather-icons
	cp -r node_modules/feather-icons/dist/* $(DIST_ROOT)/feather-icons
	rm -rf $(DIST_ROOT)/feather-icons/icons

# packaging ###################################################################
dist: $(PYTHON_ENV)
	. $(PYTHON_ENV)/bin/activate && \
	rm -rf dist *.egg-info && \
	python -m build

_release: dist
	. $(PYTHON_ENV)/bin/activate && \
	twine upload --config-file ~/.pypirc.fscherf dist/*

# tests ########################################################################
test:
	docker-compose run playwright tox $(args)

test-script: $(PYTHON_ENV)
	. $(PYTHON_ENV)/bin/activate && \
	$(PYTHON) test-script/test_script.py $(args)

test-project: | $(PYTHON_VENV)
	. $(PYTHON_ENV)/bin/activate && \
	lona run-server \
		--project-root=test-project \
		-s settings.py \
		$(args)

# django
smtp-server: $(PYTHON_ENV)
	. $(PYTHON_ENV)/bin/activate && \
	python -m smtpd -c DebuggingServer -n localhost:1025

$(DJANGO_DATABASE_NAME): | $(PYTHON_ENV)
	. $(PYTHON_ENV)/bin/activate && \
	DJANGO_SETTINGS_MODULE=$(DJANGO_SETTINGS_MODULE) django-admin migrate && \
	DJANGO_SETTINGS_MODULE=$(DJANGO_SETTINGS_MODULE) django-admin createsuperuser

test-django-project: | $(PYTHON_ENV) $(DJANGO_DATABASE_NAME)
	. $(PYTHON_ENV)/bin/activate && \
	lona run-server \
		--project-root=test-django-project \
		-s settings.py \
		$(args)
