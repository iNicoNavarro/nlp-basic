install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	
	python -m textblob.download_corpora

test:
	python -m pytest -vv --cov=main.py --cov=nlp_logic test_core.py

format:
	black *.py

lint:
	pylint --disable=R,C *.py nlp_logic/*.py

all:
	install lint test
