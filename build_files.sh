#!/bin/bash

# Print start message
echo "BUILD START"

# Install dependencies
python -m pip install -r requirements.txt

# Run Django migrations and any other necessary commands
python manage.py migrate

# Print end message
echo "BUILD END"
