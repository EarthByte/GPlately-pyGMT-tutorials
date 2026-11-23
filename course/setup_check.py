#!/usr/bin/env python3
"""Setup check for the short course "GPlates and Beyond".

Run it once at home, a few days before the course, from a terminal in which the
`gplately-pygmt` environment is active:

    python course/setup_check.py

It checks that Python and the required packages work, draws a small test map
with pyGMT, downloads the plate models used in the course (about 450 MB) into
gplately_data/ at the top of the tutorial folder, builds the paleomagnetic
reference frame that notebook F02 needs, and checks that the online services
used by some notebooks can be reached. Everything is stored inside the
tutorial folder; running the script again only fills in what is missing.

At the end it prints a summary. If every line says OK, your laptop is ready.
"""
import importlib
import platform
import shutil
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]          # the tutorial folder
DATA_DIR = REPO / "gplately_data"                   # where the notebooks look for plate models

# Plate models used by the course notebooks, with the seafloor age grids they read.
MODELS = {
    "Zahirovic2022": {"age_grids": [50]},           # A01, B03, B04, E01, F01, F02, J01, J03, J04, K01
    "Cao2024": {"age_grids": []},                   # G03, K04, F04
    "Merdith2021": {"age_grids": []},               # A02, I01, F10
    "Alfonso2024": {"age_grids": []},               # K05 (mineral-deposits track, extra)
}

PACKAGES = ["numpy", "pandas", "xarray", "matplotlib", "pygplates", "gplately",
            "plate_model_manager", "pygmt", "cmcrameri", "geopandas", "panel",
            "requests", "xlrd", "jupyterlab"]

SERVICES = {
    "GPlates Web Service (A02)": "https://gws.gplates.org/",
    "Paleobiology Database (I01)": "https://paleobiodb.org/data1.2/",
    "Macrostrat (G03, I01)": "https://macrostrat.org/api/",
}

results = []                                        # (label, ok, message)


def report(label, ok, msg=""):
    results.append((label, ok, msg))
    print(f"  {'OK  ' if ok else 'FAIL'}  {label}" + (f": {msg}" if msg else ""), flush=True)


def check_python():
    print("\n1. Python")
    v = sys.version_info
    report(f"Python {v.major}.{v.minor}.{v.micro} on {platform.system()}",
           v >= (3, 10), "" if v >= (3, 10) else "Python 3.10 or newer is needed; see course/SETUP.md")


def check_packages():
    print("\n2. Packages")
    for name in PACKAGES:
        try:
            mod = importlib.import_module(name)
            report(name, True, getattr(mod, "__version__", ""))
        except Exception as e:                      # noqa: BLE001
            report(name, False, f"{type(e).__name__}: {e}. Is the gplately-pygmt environment active?")


def check_pygmt():
    print("\n3. pyGMT test map")
    try:
        import pygmt
        out = REPO / "course" / "setup_check_map.png"
        fig = pygmt.Figure()
        fig.coast(region="g", projection="W0/12c", land="tan", water="lightblue",
                  shorelines="0.2p", frame="afg")
        fig.text(x=147.3, y=-42.9, text="Hobart", font="10p,Helvetica-Bold,black", justify="LM", offset="0.15c/0c")
        fig.plot(x=147.3, y=-42.9, style="c0.15c", fill="red", pen="0.5p,black")
        fig.savefig(out)
        report("pyGMT draws a map", out.exists(), str(out.relative_to(REPO)))
    except Exception as e:                          # noqa: BLE001
        report("pyGMT draws a map", False, f"{type(e).__name__}: {e}")


def download_models():
    print(f"\n4. Plate models (into {DATA_DIR.relative_to(REPO)}/; first run takes a few minutes)")
    try:
        from plate_model_manager import PlateModelManager
        pmm = PlateModelManager()
    except Exception as e:                          # noqa: BLE001
        report("Plate Model Manager", False, f"{type(e).__name__}: {e}")
        return
    for name, cfg in MODELS.items():
        t0 = time.time()
        try:
            model = pmm.get_model(name, data_dir=str(DATA_DIR))
            model.get_rotation_model()
            for layer in model.get_avail_layers():
                model.get_layer(layer)
            for t in cfg["age_grids"]:
                model.get_raster("AgeGrids", t)
            report(name, True, f"{time.time() - t0:.0f} s")
        except Exception as e:                      # noqa: BLE001
            report(name, False, f"{type(e).__name__}: {e}")


def build_f02_frame():
    print("\n5. Paleomagnetic frame for F02 (built by running F01 once, about 30 s)")
    rot = REPO / "data" / "Zahirovic2022_with_gpmdb_frame.rot"
    if rot.exists():
        report("F01 frame file", True, "already present")
        return
    nb = next((REPO / "Notebooks").glob("F01_*.ipynb"), None)
    if nb is None:
        report("F01 frame file", False, "Notebooks/F01_*.ipynb not found")
        return
    out_dir = REPO / "course" / "_executed"
    out_dir.mkdir(exist_ok=True)
    cmd = [sys.executable, "-m", "nbconvert", "--to", "notebook", "--execute",
           "--ExecutePreprocessor.timeout=900", "--output-dir", str(out_dir), str(nb)]
    proc = subprocess.run(cmd, cwd=REPO / "Notebooks", capture_output=True, text=True)
    ok = proc.returncode == 0 and rot.exists()
    report("F01 frame file", ok, str(rot.relative_to(REPO)) if ok else proc.stderr.strip().splitlines()[-1:])


def check_services():
    print("\n6. Online services (used live by A02, G03 and I01)")
    try:
        import requests
    except Exception as e:                          # noqa: BLE001
        report("requests", False, str(e))
        return
    for label, url in SERVICES.items():
        try:
            r = requests.get(url, timeout=15)
            report(label, r.status_code < 500, f"HTTP {r.status_code}")
        except Exception as e:                      # noqa: BLE001
            report(label, False, f"not reachable ({type(e).__name__}); these notebooks need internet on the day")


def check_ffmpeg():
    print("\n7. ffmpeg (animations; optional)")
    path = shutil.which("ffmpeg")
    report("ffmpeg on the PATH", path is not None, path or "only needed for the animation cells")


if __name__ == "__main__":
    print(f"Setup check for 'GPlates and Beyond'\nTutorial folder: {REPO}")
    if not (REPO / "Notebooks").is_dir():
        sys.exit("Run this script from inside the GPlately-pyGMT tutorial folder (course/setup_check.py).")
    check_python()
    check_packages()
    check_pygmt()
    download_models()
    build_f02_frame()
    check_services()
    check_ffmpeg()
    essential = [r for r in results if not r[0].startswith(("ffmpeg", "GPlates Web", "Paleobiology", "Macrostrat"))]
    print("\n" + "=" * 70)
    if all(ok for _, ok, _ in essential):
        print("READY: everything the course needs works on this laptop.")
    else:
        print("NOT READY. Fix the FAIL lines above (see course/SETUP.md, 'If something fails'),")
        print("then run this script again. If you are stuck, email the output to the course organiser.")
    failed_optional = [lab for lab, ok, _ in results if not ok and lab not in [e[0] for e in essential]]
    if failed_optional:
        print("Optional items not working: " + "; ".join(failed_optional))
    print("=" * 70)
