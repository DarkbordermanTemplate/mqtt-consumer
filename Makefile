.PHONY: init

init: clean
	pipenv --python 3.7
	pipenv install --dev --skip-lock

lint: pylint flake8

pylint:
	pipenv run pylint --rcfile=setup.cfg mqtt/

flake8:
	pipenv run flake8 mqtt/ --max-line-length=120

reformat: black isort

black:
	pipenv run black mqtt/

isort:
	pipenv run isort mqtt/*.py
	pipenv run isort mqtt/**/*.py

test:
	pipenv run pytest --cov-report=term-missing --cov-config=.coveragerc --cov=mqtt/topics mqtt/tests

ci-bundle: reformat lint test

clean:
	find . -type f -name '*.py[co]' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	rm -rf .hypothesis
	rm -rf .pytest_cache
	rm -rf .tox
	rm -f report.xml
	rm -f coverage.xml
