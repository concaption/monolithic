#!/usr/bin/env bash

### Sets up python packages in for devcontainer.json

#create a virtualenv
python -m venv .venv

# source virtualenv
source .venv/bin/activate

# install all software
make install
