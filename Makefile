clean:
	@echo "Removendo arquivos *.pyc|__pycache__|coverage.xml ..."
	@find tests/ app/ | egrep "*.pyc|*.pyo|__pycache__" | xargs rm -rf
	@rm -f ./coverage.xml
	@rm -f ./unit.xml

pep8: clean
	@echo "Fazendo validação PEP8"
	@find ./app/ -type f -name "*.py"| PIPENV_VERBOSITY=-1 xargs pipenv run flake8 --show-source --max-line-length=120 --ignore=E704,E402,W503 --max-complexity=5

install:
	pip install -U pip
	pip install -U setuptools
	pip install pipenv

create_base:
	python create_base.py