"""Shared helper: fail fast if required Zenodo-bundle data is missing.

Every notebook that depends on data NOT bundled in the GitHub repo (i.e.
data shipped separately via the Zenodo archive) imports and calls
``require_data(...)`` in its first code cell. If any required path is
missing, ``require_data`` raises FileNotFoundError with a clear message
pointing at the Zenodo DOI and the expected local layout.

Rationale: this catches the "user forgot to unzip the Zenodo bundle" case
IMMEDIATELY on cell 1, rather than 15 cells later inside an obscure
xarray.open_dataarray() call.

Usage inside a notebook (first code cell, after imports)::

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path("Notebooks").resolve()))
    from data_check import require_data
    require_data(["data/gmcm9/", "data/thermochronology_central_asia/"])

The paths are relative to the tutorial-suite repo root.
"""
from __future__ import annotations

import os
from pathlib import Path

ZENODO_DOI = "https://doi.org/10.5281/zenodo.XXXXXXX"     # ← replace after publication
ZENODO_ARCHIVE_NAME = "GPlately-pyGMT-tutorial-data-v1.zip"


def _repo_root() -> Path:
    """Return the repo root, whether the CWD is the repo root or Notebooks/."""
    cwd = Path.cwd()
    # If a `data/` subfolder exists next to CWD, we're at the repo root.
    if (cwd / "data").exists():
        return cwd
    # If `../data/` exists, we're inside Notebooks/ — step up.
    if (cwd.parent / "data").exists():
        return cwd.parent
    # Fall back to CWD; require_data() will fail with a clear message.
    return cwd


def require_data(paths: list[str] | list[Path]) -> None:
    """Raise FileNotFoundError if any of the listed paths is missing.

    Parameters
    ----------
    paths : list of str or Path
        Paths relative to the repo root (e.g. ``"data/gmcm9/"``,
        ``"data/thermochronology/AFEAD_Faults_CentralAsia/"``).

    Raises
    ------
    FileNotFoundError
        With a message pointing at the Zenodo DOI and expected local layout.
    """
    root = _repo_root()
    missing = []
    for p in paths:
        full = root / p
        if not full.exists():
            missing.append(p)

    if not missing:
        return

    msg = (
        "\n"
        "=" * 74 + "\n"
        f"Missing data required by this notebook ({len(missing)} of {len(paths)} paths):\n"
        + "\n".join(f"  - {p}" for p in missing) + "\n"
        "\n"
        "These data are shipped in the tutorial's companion Zenodo archive\n"
        f"(too large for GitHub). Download and unzip:\n"
        "\n"
        f"  1. Download  {ZENODO_ARCHIVE_NAME}  from  {ZENODO_DOI}\n"
        f"  2. Unzip:    unzip {ZENODO_ARCHIVE_NAME}\n"
        f"  3. Merge:    rsync -av GPlately-pyGMT-tutorial-data/data/ {root}/data/\n"
        "\n"
        "See the archive's README.md for full details. If you already downloaded\n"
        "the archive, check that you unzipped it into a location that ends up\n"
        f"with the missing paths above showing up UNDER  {root}/\n"
        + "=" * 74 + "\n"
    )
    raise FileNotFoundError(msg)
