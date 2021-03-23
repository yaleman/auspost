#!/bin/bash

if [ -d "dist/" ]; then
    find "$(pwd)/dist" -type f -exec rm "{}" \;
fi

find "$(pwd)/" -path '*.egg-info*' -type f -exec rm "{}" \;

python3 setup.py bdist_wheel && twine upload dist/*
