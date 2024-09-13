SHELL := /bin/bash
.ONESHELL:
VENV_FOLDER = env
DJANGO_PATH = crested_myna
APP_DB = app_db

lint:
	source $(VENV_FOLDER)/bin/activate;
	pylint $(DJANGO_PATH)/backend $(DJANGO_PATH)/index_view $(DJANGO_PATH)/crested_myna || true

autopep:
	source $(VENV_FOLDER)/bin/activate;
	find . -name '*.py' \
		-not -path "*/migrations/*" \
		-not -path "*/env/lib/*" \
		-exec autopep8 --in-place '{}' \;

test:
	source $(VENV_FOLDER)/bin/activate;
	cd $(DJANGO_PATH);
	python manage.py test

recreate-db:
	echo app db $(APP_DB)
	echo "DROP DATABASE \"$(APP_DB)\" WITH(FORCE);" | psql -d postgres
	echo "CREATE DATABASE \"$(APP_DB)\";" | psql -d postgres

new-migration-file:
	source $(VENV_FOLDER)/bin/activate;
	cd $(DJANGO_PATH);
	python manage.py makemigrations backend --empty
