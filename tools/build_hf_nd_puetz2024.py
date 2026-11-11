"""Build data/hf_nd_isotopes/ from the global Lu-Hf zircon and Sm-Nd whole-rock databases of Puetz et al. (2024).

Source: Puetz, S.J., Spencer, C.J., Condie, K.C. & Roberts, N.M.W. (2024). Enhanced U-Pb detrital zircon, Lu-Hf
zircon, δ18O zircon, and Sm-Nd whole rock global databases. Scientific Data 11, 56.
https://doi.org/10.1038/s41597-023-02902-9 -- data: https://doi.org/10.6084/m9.figshare.24852987 (CC BY 4.0).

The script reads two of the twelve Excel workbooks of the Figshare record:
  DB4 - Lu-Hf zircon database.xlsx       sheet Lu-Hf_Data   (one row per zircon analysis)
  DB5 - Sm-Nd whole-rock database.xlsx   sheet Sm_Nd_Data   (one row per whole-rock analysis)
and writes three files.  εHf(t), εNd(t) and the two-stage depleted-mantle model ages are copied as calculated by
Puetz et al. (2024), who recalculated them for every analysis with one set of constants.

    python tools/build_hf_nd_puetz2024.py                         # downloads both workbooks from Figshare
    python tools/build_hf_nd_puetz2024.py --dir path/to/workbooks # or reads local copies

Files written (data/hf_nd_isotopes/)
  hf_zircon_grains.csv.gz   every zircon analysis with a U-Pb age (0-4500 Ma): sample_key, age_ma, eps_hf_t,
                            tdm2_ma, rock_class (igneous / detrital / miscellaneous)
  hf_zircon_samples.csv.gz  one row per sample: sample_key, country, continent, geol_unit, lon, lat,
                            rock_class, rock_type, mafic_felsic, n_grains and the medians of the sample's grains
                            (age_ma, eps_hf_t, tdm2_ma); the medians characterise an igneous sample, not a detrital one
  nd_whole_rock.csv.gz      every whole-rock Sm-Nd analysis: sample_key, sample_id, country, continent, geol_unit,
                            lon, lat, rock_class, rock_type, mafic_felsic, age_ma (crystallisation or assumed age),
                            sm147_nd144, nd143_nd144, eps_nd_t, tdm2_ma
"""
import argparse
import hashlib
import io
import urllib.request
from pathlib import Path

import pandas as pd

FILES = {  # Figshare file id, MD5 of version 1
    "DB4 - Lu-Hf zircon database.xlsx": (43728618, "c1e4e051acb14633f6f7003829354d2e"),
    "DB5 - Sm-Nd whole-rock database.xlsx": (43728621, "0af687a0e913f786a5ca9e101c8e95f7"),
}
OUT = Path(__file__).resolve().parents[1] / "data/hf_nd_isotopes"
CITE = ("Puetz, S.J., Spencer, C.J., Condie, K.C. & Roberts, N.M.W. (2024), Scientific Data 11, 56, "
        "doi:10.1038/s41597-023-02902-9; data doi:10.6084/m9.figshare.24852987 (CC BY 4.0)")


def workbook(name, local_dir):
    fid, md5 = FILES[name]
    if local_dir:
        raw = (Path(local_dir) / name).read_bytes()
    else:
        req = urllib.request.Request(f"https://ndownloader.figshare.com/files/{fid}",
                                     headers={"User-Agent": "GPlately-pyGMT-tutorials data build"})
        with urllib.request.urlopen(req) as r:
            raw = r.read()
    assert hashlib.md5(raw).hexdigest() == md5, f"{name}: not version 1 of the Figshare record"
    return io.BytesIO(raw)


def text(s):
    return s.astype(str).str.split().str.join(" ").replace({"nan": "", "None": ""})


