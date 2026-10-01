@echo off
chcp 65001 >nul
echo ========================================================
echo   ✨ MuseKOL Studio - 1-Click Launcher (Windows)
echo   Xưởng Sản Xuất KOL Ảo Toàn Diện (Meta Muse Powered)
echo ========================================================
echo.

set PYTHONUTF8=1

if not exist .venv (
    echo [1/3] Khoi tao Virtual Environment (.venv)...
    python -m venv .venv
    if errorlevel 1 (
        echo [LOI] Khong tim thay Python! Vui long cai dat Python 3.10+ va tick 'Add Python to PATH'.
        pause
        exit /b 1
    )
    echo [2/3] Cai dat thu vien tu requirements.txt...
    call .venv\Scripts\pip install -r requirements.txt
) else (
    echo [OK] Virtual Environment (.venv) da san sang.
)

echo [3/3] Dang khoi dong may chu MuseKOL Studio tai cong 18610...
echo.
echo ========================================================
echo   Giao dien KOL Studio : http://127.0.0.1:18610/kol
echo   Trang quan tri Admin : http://127.0.0.1:18610/admin?key=m2a_admin_8888888888
echo ========================================================
echo.

start "" "http://127.0.0.1:18610/kol"

call .venv\Scripts\python -m uvicorn app:app --host 127.0.0.1 --port 18610
pause
