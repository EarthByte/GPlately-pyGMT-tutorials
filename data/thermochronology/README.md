# thermochronology — Boone ThermoPlates auxiliary datasets

**Provenance:** Boone, S.C., re-processed from multiple public sources

**LARGE (~10 GB)** auxiliary data collection assembled by Sam Boone for the ThermoPlates cooling-rate + tectonic-forcing analysis. Only the notebooks that specifically depend on this bundle (T44, T45, T46, T47) should be run against it. On disk-constrained machines, extract only the subset relevant to your consumer notebook.

## Contents (top level)

```
thermochronology/  (~10 GB total)
├── AFEAD_Faults/             AFEAD active fault database — global
├── AFEAD_Faults_CentralAsia/ AFEAD subset for Central Asia
├── GEM_Faults/               Global Earthquake Model fault database
├── HadCM3_paleoprecip/       HadCM3 paleo-precipitation forcing (Boone workflow)
└── Southern_Margin_Polygons_V4/  Boone's per-age Eurasian southern-margin polygons
                              (231 .xy files, 0-230 Ma at 1-Myr cadence)
```

All faults were pre-reconstructed by Boone under the Zahirovic 2022 plate model — if you want to reconstruct them under a different plate model, re-run the reconstruction step against the raw AFEAD/GEM databases (available separately from AFEAD.com / GEM Foundation).

## Consumer notebooks

**T44**, **T45**, **T46**, **T47** — the ThermoPlates cluster F expansion.

## References

- **Boone, S.C., Kohn, B.P., Gleadow, A.J.W. et al. (2025).** ThermoPlates: linking thermochronology to plate tectonics. *Communications Earth & Environment* 6, 1015. [doi:10.1038/s43247-025-02123-x](https://doi.org/10.1038/s43247-025-02123-x)
- **AFEAD** — Zelenin, E., Bachmanov, D., Garipova, S., Trifonov, V. & Kozhurin, A. (2022). The Active Faults of Eurasia Database (AFEAD): the ontology and design behind the continental-scale dataset. *Earth System Science Data* 14, 4489-4503. [doi:10.5194/essd-14-4489-2022](https://doi.org/10.5194/essd-14-4489-2022)
- **GEM Foundation** — Global Active Faults Database, [globalquakemodel.org](https://www.globalquakemodel.org/).
- **HadCM3** — Valdes, P.J. et al. (2017). The BRIDGE HadCM3 family of climate models: HadCM3@Bristol v1.0. *Geoscientific Model Development* 10, 3715-3743.

## License

Boone et al. (2025) supplementary material — CC BY 4.0. Underlying AFEAD/GEM/HadCM3 databases carry their own licences (see links above).
