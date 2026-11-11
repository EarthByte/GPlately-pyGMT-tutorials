"""Build the two data files of notebook J04 in data/paleoceanography/.

1. genie_sst_50Ma_leonard2025.nc -- annual-mean sea-surface temperature at 50 Ma from the PLASIM-GENIE simulations of
   Leonard et al. (2025): the top layer (0-80 m, centred at 39 m) of the GOLDSTEIN ocean temperature in the
   run with the Merdith et al. (2021) paleomagnetic reference frame (Zahirovic et al. 2022 relative plate motions,
   anchor plate 701701), file Reference_Frame_Results/Merdith2021_paleomag/50Ma_nc_outputs/gold_spn_av_0000003000_00.nc
   of the Zenodo archive. Land cells are NaN. Longitudes are shifted to -180..180.

     Leonard, J., Zahirovic, S., Holden, P.B., Salles, T., Edwards, N.R. & Mallard, C.A. (2025). Polar wander leads
     to large differences in past climate reconstructions. Communications Earth & Environment 6, 508.
     https://doi.org/10.1038/s43247-025-02485-w -- data: https://doi.org/10.5281/zenodo.15628277 (CC BY 4.0)

2. deepmip_hollis2019_compilation.csv -- the DeepMIP site compilation of sea-surface and land-air temperature
   estimates for the latest Paleocene (LP), PETM and early Eocene Climatic Optimum (EECO) of Hollis et al. (2019),
   as distributed in the supplement of Inglis et al. (2020) ("Hollis 2019 DeepMIP compilation.csv"). Copied
   unchanged except for re-encoding from Latin-1 to UTF-8 and CRLF to LF line ends.

     Hollis, C.J. et al. (2019). The DeepMIP contribution to PMIP4: methodologies for selection, compilation and
     analysis of latest Paleocene and early Eocene climate proxy data, incorporating version 0.1 of the DeepMIP
     database. Geoscientific Model Development 12, 3149-3206. https://doi.org/10.5194/gmd-12-3149-2019
     Inglis, G.N. et al. (2020). Global mean surface temperature and climate sensitivity of the early Eocene Climatic
     Optimum (EECO), Paleocene-Eocene Thermal Maximum (PETM), and latest Paleocene. Climate of the Past 16,
     1953-1968. https://doi.org/10.5194/cp-16-1953-2020 -- supplement (CC BY 4.0)

Both files are read from inside large zip archives with HTTP range requests, so only the two members are downloaded:

    pip install remotezip
    python tools/build_paleoceanography_j04.py
"""
import hashlib
import tempfile
from pathlib import Path

import numpy as np
import xarray as xr
from remotezip import RemoteZip

OUT = Path(__file__).resolve().parents[1] / "data/paleoceanography"
LEONARD_ZIP = "https://zenodo.org/api/records/15628277/files/Reference_Frame_Results.zip/content"
LEONARD_MEMBER = "Reference_Frame_Results/Merdith2021_paleomag/50Ma_nc_outputs/gold_spn_av_0000003000_00.nc"
INGLIS_ZIP = "https://cp.copernicus.org/articles/16/1953/2020/cp-16-1953-2020-supplement.zip"
INGLIS_MEMBER = "Hollis 2019 DeepMIP compilation.csv"
INGLIS_MD5 = "0c1cba10995209d39d0ccae9f4899635"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        with RemoteZip(LEONARD_ZIP) as z:
            nc = z.extract(LEONARD_MEMBER, tmp)
        ds = xr.open_dataset(nc, decode_times=False)
        top = ds["temp"].isel(time=0, depth=0).load()           # top ocean layer; land is NaN
        lon = ((top.longitude.values + 180.0) % 360.0) - 180.0
        order = np.argsort(lon)
        sst = xr.DataArray(top.values[:, order].astype("float32"), name="sst", dims=("lat", "lon"),
                           coords={"lat": ("lat", top.latitude.values.astype("float64"), {"units": "degrees_north"}),
                                   "lon": ("lon", lon[order].astype("float64"), {"units": "degrees_east"})},
                           attrs={"long_name": "annual-mean sea-surface temperature (top ocean layer, 0-81 m)",
                                  "units": "degC"})
        out = sst.to_dataset()
        out.attrs = {
            "title": "PLASIM-GENIE sea-surface temperature at 50 Ma (Leonard et al. 2025)",
            "source": f"Leonard et al. (2025), Zenodo 10.5281/zenodo.15628277, {LEONARD_MEMBER}",
            "reference_frame": "Merdith et al. (2021) paleomagnetic frame with Zahirovic et al. (2022) relative plate "
                               "motions (anchor plate 701701)",
            "age_ma": 50,
            "license": "CC BY 4.0",
            "history": "built by tools/build_paleoceanography_j04.py",
        }
        out.to_netcdf(OUT / "genie_sst_50Ma_leonard2025.nc",
                      encoding={"sst": {"zlib": True, "complevel": 4, "_FillValue": np.float32(np.nan)}})
        print(f"wrote genie_sst_50Ma_leonard2025.nc: {dict(sst.sizes)}, "
              f"{float(sst.min()):.1f} to {float(sst.max()):.1f} degC, {int(sst.notnull().sum())} ocean cells")

        with RemoteZip(INGLIS_ZIP) as z:
            csv = Path(z.extract(INGLIS_MEMBER, tmp))
        raw = csv.read_bytes()
        assert hashlib.md5(raw).hexdigest() == INGLIS_MD5, "not the published version of the DeepMIP compilation"
        text = raw.decode("latin-1").replace("\r\n", "\n")
        (OUT / "deepmip_hollis2019_compilation.csv").write_text(text, encoding="utf-8")
        print(f"wrote deepmip_hollis2019_compilation.csv: {text.count(chr(10)) - 1} rows")


if __name__ == "__main__":
    main()
