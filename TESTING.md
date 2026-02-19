## Testing Strategy for Skopos

Recommended (Standard) strategy — pragmatic, professional, and scalable.

1. Unit tests
   - Fast tests for `checker_logic` heuristics, config merging, and utility functions.
   - Aim for high coverage on core logic (70%+ to start).

2. Integration tests
   - Tests that exercise the CLI entrypoint via `python -m skopos.checker` with `PYTHONPATH=src`.
   - Lightweight tests for the `scripts/skopos-uv.sh` shim and PowerShell shim.

3. Packaging checks (manual/local)
   - Build sdist/wheel locally and inspect contents:

```bash
python -m build --sdist --wheel -o dist
tar -tf dist/*.tar.gz | sed -n '1,200p'
```

Ensure `README.md` and `LICENSE` are included and that repo-only demo files are excluded.

4. CI (optional)
   - If desired later, add a minimal smoke CI that builds and installs the wheel into a venv and runs a couple CLI checks. Keep CI off by default unless you want workflows to run on GitHub.

5. When to use TDD
   - Use TDD selectively for high-risk parsing or matching logic.
   - For general development, add tests incrementally focusing on bugs and regressions.

Checklist (short-term)
- [ ] Expand unit tests for `checker_logic` edge cases
- [ ] Add integration tests for `checker` commands and shim behavior (done)
- [ ] Run manual packaging checks before any PyPI publish
