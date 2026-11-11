# paleoceanography — Eocene model SST and the DeepMIP proxy compilation

**Provenance:** Leonard et al. (2025) PLASIM-GENIE simulations; Hollis et al. (2019) DeepMIP compilation, as distributed by Inglis et al. (2020)

The model and proxy data of notebook J04. `tools/build_paleoceanography_j04.py` rebuilds both files from the published archives.

## Contents

```
paleoceanography/  (48 KB)
├── README.md
├── genie_sst_50Ma_leonard2025.nc
└── deepmip_hollis2019_compilation.csv
```

**`genie_sst_50Ma_leonard2025.nc`** — annual-mean sea-surface temperature (`sst`, °C) at 50 Ma: the top layer (0–81 m) of the GOLDSTEIN ocean of the PLASIM-GENIE simulation of Leonard et al. (2025) with the Merdith et al. (2021) paleomagnetic reference frame (Zahirovic et al. 2022 relative plate motions, anchor plate 701701). 64 × 32 cells; `lon` −177.2…177.2, `lat` −86.6…86.6; land cells are NaN. Extracted from `Reference_Frame_Results/Merdith2021_paleomag/50Ma_nc_outputs/gold_spn_av_0000003000_00.nc` of the Zenodo archive; longitudes shifted from 0–360 to −180–180.

**`deepmip_hollis2019_compilation.csv`** — the DeepMIP site compilation of Hollis et al. (2019): 209 sea-surface (`sst`) and land-air (`lat`) temperature estimates for the latest Paleocene (`lp`), the PETM (`petm`) and the early Eocene Climatic Optimum (`eeco`), each with site, proxy, modern coordinates, mantle-frame and paleomagnetic-frame paleo-coordinates at 56 Ma (LP, PETM) or 52 Ma (EECO), percentiles 5/50/95, uncertainty bounds, and flags `v1`–`v5` marking the subsets of Inglis et al. (2020). Missing values are −999.9. This is the file `Hollis 2019 DeepMIP compilation.csv` of the Inglis et al. (2020) supplement, re-encoded from Latin-1 to UTF-8 with LF line ends; the column definitions are in `Read Me Hollis 2019 DeepMIP Compilation.xlsx` of the same supplement. J04 corrects one longitude on reading (the δ18O row of Hampden Beach, 107.83 → 170.83, as in its other rows and its paleo-coordinates).

## Consumer notebooks

**J04**

## References

Leonard, J., Zahirovic, S., Holden, P.B., Salles, T., Edwards, N.R. & Mallard, C.A. (2025). Polar wander leads to large differences in past climate reconstructions. *Communications Earth & Environment* 6, 508. https://doi.org/10.1038/s43247-025-02485-w — data: https://doi.org/10.5281/zenodo.15628277

Holden, P.B., Edwards, N.R., Fraedrich, K., Kirk, E., Lunkeit, F. & Zhu, X. (2016). PLASIM-GENIE v1.0: a new intermediate complexity AOGCM. *Geoscientific Model Development* 9, 3347–3361. https://doi.org/10.5194/gmd-9-3347-2016

Hollis, C.J. et al. (2019). The DeepMIP contribution to PMIP4: methodologies for selection, compilation and analysis of latest Paleocene and early Eocene climate proxy data, incorporating version 0.1 of the DeepMIP database. *Geoscientific Model Development* 12, 3149–3206. https://doi.org/10.5194/gmd-12-3149-2019

Inglis, G.N. et al. (2020). Global mean surface temperature and climate sensitivity of the early Eocene Climatic Optimum (EECO), Paleocene–Eocene Thermal Maximum (PETM), and latest Paleocene. *Climate of the Past* 16, 1953–1968. https://doi.org/10.5194/cp-16-1953-2020

## License

CC BY 4.0 (Leonard et al. 2025 Zenodo archive; Inglis et al. 2020 supplement).
