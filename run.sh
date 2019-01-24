#!/bin/bash

echo "Processing text file $1"
python process_file.py $1
echo "$1 processed"

echo "Starting server..."
gunicorn --bind 0.0.0.0:8000 --workers 4 --env FILENAME=$1 wsgi