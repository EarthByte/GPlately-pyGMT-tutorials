#!/usr/bin/env python3
"""Build data/paleomag/gilder2001_xishuigou_directions.csv from the MagIC database.

Source data: Gilder, S., Chen, Y. & Sen, S. (2001), Oligo-Miocene magnetostratigraphy
and rock magnetism of the Xishuigou section, Subei (Gansu Province, western China) and
implications for shallow inclinations in central Asia, J. Geophys. Res. 106(B12),
30505-30521, https://doi.org/10.1029/2001JB000325.  MagIC contribution 20098
(https://earthref.org/MagIC/20098).

What the script does
  1. downloads the MagIC contribution file (or reads one given with --file),
  2. keeps the specimen-level characteristic directions with MAD <= --max-mad (default 10 deg;
     the MagIC contribution is already filtered this way),
  3. attaches the site coordinates (sites table, otherwise locations table),
  4. writes ONE csv (staged in a temporary file, then moved into place) and prints a summary.

Usage (from the repository root). Behind a TLS-inspecting VPN either point SSL_CERT_FILE and
REQUESTS_CA_BUNDLE to a CA bundle that contains the VPN root certificate, install `truststore`
(pip install truststore; used automatically), or download the file in a browser and pass --file:

    python data/paleomag/build_gilder2001_csv.py
    python data/paleomag/build_gilder2001_csv.py --file /path/to/magic_contribution_20098.txt
"""
import argparse
import io
import os
import sys
import tempfile

import numpy as np
import pandas as pd

URL = "https://earthref.org/MagIC/download/20098/magic_contribution_20098.txt"
OUT_DEFAULT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "gilder2001_xishuigou_directions.csv")


def parse_magic(text):
    """Split a MagIC 3.0 contribution file into {table name: DataFrame of strings}."""
    lines = [l.rstrip("\r") for l in text.split("\n")]
    lines = [l for l in lines if l.startswith(">>>>") or l.strip()]
    tables, i = {}, 0
    while i < len(lines):
        if lines[i].startswith(">>>>"):
            i += 1
            continue
        name = lines[i].split("\t")[1].strip().lower()
        i += 1
        while i < len(lines) and lines[i].startswith("*"):     # compact-format titles
            i += 1
        if i >= len(lines) or lines[i].startswith(">>>>"):     # empty table
            continue
        keys = [k.strip() for k in lines[i].split("\t")]
        i += 1
        rows = []
        while i < len(lines) and not lines[i].startswith(">>>>"):
            vals = lines[i].split("\t")
            vals += [""] * (len(keys) - len(vals))
            rows.append(dict(zip(keys, vals[:len(keys)])))
            i += 1
        if rows:
            tables.setdefault(name, []).extend(rows)
    return {k: pd.DataFrame(v) for k, v in tables.items()}


def num(s):
    return pd.to_numeric(s, errors="coerce")


def flip_to_common_polarity(dec, inc):
    """Return directions (deg) with reversed ones replaced by their antipodes,
    using the principal axis (Bingham) of the data as reference."""
    d, i = np.radians(dec), np.radians(inc)
    xyz = np.column_stack([np.cos(i) * np.cos(d), np.cos(i) * np.sin(d), np.sin(i)])
    w, v = np.linalg.eigh(xyz.T @ xyz)
    ax = v[:, -1]
    if ax[2] < 0:
        ax = -ax
    xyz = xyz * np.where(xyz @ ax < 0, -1.0, 1.0)[:, None]
    return (np.degrees(np.arctan2(xyz[:, 1], xyz[:, 0])) % 360.0,
            np.degrees(np.arcsin(np.clip(xyz[:, 2], -1, 1))))


