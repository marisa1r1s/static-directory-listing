#!/usr/bin/env bash

python3 -m venv _venv

source _venv\Scripts\activate

pip3 install --upgrade -r requirements.txt

python3 treegen.py

deactivate