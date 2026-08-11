# evenick_2021_basins — Evenick (2021) revised global sedimentary basin map — 768 basins

**Provenance:** Evenick, J.C. (2021), *Earth-Science Reviews* 215, 103564 — supplementary material, redistributed verbatim

A revised global compilation of 768 sedimentary basin polygons, each carrying rich per-basin attributes: basin type (passive margin, rift, foreland, forearc, backarc, strike-slip, intracratonic, fold-and-thrust belt), region, sediment-thickness statistics from two independent sources (Straume et al. 2019 and Laske et al. 2013), Moho-depth statistics, and evaporite (salt) presence/style. The companion `mmc1` spreadsheet lists 368 individually dated evaporite occurrences across 217 of these basins (formation name, period, age range), joinable back onto the shapefile via `Basin UBI`. `mmc2` is Evenick's own column data-dictionary for the shapefile's attribute table.

All three files are the **unmodified originals** from the article's ScienceDirect supplementary material (only renamed for repo-naming consistency — byte content is untouched). Every derived artifact used in the tutorial notebook — GPML conversion, reconstruction plate-ID assignment, `.gpmlz` export — is generated **at runtime** by T53, not pre-baked and redistributed here (see License below).

## Contents

```
evenick_2021_basins/  (2.7 MB)
Evenick2021_GlobalBasins.shp (0.5 MB)
Evenick2021_GlobalBasins.shx
Evenick2021_GlobalBasins.dbf (2.1 MB)
Evenick2021_GlobalBasins.prj
Evenick2021_GlobalBasins.cpg
Evenick2021_GlobalBasins.qpj
Evenick2021_mmc1_evaporite_list.xlsx (48 KB) — "Evaporite list by basin"; join key: Basin UBI
Evenick2021_mmc2_column_dictionary.xlsx (10 KB) — data dictionary for the shapefile's attribute columns
```

## Consumer notebooks

**T53**

## References

Evenick, J.C. (2021). Glimpses into Earth's history using a revised global sedimentary basin map. *Earth-Science Reviews* 215, 103564. https://doi.org/10.1016/j.earscirev.2021.103564

Straume, E.O., et al. (2019). GlobSed: Updated total sediment thickness in the world's oceans. *Geochemistry, Geophysics, Geosystems* 20(4), 1756-1772. https://doi.org/10.1029/2018GC008115 — source of the shapefile's `Max Sed St` / `Mean Sed S` columns.

Laske, G., Masters, G., Ma, Z. & Pasyanos, M. (2013). Update on CRUST1.0 — A 1-degree global model of Earth's crust. *Geophysical Research Abstracts* 15, EGU2013-2658 — source of the shapefile's Moho-depth and alternative sediment-thickness columns.

## License

**CC BY-NC-ND 4.0** (verified via the article's Crossref record). These three files are redistributed **verbatim and unmodified**, which trivially satisfies the license's NoDerivatives (ND) term. Because ND prohibits redistributing an *adapted* version, this repo does not bundle any pre-converted or pre-joined form of this data (e.g. a `.gpmlz` conversion, or a shapefile pre-joined to the evaporite list) — T53 builds those at runtime from these originals, on demand, for the end user. The NonCommercial (NC) term is not a concern for this non-commercial teaching repo but is noted for completeness. Attribution: Evenick (2021), full citation above.
