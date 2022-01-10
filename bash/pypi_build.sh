#!/bin/bash

rm -rf gnow.egg-info/*
rm -rf dist/*
rm -rf build/*

python3 setup.py sdist
python3 setup.py bdist_wheel
