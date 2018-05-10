all: clean test

test: api_tests

api_tests: api_model_tests api_view_tests

api_model_tests:
	./manage.py test api.models

api_view_tests:
	./manage.py test api.view