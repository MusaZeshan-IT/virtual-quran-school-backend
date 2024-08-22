#!/bin/bash

# Print start message
echo "BUILD START"

# Install dependencies
python -m pip install -r requirements.txt

# Collect static files (optional, if you have any static files)
python manage.py collectstatic --noinput --clear

# Run migrations
python manage.py migrate

# Print end message
echo "BUILD END"
