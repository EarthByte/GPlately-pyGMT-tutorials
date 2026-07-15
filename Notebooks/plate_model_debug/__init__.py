"""plate_model_debug — helpers for diagnosing plate-model artefacts.

Bundled with the GPlately x pyGMT tutorial suite for notebooks T59-T62.

The four notebooks that consume this package:

- T59  Diagnosing-negative-divergence-and-convergence (MORs, SZs, transforms)
- T60  Diagnosing velocity magnitude at MORs (via PlateTectonicTools)
- T61  Topology construction anomalies (gaps/overlaps, non-unique sections,
       missing polarity)
- T62  Feature extractability at subduction zones (buffer zones, convergence
       rates)

Upstream repo: https://github.com/EarthByte/plate-model-debug (made public
via this suite; primary authors Ben Sculley + John Cannon, EarthByte).
"""

from .diagnose_convergence import diagnose_topology_convergence
from .detect_anomalies import (
    detect_gaps_and_overlaps_at_time,
    detect_non_unique_sections_at_time,
    detect_missing_polarity_at_time,
)

__all__ = [
    "diagnose_topology_convergence",
    "detect_gaps_and_overlaps_at_time",
    "detect_non_unique_sections_at_time",
    "detect_missing_polarity_at_time",
]
