## What this pull request adds or changes

<!-- New notebook (T-number and name), fix, or dataset. -->

## Checklist for new or changed notebooks

- [ ] Follows the suite structure: three-section header (motivation, learning objectives, prerequisites and runtime), `# === USER CONFIGURATION ===` block, in-frame `{time} Ma` stamp on every map, closing *Extend this* section.
- [ ] Runs top to bottom in the `environment.yml` environment from a clean kernel; any new package is added to `environment.yml`.
- [ ] Executed outputs are preserved in the committed notebook.
- [ ] Data: anything beyond plate models is bundled in `data/` or declared as an external (Zenodo) dependency that raises a clear error pointing to the DOI when missing.
- [ ] Every method and dataset is cited, and each DOI has been checked to resolve to the cited work.
- [ ] Scientific provenance: contributed methodology or data is credited in the notebook header (`*Contributed by:*`), in `CONTRIBUTORS.md` and in the README Attribution section.
- [ ] Figures use pyGMT (no other plotting library for maps) and the plate model and reference frame are stated.
- [ ] `CHANGELOG.md` updated.
- [ ] Use of generative-AI tools in writing or code is disclosed in the pull request description.
