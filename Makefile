.PHONY: test build dist publish

test:
	pytest --capture=no

dist:
	rm dist/*
	python3 setup.py sdist bdist_wheel

publish:
	twine upload dist/* -r pypi
	
