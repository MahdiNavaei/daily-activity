@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ========================================
echo Daily Engineering Activity Tracker
echo ========================================
echo.

echo [1/3] در حال به‌روزرسانی یادداشت‌های روزانه...
python update_daily.py
if %errorlevel% neq 0 (
    echo ✗ خطا در به‌روزرسانی
    pause
    exit /b 1
)

echo.
echo [2/3] در حال اضافه کردن تغییرات به Git...
git add -A

echo.
echo [3/3] در حال commit و push...
set DATE=%date:~-4,4%-%date:~-7,2%-%date:~-10,2%

REM Generate random commit message
set /a RAND=%RANDOM% %% 10
if %RAND% lss 3 (
    set COMMIT_MSG=📝 Update daily engineering log - %DATE%
) else if %RAND% lss 6 (
    set COMMIT_MSG=🔧 Daily ML/AI engineering activities - %DATE%
) else if %RAND% lss 8 (
    set COMMIT_MSG=✨ Update project progress log - %DATE%
) else (
    set COMMIT_MSG=🚀 Engineering activities update - %DATE%
)

git commit -m "%COMMIT_MSG%"
if %errorlevel% neq 0 (
    echo ℹ هیچ تغییری برای commit وجود ندارد
) else (
    git push
    if %errorlevel% equ 0 (
        echo.
        echo ✓ به‌روزرسانی با موفقیت انجام شد!
        echo ✓ Commit message: %COMMIT_MSG%
    ) else (
        echo ✗ خطا در push به remote
    )
)

echo.
echo ========================================
pause
