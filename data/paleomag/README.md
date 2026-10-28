        # paleomag — Paleomagnetic databases (GPMDB 2022 snapshot, Osler, Vaes 2023 APWP, tutorial datasets)

        **Provenance:** Multiple curators

        Paleomagnetic data used by cluster F reference-frame + paleomagnetism tutorials: (1) `gpmdb_2022.csv` — 2022 snapshot of the Global Paleomagnetic Database (Torsvik + Van der Voo curators); (2) `vaes2023_global_apwp.csv` — global APWP of Vaes et al. (2023) in the South African frame (33 poles, 1.4–320.2 Ma; used by F05 and F07); (3) `gilder2001_xishuigou_directions.csv` — specimen-level directions of the Oligo-Miocene Xishuigou section (Gilder et al. 2001, MagIC contribution 20098) for the inclination-shallowing tutorial F08, built by `build_gilder2001_csv.py`; (4) `osler_upper_sites_*` — Osler VGP compilation; (5) `torsvik2012_laurentia_apwp.csv` — rounded tutorial values, no longer used by any notebook (superseded by the Vaes 2023 APWP); (6) rotation files with GPMDB-frame anchors.

        ## Contents

        ```
        paleomag/  (4.0 MB)
  build_gilder2001_csv.py
  gilder2001_xishuigou_directions.csv (built by the script)
  gpmdb_2022.csv (4.0 MB)
  osler_upper_sites_Halls1974_SwansonHysell2014.csv
  test_poles_assorted.csv
  torsvik2012_laurentia_apwp.csv
  vaes2023_global_apwp.csv
        ```


        ## Consumer notebooks

        **F01**, **F02**, **F05**, **F06**, **F07**, **F08**, **J01**

        ## References

        Torsvik, T.H., Van der Voo, R., Preeden, U. et al. (2012). Phanerozoic polar wander, palaeogeography and dynamics. *Earth-Science Reviews* 114, 325-368.
        Vaes, B., van Hinsbergen, D.J.J., van de Lagemaat, S.H.A. et al. (2023). A global apparent polar wander path for the last 320 Ma calculated from site-level paleomagnetic data. *Earth-Science Reviews* 245, 104547. https://doi.org/10.1016/j.earscirev.2023.104547
        Gilder, S., Chen, Y. & Sen, S. (2001). Oligo-Miocene magnetostratigraphy and rock magnetism of the Xishuigou section, Subei (Gansu Province, western China). *Journal of Geophysical Research* 106, 30505-30521. https://doi.org/10.1029/2001JB000325

        ## License

        Public paleomag data. GPMDB: Torsvik curators.
