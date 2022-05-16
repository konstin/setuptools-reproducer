#!/bin/bash

set -e

virtualenv -p 3.8 .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python main.py
