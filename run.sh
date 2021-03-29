#!/bin/sh
export PATH="$PATH:$PWD/geckodriver"
pipenv run python src/main.py