def fisher_mean_inc(dec, inc):
    d, i = np.radians(dec), np.radians(inc)
    x, y, z = (np.cos(i) * np.cos(d)).mean(), (np.cos(i) * np.sin(d)).mean(), np.sin(i).mean()
    r = np.sqrt(x * x + y * y + z * z)
    return float(np.degrees(np.arcsin(z / r))), float(np.degrees(np.arctan2(y, x)) % 360.0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--file", help="use this local MagIC contribution file instead of downloading")
    ap.add_argument("--out", default=OUT_DEFAULT)
    ap.add_argument("--max-mad", type=float, default=10.0)
    a = ap.parse_args()

    if a.file:
        raw = open(a.file, "rb").read()
    else:
        import requests
        try:                      # use the operating-system certificate store (helps behind TLS-inspecting VPNs)
            import truststore
            truststore.inject_into_ssl()
        except Exception:
            pass
        print(f"downloading {URL}")
        r = requests.get(URL, timeout=(15, 180))
        r.raise_for_status()
        raw = r.content
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("latin-1")
    T = parse_magic(text)
    print("tables found:", {k: len(v) for k, v in T.items()})
    for k in ("specimens", "samples", "sites", "locations", "ages"):
        if k in T:
            print(f"  {k} columns: {list(T[k].columns)}")
    if "specimens" not in T:
        sys.exit("no specimens table in the file: cannot continue")

    sp = T["specimens"].copy()
    for c in ("dir_dec", "dir_inc"):
        if c not in sp:
            sys.exit(f"specimens table has no column {c}")
        sp[c] = num(sp[c])
    sp = sp.dropna(subset=["dir_dec", "dir_inc"])
    if "dir_tilt_correction" in sp:
        tc = num(sp["dir_tilt_correction"])
        if (tc == 100).any():
            sp = sp[tc == 100]
            print("kept tilt-corrected directions (dir_tilt_correction = 100)")
        else:
            print("WARNING: no dir_tilt_correction = 100 rows: using all directions as stored")
    mad_col = "dir_mad_free" if "dir_mad_free" in sp else None
    sp["mad"] = num(sp[mad_col]) if mad_col else np.nan
    if mad_col:
        sp = sp[(sp["mad"] <= a.max_mad) | sp["mad"].isna()]
    sp = sp.reset_index(drop=True)

    # ---- site of every specimen and the site coordinates
    if "site" not in sp.columns:
        sp["site"] = ""
    if "sample" in sp and "samples" in T and "site" in T["samples"]:
        m = dict(zip(T["samples"]["sample"], T["samples"]["site"]))
        sp["site"] = [m.get(s, "") or old for s, old in zip(sp["sample"], sp["site"])]
    site_lat = site_lon = None
    if "sites" in T and {"lat", "lon"} <= set(T["sites"].columns):
        st = T["sites"].copy()
        st["lat"], st["lon"] = num(st["lat"]), num(st["lon"])
        mlat, mlon = dict(zip(st["site"], st["lat"])), dict(zip(st["site"], st["lon"]))
        sp["site_lat"] = sp["site"].map(mlat)
        sp["site_lon"] = sp["site"].map(mlon)
    else:
        sp["site_lat"] = np.nan
        sp["site_lon"] = np.nan
    if sp["site_lat"].isna().all() and "locations" in T:
        lc = T["locations"]
        def col(c): return num(lc[c]).mean() if c in lc else np.nan
        site_lat = np.nanmean([col("lat_n"), col("lat_s")])
        site_lon = np.nanmean([col("lon_e"), col("lon_w")])
        sp["site_lat"], sp["site_lon"] = site_lat, site_lon
        print(f"site coordinates taken from the locations table: {site_lat:.3f} N, {site_lon:.3f} E")
    if sp["site_lat"].isna().all():
        print("WARNING: no coordinates found; set SITE_LON_LAT by hand in the notebook")

    out = sp[[c for c in ("specimen", "sample", "site", "site_lat", "site_lon",
                          "dir_dec", "dir_inc", "mad") if c in sp.columns]].rename(
        columns={"dir_dec": "dec", "dir_inc": "inc"})
    hdr = ("# Specimen-level characteristic directions (tilt-corrected), Xishuigou section, Subei, Gansu, China.\n"
           "# Source: Gilder, S., Chen, Y. & Sen, S. (2001), J. Geophys. Res. 106(B12), 30505-30521,\n"
           "#         https://doi.org/10.1029/2001JB000325 ; MagIC contribution 20098 (https://earthref.org/MagIC/20098).\n"
           f"# Selection: MAD <= {a.max_mad:g} deg. Written by data/paleomag/build_gilder2001_csv.py.\n"
           "# Both polarities are kept as published (reversed directions are not flipped here).\n")
    buf = io.StringIO()
    out.to_csv(buf, index=False, float_format="%.2f")
    d = os.path.dirname(os.path.abspath(a.out))
    fd, tmp = tempfile.mkstemp(dir=d, suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(hdr + buf.getvalue())
    os.replace(tmp, a.out)          # staged write: an interrupted run cannot damage an existing file

    dec_f, inc_f = flip_to_common_polarity(out["dec"].values, out["inc"].values)
    mi, md = fisher_mean_inc(dec_f, inc_f)
    print(f"\nwrote {a.out}")
    print(f"  N specimens        : {len(out)}  (normal {int((out['inc']>0).sum())}, negative inclination {int((out['inc']<0).sum())})")
    print(f"  mean direction     : Dec {md:.1f}, Inc {mi:.1f}  (after flipping reversed directions)")
    print(f"  site coordinates   : {out['site_lat'].mean():.2f} N, {out['site_lon'].mean():.2f} E")
    print("  (reference: with these data the PmagPy SVEI demo finds f ~ 0.52 and a corrected inclination of ~61 deg)")
    for k in ("ages", "sites"):
        if k in T:
            ac = [c for c in T[k].columns if c.startswith("age")]
            if ac:
                print(f"  {k} table age columns: {ac}; first rows:\n{T[k][ac].head(3).to_string(index=False)}")
                break


if __name__ == "__main__":
    main()
