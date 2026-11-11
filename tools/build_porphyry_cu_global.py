"""Build data/porphyry_cu_global/global_porphyry_cu.csv from the USGS global porphyry copper database.

Source: Singer, D.A., Berger, V.I. & Moring, B.C. (2008). Porphyry copper deposits of the world: database and grade
and tonnage models, 2008. U.S. Geological Survey Open-File Report 2008-1155. https://pubs.usgs.gov/of/2008/1155/
(public domain).  The script reads the database's Excel table (data/PorCuEX2008.xls in the USGS release) and keeps
every deposit with a published age (AgeMY > 0): 576 of the 690 deposits.

    python tools/build_porphyry_cu_global.py                       # downloads the table from the USGS
    python tools/build_porphyry_cu_global.py --xls PorCuEX2008.xls # or reads a local copy

Columns written
  deposit_id   USGS DepositID
  name         deposit name (NameDeposit, whitespace normalised)
  country      Country
  lon, lat     LongitudeDecimal, LatitudeDecimal (degrees, present day)
  age_ma       AgeMY: age of mineralisation (Ma); the database's age range is in age_range
  age_range    "Deposit Age" as given in the database (e.g. "6–5")
  subtype      Cox & Singer (1992) model type: 17 porphyry Cu, 20c porphyry Cu-Au, 21a porphyry Cu-Mo
  commodity    the same as a label: Cu, Cu-Au or Cu-Mo
  tonnage_mt   ore tonnage (million tonnes)
  cu_pct, mo_pct, au_gt, ag_gt
               average grades (Cu and Mo in percent, Au and Ag in g/t)
Tonnage and grades are left empty where the database reports no tonnage (its grades are 0 there). Where a tonnage
is reported, grades are copied as given; a grade of 0 means not reported or not significant, as in the source.
"""
import argparse
import io
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd

URL = "https://pubs.usgs.gov/of/2008/1155/data/PorCuEX2008.xls"
OUT = Path(__file__).resolve().parents[1] / "data/porphyry_cu_global/global_porphyry_cu.csv"
SUBTYPE = {"17": "Cu", "20c": "Cu-Au", "21a": "Cu-Mo"}

HEADER = """\
# Global porphyry copper deposits with a published age of mineralisation: 576 of the 690 deposits in
# Singer, D.A., Berger, V.I. & Moring, B.C. (2008), Porphyry copper deposits of the world: database and grade and
# tonnage models, 2008, U.S. Geological Survey Open-File Report 2008-1155, https://pubs.usgs.gov/of/2008/1155/
# (public domain). Built by tools/build_porphyry_cu_global.py; see README.md in this folder for the columns.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--xls", help="local copy of PorCuEX2008.xls (default: download from the USGS)")
    a = ap.parse_args()
    if a.xls:
        src = a.xls
    else:
        req = urllib.request.Request(URL, headers={"User-Agent": "GPlately-pyGMT-tutorials data build"})
        with urllib.request.urlopen(req) as r:
            src = io.BytesIO(r.read())
    d = pd.read_excel(src)
    assert len(d) == 690, f"expected the 690 deposits of the 2008 database, got {len(d)}"

    age = pd.to_numeric(d["AgeMY"], errors="coerce")
    d = d.loc[age > 0].copy()
    sub = d["Subtype"].astype(str).str.strip()
    assert sub.isin(SUBTYPE).all(), sorted(set(sub) - set(SUBTYPE))
    has_t = d["Tonnage"].notna() & (d["Tonnage"] > 0)

    def grade(col):
        return d[col].where(has_t).round(4)

    out = pd.DataFrame({
        "deposit_id": d["DepositID"].astype(int),
        "name": d["NameDeposit"].astype(str).str.split().str.join(" "),
        "country": d["Country"].astype(str).str.strip(),
        "lon": d["LongitudeDecimal"].round(5),
        "lat": d["LatitudeDecimal"].round(5),
        "age_ma": pd.to_numeric(d["AgeMY"]).round(3),
        "age_range": d["Deposit Age"].astype(str).str.split().str.join(" "),   # some entries contain line breaks
        "subtype": sub,
        "commodity": sub.map(SUBTYPE),
        "tonnage_mt": d["Tonnage"].where(has_t),
        "cu_pct": grade("Copper grade"),
        "mo_pct": grade("Molybdenum grade"),
        "au_gt": grade("Gold grade"),
        "ag_gt": grade("Silver grade"),
    }).sort_values(["age_ma", "deposit_id"]).reset_index(drop=True)
    assert out[["lon", "lat", "age_ma"]].notna().all().all()
    assert out["lon"].between(-180, 180).all() and out["lat"].between(-90, 90).all()

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write(HEADER)
        out.to_csv(f, index=False)
    print(f"wrote {OUT}: {len(out)} deposits, ages {out.age_ma.min():g}-{out.age_ma.max():g} Ma, "
          f"{out.commodity.value_counts().to_dict()}, tonnage for {int(out.tonnage_mt.notna().sum())}")


if __name__ == "__main__":
    main()
