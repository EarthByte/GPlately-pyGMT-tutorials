# SCION end-Permian (252 Ma) CO2-sensitivity ensemble — compact bundle

Source: Andrew Merdith's SCION coupled-model output, version `MER25rev6` (2025-08-01).
SCION = cGENIE + PLASIM + GOLDSTEIN. PLASIM atmosphere is T21 (64 lon x 32 lat,
~5.625 deg). GOLDSTEIN ocean is on a 64 lon x 32 lat C-grid with 16 depth
levels (only the surface and 2D bathymetry are bundled here).

## Files

- `scion_252Ma_equilibrium.nc` — last-year (year 3000) snapshot per CO2 level.
  Dims (co2_ppm: 10, latitude: 32, longitude: 64). Variables: SAT, surface_T,
  sea_ice_cover, sea_ice_thickness, snow_depth, surface_albedo, landsea_mask,
  orography, top_thermal, top_solar.
- `scion_252Ma_bathymetry.nc` — GOLDSTEIN bathymetry per CO2. Identical
  across CO2 levels (same input geography); bundled per-CO2 for symmetry.
- `scion_252Ma_spinup.nc` — (co2_ppm, year) energy-balance time series for
  the model-stability / spin-up curves (T41 cell 5). 30 yearly steps per
  CO2 level (years 100..3000 in steps of 100).

## CO2 levels

140, 280, 560, 1120, 2240, 3360, 4480, 8960, 17920, 35840 ppm.
End-Permian best-estimate ~1120 ppm; runaway scenarios up to 35840 ppm.

## Size

Full bundle ~50 KB compressed (vs 1.5 GB for the raw model output).
That covers everything T41 + T42 need.

## Provenance

Original output lives at
`/Users/dietmar/Documents/Software/paleoclimate_notebooks/scion_stacks_2025_MER25rev6_252_Ma/`.
For the full model output (every yearly snapshot, every variable, all of
cGENIE biogeochemistry), contact Andrew Merdith.

## Citation

For now, cite the SCION model description:

  Mills, B.J.W., Donnadieu, Y., Godderis, Y. (2021). Spatial continuous
  integration of Phanerozoic global biogeochemistry and climate. *Gondwana
  Research* 100, 73-86.

And acknowledge Andrew Merdith's 252 Ma ensemble as personal communication
pending publication.
