SHELL = /bin/sh

spam:
	python3 spam.py
freeze:
	pip freeze > requirements.txt
init:
	pip install -r requirements.txt
upgrade:
	OUTDATED_PIP_PACKAGES = $(shell pip list --outdated 2>/dev/null | sed 1,2d | awk '{printf $$1 " " }' | sed 's/\ $$//' )
	pip install -U $(OUTDATED_PIP_PACKAGES)