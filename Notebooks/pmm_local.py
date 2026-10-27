"""Shared helper: plate-model loading that keeps working without the model server.

``PlateModelManager()`` always contacts repo.gplates.org (model list, metadata
and checksum checks) -- also when every file of the model is already in the
local cache.  When that server cannot be reached (offline, VPN or firewall
problems, server maintenance) the cells then hang or fail although all the data
are on disk.

``LocalFirstPMM`` is a drop-in replacement for ``PlateModelManager`` that

1. checks once per session (5 s timeout) whether the model server answers;
2. if it does, behaves exactly like ``PlateModelManager`` (new models are
   downloaded, cached models are verified), but with finite network timeouts
   so a stalled connection cannot hang a cell forever;
3. if it does not, loads the model straight from the local cache folder
   (``data_dir/<model name in lower case>/``) in read-only mode and says so.

A model that has never been downloaded cannot be loaded offline; the error
message then names the missing folder.  Set the environment variable
``PMM_OFFLINE=1`` to skip the server check and always use the local cache.

Usage in a notebook (the import cell already changes to the repo root)::

    import sys
    from pathlib import Path
    for _d in (Path("Notebooks"), Path("."), Path("../Notebooks")):
        if (_d / "pmm_local.py").exists():
            sys.path.insert(0, str(_d.resolve())); break
    from pmm_local import LocalFirstPMM

    pmm = LocalFirstPMM()                       # instead of PlateModelManager()
    model = pmm.get_model("Zahirovic2022", data_dir="./gplately_data")
"""
from __future__ import annotations

import os
from pathlib import Path

import requests
from plate_model_manager import PlateModel, PlateModelManager

# Same mirrors that plate_model_manager tries by default.
_REPO_URLS = (
    "https://repo.gplates.org/webdav/pmm/config/models_v2.json",
    "https://www.earthbyte.org/webdav/pmm/config/models_v2_eb.json",
    "https://portal.gplates.org/static/pmm/config/models_v2_gp.json",
)

_STATE: dict = {"online": None, "announced": False}


def server_reachable(timeout: float = 5.0, force: bool = False) -> bool:
    """True if one of the plate-model servers answers (result cached)."""
    if os.environ.get("PMM_OFFLINE", "").strip().lower() in ("1", "true", "yes"):
        return False
    if _STATE["online"] is not None and not force:
        return _STATE["online"]
    ok = False
    for url in _REPO_URLS:
        try:
            if requests.head(url, timeout=(timeout, timeout)).status_code == 200:
                ok = True
                break
        except Exception:
            continue
    _STATE["online"] = ok
    return ok


class _CachedPlateModel(PlateModel):
    """Read-only ``PlateModel`` that fails loudly when a layer is not cached.

    The stock read-only model silently returns an empty file list for a layer
    that was never downloaded, which surfaces much later as an obscure error.
    """

    def _need(self, layer: str) -> None:
        folder = Path(self.model_dir) / layer
        if not folder.is_dir():
            raise FileNotFoundError(
                f"Layer '{layer}' of model '{self.model_name}' is not in the local "
                f"cache ({folder}) and the plate-model server cannot be reached. "
                "Run once with a working connection to download it."
            )

    def get_rotation_model(self):
        self._need("Rotations")
        return super().get_rotation_model()

    def get_layer(self, layer_name, return_none_if_not_exist=False):
        if layer_name in self.get_avail_layers():
            if not (Path(self.model_dir) / layer_name).is_dir():
                if return_none_if_not_exist:
                    return None
                self._need(layer_name)
        return super().get_layer(layer_name, return_none_if_not_exist)


class LocalFirstPMM:
    """Drop-in for ``PlateModelManager`` that falls back to the local cache."""

    def __init__(self, timeout=(10, 120), model_manifest: str = ""):
        self.timeout = timeout
        self._pmm = None
        self._data_dir = "./gplately_data"
        if model_manifest or server_reachable():
            try:
                self._pmm = PlateModelManager(model_manifest=model_manifest,
                                              timeout=timeout)
            except Exception:
                _STATE["online"] = False
        if self._pmm is None and not _STATE["announced"]:
            _STATE["announced"] = True
            print("Plate-model server not reachable: using models cached in "
                  "the local data folder (read-only).")

    @property
    def offline(self) -> bool:
        return self._pmm is None

    def get_model(self, model_name: str = "default", data_dir: str = "."):
        self._data_dir = data_dir
        if self._pmm is not None:
            try:
                m = self._pmm.get_model(model_name, data_dir=data_dir)
                if m is not None:
                    m.timeout = self.timeout
                return m
            except Exception as exc:           # server vanished mid-session
                print(f"Plate-model server error ({type(exc).__name__}); "
                      "falling back to the local cache.")
                self._pmm = None
        model_dir = Path(data_dir) / model_name.lower()
        if not PlateModel.is_model_dir(str(model_dir)):
            have = self.get_available_model_names()
            raise FileNotFoundError(
                f"Model '{model_name}' is not cached in {Path(data_dir).resolve()} "
                f"and the plate-model server cannot be reached. Cached models: "
                f"{have or 'none'}.")
        return _CachedPlateModel(model_name, data_dir=data_dir, readonly=True)

    def get_available_model_names(self):
        if self._pmm is not None:
            return self._pmm.get_available_model_names()
        d = Path(self._data_dir)
        return (PlateModelManager.get_local_available_model_names(str(d))
                if d.is_dir() else [])

    def __getattr__(self, name):
        # Anything else (e.g. ``models``) is delegated to the real manager.
        pmm = self.__dict__.get("_pmm")
        if pmm is None:
            raise AttributeError(
                f"'{name}' needs the plate-model server, which is not reachable")
        return getattr(pmm, name)
