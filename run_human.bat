@echo off
REM Run the WikiRace human web UI
set SCRIPT_DIR=%~dp0
set VENV=%SCRIPT_DIR%.venv

if not exist "%VENV%" (
    echo Virtual environment not found. Running setup first...
    call "%SCRIPT_DIR%setup.bat"
)

call "%VENV%\Scripts\activate.bat"
cd /d "%SCRIPT_DIR%"
python app.py %*
