@echo off
REM Run the WikiRace bot terminal
REM Options:
REM   --bot               pipe-mode (JSON stdin/stdout)
REM   --start X --target Y  start with specific articles
set SCRIPT_DIR=%~dp0
set VENV=%SCRIPT_DIR%.venv

if not exist "%VENV%" (
    echo Virtual environment not found. Running setup first...
    call "%SCRIPT_DIR%setup.bat"
)

call "%VENV%\Scripts\activate.bat"
cd /d "%SCRIPT_DIR%"
python bot_terminal.py %*
