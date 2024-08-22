#!/bin/bash

# Print start message
echo "BUILD START"

# Use the Python version from the virtual environment
python -m pip install -r requirements.txt
python manage.py collectstatic --noinput --clear

# Print end message
echo "BUILD END"

# Create output directory (Windows-compatible command)
mkdir staticfiles_build
