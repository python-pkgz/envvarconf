.PHONY: clean
clean:
	rm -rf dist .mypy_cache .pytest_cache *.egg-info

.PHONY: test
test:
	flake8 .
	mypy .
	pytest --cov=envvarconf

.PHONY: dist
dist:
	python3 setup.py sdist
	twine upload dist/*
	git tag `cat setup.py | grep VERSION | grep -v version | cut -d= -f2 | tr -d "[:space:]"`
	git push --tags
