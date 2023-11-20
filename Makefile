.PHONY: install

install:
	@echo "Création de l'environnement virtuel..."
	@python3 -m venv venv
	@echo "Activation de l'environnement virtuel..."
	@. venv/bin/activate
	@echo "Installation des dépendances Python..."
	@pip install -r requirements.txt
	@echo "Installation terminée."



.PHONY: run

run:
	@echo "Tickets in preparation, please wait ..."
	@python3 sample01.py
	@echo "Done! Thanks!"
