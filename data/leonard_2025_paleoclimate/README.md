# leonard_2025_paleoclimate — Leonard 2025 reference-frame paleoclimate outputs

**Provenance:** Leonard et al. (2025), *Communications Earth & Environment*; data archive Zenodo 10.5281/zenodo.15628277

Compact subset of Leonard et al.'s (2025) PLASIM paleoclimate simulations run under three different reference frames (Merdith 2021 paleomag, Müller 2016 mantle, Torsvik 2019 paleomag). Three variables (SAT, GMST, landsea) × 26 ages (0–250 Ma at 10-Myr cadence) × 3 frames. Used to quantify reference-frame uncertainty in reconstructed paleoclimate (J07).

## Contents

```
leonard_2025_paleoclimate/  (190 MB)
merdith2021_paleomag/      26 NetCDF files, 000Ma.nc ... 250Ma.nc
muller2016_mantle/         26 NetCDF files
torsvik2019_paleomag/      26 NetCDF files
plate_reconstructions/     the plate models behind the three frames (188 MB):
  CITATIONS.txt            citations of the plate models
  Torsvik_etal_2019/       Torsvik et al. (2019) model, with its mantle and paleomagnetic frames
  Zahirovic_etal_2022_GDJ_NNR/   Zahirovic et al. (2022) relative motions used with the other frames
```
The climate fields are a compact subset (about 2 MB) of the 384 MB Leonard et al. archive on Zenodo.

## Consumer notebooks

**J07**

## References

Leonard, J., Zahirovic, S., Holden, P.B., Salles, T., Edwards, N.R. & Mallard, C.A. (2025). Polar wander leads to large differences in past climate reconstructions. *Communications Earth & Environment* 6, 508. https://doi.org/10.1038/s43247-025-02485-w — data: https://doi.org/10.5281/zenodo.15628277

The plate-model citations are in `plate_reconstructions/CITATIONS.txt`.

## License

CC BY 4.0 (Leonard et al. supplementary material).
