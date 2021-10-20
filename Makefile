default:
	poetry run black **/*.py
	bash ./scripts/unit_test.sh

serve:
	bash ./scripts/serve.sh

test:
	bash ./scripts/unit_test.sh

format:
	poetry run black **/*.py