@echo off
REM Egyptian Stock Tracker - Startup Script

echo Launching Egyptian Stock Tracker...
cd /d "%~dp0\src"
python main.py
pause
