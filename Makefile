SHELL := /bin/bash
######################
#
# To setup:
#   make setup venv=name_of_venv
#
# To use other commands make sure the virtualenv is active
#   make install
#
# This fancy makfile will setup a django project for you. It will create the virtualenv that
# you specify, set the project directory, and setup postactivate and decativate files.
# You can also use it for quick installation but that only works on an active environment.
#
######################


# this line finds the folder name to the manage.py folder, we need it for the postactivate
APP := $(shell find . -maxdepth 5 -name 'manage.py' | xargs -I{} dirname {} | xargs -I{} basename {})

MIGRATE=$(shell read -p "Did you create the database? y/n " var; echo $$var;)

#Add a comment to this line

# this doesn't want to run only on setup even when traget is set
# setup: VENV = $(shell if [ -z $(VENV) ] ; then read -p "Virtualenv name (you can decide): " NAME ; echo $$NAME ; fi )
setup:
	@source /usr/local/bin/virtualenvwrapper.sh; mkvirtualenv $(venv); workon $(venv);
	@source /usr/local/bin/virtualenvwrapper.sh; workon $(venv); echo "export PYTHONPATH=\$$PYTHONPATH:$$PWD/website/$(APP)/" >> $$VIRTUAL_ENV/bin/postactivate
	@source /usr/local/bin/virtualenvwrapper.sh; workon $(venv); echo "export DJANGO_SETTINGS_MODULE='$(APP).settings.dev'" >> $$VIRTUAL_ENV/bin/postactivate
	@source /usr/local/bin/virtualenvwrapper.sh; workon $(venv); echo "unset DJANGO_SETTINGS_MODULE" >> $$VIRTUAL_ENV/bin/postdeactivate
	@source /usr/local/bin/virtualenvwrapper.sh; workon $(venv); deactivate;
	@source /usr/local/bin/virtualenvwrapper.sh; workon $(venv); setvirtualenvproject;
	@source /usr/local/bin/virtualenvwrapper.sh; workon $(venv); add2virtualenv $$PWD/website/$(APP)/apps/;
	# git, for compiled files
	git init
	@echo '[merge "ours"]' >> .git/config
	@echo -e '\t name = "Keep ours merge"' >> .git/config
	@echo -e '\t driver = true' >> .git/config



setup_prod:
	@source /usr/local/bin/virtualenvwrapper.sh; mkvirtualenv $(venv); workon $(venv);
	@source /usr/local/bin/virtualenvwrapper.sh; workon $(venv); echo "export PYTHONPATH=\$$PYTHONPATH:$$PWD/website/$(APP)/" >> $$VIRTUAL_ENV/bin/postactivate
	@source /usr/local/bin/virtualenvwrapper.sh; workon $(venv); echo "export DJANGO_SETTINGS_MODULE='$(APP).settings.production'" >> $$VIRTUAL_ENV/bin/postactivate
	@source /usr/local/bin/virtualenvwrapper.sh; workon $(venv); echo "unset DJANGO_SETTINGS_MODULE" >> $$VIRTUAL_ENV/bin/postdeactivate
	@source /usr/local/bin/virtualenvwrapper.sh; workon $(venv); deactivate;
	@source /usr/local/bin/virtualenvwrapper.sh; workon $(venv); setvirtualenvproject;
	@source /usr/local/bin/virtualenvwrapper.sh; workon $(venv); add2virtualenv $$PWD/website/$(APP)/apps/;

install:
	pip install -r website/requirements/dev.txt
	@if [ $(MIGRATE) == 'y' ]; then \
		django-admin.py migrate; \
	else \
		echo "Ok,don't forget to do django-admin.py migrate after"; \
	fi;


deploy:
	git pull
	pip install -r website/requirements/production.txt
	django-admin.py migrate
	django-admin.py collectstatic --noinput
