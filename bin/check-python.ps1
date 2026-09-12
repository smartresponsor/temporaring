$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $PSScriptRoot
$pythonRoot = Join-Path $root 'python'
$python = Join-Path $pythonRoot '.venv\Scripts\python.exe'
$pyright = Join-Path $pythonRoot '.venv\Scripts\pyright.exe'

& $pyright --project (Join-Path $root 'pyrightconfig.json')
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

& $python -m pytest (Join-Path $pythonRoot 'tests') -q
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

$env:PYTHONPATH = Join-Path $pythonRoot 'src'
& $python -m temporaring.runner --input (Join-Path $root 'research\hypothesis\common-positive.json')
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

& $python -m temporaring.runner --input (Join-Path $root 'research\hypothesis\relative-tempo.json')
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
