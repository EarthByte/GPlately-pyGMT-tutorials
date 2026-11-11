# pmm_cache — local copies of the plate models

**Provenance:** EarthByte plate-model repository, as downloaded by GPlately's Plate Model Manager

Local copies of five plate models, in the layout the Plate Model Manager (part of GPlately; Mather et al., 2024) writes. Notebooks that pass `data_dir="data/pmm_cache"` read the models from here instead of downloading them, so they run offline. Each model folder has a `readme.txt` naming the model's time range and its Zenodo record.

## Contents

```
pmm_cache/  (530 MB)
├── README.md
├── cao2024/         0–1800 Ma   https://doi.org/10.5281/zenodo.11536686
├── merdith2021/     0–1000 Ma   https://doi.org/10.5281/zenodo.10346399
├── muller2016/      0–230 Ma    https://doi.org/10.5281/zenodo.10565444
├── muller2022/      0–1000 Ma   https://doi.org/10.5281/zenodo.10297173
└── zahirovic2022/   0–410 Ma    https://doi.org/10.5281/zenodo.4729045  (with seafloor age grids, mantle frame)
```

Each model folder holds the layers the notebooks use: `Rotations/`, `Topologies/`, `StaticPolygons/` and, where the model has them, `Coastlines/`, `ContinentalPolygons/` and `COBs/`.

## Consumer notebooks

**B09**, **D05**, **F09**, **F10**, **G10**, **H01**, **H02**, **H03**, **I05**, **I06**, **J04**, **J08**, **J09**, **J10**, **J11**, **K07**, **K08**

## References

Cao, X., Collins, A.S., Pisarevsky, S., Flament, N., Li, S., Hasterok, D. & Müller, R.D. (2024). Earth's tectonic and plate boundary evolution over 1.8 billion years. *Geoscience Frontiers* 15, 101922. https://doi.org/10.1016/j.gsf.2024.101922

Merdith, A.S., Williams, S.E., Collins, A.S., Tetley, M.G., Mulder, J.A., Blades, M.L., Young, A., Armistead, S.E., Cannon, J., Zahirovic, S. & Müller, R.D. (2021). Extending full-plate tectonic models into deep time: Linking the Neoproterozoic and the Phanerozoic. *Earth-Science Reviews* 214, 103477. https://doi.org/10.1016/j.earscirev.2020.103477

Müller, R.D., Seton, M., Zahirovic, S., Williams, S.E., Matthews, K.J., Wright, N.M., et al. (2016). Ocean basin evolution and global-scale plate reorganization events since Pangea breakup. *Annual Review of Earth and Planetary Sciences* 44, 107-138. https://doi.org/10.1146/annurev-earth-060115-012211

Müller, R.D., Flament, N., Cannon, J., Tetley, M.G., Williams, S.E., Cao, X., Bodur, Ö.F., Zahirovic, S. & Merdith, A. (2022). A tectonic-rules-based mantle reference frame since 1 billion years ago. *Solid Earth* 13(7), 1127–1159. https://doi.org/10.5194/se-13-1127-2022

Zahirovic, S., Eleish, A., Doss, S., Pall, J., Cannon, J., Pistone, M., Tetley, M.G., Young, A. & Fox, P. (2022). Subduction and carbonate platform interactions. *Geoscience Data Journal* 9(2), 371-383. https://doi.org/10.1002/gdj3.146

Mather, B.R., Müller, R.D., Zahirovic, S., Cannon, J., Chin, M., Ilano, L., Wright, N.M., Alfonso, C., Williams, S., Tetley, M. & Merdith, A. (2024). Deep time spatio-temporal data analysis using pyGPlates with PlateTectonicTools and GPlately. *Geoscience Data Journal* 11(1), 3-10. https://doi.org/10.1002/gdj3.185
