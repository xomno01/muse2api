$env:PYTHONUTF8 = "1"
Write-Host "========================================================" -ForegroundColor Magenta
Write-Host "  ✨ MuseKOL Studio - 1-Click Launcher (PowerShell)" -ForegroundColor Magenta
Write-Host "  Xưởng Sản Xuất KOL Ảo Toàn Diện (Meta Muse Powered)" -ForegroundColor Magenta
Write-Host "========================================================" -ForegroundColor Magenta

if (-not (Test-Path ".venv")) {
    Write-Host "[1/3] Khoi tao Virtual Environment (.venv)..." -ForegroundColor Yellow
    python -m venv .venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[LOI] Khong tim thay Python! Vui long cai dat Python 3.10+." -ForegroundColor Red
        exit 1
    }
    Write-Host "[2/3] Cai dat thu vien tu requirements.txt..." -ForegroundColor Yellow
    .\.venv\Scripts\pip install -r requirements.txt
} else {
    Write-Host "[OK] Virtual Environment (.venv) da san sang." -ForegroundColor Green
}

Write-Host "`n[3/3] Dang khoi dong may chu MuseKOL Studio..." -ForegroundColor Yellow
Write-Host "Giao dien KOL Studio : http://127.0.0.1:18610/kol" -ForegroundColor Cyan
Write-Host "Trang quan tri Admin : http://127.0.0.1:18610/admin?key=m2a_admin_8888888888`n" -ForegroundColor Green

Start-Process "http://127.0.0.1:18610/kol"

.\.venv\Scripts\python -m uvicorn app:app --host 127.0.0.1 --port 18610
