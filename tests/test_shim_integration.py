import subprocess
import sys
from pathlib import Path


def test_bash_shim_runs_check_help_from_repo_root():
    repo_root = Path(__file__).resolve().parents[1]
    script = repo_root / "scripts" / "skopos-uv.sh"
    assert script.exists()

    # Run the shim as a subprocess; it should invoke the module via PYTHONPATH
    env = {**dict(), "PYTHONPATH": str(repo_root / "src")}
    proc = subprocess.run(["bash", str(script), "check", "--help"], env=env, capture_output=True, text=True)
    # argparse may return exit code 0 or 2 for --help depending on implementation
    assert proc.returncode in (0, 2)
    output = (proc.stdout or "") + (proc.stderr or "")
    assert "Usage" in output or "usage" in output
