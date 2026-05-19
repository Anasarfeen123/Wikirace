@echo off
REM Run the WikiRace human web UI
set SCRIPT_DIR=%~dp0
set VENV=%SCRIPT_DIR%.venv

if not exist "%VENV%" (
    echo First-time setup is needed. This may take a few minutes.
    call "%SCRIPT_DIR%setup.bat"
    if errorlevel 1 exit /b 1
)

call "%VENV%\Scripts\activate.bat"
cd /d "%SCRIPT_DIR%"
echo.
echo Starting WikiRace...
echo Your browser should open automatically.
echo If it does not, open this address yourself: http://127.0.0.1:5000
echo Keep this window open while playing.
echo.
start "" http://127.0.0.1:5000
python app.py %*
