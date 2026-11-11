# macrostrat — Macrostrat columns and units

**Provenance:** Macrostrat public API (Peters et al., 2018)

Responses of the Macrostrat API (https://macrostrat.org/api/) saved by the notebooks on their last successful live query. G03 and I01 query the API live and fall back to these files only when it cannot be reached.

## Contents

```
macrostrat/  (1.0 MB)
├── README.md
├── macrostrat_columns.csv                (G03: column centroids, /api/columns)
├── units_cache_472_635_sedimentary.csv   (G03: sedimentary units 635–472 Ma, /api/units)
└── units_lith_cache_440_520.csv          (I01: units 520–440 Ma with lithology, /api/units?response=long)
```

`units_lith_cache_440_520.csv` keeps, for each unit, its centroid (`clat`, `clng`), age span (`t_age`, `b_age`), the summed proportions of its carbonate and siliciclastic lithologies, and its dominant lithology (carbonate, siliciclastic or other), as computed by I01.

## Consumer notebooks

**G03**, **I01**

## References

Peters, S.E., Husson, J.M. & Czaplewski, J. (2018). Macrostrat: A platform for geological data integration and deep-time Earth crust research. *Geochemistry, Geophysics, Geosystems* 19, 1393-1409. [doi:10.1029/2018GC007467](https://doi.org/10.1029/2018GC007467)

## License

CC0 (Macrostrat public data).
