.PHONY: format run

format:
	pre-commit run --all-files

run:
	python main.py
