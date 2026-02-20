# Release Checklist

This checklist is intended to guide a manual, cautious PyPI release of `skopos-audit`.

1. Bump version in `pyproject.toml` (e.g., 0.23.2)
2. Update `CHANGELOG.md` with highlights and contributors.
3. Run tests and coverage locally:

```bash
source .venv_test/bin/activate
pytest --cov=skopos --cov-report=term-missing --cov-report=xml:coverage.xml -q
python scripts/generate_coverage_badge.py  # update docs/coverage-badge.svg
```

4. Build packages:

```bash
python3 -m build --sdist --wheel -o dist
```

5. Inspect sdist contents:

```bash
tar -tf dist/*.tar.gz
```

6. Test install in a clean venv:

```bash
python3 -m venv .venv_release_test
. .venv_release_test/bin/activate
python -m pip install --upgrade pip
python -m pip install dist/*.whl
python -c "import skopos; print(skopos.__name__)"
```

7. Tag the release locally and push when ready:

```bash
# create annotated tag
git tag -a vX.Y.Z -m "Release vX.Y.Z"
# push tag to remote
git push origin vX.Y.Z
```

8. Upload to PyPI (manual):

```bash
python -m pip install --upgrade twine
python -m twine upload dist/*
```

9. Create GitHub Release notes and attach built artifacts if desired.

Notes:
- This project intentionally uses a manual CI workflow (`.github/workflows/ci_manual.yml`) to avoid accidental automated runs.
- Ensure you have the PyPI credentials and twine configured before uploading.
