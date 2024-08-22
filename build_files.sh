#!/bin/bash

# Print start message
echo "BUILD START"

# Install dependencies
python3 -m pip install -r requirements.txt

# Perform Django management tasks
python3 manage.py migrate

# Print end message
echo "BUILD END"
