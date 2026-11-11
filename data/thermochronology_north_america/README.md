# thermochronology_north_america — USGS Geochron v4.0, fission-track and (U-Th)/He subset

**Provenance:** Hillenbrand et al. (2023, rev. 2025), USGS Geochron v4.0

The three USGS Geochron v4.0 tables G09 needs: sample metadata, apatite/zircon fission-track dates, and (U-Th)/He dates. On first run G09 reduces them to a flat thermal-history table, `na_thermal_histories.csv`, which it writes to `zenodo_data/thermochronology_geochronology_USGS_NorthAmerica/`. That Zenodo folder also holds G09's precomputed per-age dynamic-topography cache, `dyntopo_master/` (see `zenodo_data/README.md`).

## Contents

```
thermochronology_north_america/  (36 MB)
├── README.md
└── usgs_geochron_v4/
    ├── fissiontrack_USGS_data_release_v4.csv   (2.6 MB)
    ├── samples_USGS_data_release_v4.csv        (31.6 MB)
    └── uthhe_USGS_data_release_v4.csv          (1.9 MB)
```

## Consumer notebooks

**G09**

## References

Hillenbrand, I.W., et al. (2023, rev. 2025). *USGS Geochron: A Database of Geochronological and Thermochronological Dates and Data (ver. 4.0)*. U.S. Geological Survey data release. https://doi.org/10.5066/P9RZNPIF

## License

Public domain (U.S. Geological Survey).
