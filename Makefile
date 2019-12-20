.PHONY: run
run:
	export LC_ALL=C.UTF-8; export LANG=C.UTF-8; export FLASK_APP=WeatherAPI; flask run --host 0.0.0.0 --port 8000

.PHONY: test
test:
	export LC_ALL=C.UTF-8; export LANG=C.UTF-8; python3 -m unittest discover -v

.PHONY: init
init: 
	python -m pip install --upgrade pip
	pip install -r requirements.txt
