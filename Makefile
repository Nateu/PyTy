default:
	poetry run coverage run -m pytest && \
	poetry run coverage report -m && \
	poetry run coverage html

serve:
	bash serve.sh
