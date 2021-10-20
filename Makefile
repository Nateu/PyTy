default: format flake pytest

serve:
	bash ./scripts/serve.sh

pytest:
	bash ./scripts/pytest.sh

format:
	bash ./scripts/black.sh

flake:
	bash ./scripts/flake8.sh
