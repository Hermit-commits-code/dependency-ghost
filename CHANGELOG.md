# Changelog

## [0.18.0] - 2026-02-15

### Added

- **The Brain**: Implemented the SpectrScore weighted 0-100 risk engine.
- **Giant's Immunity**: Prevention of false positives on legacy giants like NumPy/Pandas.
- **Fix**: Resolved integer unpacking TypeErrors in recursive loops.

## [0.17.0] - 2026-02-15

### Added

- **Metadata Plus**: Enhanced forensic metadata extraction for deeper package insights.
- Refined Reputation heuristics for more accurate "Days Old" calculations.

## [0.16.0] - 2026-02-15

### Added

- **Recursive Auditor**: Added `--recursive` and `--max-depth` to scan dependency trees.
- **Deep Scanning**: Improved payload analysis for nested sub-dependencies.

## [0.15.0] - 2026-02-15

### Added

- **The TUI & Forensics**: Rich-powered Terminal UI with animated spinners.
- **Forensics**: Color-coded status tables for human-readable audits.

## [0.14.0] - 2026-02-15

### Added

- **Automated Test Suite**: Integrated CI-ready testing for forensic heuristics.
- Refactored core logic into `checker_logic.py` for modularity.

## [0.13.0] - 2026-02-15

### Added

- **Update Engine**: Automated version checking via PyPI API.
- **Documentation**: Finalized shell hook installation guides.

## [0.12.0] - 2026-02-15

### Added

- **JSON Support**: Implemented `--json` flag for machine-readable output.
- **Forensic Metadata**: Expansion of structural analysis metrics (sdist size).

## [0.11.0] - 2026-02-15

### Added

- **The Forensic Update**: Broadening of the heuristic suite.
- **Typosquatting Engine**: Local Levenshtein distance checks for high-value targets.

## [0.10.0] - 2026-02-15

### Added

- **Identity & Structure**: Detecting "Skeleton" packages and brand-jacking.
- **Rebranding**: Finalized migration from "Ghost" to **Spectr**.

## [0.9.0] - 2026-02-15

### Added

- **The Identity Update**: Implementation of author email verification heuristics.

## [0.8.2] - 2026-02-15

### Added

- Navigation polish and terminal output formatting improvements.

## [0.8.1] - 2026-02-15

### Added

- **Case Study**: Documentation of "Inflated Trust" attack vectors.

## [0.8.0] - 2026-02-15

### Added

- **The Integration Release**: Automated shell hook (`pip-install`) installer.

## [0.6.0] - 2026-02-15

### Added

- **Deep Analysis Engine**: High-download/low-age "inflated trust" flagging.

## [0.5.0] - 2026-02-15

### Added

- **The Trust Update**: Initial implementation of the `~/.spectr-whitelist` system.

## [0.4.0] - 2026-02-15

### Added

- Similarity engine using `difflib` for typosquatting detection.

## [0.3.0] - 2026-02-14

### Added

- Multi-Package Support for interception loops.
- **The Kill Switch**: `spectr-off` command to remove shell aliases.

## [0.2.0] - 2026-02-14

### Added

- `spectr-init` command to generate shell interception logic.

## [0.1.0] - 2026-02-14

### Added

- Initial project release with 72-hour age-gating policy.

- **The Integration Release**: Automated shell hook (`pip-install`) installer.

## [0.6.0] - 2026-02-15

### Added

- **Deep Analysis Engine**: High-download/low-age "inflated trust" flagging.

## [0.5.0] - 2026-02-15

### Added

- **The Trust Update**: Initial implementation of the `~/.spectr-whitelist` system.

## [0.4.0] - 2026-02-15

### Added

- Similarity engine using `difflib` for typosquatting detection.

## [0.3.0] - 2026-02-14

### Added

- Multi-Package Support for interception loops.
- **The Kill Switch**: `spectr-off` command to remove shell aliases.

## [0.2.0] - 2026-02-14

### Added

- `spectr-init` command to generate shell interception logic.

## [0.1.0] - 2026-02-14

### Added

- Initial project release with 72-hour age-gating policy.
