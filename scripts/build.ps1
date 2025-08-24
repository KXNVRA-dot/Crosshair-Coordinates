param(
    [switch]$Clean
)

$ErrorActionPreference = 'Stop'

if ($Clean) {
    Write-Host 'Cleaning build artifacts...'
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue 'build','dist','*.spec'
}

Write-Host 'Upgrading pip and installing PyInstaller...'
python -m pip install --upgrade pip | Out-Host
python -m pip install pyinstaller | Out-Host

Write-Host 'Building CursorTracker.exe (one-file, windowed)...'
$scriptPath = Join-Path $PSScriptRoot '..\src\cursor_tracker\app.py'
pyinstaller --noconsole --onefile --name CursorTracker "$scriptPath" | Out-Host

Write-Host 'Build complete. Output in dist\CursorTracker.exe'
