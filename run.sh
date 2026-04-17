#!/bin/bash
# Egyptian Stock Tracker - Startup Script

echo "Launching Egyptian Stock Tracker..."
cd "$(dirname "$0")/src"
python3 main.py
