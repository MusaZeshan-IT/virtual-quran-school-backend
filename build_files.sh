#!/bin/bash

# Print start message
echo "BUILD START"

# Install dependencies
python3.9 -m pip install -r requirements.txt

# Collect static files (optional, if you have any static files)
python3.9 manage.py collectstatic --noinput --clear

# Run migrations
python3.9 manage.py migrate --noinput

# Print end message
echo "BUILD END"
