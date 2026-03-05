@echo off
echo =====================================
echo Setting up Trading Bot Environment
echo =====================================

:: Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not in PATH.
    echo Please install Python and try again.
    pause
    exit /b
)

echo Python detected.

echo Creating virtual environment...
python -m venv trading

IF NOT EXIST venv (
    echo Failed to create virtual environment.
    pause
    exit /b
)

echo Activating virtual environment...
call trading\Scripts\activate

echo Upgrading pip...
python -m pip install --upgrade pip

echo Installing project dependencies...
pip install -r requirements.txt

echo Creating project folders...

echo.
echo =====================================
echo Setup complete!
echo =====================================
echo.
echo To start the project:
echo 1. Activate environment: venv\Scripts\activate
echo 2. Run program: python main.py
echo.

pause