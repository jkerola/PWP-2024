VENV_DIR := api/venv
VENV := source $(VENV_DIR)/bin/activate &&

venv:
	pushd $(VENV_DIR) && python3 -m venv venv

db:
	docker-compose up -d

flask:
	$(VENV) pushd api && pip install -r requirements.txt && prisma generate && prisma db push && flask run

clientn:
	pushd client && nohup npm start &
    
up: db clientn flask
	echo "Done!"

tests:
	$(VENV) pushd api && pytest -s