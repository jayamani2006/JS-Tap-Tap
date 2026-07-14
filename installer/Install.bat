@echo off
REM ============================================================
REM  JS Tap-Tap — Installer Script
REM  Location: installer\Install.bat
REM
REM  What this does:
REM    1. Copies JS Tap-Tap.exe to the user's Desktop
REM    2. Creates a Start Menu shortcut pointing to the Desktop EXE
REM    3. Launches the welcome popup via pythonw (requires Python + Pillow)
REM
REM  Run this script from the repo root or the installer\ folder.
REM  The EXE must be present in the same folder as this script
REM  (provided via a GitHub Release ZIP — see INSTALL.md).
REM ============================================================

set APPNAME=JS Tap-Tap
set EXEFILE=JS Tap-Tap.exe
set ICONFILE=..\assets\branding\icon.ico
set WELCOME=%~dp0welcome.py

REM ── Resolve Desktop path ─────────────────────────────────────────────────────
set DESKTOP=%USERPROFILE%\Desktop

REM ── Copy EXE to Desktop ──────────────────────────────────────────────────────
echo Copying %EXEFILE% to Desktop...
copy "%~dp0%EXEFILE%" "%DESKTOP%\%EXEFILE%" /Y
if errorlevel 1 (
    echo ERROR: Could not copy EXE. Make sure JS Tap-Tap.exe is in the same folder as this script.
    pause
    exit /b 1
)

REM ── Create Start Menu shortcut ────────────────────────────────────────────────
set STARTMENU=%APPDATA%\Microsoft\Windows\Start Menu\Programs\%APPNAME%.lnk
echo Creating Start Menu shortcut...
powershell -NoProfile -Command ^
    "$s=(New-Object -COM WScript.Shell).CreateShortcut('%STARTMENU%');^
     $s.TargetPath='%DESKTOP%\%EXEFILE%';^
     $s.IconLocation='%~dp0%ICONFILE%';^
     $s.Save()"

REM ── Launch welcome popup (optional — requires Python + Pillow) ────────────────
echo Launching welcome guide...
start "" pythonw "%WELCOME%"

REM ── Done ──────────────────────────────────────────────────────────────────────
echo.
echo ============================================================
echo   Installation complete!
echo   - %APPNAME% copied to Desktop.
echo   - Shortcut added to Start Menu.
echo   - Search "%APPNAME%" in Windows to launch from Start Menu.
echo ============================================================
echo.
pause
