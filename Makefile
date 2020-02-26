.PHONY: test

clean:
	rm -rf dist .mypy_cache .pytest_cache *.egg-info

test:
	flake8 .
	mypy .
	pytest --cov=envvarconf
