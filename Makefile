# Delete target on error.
# https://www.gnu.org/software/make/manual/html_node/Errors.html#Errors
# > This is almost always what you want make to do, but it is not historical
# > practice; so for compatibility, you must explicitly request it
.DELETE_ON_ERROR:

PYTHON_VERSION := python3.11
REQUIREMENTS_PATH ?= requirements/dev.txt

VIRTUAL_ENV ?= .venv
export PATH := $(VIRTUAL_ENV)/bin:$(PATH)

# Python dependencies
# =============================================================================
.PHONY: venv compile-deps

$(VIRTUAL_ENV): $(REQUIREMENTS_PATH)
	$(PYTHON_VERSION) -m venv $@
	$@/bin/pip install uv
	$@/bin/uv pip sync --require-hashes $^
	touch $@

venv: $(VIRTUAL_ENV)

PIP_COMPILE_FLAGS := --generate-hashes $(PIP_COMPILE_OPTIONS)
compile-deps: $(VIRTUAL_ENV)
	uv pip compile $(PIP_COMPILE_FLAGS) -o requirements/base.txt requirements/base.in
	uv pip compile $(PIP_COMPILE_FLAGS) -o requirements/dev.txt requirements/dev.in

# Django
# =============================================================================
.PHONY: runserver

runserver: $(VIRTUAL_ENV)
	python manage.py runserver $(RUNSERVER_DOMAIN)

# Quality
# =============================================================================
.PHONY: clean quality fast_fix fix

LINTER_CHECKED_DIRS := config pilotage

clean:
	find . -type d -name "__pycache__" -depth -exec rm -rf '{}' \;

quality: $(VIRTUAL_ENV)
	ruff format --check $(LINTER_CHECKED_DIRS)
	ruff check $(LINTER_CHECKED_DIRS)
	djlint --lint --check $(LINTER_CHECKED_DIRS)
	python manage.py makemigrations --check --dry-run --noinput || (echo "⚠ Missing migration ⚠"; exit 1)
	python manage.py collectstatic --no-input

fast_fix: $(VIRTUAL_ENV)
	ruff format $(LINTER_CHECKED_DIRS)
	ruff check --fix $(LINTER_CHECKED_DIRS)

fix: fast_fix
	djlint --reformat pilotage

# Deployment
# =============================================================================
.PHONY: deploy_prod

deploy_prod:
	git fetch origin && git push origin origin/staging:main  # Deploy by pushing the latest `staging` to `main`
