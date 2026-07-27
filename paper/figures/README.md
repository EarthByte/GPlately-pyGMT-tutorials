# paper/figures/

Publication figures for the *Extending pyGMT into Deep Time via GPlately* paper. This folder lives in the tutorial repo (not in a separate paper-scratch folder) so figures + build scripts + output artefacts are version-controlled together and survive between sessions.

## Contents

- `build_fig1_suite_ladder.py` — Fig 1 build script. Generates a cluster ladder view of the whole tutorial suite as an SVG-style matplotlib figure. Regenerate whenever notebooks are added / moved / renamed. Runs in ~2 s.
- `fig1_suite_ladder.png`, `fig1_suite_ladder.pdf` — the current committed output artefacts. Overwritten on re-run.

## Regenerating Fig 1

```bash
cd paper/figures
python build_fig1_suite_ladder.py
```

The script has a built-in sanity check that fails loudly if T-numbers go non-contiguous or a notebook is missing from the ladder — so it doubles as a rendering test.

## Layout convention

The cluster ladder is organised by **thematic cluster (A-K)**, not by T-number order, fully contiguous as of the 2026-07-26 renumber sweep. Tail extensions (notebooks added out of cluster order without a further renumber sweep, e.g. T79 in cluster B) sit at the RIGHT end of their target cluster's tile row.

If a new notebook is added, edit the `CLUSTERS` list in `build_fig1_suite_ladder.py`, add the tile to the target cluster, re-run, commit.

## Mirror to the paper draft folder

A parallel copy lives at `~/Documents/Papers/in_prep/GPlately-pyGMT/figures/` (Dietmar's local paper drafting area). When the tutorial-repo copy is regenerated, mirror the PNG + PDF to that folder for paper writing. The tutorial-repo copy is the source of truth.

## Other figures

Figs 2-8 (individual-notebook feature figures) currently live in Dietmar's local paper folder; a future sweep will bring their build scripts into this folder too.
