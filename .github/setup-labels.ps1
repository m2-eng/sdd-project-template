# CR-Labels für SUP.10 anlegen
# Voraussetzung: GitHub CLI installiert (winget install --id GitHub.cli)
#                gh auth login abgeschlossen
# Ausführen im Repository-Verzeichnis: .\.github\setup-labels.ps1

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Error "GitHub CLI (gh) nicht gefunden. Installation: winget install --id GitHub.cli"
    exit 1
}

gh label create "cr-open"        --color "e4e669" --description "Change Request eingegangen, noch nicht bewertet" --force
gh label create "cr-assessed"    --color "0075ca" --description "Change Request bewertet, Aufwand bekannt" --force
gh label create "cr-approved"    --color "0e8a16" --description "Change Request freigegeben zur Umsetzung" --force
gh label create "cr-implemented" --color "6f42c1" --description "Change Request umgesetzt, Spec aktualisiert" --force

Write-Host "✅ CR-Labels angelegt."
