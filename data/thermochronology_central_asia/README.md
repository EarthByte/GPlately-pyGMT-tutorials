# thermochronology_central_asia — Central Asia thermal-history compilation

**Provenance:** Nixon et al. (2025), Central Asia thermochronology compilation (EarthBank); workflow of Boone et al. (2025)

Per-sample inverse thermal-history models for Central Asia used by Boone et al. (2025), from the ThermoPlates example data (https://github.com/samuelcboone/ThermoPlates, `Example_data_Central_Asia.csv`), downsampled to a 5-Myr cadence. The `TempDiff` column is the per-sample cooling rate in °C/Myr. `central_asia_regions.csv` names the region and sub-region codes.

## Contents

```
thermochronology_central_asia/  (1.9 MB)
├── README.md
├── central_asia_regions.csv
└── central_asia_thermal_histories.csv   (1.2 MB)
```

The per-age Parquet caches that G06 and G07 write (`thermochron_master/`, `kinematics_master/`) are not part of this folder: they are rebuilt on first run, or can be downloaded as `thermochronology_precomputed_cache_CentralAsia.zip` from the Zenodo companion archive (see `zenodo_data/README.md`).

## Consumer notebooks

**G05**, **G06**, **G07**, **G08**

## References

Boone, S.C. et al. (2025). Deciphering mantle, tectonic and climatic drivers of exhumation. *Communications Earth & Environment* 6, 1015. https://doi.org/10.1038/s43247-025-03005-6

Nixon, A., Glorie, S., Boone, S.C., Kohlmann, F. et al. (2025). Central Asia thermochronology compilation. AusGeochem/EarthBank. https://doi.org/10.58024/AGUA6E7B32B9

## License

CC BY 4.0.
