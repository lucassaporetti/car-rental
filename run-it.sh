#!/usr/bin/env bash

export PYTHONPATH="$(pwd)"

if [[ "qt" == "$1" ]]; then
  pyrcc5 src/resources.qrc -o src/resources_rc.py
  python3 src/car_rental.py
else
  python3 src/main.py
fi
