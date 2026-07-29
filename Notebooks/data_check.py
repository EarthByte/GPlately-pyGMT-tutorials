"""Shared helper: fail fast if required Zenodo-bundle data is missing.

Every notebook that depends on data NOT bundled in the GitHub repo (i.e.
data shipped separately via the Zenodo archive) imports and calls
``require_data(...)`` in its first code cell. If any required path is
missing, ``require_data`` raises FileNotFoundError with a clear message
pointing at the Zenodo DOI and the expected local layout.

Rationale: this catches the "user forgot to unzip the Zenodo bundle" case
IMMEDIATELY on cell 1, rather than 15 cells later inside an obscure
xarray.open_dataarray() call.

Convention: the suite's Zenodo archive extracts to a SINGLE folder,
``zenodo_data/``, placed at the repo root as a sibling of ``Notebooks/``
and ``data/`` (never merged into ``data/`` -- ``data/`` holds only the
small files that are small enough to live in git). Every not-bundled
dataset gets its own subfolder under zenodo_data/, e.g.
``zenodo_data/gmcm9/``, ``zenodo_data/santosh_dynamic_topography/``. See
Notebooks/README.md > External data dependencies, and
zenodo_data/README.md (the manifest) for the full list of subfolders,
what each one contains, and where the data currently lives on the
maintainer's machine pending upload.

Each dataset's env var (e.g. ``ZENODO_GMCM9_DIR``) is a secondary
override for users who keep the data at a non-default location -- it is
read directly by the notebook's configuration cell, not by this module.

Usage inside a notebook (first code cell, after imports)::

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path("Notebooks").resolve()))
    from data_check import require_data
    require_data(["zenodo_data/gmcm9/", "zenodo_data/thermochronology_boone/"])

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
        Paths relative to the repo root (e.g. ``"zenodo_data/gmcm9/"``,
        ``"zenodo_data/thermochronology_boone/AFEAD_Faults/"``).

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
        f"(too large for GitHub). Download and extract it as zenodo_data/ at\n"
        f"the repo root (a sibling of Notebooks/ and data/ -- do NOT merge it\n"
        f"into data/):\n"
        "\n"
        f"  1. Download  {ZENODO_ARCHIVE_NAME}  from  {ZENODO_DOI}\n"
        f"  2. Unzip it so its contents land at  {root}/zenodo_data/\n"
        "     (e.g. `unzip {ZENODO_ARCHIVE_NAME} -d {root}/zenodo_data`)\n"
        "\n"
        "See zenodo_data/README.md (the data manifest) and Notebooks/README.md\n"
        "> External data dependencies for the full per-dataset layout. If you\n"
        "already have the data elsewhere, most notebooks also accept a\n"
        "per-dataset ZENODO_<NAME>_DIR environment-variable override -- see\n"
        "this notebook's configuration cell.\n"
        + "=" * 74 + "\n"
    )
    raise FileNotFoundError(msg)
