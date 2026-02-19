param(
  [string]$Command,
  [Parameter(ValueFromRemainingArguments=$true)]
  [string[]]$Args
)

# PowerShell shim for Windows users. Attempts to run installed `skopos`
# otherwise runs module from repository `src` if available.

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Resolve-Path "$ScriptDir\.."

function Run-Skopos {
    if (Get-Command skopos -ErrorAction SilentlyContinue) {
        skopos @Args
        return $LASTEXITCODE
    }

    $py = Get-Command python3 -ErrorAction SilentlyContinue | Select-Object -First 1
    if (-not $py) { $py = Get-Command python -ErrorAction SilentlyContinue }
    if (-not $py) { Write-Warning 'Python not found on PATH'; return 127 }

    $src = Join-Path $RepoRoot 'src'
    if (Test-Path (Join-Path $src 'skopos')) {
        & $py.Path -c "import sys; sys.path.insert(0, '$src'); import runpy; runpy.run_module('skopos.checker', run_name='__main__')" @Args
        return $LASTEXITCODE
    }

    Write-Warning 'skopos not found; install or run from repo root.'
    return 127
}

if (-not $Command) {
    Write-Output "Usage: .\scripts\skopos-uv.ps1 <command> [args]"
    exit 1
}

exit (Run-Skopos)
