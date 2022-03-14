@echo off

: ====================
: Activate venv
: ====================
echo Activating virtual environment...
set venv_name=venv

py -m venv %venv_name%
call %venv_name%\Scripts\activate
cls
echo Activating virtual environment... Done

: ====================
: Install dependencies
: ====================
echo Installing dependencies...
pip install -r requirements.txt 1>nul 2>&1
echo Activating virtual environment... Done
echo Installing dependencies... Done

pip list

timeout -1