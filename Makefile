SRC = $(wildcard ./*.ipynb)

all: vvapp clean docs

vvapp: $(SRC)
	nbdev_build_lib
	touch vvapp
	nbdev_clean_nbs

docs_serve: docs
	cd docs && bundle exec jekyll serve

docs: $(SRC)
	nbdev_build_docs
	touch docs
	nbdev_clean_nbs

test:
	nbdev_test_nbs

release: pypi
	nbdev_bump_version

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist
