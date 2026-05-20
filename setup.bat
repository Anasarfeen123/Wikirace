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
echo This prepares WikiRace on this computer. It may take a few minutes.
echo You only need to run setup once.
echo.

REM ── 1. Find Python ───────────────────────────────────────
set PYTHON=
for %%p in (python python3 py) do (
    %%p -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 9) else 1)" >nul 2>&1
    if not errorlevel 1 (
        set PYTHON=%%p
        goto :found_python
    )
)

echo [warn] Python 3.9 or newer was not found.
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

:confirm
echo.
echo ============================================================
echo   PROMPT: %~1
echo   DETAIL: %~2
echo ============================================================
choice /M "Proceed?"
echo.
if errorlevel 2 (
    echo [error] Aborted by user.
    pause
    exit /b 1
)
goto :eof

:found_python
echo [setup] Found Python: %PYTHON%
%PYTHON% --version

REM ── 2. Virtual environment ────────────────────────────────
set VENV_DIR=%~dp0.venv

if not exist "%VENV_DIR%" (
    call :confirm "Create Virtual Environment" "This creates an isolated folder (.venv) to store dependencies."
    echo [setup] Creating virtual environment at .venv ...
    %PYTHON% -m venv "%VENV_DIR%"
    if errorlevel 1 (
        echo [error] Could not create virtual environment.
        pause
        exit /b 1
    )
) else (
    echo [setup] Virtual environment already exists.
)

REM ── 3. Activate and install dependencies ─────────────────
call :confirm "Upgrade pip and install dependencies" "This installs the libraries WikiRace needs to run."
echo [setup] Activating virtual environment...
call "%VENV_DIR%\Scripts\activate.bat"

echo [setup] Upgrading pip...
python -m pip install --upgrade pip --quiet

echo [setup] Installing dependencies...
pip install -r "%~dp0requirements.txt" --quiet

call :confirm "AI Warmup" "This downloads the AI model (approx 80MB). One-time download."
python "%~dp00_warmup.py"

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
exit /b 0

:install_failed
echo.
echo [error] Setup did not finish.
echo         Check your internet connection, then run setup.bat again.
echo         If it still fails, copy the error above and send email to "codecrusader07@gmail.com".
pause
exit /b 1
