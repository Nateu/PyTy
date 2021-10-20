#!/usr/bin/env bash
poetry run coverage run -m pytest && \
poetry run coverage html && \
poetry run coverage report -m
