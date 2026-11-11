# sediment_hosted_cu — Sediment-hosted copper deposits of the world (USGS)

**Provenance:** Cox, Lindsey, Singer, Moring & Diggles (2003, rev. 2007), U.S. Geological Survey Open-File Report 03-107

`sediment_hosted_cu.csv` holds all 785 deposits of the USGS database *Sediment-hosted copper deposits of the world: deposit models and database*, version 1.3 (https://pubs.usgs.gov/of/2003/of03-107/). `tools/build_sediment_hosted_cu.py` rebuilds it from the database's comma-separated file, downloaded from the USGS. K04 reconstructs the 736 deposits whose host rocks are younger than 1800 Ma, the span of the Cao et al. (2024) plate model.

## Contents

```
sediment_hosted_cu/  (90 KB)
├── README.md
└── sediment_hosted_cu.csv
```

| Column | Meaning |
|---|---|
| `deposit_id` | USGS DepositID |
| `name`, `other_names`, `country` | deposit name, other names, country |
| `lon`, `lat` | present-day location (decimal degrees) |
| `host_age_ma`, `host_age` | age of the host rocks (Ma), and the same in words (e.g. `U. Proterozoic`, `Permian`) |
| `deposit_type` | the database's subtype: `Reduced-facies Cu`, `Redbed Cu`, `Revett Cu` or `Unclassified` |
| `ore_mt`, `cu_pct`, `co_pct`, `ag_ppm`, `cu_mt` | ore tonnage (Mt), Cu and Co grade (%), Ag grade (ppm), contained Cu (Mt); empty where not reported |
| `host_rocks`, `geol_province` | host-rock description and geologic province code |

The database gives the age of the host rocks, not a dated age of mineralisation. Contained copper is reported for 141 deposits (305 Mt Cu in all).

## Consumer notebooks

**K04**

## References

Cox, D.P., Lindsey, D.A., Singer, D.A., Moring, B.C. & Diggles, M.F. (2003, rev. 2007). Sediment-hosted copper deposits of the world: deposit models and database. *U.S. Geological Survey Open-File Report* 03-107, version 1.3. https://doi.org/10.3133/ofr2003107 (data: https://pubs.usgs.gov/of/2003/of03-107/)

## License

Public domain (U.S. Geological Survey).
