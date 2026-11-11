# hf_nd_isotopes — Global Lu-Hf zircon and Sm-Nd whole-rock databases

**Provenance:** Puetz, Spencer, Condie & Roberts (2024), *Scientific Data* 11, 56

Three tables built from two workbooks of the Figshare record of Puetz et al. (2024): DB4, the Lu-Hf zircon database (one row per zircon analysis, with U-Pb age), and DB5, the Sm-Nd whole-rock database. εHf(t), εNd(t) and the two-stage depleted-mantle model ages (T_DM2) are copied as Puetz et al. (2024) calculated them; they recalculated these quantities for every analysis with one set of constants. `tools/build_hf_nd_puetz2024.py` rebuilds the three files from the workbooks, which it downloads from Figshare and checks against the MD5 sums of version 1.

## Contents

```
hf_nd_isotopes/  (2.4 MB)
├── README.md
├── hf_zircon_grains.csv.gz    210,064 zircon analyses with a U-Pb age between 0 and 4500 Ma
├── hf_zircon_samples.csv.gz   7,061 samples (3,266 igneous, 3,791 detrital, 4 miscellaneous)
└── nd_whole_rock.csv.gz       22,019 whole-rock analyses (19,039 igneous, 2,980 detrital)
```

Each file starts with three `#` comment lines (read with `pd.read_csv(path, comment="#")`).

**hf_zircon_grains.csv.gz**

| Column | Meaning |
|---|---|
| `sample_key` | Puetz et al. sample key (reference and sample number, e.g. `R10002-S00003`); joins to `hf_zircon_samples` |
| `age_ma` | zircon U-Pb age (Ma) |
| `eps_hf_t` | εHf(t) at the U-Pb age |
| `tdm2_ma` | two-stage depleted-mantle Hf model age (Ma) |
| `rock_class` | `igneous`, `detrital` or `miscellaneous` (the database's Class-1 rock type) |

**hf_zircon_samples.csv.gz**

| Column | Meaning |
|---|---|
| `sample_key` | as above |
| `country`, `continent`, `geol_unit` | location as given in the database (`geol_unit`: its major geographic-geologic description) |
| `lon`, `lat` | sample location (WGS84 decimal degrees) |
| `rock_class`, `rock_type`, `mafic_felsic` | Class-1 and Class-3 rock types; mafic/felsic class |
| `n_grains` | number of analyses of the sample in `hf_zircon_grains` |
| `age_ma`, `eps_hf_t`, `tdm2_ma` | medians of the sample's analyses; they characterise an igneous sample, not a detrital one |

**nd_whole_rock.csv.gz**

| Column | Meaning |
|---|---|
| `sample_key`, `sample_id` | Puetz et al. sample key and published sample ID |
| `country`, `continent`, `geol_unit` | as above |
| `lon`, `lat` | sample location (decimal degrees) |
| `rock_class`, `rock_type`, `mafic_felsic` | as above |
| `age_ma` | crystallisation age, or the assumed age used for εNd(t) (Ma) |
| `sm147_nd144`, `nd143_nd144` | measured ¹⁴⁷Sm/¹⁴⁴Nd and ¹⁴³Nd/¹⁴⁴Nd |
| `eps_nd_t` | εNd(t) at `age_ma` |
| `tdm2_ma` | two-stage depleted-mantle Nd model age (Ma), the authors' preferred model age; empty for 500 analyses |

## Consumer notebooks

**D05**

## References

Puetz, S.J., Spencer, C.J., Condie, K.C. & Roberts, N.M.W. (2024). Enhanced U-Pb detrital zircon, Lu-Hf zircon, δ18O zircon, and Sm-Nd whole rock global databases. *Scientific Data* 11, 56. https://doi.org/10.1038/s41597-023-02902-9 — data: https://doi.org/10.6084/m9.figshare.24852987

The original publications of each analysis are listed in the `References` sheets of the two workbooks.

## License

CC BY 4.0 (Puetz et al. 2024, Figshare record). The files here are derived from the original workbooks (columns selected and renamed, sample medians computed).
