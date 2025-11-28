@echo off
chcp 65001 >nul
cd /d "%~dp0"
python update_daily.py
git add -A
if not errorlevel 1 (
    git commit -m "Update daily log"
    git push
)
