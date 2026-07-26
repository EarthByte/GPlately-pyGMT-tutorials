"""Build Figure 1 — the tutorial suite organised by thematic cluster.

Layout 2026-07-26: **78 notebooks across 11 clusters (A–L, skipping K)**
after the T73-T78 tail extensions landed in clusters A/E/H/L without
renumbering. Cluster L (Sedimentary basins) is new.

Run:
    cd paper/figures
    python build_fig1_suite_ladder.py

Output: fig1_suite_ladder.png + fig1_suite_ladder.pdf (this folder).

Cluster structure (2026-07-26 tail extensions):
    A : T01-T08 + T73  Getting started / core workflows
                              (T73 = paleolatitude via reverse reconstruction)
    B : T09-T14        Plate kinematics + tectonics (T14 = rift obliquity)
    C : T15-T18        Plate-model debugging (Sculley + Cannon)
    D : T19-T23        Zircons + tectonic-setting predictors
                              (T23 = Hf-Nd terrane mapping)
    E : T24-T30 + T78  Mantle dynamics + dynamic topography
                              (T24-T25 REVEAL pair; T30 = subducted-slab flux;
                               T78 = mantle→plate frame conversion walkthrough)
    F : T31-T40        Paleomagnetism (T40 = TPW decomposition)
    G : T41-T49        Paleo-geography + paleo-topography + thermochronology
                              (T43-T47 = ThermoPlates suite;
                               T48 = North American thermochron;
                               T49 = ophiolite paleo-map)
    H : T50-T54 + T74  Paleobiogeography (T74 = H3 bioregionalisation)
    I : T55-T63        Paleoclimate (T60-T63 = Leonard 2025 quartet)
    J : T64-T72        Mineral exploration
                              (T64-T69 = porphyry/Cu suite;
                               T70 = carbonate-platform degassing;
                               T71 = Mn 1.8 Ga; T72 = craton boundaries)
    L : T75-T77        Sedimentary basins (Heine ICONS Atlas trio)
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
        ("T06", "Animations"),
        ("T07", "Interactive" + NL + "paleogeog." + NL + "reconstr."),
        ("T08", "Deep-time" + NL + "diagnostics"),
        ("T73", "Paleolat." + NL + "reverse" + NL + "reconstr."),
    ]),
    ("B", "Plate kinematics + tectonics", "#7DCEA0", [
        ("T09", "Age of" + NL + "subd. crust"),
        ("T10", "Paleo-" + NL + "bathymetry" + NL + "profile"),
        ("T11", "Paleo-" + NL + "strain rates"),
        ("T12", "Paleo-LAB" + NL + "retro-" + NL + "deformation"),
        ("T13", "Paleo-" + NL + "sHmax" + NL + "Andes"),
        ("T14", "Rift" + NL + "obliquity"),
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
        ("T78", "Mantle→" + NL + "plate frame" + NL + "conversion"),
    ]),
    ("F", "Paleomagnetism", "#E74C3C", [
        ("T31", "GPMDB" + NL + "reference" + NL + "frame"),
        ("T32", "Frame" + NL + "comparison"),
        ("T33", "Plate/mantle" + NL + "frame" + NL + "uncertainty"),
        ("T34", "Continent" + NL + "reconstr." + NL + "(gplately)"),
        ("T35", "APWP vs" + NL + "gplately" + NL + "site"),
        ("T36", "Osler" + NL + "1.1 Ga"),
        ("T37", "Phaner." + NL + "APWP on" + NL + "Laurentia"),
        ("T38", "SVEI" + NL + "shallowing"),
        ("T39", "Rotated" + NL + "poles"),
        ("T40", "TPW" + NL + "decomp."),
    ]),
    ("G", "Paleo-geography +" + NL + "paleo-topography", "#16A085", [
        ("T41", "Geochem-" + NL + "corrected" + NL + "paleo-elev"),
        ("T42", "Macrostrat" + NL + "Great" + NL + "Unconf."),
        ("T43", "Highland" + NL + "footprints"),
        ("T44", "C. Asia" + NL + "thermo-" + NL + "chron."),
        ("T45", "Cooling ×" + NL + "Earth-" + NL + "system"),
        ("T46", "Cooling ×" + NL + "kinematics" + NL + "× faults"),
        ("T47", "Cooling-" + NL + "rate" + NL + "correl."),
        ("T48", "N. America" + NL + "thermo-" + NL + "chron. + DT"),
        ("T49", "Ophiolite" + NL + "paleo-map"),
    ]),
    ("H", "Paleobiogeography", "#F39C12", [
        ("T50", "PBDB ×" + NL + "Macrostrat" + NL + "paleo-litho"),
        ("T51", "Reef" + NL + "builders" + NL + "paleolat"),
        ("T52", "Kimmer." + NL + "dinos +" + NL + "paleo-elev"),
        ("T53", "Cenozoic" + NL + "forams"),
        ("T54", "PBDB" + NL + "paleobio-" + NL + "geography"),
        ("T74", "H3 bio-" + NL + "regional-" + NL + "isation"),
    ]),
    ("I", "Paleoclimate", "#2980B9", [
        ("T55", "Boucot" + NL + "climate" + NL + "lithos"),
        ("T56", "Deep-time" + NL + "SAT"),
        ("T57", "cGENIE" + NL + "SST vs" + NL + "proxies"),
        ("T58", "PLASIM" + NL + "CO2" + NL + "sensitivity"),
        ("T59", "pySCION" + NL + "Phanerozoic"),
        ("T60", "Ref-frame" + NL + "paleoclim." + NL + "uncertainty"),
        ("T61", "Ocean" + NL + "gateways" + NL + "vs frame"),
        ("T62", "Multi-study" + NL + "GMST"),
        ("T63", "Proxy" + NL + "validation" + NL + "of frames"),
    ]),
    ("J", "Mineral exploration", "#7D6608", [
        ("T64", "SW-Pacific" + NL + "porphyries"),
        ("T65", "Global" + NL + "porphyry" + NL + "envelope"),
        ("T66", "Seafloor" + NL + "anomalies"),
        ("T67", "Sediment-" + NL + "hosted Cu"),
        ("T68", "Porphyry-Cu" + NL + "deep-time" + NL + "trajectories"),
        ("T69", "Continent" + NL + "prospectivity" + NL + "maps"),
        ("T70", "Carbonate" + NL + "platform" + NL + "degassing"),
        ("T71", "Manganese" + NL + "1.8 Ga" + NL + "paleogeo"),
        ("T72", "Craton" + NL + "boundary" + NL + "framework"),
    ]),
    ("L", "Sedimentary basins", "#8E44AD", [
        ("T75", "Global" + NL + "basins" + NL + "ICONS"),
        ("T76", "Crustal" + NL + "stretching" + NL + "factor β"),
        ("T77", "Individual" + NL + "rift" + NL + "analysis"),
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
# Cluster sizes now: A(9), B(6), C(4), D(5), E(8), F(10), G(9), H(6), I(9), J(9), L(3)
ROWS = [
    ["A"],               # A(9) alone
    ["B", "C", "D"],     # B(6) + C(4) + D(5) = 15 tiles
    ["E", "F"],          # E(8) + F(10) = 18 — widest row
    ["G", "L"],          # G(9) + L(3) = 12 — L pairs with G nicely
    ["H", "I"],          # H(6) + I(9) = 15
    ["J"],               # J(9) alone
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

    # Widen x-range slightly to accommodate the widened cluster E and cluster A
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

    # Sanity check — did we cover all 78 notebooks?
    all_tiles = [tn for _, _, _, tiles in CLUSTERS for tn, _ in tiles]
    assert len(all_tiles) == len(set(all_tiles)), "duplicate T-numbers"
    numbers = sorted(int(t[1:]) for t in all_tiles)
    assert numbers == list(range(1, 79)), (
        f"expected T01-T78 contiguous, got missing/extra: "
        f"{set(range(1, 79)) ^ set(numbers)}")
    print(f"  ✓ all 78 notebooks covered (T01-T78 contiguous)")


if __name__ == "__main__":
    build()
