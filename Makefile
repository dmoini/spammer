OUTDATED_PIP_PACKAGES=$(shell pip list --outdated 2>/dev/null | sed 1,2d | awk '{printf $$1 " " }' | sed 's/\ $$//')

spam:
	python3 spam.py

freeze:
	pip freeze > requirements.txt

init:
	pip install -r requirements.txt

ifeq ($(strip $(OUTDATED_PIP_PACKAGES)),)
upgrade: 
	@echo "All pip packages are up to date"
else
upgrade: 
	pip install -U $(OUTDATED_PIP_PACKAGES)
endif