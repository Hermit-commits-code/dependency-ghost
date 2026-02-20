# Contributing and Release Guide

Thank you for contributing to Skopos. This document covers the recommended workflow for development, testing, and releasing to PyPI.

Development
- Create a branch for your change and open a PR against `main`.
- Run tests locally:

```bash
source .venv_test/bin/activate
pytest -q
```

Testing & Packaging (local)
1. Create a clean venv and install dev deps:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
pip install build pytest pytest-mock pytest-cov
```

2. Run tests and generate coverage:

```bash
pytest --cov=skopos --cov-report=term-missing --cov-report=xml:coverage.xml -q
```

3. Build sdist and wheel:

```bash
python -m build --sdist --wheel -o dist
```

4. Inspect sdist contents:

```bash
tar -tf dist/*.tar.gz
```

Release to PyPI (manual)
- Ensure version bump in `pyproject.toml`.
- Build distribution as above.
- Upload via `twine` (recommended):

```bash
python -m pip install --upgrade twine
python -m twine upload dist/*
```

Notes
- CI: A manual GitHub Actions workflow is provided at `.github/workflows/ci_manual.yml`. It's manual-only (`workflow_dispatch`) so it won't run automatically.
- Badge: Coverage badge generation is described in `TESTING.md` and can be generated locally.
