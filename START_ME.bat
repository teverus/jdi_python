@echo off

: ====================
: Activate venv
: ====================
echo Activating virtual environment...
set venv_name=venv2

py -m venv %venv_name%
call %venv_name%\Scripts\activate
cls
echo Activating virtual environment... Done

: ====================
: Install dependencies
: ====================
echo Installing dependencies...
pip install -r requirements.txt 1>nul 2>&1
cls
echo Activating virtual environment... Done
echo Installing dependencies... Done

cls
py main.py