# pbdb — Paleobiology Database query responses

**Provenance:** Paleobiology Database public API

`pbdb_cache_Brachiopoda_440_520.csv` is the response of I01's live query of the Paleobiology Database (https://paleobiodb.org/data1.2/occs/list.json with `base_name=Brachiopoda`, `max_ma=520`, `min_ma=440`, `show=coords`, `vocab=pbdb`, `limit=all`), saved on 11 November 2026: 40,058 brachiopod occurrences with their accepted names, collection numbers, age ranges and present-day coordinates. I01 queries the API live on every run and refreshes this file; it reads the file only when the API cannot be reached.

## Contents

```
pbdb/  (3.2 MB)
├── README.md
└── pbdb_cache_Brachiopoda_440_520.csv
```

## Consumer notebooks

**I01**

## References

Paleobiology Database, [paleobiodb.org](https://paleobiodb.org). Public API [paleobiodb.org/data1.2/](https://paleobiodb.org/data1.2/).

## License

CC BY 4.0 (Paleobiology Database data).
