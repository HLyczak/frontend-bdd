#!/bin/bash

# install.sh

set -e

python3 -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
pip install --require-virtualenv --upgrade pip
pip install -r requirements.txt

echo Remember to activate virtual environment