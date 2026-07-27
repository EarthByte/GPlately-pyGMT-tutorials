"""Build Figure 1 — the tutorial suite organised by thematic cluster.

Layout 2026-07-27: **79 notebooks across 11 clusters (A-K), fully contiguous**,
reflecting the 2026-07-26 renumbering sweep (T01-T78 contiguous, no tail
extensions) plus the T79 tail addition (Farahbakhsh kinematic-feature-
extraction notebook, landed 2026-07-27 in cluster B without a further
resweep, per the suite's tail-extension convention).

This replaces the previous (2026-07-26-dated but never actually updated)
version of this script, whose CLUSTERS data still reflected the *pre-sweep*
A-L-skipping-K tail-extension layout (T73 in A, T78 in E, T74 in H, a
separate L cluster for T75-T77) even though the underlying notebook files
had already been renamed to the contiguous A-K scheme. The docstring here
and the tile data below are the corrected, disk-verified version.

Run:
    cd paper/figures
    python build_fig1_suite_ladder.py

Output: fig1_suite_ladder.png + fig1_suite_ladder.pdf (this folder).

Cluster structure (2026-07-26 contiguous sweep, disk-verified 2026-07-27):
    A : T01-T07        Getting started / core workflows
    B : T08-T14 + T79  Plate kinematics + tectonics
                              (T14 = rift obliquity; T79 = kinematic feature
                               extraction at subduction zones, tail addition
                               contributed by Ehsan Farahbakhsh)
    C : T15-T18        Plate-model debugging (Sculley + Cannon)
    D : T19-T23        Zircons + tectonic-setting predictors
                              (T23 = Hf-Nd terrane mapping)
    E : T24-T31        Mantle dynamics + dynamic topography
                              (T24-T25 REVEAL pair; T30 = subducted-slab flux;
                               T31 = mantle-to-plate frame conversion)
    F : T32-T42        Paleomagnetism (T41 = TPW decomposition)
    G : T43-T51        Paleo-geography + paleo-topography + thermochronology
                              (T43-T49 = ThermoPlates suite;
                               T50 = North American thermochron;
                               T51 = ophiolite paleo-map)
    H : T52-T54        Sedimentary basins (Heine ICONS Atlas trio)
    I : T55-T60        Paleobiogeography
    J : T61-T69        Paleoclimate (T61-T69 = Leonard 2025 quartet + others)
    K : T70-T78        Mineral exploration
                              (T70-T75 = porphyry/Cu suite;
                               T76 = carbonate-platform degassing;
                               T77 = Mn 1.8 Ga; T78 = craton boundaries)
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

HERE = Path(__file__).parent

NL = "\n"

# ----- Cluster definition: (letter, header_name, colour, tiles) -----
CLUSTERS = [
    ("A", "Getting started / core workflows", "#7FB3D5", [
        ("T01", "Hello," + NL + "deep time"),
        ("T02", "GPlates" + NL + "Web Service"),
        ("T03", "Projection" + NL + "cookbook"),
        ("T04", "Plate model" + NL + "comparison"),
        ("T05", "Rotation" + NL + "model" + NL + "comparison"),
        ("T06", "Plate motion" + NL + "animation"),
        ("T07", "Interactive" + NL + "paleogeog." + NL + "reconstr."),
    ]),
    ("B", "Plate kinematics + tectonics", "#7DCEA0", [
        ("T08", "Plate" + NL + "tectonic" + NL + "diagnostics"),
        ("T09", "Age of" + NL + "subd. crust"),
        ("T10", "Paleo-" + NL + "bathymetry" + NL + "profile"),
        ("T11", "Paleo-" + NL + "strain rates"),
        ("T12", "Paleo-LAB" + NL + "retro-" + NL + "deformation"),
        ("T13", "Paleo-" + NL + "SHmax" + NL + "subduction"),
        ("T14", "Rift" + NL + "obliquity"),
        ("T79", "Kinematic" + NL + "feature" + NL + "extraction"),
    ]),
    ("C", "Plate-model debugging", "#34495E", [
        ("T15", "Div. +" + NL + "convergence" + NL + "anomalies"),
        ("T16", "MOR" + NL + "velocity" + NL + "magnitude"),
        ("T17", "Topology" + NL + "construction" + NL + "anomalies"),
        ("T18", "SZ feature" + NL + "extract-" + NL + "ability"),
    ]),
    ("D", "Zircons + tectonic-" + NL + "setting predictors", "#F4A261", [
        ("T19", "Detrital" + NL + "zircons"),
        ("T20", "Igneous" + NL + "zircons"),
        ("T21", "Meta-" + NL + "morphic" + NL + "zircons"),
        ("T22", "Dist. to" + NL + "subduction"),
        ("T23", "Hf-Nd" + NL + "terrane" + NL + "mapping"),
    ]),
    ("E", "Mantle dynamics +" + NL + "dynamic topography", "#A569BD", [
        ("T24", "REVEAL" + NL + "tomography" + NL + "slices"),
        ("T25", "REVEAL" + NL + "plume" + NL + "cross-sect."),
        ("T26", "Mantle" + NL + "transect" + NL + "deep time"),
        ("T27", "DT cluster" + NL + "histories"),
        ("T28", "DT vs" + NL + "sediment"),
        ("T29", "DT change" + NL + "deep time"),
        ("T30", "Subducted-" + NL + "slab flux"),
        ("T31", "Mantle→" + NL + "plate frame" + NL + "conversion"),
    ]),
    ("F", "Paleomagnetism", "#E74C3C", [
        ("T32", "Paleomag." + NL + "reference" + NL + "frame"),
        ("T33", "Frame" + NL + "comparison"),
        ("T34", "Plate/mantle" + NL + "frame" + NL + "uncertainty"),
        ("T35", "Continent" + NL + "reconstr." + NL + "(gplately)"),
        ("T36", "APWP vs" + NL + "gplately" + NL + "site"),
        ("T37", "Osler" + NL + "1.1 Ga"),
        ("T38", "Phaner." + NL + "APWP on" + NL + "Laurentia"),
        ("T39", "SVEI" + NL + "shallowing"),
        ("T40", "Rotated" + NL + "poles"),
        ("T41", "TPW" + NL + "decomp."),
        ("T42", "Paleolat." + NL + "reverse" + NL + "reconstr."),
    ]),
    ("G", "Paleo-geography +" + NL + "paleo-topography", "#16A085", [
        ("T43", "Geochem-" + NL + "corrected" + NL + "paleo-elev"),
        ("T44", "Macrostrat" + NL + "Great" + NL + "Unconf."),
        ("T45", "Highland" + NL + "footprints"),
        ("T46", "C. Asia" + NL + "thermo-" + NL + "chron."),
        ("T47", "Cooling ×" + NL + "Earth-" + NL + "system"),
        ("T48", "Cooling ×" + NL + "kinematics" + NL + "× faults"),
        ("T49", "Cooling-" + NL + "rate" + NL + "correl."),
        ("T50", "N. America" + NL + "thermo-" + NL + "chron."),
        ("T51", "Ophiolite" + NL + "paleo-map"),
    ]),
    ("H", "Sedimentary basins", "#8E44AD", [
        ("T52", "Global" + NL + "basins" + NL + "ICONS"),
        ("T53", "Crustal" + NL + "stretching" + NL + "factor β"),
        ("T54", "Individual" + NL + "rift" + NL + "analysis"),
    ]),
    ("I", "Paleobiogeography", "#F39C12", [
        ("T55", "PBDB ×" + NL + "Macrostrat" + NL + "paleo-litho"),
        ("T56", "Reef" + NL + "builders" + NL + "paleolat"),
        ("T57", "Kimmer." + NL + "dinos"),
        ("T58", "Cenozoic" + NL + "forams"),
        ("T59", "PBDB" + NL + "paleobio-" + NL + "geography"),
        ("T60", "H3 bio-" + NL + "regional-" + NL + "isation"),
    ]),
    ("J", "Paleoclimate", "#2980B9", [
        ("T61", "Boucot" + NL + "climate" + NL + "lithos"),
        ("T62", "Deep-time" + NL + "paleoclim." + NL + "snapshots"),
        ("T63", "cGENIE" + NL + "SST vs" + NL + "proxies"),
        ("T64", "PLASIM" + NL + "CO2" + NL + "sensitivity"),
        ("T65", "pySCION" + NL + "Phanerozoic"),
        ("T66", "Ref-frame" + NL + "paleoclim."),
        ("T67", "Ocean" + NL + "gateways" + NL + "vs frame"),
        ("T68", "Multi-study" + NL + "GMST"),
        ("T69", "Proxy" + NL + "validation" + NL + "of frames"),
    ]),
    ("K", "Mineral exploration", "#7D6608", [
        ("T70", "SW-Pacific" + NL + "porphyries"),
        ("T71", "Global" + NL + "porphyry" + NL + "envelope"),
        ("T72", "Seafloor" + NL + "anomalies"),
        ("T73", "Sediment-" + NL + "hosted Cu"),
        ("T74", "Porphyry-Cu" + NL + "deep-time" + NL + "trajectories"),
        ("T75", "Continent" + NL + "prospectivity" + NL + "maps"),
        ("T76", "Carbonate" + NL + "platform" + NL + "degassing"),
        ("T77", "Manganese" + NL + "1.8 Ga" + NL + "paleogeo"),
        ("T78", "Craton" + NL + "boundary" + NL + "framework"),
    ]),
]

# ----- Tile + cluster geometry — boxes sized so 3-line labels fit -----
BOX_W, BOX_H       = 1.05, 1.20
TILE_GAP           = 0.08
CLUSTER_PAD_INNER  = 0.30
CLUSTER_PAD_X      = 0.70

FS_TN     = 10.5
FS_LABEL  = 7.2
FS_HEADER = 11.0

# 6 rows for 11 clusters — pair small ones with big ones.
# Cluster sizes: A(7), B(8, incl. T79 tail), C(4), D(5), E(8), F(11),
# G(9), H(3), I(6), J(9), K(9)
ROWS = [
    ["A"],               # A(7) alone
    ["B", "C", "D"],     # B(8) + C(4) + D(5) = 17 tiles
    ["E", "F"],          # E(8) + F(11) = 19 — widest row
    ["G", "H"],          # G(9) + H(3) = 12 — H pairs with G nicely
    ["I", "J"],          # I(6) + J(9) = 15
    ["K"],               # K(9) alone
]


def cluster_width(c_tiles):
    return (len(c_tiles) * BOX_W
            + (len(c_tiles) - 1) * TILE_GAP
            + 2 * CLUSTER_PAD_INNER)


def build():
    fig, ax = plt.subplots(figsize=(19.0, 16.5), dpi=300)
    fig.patch.set_facecolor("white")

    by_letter = {c[0]: c for c in CLUSTERS}

    y_top              = 18.0
    row_h              = 2.85
    header_above_tile  = 0.75
    tile_band_pad      = 0.55

    def draw_cluster(letter, name, colour, tiles, x_start, y_centre):
        w = cluster_width(tiles)
        rect = mpatches.FancyBboxPatch(
            (x_start, y_centre - BOX_H / 2 - tile_band_pad),
            w,
            BOX_H + 2 * tile_band_pad + header_above_tile,
            boxstyle="round,pad=0.04,rounding_size=0.10",
            linewidth=0.6, edgecolor=colour, facecolor=colour, alpha=0.10,
            zorder=1,
        )
        ax.add_patch(rect)
        ax.text(x_start + 0.12,
                y_centre + header_above_tile + tile_band_pad - 0.05,
                f"{letter}  {name}",
                ha="left", va="top",
                fontsize=FS_HEADER,
                fontweight="bold",
                color=colour, zorder=3,
                linespacing=1.05)
        x = x_start + CLUSTER_PAD_INNER
        for tn, label in tiles:
            tile = mpatches.FancyBboxPatch(
                (x, y_centre - BOX_H / 2),
                BOX_W, BOX_H,
                boxstyle="round,pad=0.02,rounding_size=0.07",
                linewidth=0.6, edgecolor="#222222",
                facecolor=colour, zorder=2,
            )
            ax.add_patch(tile)
            text_colour = "white" if colour in ("#5B2C6F", "#A569BD",
                                                 "#16A085", "#2980B9",
                                                 "#7D6608", "#A04000",
                                                 "#5D6D7E", "#34495E",
                                                 "#8E44AD") else "#1A1A1A"
            ax.text(x + BOX_W / 2, y_centre + 0.34, tn,
                    ha="center", va="center",
                    fontsize=FS_TN, fontweight="bold",
                    color=text_colour, zorder=3)
            ax.text(x + BOX_W / 2, y_centre - 0.16, label,
                    ha="center", va="center",
                    fontsize=FS_LABEL, color=text_colour,
                    linespacing=0.95, zorder=3)
            x += BOX_W + TILE_GAP
        return w

    for r, row in enumerate(ROWS):
        y_centre = y_top - (r + 1) * row_h
        widths   = [cluster_width(by_letter[L][3]) for L in row]
        total_w  = sum(widths) + (len(row) - 1) * CLUSTER_PAD_X
        x        = -total_w / 2
        for L, w in zip(row, widths):
            letter, name, colour, tiles = by_letter[L]
            draw_cluster(letter, name, colour, tiles, x, y_centre)
            x += w + CLUSTER_PAD_X

    # Widen x-range slightly to accommodate the widest rows
    ax.set_xlim(-12.0, 12.0)
    ax.set_ylim(-0.5, 18.5)
    ax.set_aspect("equal")
    ax.axis("off")

    out_png = HERE / "fig1_suite_ladder.png"
    out_pdf = HERE / "fig1_suite_ladder.pdf"
    fig.savefig(out_png, dpi=300, bbox_inches="tight", facecolor="white")
    fig.savefig(out_pdf, bbox_inches="tight", facecolor="white")
    print(f"wrote {out_png}")
    print(f"wrote {out_pdf}")

    # Sanity check — did we cover all 79 notebooks (T01-T78 + T79 tail)?
    all_tiles = [tn for _, _, _, tiles in CLUSTERS for tn, _ in tiles]
    assert len(all_tiles) == len(set(all_tiles)), "duplicate T-numbers"
    numbers = sorted(int(t[1:]) for t in all_tiles)
    expected = list(range(1, 79)) + [79]
    assert numbers == expected, (
        f"expected T01-T78 contiguous + T79 tail, got missing/extra: "
        f"{set(expected) ^ set(numbers)}")
    print(f"  ✓ all 79 notebooks covered (T01-T78 contiguous + T79 tail extension)")


if __name__ == "__main__":
    build()
