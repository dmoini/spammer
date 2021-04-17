freeze:
	pip freeze > requirements.txt

init:
	pip install -r requirements.txt

lint:
	pylint spam/*.py

run:
	python3 spam/spam.py

help:
	@echo "    freeze"
	@echo "        Freeze and save installed pip packages"
	@echo "    init"
	@echo "        Install pip packages"
	@echo "    run"
	@echo "        Run spammer program"