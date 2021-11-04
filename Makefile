.PHONY: default init bdd test format sort lint

default: test format sort lint

bdd: mamba format sort lint

init:
	poetry install

serve:
	bash ./scripts/serve.sh

test:
	bash ./scripts/pytest.sh

format:
	bash ./scripts/black.sh

lint:
	bash ./scripts/flakehell.sh

sort:
	bash ./scripts/isort.sh

mamba:
	bash ./scripts/mamba.sh
