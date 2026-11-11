"""Build data/sediment_hosted_cu/sediment_hosted_cu.csv from the USGS sediment-hosted copper database.

Source: Cox, D.P., Lindsey, D.A., Singer, D.A., Moring, B.C. & Diggles, M.F. (2003, revised 2007). Sediment-hosted
copper deposits of the world: deposit models and database. U.S. Geological Survey Open-File Report 03-107,
version 1.3. https://pubs.usgs.gov/of/2003/of03-107/ (public domain). 785 deposits.

The script reads the database's comma-separated file (data_v1.3/sed_cu_v1.3.csv: Mac Roman text, CR line ends, no
header row) with the 34 column names of the database's Excel file, and keeps every deposit.

    python tools/build_sediment_hosted_cu.py                          # downloads the file from the USGS
    python tools/build_sediment_hosted_cu.py --csv sed_cu_v1.3.csv    # or reads a local copy

Columns written
  deposit_id          USGS DepositID
  name, other_names   NameDeposit, OtherNames
  country             Country
  lon, lat            Dec.Long, Dec.Lat (degrees, present day)
  host_age_ma         Ma: age of the host rocks (Ma), as given in the database
  host_age            Age: the host-rock age in words (e.g. "U. Proterozoic", "Permian")
  deposit_type        Reduced-facies Cu, Redbed Cu, Revett Cu or Unclassified (the database's subtypes)
  ore_mt, cu_pct, co_pct, ag_ppm, cu_mt
                      ore tonnage (Mt), Cu and Co grade (%), Ag grade (ppm), contained Cu (Mt); empty where the
                      database reports none
  host_rocks          HostRocks
  geol_province       GeolProv
"""
import argparse
import io
import urllib.request
from pathlib import Path

import pandas as pd

URL = "https://pubs.usgs.gov/of/2003/of03-107/data_v1.3/sed_cu_v1.3.csv"
OUT = Path(__file__).resolve().parents[1] / "data/sediment_hosted_cu/sediment_hosted_cu.csv"
# column names of the database's Excel file (data_v1.3/sed_cu_v1.3.xls), in file order
COLS = ["DepositID", "NameDeposit", "OtherNames", "Includes", "Country Code", "LatitudeDegrees", "LatitudeMinutes",
        "LatitudeSeconds", "LongitudeDegrees", "LongitudeMinutes", "LongitudeSeconds", "OreMmt", "CuGrade%",
        "CoGrade%", "AgGradeppm", "Country", "StateProvince", "DepositType", "HostRocks", "Footwall", "Age", "Ma",
        "Mineralogy", "HangingwallBeds", "AssociatedTypes", "Comments", "Reference", "TraceMinerals", "Unit",
        "GeolProv", "Dec.Lat", "Dec.Long", "CuMmt", "Cont"]
TYPES = {"Reduced facies Cu": "Reduced-facies Cu", "Redbed Cu": "Redbed Cu", "Revett Cu": "Revett Cu",
         "Uncl.": "Unclassified", "Unclassified": "Unclassified"}

HEADER = """\
# Sediment-hosted copper deposits of the world: all 785 deposits of Cox, D.P., Lindsey, D.A., Singer, D.A.,
# Moring, B.C. & Diggles, M.F. (2003, rev. 2007), U.S. Geological Survey Open-File Report 03-107, v1.3,
# https://pubs.usgs.gov/of/2003/of03-107/ (public domain). host_age_ma is the age of the host rocks.
# Built by tools/build_sediment_hosted_cu.py; see README.md in this folder for the columns.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", help="local copy of sed_cu_v1.3.csv (default: download from the USGS)")
    a = ap.parse_args()
    if a.csv:
        raw = Path(a.csv).read_bytes()
    else:
        req = urllib.request.Request(URL, headers={"User-Agent": "GPlately-pyGMT-tutorials data build"})
        with urllib.request.urlopen(req) as r:
            raw = r.read()
    # every value as text first (keep_default_na=False: the continent code "NA" is North America, not missing)
    d = pd.read_csv(io.StringIO(raw.decode("mac_roman")), header=None, names=COLS, lineterminator="\r",
                    dtype=str, keep_default_na=False)
    d = d[d["DepositID"].str.strip() != ""]
    assert len(d) == 785, f"expected the 785 deposits of version 1.3, got {len(d)}"
    assert d.iloc[0]["NameDeposit"].strip() == "Mehirize", "column order does not match the USGS file"

    def num(c):
        return pd.to_numeric(d[c].str.strip(), errors="coerce")

    def text(c):
        return d[c].str.split().str.join(" ")

    t = text("DepositType")
    assert t.isin(TYPES).all(), sorted(set(t) - set(TYPES))
    out = pd.DataFrame({
        "deposit_id": num("DepositID").astype(int),
        "name": text("NameDeposit"),
        "other_names": text("OtherNames"),
        "country": text("Country"),
        "lon": num("Dec.Long").round(5),
        "lat": num("Dec.Lat").round(5),
        "host_age_ma": num("Ma"),
        "host_age": text("Age"),
        "deposit_type": t.map(TYPES),
        "ore_mt": num("OreMmt"),
        "cu_pct": num("CuGrade%"),
        "co_pct": num("CoGrade%"),
        "ag_ppm": num("AgGradeppm"),
        "cu_mt": num("CuMmt"),
        "host_rocks": text("HostRocks"),
        "geol_province": text("GeolProv"),
    }).sort_values("deposit_id").reset_index(drop=True)
    assert out["lon"].between(-180, 180).all() and out["lat"].between(-90, 90).all()

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write(HEADER)
        out.to_csv(f, index=False)
    print(f"wrote {OUT}: {len(out)} deposits, {int(out.host_age_ma.notna().sum())} with a host-rock age "
          f"({out.host_age_ma.min():g}-{out.host_age_ma.max():g} Ma), {out.deposit_type.value_counts().to_dict()}, "
          f"contained Cu for {int(out.cu_mt.notna().sum())}")


if __name__ == "__main__":
    main()
