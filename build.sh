#!/bin/bash
echo "Install python libraries..."
pip install -r requirements.txt
echo "All libraries installed"

echo "Building application database..."
python database.py
echo "Database has been created"
