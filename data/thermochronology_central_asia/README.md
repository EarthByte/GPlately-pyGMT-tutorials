      # thermochronology_central_asia — Boone Central Asia thermochronology (flat sample-history CSV + Parquet caches)

      **Provenance:** Boone et al. (2025) — the central-Asia core dataset of ThermoPlates

      The canonical Central Asia thermochronology compilation of Boone et al. (2025), with the flat per-sample thermal-history CSV and per-snapshot Parquet caches produced by T45/T46 (writers) and consumed by T47 (reader). The `TempDiff` column is the authoritative per-sample cooling rate in °C/Myr — do NOT recompute from OnlyCooling.

      ## Contents

      ```
      thermochronology_central_asia/  (1.9 MB)
central_asia_regions.csv
central_asia_thermal_histories.csv (1.2 MB)
kinematics_master/
  kinematics_master_100Ma.parquet
thermochron_master/
  thermochron_master_000Ma.parquet
  thermochron_master_005Ma.parquet
  thermochron_master_010Ma.parquet
  thermochron_master_015Ma.parquet
  thermochron_master_020Ma.parquet
  thermochron_master_025Ma.parquet
  thermochron_master_030Ma.parquet
  thermochron_master_035Ma.parquet
  thermochron_master_040Ma.parquet
  thermochron_master_045Ma.parquet
  thermochron_master_050Ma.parquet
  thermochron_master_055Ma.parquet
  thermochron_master_060Ma.parquet
  thermochron_master_065Ma.parquet
  thermochron_master_070Ma.parquet
  thermochron_master_075Ma.parquet
  thermochron_master_080Ma.parquet
  thermochron_master_085Ma.parquet
  thermochron_master_090Ma.parquet
  thermochron_master_095Ma.parquet
  thermochron_master_100Ma.parquet
  thermochron_master_105Ma.parquet
  thermochron_master_110Ma.parquet
  thermochron_master_115Ma.parquet
  thermochron_master_120Ma.parquet
  thermochron_master_125Ma.parquet
  thermochron_master_130Ma.parquet
  thermochron_master_135Ma.parquet
  thermochron_master_140Ma.parquet
  thermochron_master_145Ma.parquet
  thermochron_master_150Ma.parquet
      ```


      ## Consumer notebooks

      **T44**, **T45**, **T46**, **T47**

      ## References

      Boone, S.C., Kohn, B.P., Gleadow, A.J.W. et al. (2025). ThermoPlates: linking thermochronology to plate tectonics. *Communications Earth & Environment* 6, 1015.

      ## License

      CC BY 4.0.
