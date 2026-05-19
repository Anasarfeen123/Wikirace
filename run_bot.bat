@echo off
REM Run the WikiRace bot terminal
REM Options:
REM   --bot               pipe-mode (JSON stdin/stdout)
REM   --start X --target Y  start with specific articles
set SCRIPT_DIR=%~dp0
set VENV=%SCRIPT_DIR%.venv

if not exist "%VENV%" (
    echo First-time setup is needed. This may take a few minutes.
    call "%SCRIPT_DIR%setup.bat"
    if errorlevel 1 exit /b 1
)

call "%VENV%\Scripts\activate.bat"
cd /d "%SCRIPT_DIR%"
python bot_terminal.py %*
