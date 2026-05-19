@echo off
REM ════════════════════════════════════════════════════════
REM  WikiRace — Setup Script (Windows)
REM  Run once: setup.bat
REM ════════════════════════════════════════════════════════

echo.
echo ===================================
echo    WikiRace - Setup (Windows)
echo ===================================
echo.

REM ── 1. Find Python ───────────────────────────────────────
set PYTHON=
for %%p in (python3.12 python3.11 python3.10 python3.9 python3 python py) do (
    where %%p >nul 2>&1
    if not errorlevel 1 (
        set PYTHON=%%p
        goto :found_python
    )
)

echo [warn] Python not found in PATH.
echo.
echo  Option A: Download Python from https://www.python.org/downloads/
echo            Make sure to check "Add Python to PATH" during install.
echo.
echo  Option B: Install via winget (Windows 10/11):
echo            winget install Python.Python.3.12
echo.
echo  After installing Python, re-run this script.
pause
exit /b 1

:found_python
echo [setup] Found Python: %PYTHON%
%PYTHON% --version

REM ── 2. Virtual environment ────────────────────────────────
set VENV_DIR=%~dp0.venv

if not exist "%VENV_DIR%" (
    echo [setup] Creating virtual environment at .venv ...
    %PYTHON% -m venv "%VENV_DIR%"
    if errorlevel 1 (
        echo [error] Could not create virtual environment.
        echo         Try: %PYTHON% -m pip install virtualenv
        pause
        exit /b 1
    )
) else (
    echo [setup] Virtual environment already exists.
)

REM ── 3. Activate and install dependencies ─────────────────
echo [setup] Activating virtual environment...
call "%VENV_DIR%\Scripts\activate.bat"

echo [setup] Upgrading pip...
pip install --upgrade pip --quiet

echo [setup] Installing dependencies...
pip install -r "%~dp0requirements.txt" --quiet
if errorlevel 1 (
    echo [error] Failed to install dependencies. Check your internet connection.
    pause
    exit /b 1
)

echo.
echo ============================
echo    Setup complete!
echo ============================
echo.
echo  To play WikiRace (browser UI):
echo    run_human.bat
echo.
echo  To use the bot terminal:
echo    run_bot.bat
echo.
pause
