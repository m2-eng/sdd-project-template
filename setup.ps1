#Requires -Version 5.1
<#
.SYNOPSIS
    Projekt – Entwicklungsumgebung einrichten.

.DESCRIPTION
    Erstellt die Python-venv (falls nicht vorhanden),
    aktiviert sie und installiert alle Entwicklungsabhaengigkeiten
    aus requirements-dev.txt.

.EXAMPLE
    .\setup.ps1
#>

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$root    = $PSScriptRoot
$venv    = Join-Path $root '.venv'
$python  = 'python'
$req     = Join-Path $root 'requirements-dev.txt'

Write-Host ""
Write-Host "=== Project Setup ===" -ForegroundColor Cyan

# --- Execution Policy pruefen ---
$policy = Get-ExecutionPolicy -Scope Process
if ($policy -eq 'Restricted') {
    Write-Host "[INFO] Setze ExecutionPolicy fuer diesen Prozess auf RemoteSigned..." -ForegroundColor Yellow
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned -Force
}

# --- Python pruefen ---
if (-not (Get-Command $python -ErrorAction SilentlyContinue)) {
    Write-Error "Python nicht gefunden. Bitte Python 3.10+ installieren und im PATH verfuegbar machen."
    exit 1
}

$version = & $python --version
Write-Host "[OK] $version gefunden" -ForegroundColor Green

# --- venv erstellen ---
if (-not (Test-Path $venv)) {
    Write-Host "[...] Erstelle .venv ..." -ForegroundColor Yellow
    & $python -m venv $venv
    Write-Host "[OK] .venv erstellt" -ForegroundColor Green
} else {
    Write-Host "[OK] .venv bereits vorhanden" -ForegroundColor Green
}

# --- venv aktivieren ---
$activate = Join-Path $venv 'Scripts\Activate.ps1'
Write-Host "[...] Aktiviere .venv ..." -ForegroundColor Yellow
. $activate
Write-Host "[OK] .venv aktiv" -ForegroundColor Green

# --- pip aktualisieren ---
Write-Host "[...] Aktualisiere pip ..." -ForegroundColor Yellow
python -m pip install --upgrade pip --quiet

# --- Abhaengigkeiten installieren ---
if (-not (Test-Path $req)) {
    Write-Error "requirements-dev.txt nicht gefunden: $req"
    exit 1
}

Write-Host "[...] Installiere Abhaengigkeiten aus requirements-dev.txt ..." -ForegroundColor Yellow
pip install -r $req

Write-Host ""
Write-Host "=== Setup abgeschlossen ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Naechste Schritte:" -ForegroundColor White
Write-Host "  Venv aktivieren:  .venv\Scripts\Activate.ps1"
Write-Host "  Tests ausfuehren: pytest tests\"
Write-Host "  Spec-Server:      strictdoc server ."
Write-Host ""
