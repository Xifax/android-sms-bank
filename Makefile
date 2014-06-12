# Core tasks
update:
	pip install -r requirements/dev.txt
	cd etc && bower update

run:
	python manage.py runserver
