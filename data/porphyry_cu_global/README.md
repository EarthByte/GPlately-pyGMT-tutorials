# porphyry_cu_global — Global porphyry copper deposits

**Provenance:** Singer, Berger & Moring (2008), U.S. Geological Survey Open-File Report 2008-1155

`global_porphyry_cu.csv` holds the 576 deposits with a published age of mineralisation among the 690 deposits of the USGS database *Porphyry copper deposits of the world: database and grade and tonnage models, 2008* (https://pubs.usgs.gov/of/2008/1155/). `tools/build_porphyry_cu_global.py` rebuilds it from the database's Excel table (`PorCuEX2008.xls`), downloaded from the USGS. K02 reconstructs the 539 deposits younger than 410 Ma, the span of the Zahirovic et al. (2022) plate model, to their mineralisation ages; K01 uses the 22 Cenozoic deposits of New Guinea and the Solomon Islands.

## Contents

```
porphyry_cu_global/  (47 KB)
├── README.md
└── global_porphyry_cu.csv
```

| Column | Meaning |
|---|---|
| `deposit_id` | USGS DepositID |
| `name`, `country` | deposit name and country |
| `lon`, `lat` | present-day location (decimal degrees) |
| `age_ma` | age of mineralisation (Ma), the database's `AgeMY` |
| `age_range` | the database's `Deposit Age` text, e.g. `6–5` |
| `subtype`, `commodity` | model type: `17` porphyry Cu (`Cu`), `20c` porphyry Cu-Au (`Cu-Au`), `21a` porphyry Cu-Mo (`Cu-Mo`) |
| `tonnage_mt` | ore tonnage (million tonnes) |
| `cu_pct`, `mo_pct` | average Cu and Mo grades (%) |
| `au_gt`, `ag_gt` | average Au and Ag grades (g/t) |

Tonnage and grades are empty for the 205 deposits without a reported tonnage. Where a tonnage is reported, grades are as given in the database, where 0 means not reported or not significant. The database assigns the subtype from the Au/Mo ratio: Cu-Au if Au (ppm)/Mo (%) ≥ 30, Cu-Mo if ≤ 3, Cu otherwise.

## Consumer notebooks

**K01**, **K02**

## References

Singer, D.A., Berger, V.I. & Moring, B.C. (2008). Porphyry copper deposits of the world: database and grade and tonnage models, 2008. *U.S. Geological Survey Open-File Report* 2008-1155. https://pubs.usgs.gov/of/2008/1155/

## License

Public domain (U.S. Geological Survey).