def write(df, path, what):
    with open(path, "wb") as f:
        head = f"# {what}\n# from {CITE}\n# Built by tools/build_hf_nd_puetz2024.py; see README.md in this folder for the columns.\n"
        if path.suffix == ".gz":
            import gzip
            with gzip.GzipFile(fileobj=f, mode="wb", mtime=0) as g:
                g.write(head.encode())
                g.write(df.to_csv(index=False).encode())
        else:
            f.write(head.encode())
            f.write(df.to_csv(index=False).encode())
    print(f"wrote {path.name}: {len(df)} rows, {path.stat().st_size / 1e6:.2f} MB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", help="folder with local copies of the two workbooks (default: download)")
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)

    # ---- Lu-Hf zircon (DB4) ------------------------------------------------------------------------------------
    hf = pd.read_excel(workbook("DB4 - Lu-Hf zircon database.xlsx", a.dir), sheet_name="Lu-Hf_Data",
                       usecols=range(27))
    hf.columns = [" ".join(str(c).split()) for c in hf.columns]
    num = {c: pd.to_numeric(hf[c], errors="coerce") for c in
           ["U-Pb Age (Ma)", "εHf(t) calc", "TDM2 (Ma) calc", "Latitude", "Longitude"]}
    ok = num["U-Pb Age (Ma)"].between(0, 4500, inclusive="right") & num["εHf(t) calc"].notna() \
        & hf["Ref-Sample Key"].notna()
    hf = hf[ok]
    grains = pd.DataFrame({
        "sample_key": hf["Ref-Sample Key"].astype(str).str.strip(),
        "age_ma": num["U-Pb Age (Ma)"][ok].round(1),
        "eps_hf_t": num["εHf(t) calc"][ok].round(2),
        "tdm2_ma": num["TDM2 (Ma) calc"][ok].round(0),
        "rock_class": text(hf["Class-1 Rock Type"]),
        "lon": num["Longitude"][ok], "lat": num["Latitude"][ok],
    })
    assert grains["lon"].between(-180, 180).all() and grains["lat"].between(-90, 90).all()
    meta = pd.DataFrame({
        "sample_key": grains["sample_key"],
        "country": text(hf["Country/Small Region"]), "continent": text(hf["Continent"]),
        "geol_unit": text(hf["Major Geographic-Geologic Description"]),
        "lon": grains["lon"].round(5), "lat": grains["lat"].round(5), "rock_class": grains["rock_class"],
        "rock_type": text(hf["Class-3 Rock Type"]), "mafic_felsic": text(hf["Mafic_Felsic"]),
    }).drop_duplicates("sample_key").set_index("sample_key")
    g = grains.groupby("sample_key")
    samples = meta.join(pd.DataFrame({
        "n_grains": g.size(),
        "age_ma": g["age_ma"].median().round(1),
        "eps_hf_t": g["eps_hf_t"].median().round(2),
        "tdm2_ma": g["tdm2_ma"].median().round(0),
    })).reset_index()
    write(grains.drop(columns=["lon", "lat"]).sort_values(["sample_key", "age_ma"]),
          OUT / "hf_zircon_grains.csv.gz", "Lu-Hf zircon analyses with a U-Pb age (one row per grain)")
    write(samples.sort_values("sample_key"), OUT / "hf_zircon_samples.csv.gz",
          "Lu-Hf zircon samples (one row per sample; age_ma, eps_hf_t, tdm2_ma are medians of the sample's grains)")

    # ---- Sm-Nd whole rock (DB5) --------------------------------------------------------------------------------
    nd = pd.read_excel(workbook("DB5 - Sm-Nd whole-rock database.xlsx", a.dir), sheet_name="Sm_Nd_Data",
                       usecols=range(18))
    nd.columns = [" ".join(str(c).split()) for c in nd.columns]

    def n(c):
        return pd.to_numeric(nd[c], errors="coerce")

    out = pd.DataFrame({
        "sample_key": text(nd["Sample-Ref Key"]), "sample_id": text(nd["Sample ID"]),
        "country": text(nd["Country/Small Region"]), "continent": text(nd["Continent"]),
        "geol_unit": text(nd["Major Geographic-Geologic Description"]),
        "lon": n("GPS Longitude").round(5), "lat": n("GPS Latitude").round(5),
        "rock_class": text(nd["Rock-Type-1"]), "rock_type": text(nd["Rock-Type-3"]),
        "mafic_felsic": text(nd["Felsic or Mafic ?"]),
        "age_ma": n("Crystal-Age or Assumed Age (Ma)"),
        "sm147_nd144": n("Sampled 147Sm/144Nd"), "nd143_nd144": n("Sampled 143Nd/144Nd"),
        "eps_nd_t": n("εNd(t)").round(2), "tdm2_ma": n("Preferred 2-stage TDM2").round(0),
    })
    assert len(out) == 22019, len(out)
    assert out["lon"].between(-180, 180).all() and out["lat"].between(-90, 90).all()
    write(out, OUT / "nd_whole_rock.csv.gz", "Sm-Nd whole-rock analyses (one row per analysis)")


if __name__ == "__main__":
    main()
