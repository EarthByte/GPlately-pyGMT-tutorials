#!/usr/bin/env python3
"""Rebuild the companion-archive zips so that each one extracts to the folder the notebooks read.

The notebooks look for their external data in zenodo_data/<folder>/ (folder names listed in
zenodo_data/README.md). Version 1 of the Zenodo archive (10.5281/zenodo.21836196) holds the right data,
but most of its zips extract to older folder names (wu2023_zircons/, santosh_dynamic_topography/,
sediment_thickness_bird_mooney/, ...), and the two Boone zips have no top folder at all.

This script copies every file of each v1 zip, byte for byte, into a new zip whose paths start with the
folder the notebooks read, leaves out macOS metadata (__MACOSX/, .DS_Store, ._*), and checks that the
new zip holds the same files with the same sizes and CRC-32 checksums. It reads one zip and writes one
zip per dataset (17 in all) to zenodo_data/upload_v1.1/, each first under a .part name, plus MD5SUMS.txt
and SIZES.txt. The v1 zips are not changed.

    python3 tools/build_zenodo_archive.py --only zircon_geochronology_Wu2023.zip    # pilot (2 MB)
    python3 tools/build_zenodo_archive.py                                            # all 17 (~3.7 GB)
"""
import argparse, hashlib, os, shutil, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "zenodo_data"
OUT = SRC / "upload_v1.1"

# zip name -> folder the notebooks read; "prefix" = v1 zip has no top folder, prepend the folder
ZIPS = {
    "zircon_geochronology_Wu2023.zip": ("zircon_geochronology_Wu2023", "strip"),
    "REVEAL_mantle_tomography.zip": ("REVEAL_mantle_tomography", "strip"),
    "paleoDEM_ScoteseWright2018.zip": ("paleoDEM_ScoteseWright2018", "strip"),
    "pySCION_biogeochemistry_model.zip": ("pySCION_biogeochemistry_model", "strip"),
    "dynamic_topography_Dhungana.zip": ("dynamic_topography_Dhungana", "strip"),
    "dynamic_topography_Young2022.zip": ("dynamic_topography_Young2022", "strip"),
    "gmcm9_dynamic_topography_Braz.zip": ("gmcm9_dynamic_topography_Braz", "strip"),
    "paleo_elevation_Zhou.zip": ("paleo_elevation_Zhou", "strip"),
    "thermochronology_precomputed_cache_CentralAsia.zip": ("thermochronology_precomputed_cache_CentralAsia", "strip"),
    "thermochronology_faults_Boone_core.zip": ("thermochronology_faults_Boone", "prefix"),
    "AFEAD_faults_Boone.zip": ("thermochronology_faults_Boone", "prefix"),
    "thermochronology_geochronology_USGS_NorthAmerica.zip": ("thermochronology_geochronology_USGS_NorthAmerica", "strip"),
    "sediment_thickness_BirdMooney.zip": ("sediment_thickness_BirdMooney", "strip"),
    "crustal_thickness_Afonso.zip": ("crustal_thickness_Afonso", "strip"),
    "foam_devonian_climatology_Pohl.zip": ("foam_devonian_climatology_Pohl", "strip"),
    "phansst_proxy_database_Judd2022.zip": ("phansst_proxy_database_Judd2022", "strip"),
    "gateway_reconstruction_Straume2020.zip": ("gateway_reconstruction_Straume2020", "strip"),
}


def junk(name):
    parts = name.split("/")
    return "__MACOSX" in parts or parts[-1] == ".DS_Store" or parts[-1].startswith("._")


def new_name(name, folder, mode):
    if mode == "prefix":
        return f"{folder}/{name}"
    top, _, rest = name.partition("/")
    if not rest:
        raise SystemExit(f"unexpected entry without a top folder: {name}")
    return f"{folder}/{rest}"


def md5(path, block=1 << 22):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(block), b""):
            h.update(chunk)
    return h.hexdigest()


def rebuild(zname, folder, mode):
    src = SRC / zname
    dst = OUT / zname
    tmp = OUT / (zname + ".part")
    with zipfile.ZipFile(src) as zin:
        members = [i for i in zin.infolist() if not i.is_dir() and not junk(i.filename)]
        tops = {i.filename.split("/")[0] for i in members}
        if mode == "strip" and len(tops) != 1:
            raise SystemExit(f"{zname}: expected one top folder, found {sorted(tops)}")
        with zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6, allowZip64=True) as zout:
            for info in members:
                zi = zipfile.ZipInfo(new_name(info.filename, folder, mode), date_time=info.date_time)
                zi.compress_type = zipfile.ZIP_DEFLATED
                zi.external_attr = info.external_attr
                with zin.open(info) as fi, zout.open(zi, "w", force_zip64=True) as fo:
                    shutil.copyfileobj(fi, fo, 1 << 22)
    # verify: same files, sizes and CRCs; every path starts with the folder
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(tmp) as zchk:
        a = {new_name(i.filename, folder, mode): (i.file_size, i.CRC) for i in zin.infolist()
             if not i.is_dir() and not junk(i.filename)}
        b = {i.filename: (i.file_size, i.CRC) for i in zchk.infolist()}
        if a != b:
            raise SystemExit(f"{zname}: content check FAILED ({len(a)} vs {len(b)} files)")
        assert all(n.startswith(folder + "/") for n in b)
    os.replace(tmp, dst)
    return len(b)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="comma-separated zip names (pilot)")
    a = ap.parse_args()
    names = a.only.split(",") if a.only else list(ZIPS)
    for n in names:
        if n not in ZIPS:
            raise SystemExit(f"unknown zip {n}")
        if not (SRC / n).exists():
            raise SystemExit(f"missing v1 zip {SRC / n}")
    OUT.mkdir(exist_ok=True)
    for n in names:
        folder, mode = ZIPS[n]
        count = rebuild(n, folder, mode)
        print(f"  {n}: {count} files -> {folder}/", flush=True)
    sums, sizes = [], []
    for n in ZIPS:
        p = OUT / n
        if p.exists():
            sums.append(f"{md5(p)}  {n}")
            sizes.append(f"{n}\t{p.stat().st_size}")
    (OUT / "MD5SUMS.txt").write_text("\n".join(sums) + "\n")
    (OUT / "SIZES.txt").write_text("\n".join(sizes) + "\n")
    print(f"done: {len(sums)} zips in {OUT}; see MD5SUMS.txt and SIZES.txt")


if __name__ == "__main__":
    main()
