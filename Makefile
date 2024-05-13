# Delete target on error.
# https://www.gnu.org/software/make/manual/html_node/Errors.html#Errors
# > This is almost always what you want make to do, but it is not historical
# > practice; so for compatibility, you must explicitly request it
.DELETE_ON_ERROR:

# Global tasks.
# =============================================================================
PYTHON_VERSION := python3.11
LINTER_CHECKED_DIRS := config pilotage

REQUIREMENTS_PATH ?= requirements.txt

VIRTUAL_ENV ?= .venv
export PATH := $(VIRTUAL_ENV)/bin:$(PATH)

VENV_REQUIREMENT := $(VIRTUAL_ENV)

runserver: $(VIRTUAL_ENV)
	python manage.py runserver $(RUNSERVER_DOMAIN)

$(VIRTUAL_ENV): $(REQUIREMENTS_PATH)
	$(PYTHON_VERSION) -m venv $@
	$@/bin/pip install -r $^
	$@/bin/pip-sync $^
	touch $@

venv: $(VIRTUAL_ENV)

clean:
	find . -type d -name "__pycache__" -depth -exec rm -rf '{}' \;

fast_fix: $(VENV_REQUIREMENT)
	black $(LINTER_CHECKED_DIRS)
	ruff check --fix $(LINTER_CHECKED_DIRS)
	find * -type f -name '*.sh' -exec shellcheck --external-sources --format=diff {} + | git apply --allow-empty

fix: fast_fix
	djlint --reformat pilotage

