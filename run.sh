#!/bin/bash

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Set Flask environment variables
export FLASK_APP=app.py
export FLASK_DEBUG=1

# Run Flask application
flask run --host=0.0.0.0 --port=5000
