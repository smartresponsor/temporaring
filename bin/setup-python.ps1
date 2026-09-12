$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $PSScriptRoot
$pythonRoot = Join-Path $root 'python'
$venv = Join-Path $pythonRoot '.venv'

if (-not (Test-Path $venv)) {
    python -m venv $venv
}

$python = Join-Path $venv 'Scripts\python.exe'
& $python -m pip install --upgrade pip
& $python -m pip install -e "$pythonRoot[dev]"

Write-Host "Temporaring Python environment ready: $venv"
