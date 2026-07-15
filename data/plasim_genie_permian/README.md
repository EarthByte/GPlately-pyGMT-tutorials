# PLASIM-GENIE end-Permian (252 Ma) CO2-sensitivity ensemble — compact bundle

Source: Andrew Merdith's PLASIM-GENIE coupled-model output, version `MER25rev6`
(2025-08-01). PLASIM-GENIE = PLASIM atmosphere + GOLDSTEIN ocean (the cGENIE
biogeochemistry module was off for these runs). PLASIM atmosphere is T21
(64 lon x 32 lat, ~5.625 deg). GOLDSTEIN ocean is on a 64 lon x 32 lat C-grid
with 16 depth levels (only the surface and 2D bathymetry are bundled here).

## Files

- `plasim_genie_252Ma_equilibrium.nc` — last-year (year 3000) snapshot per CO2
  level. Dims (co2_ppm: 10, latitude: 32, longitude: 64). Variables: SAT,
  surface_T, sea_ice_cover, sea_ice_thickness, snow_depth, surface_albedo,
  landsea_mask, orography, top_thermal, top_solar.
- `plasim_genie_252Ma_bathymetry.nc` — GOLDSTEIN bathymetry per CO2. Identical
  across CO2 levels (same input geography); bundled per-CO2 for symmetry.
- `plasim_genie_252Ma_spinup.nc` — (co2_ppm, year) energy-balance time series
  for the model-stability / spin-up curves (T44 §5). 30 yearly steps per CO2
  level (years 100..3000 in steps of 100).

## CO2 levels

140, 280, 560, 1120, 2240, 3360, 4480, 8960, 17920, 35840 ppm.
End-Permian best-estimate ~1120 ppm; runaway scenarios up to 35840 ppm.

## Size

Full bundle ~50 KB compressed (vs 1.5 GB for the raw model output).
That covers everything T43 + T44 need.

## Provenance

For the full model output (every yearly snapshot, every variable), contact
Andrew Merdith.

## Citation

Cite the PLASIM-GENIE model description:

  Holden, P.B., Edwards, N.R., Fraedrich, K., Kirk, E., Lunkeit, F. & Zhu, X.
  (2016). PLASIM-GENIE v1.0: a new intermediate complexity AOGCM.
  *Geoscientific Model Development* 9, 3347-3361.

And acknowledge Andrew Merdith's 252 Ma ensemble as personal communication
pending publication.
