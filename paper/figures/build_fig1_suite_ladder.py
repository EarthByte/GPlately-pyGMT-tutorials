"""Build Figure 1 — the tutorial suite organised by thematic cluster.

Tiles are labelled with the notebook ID: the cluster letter followed by the
index of the notebook within its cluster (for example F03). 80 notebooks in
11 clusters (A-K).

Run:
    cd paper/figures
    python build_fig1_suite_ladder.py

Output: fig1_suite_ladder.png + fig1_suite_ladder.pdf (this folder).

Cluster structure:
    A : A01-A07        Getting started / core workflows
    B : B01-B09        Plate kinematics + tectonics
    C : C01-C04        Plate-model debugging
    D : D01-D05        Zircons + tectonic-setting predictors
    E : E01-E07        Mantle dynamics + dynamic topography
    F : F01-F10        Paleomagnetism
    G : G01-G10        Paleo-geography + paleo-topography + thermochronology
    H : H01-H03        Sedimentary basins
    I : I01-I06        Paleobiogeography
    J : J01-J11        Paleoclimate
    K : K01-K08        Mineral exploration
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

HERE = Path(__file__).parent

NL = "\n"

# ----- Cluster definition: (letter, header_name, colour, tiles) -----
CLUSTERS = [
    ("A", "Getting started / core workflows", "#7FB3D5", [
        ("A01", "Hello," + NL + "deep time"),
        ("A02", "GPlates" + NL + "Web Service"),
        ("A03", "Projection" + NL + "cookbook"),
        ("A04", "Plate model" + NL + "comparison"),
        ("A05", "Rotation" + NL + "model" + NL + "comparison"),
        ("A06", "Plate motion" + NL + "animation"),
        ("A07", "Interactive" + NL + "paleogeog." + NL + "reconstr."),
    ]),
    ("B", "Plate kinematics + tectonics", "#7DCEA0", [
        ("B01", "Plate" + NL + "tectonic" + NL + "diagnostics"),
        ("B02", "Age of" + NL + "subd. crust"),
        ("B03", "Paleo-" + NL + "bathymetry" + NL + "profile"),
        ("B04", "Paleo-" + NL + "strain rates"),
        ("B05", "Paleo-LAB" + NL + "retro-" + NL + "deformation"),
        ("B06", "Paleo-" + NL + "SHmax" + NL + "subduction"),
        ("B07", "Rift" + NL + "obliquity"),
        ("B08", "Kinematic" + NL + "feature" + NL + "extraction"),
        ("B09", "Subducted-" + NL + "slab flux"),
    ]),
    ("C", "Plate-model debugging", "#34495E", [
        ("C01", "Div. +" + NL + "convergence" + NL + "anomalies"),
        ("C02", "MOR" + NL + "velocity" + NL + "magnitude"),
        ("C03", "Topology" + NL + "construction" + NL + "anomalies"),
        ("C04", "SZ feature" + NL + "extract-" + NL + "ability"),
    ]),
    ("D", "Zircons + tectonic-" + NL + "setting predictors", "#F4A261", [
        ("D01", "Detrital" + NL + "zircons"),
        ("D02", "Igneous" + NL + "zircons"),
        ("D03", "Meta-" + NL + "morphic" + NL + "zircons"),
        ("D04", "Dist. to" + NL + "subduction"),
        ("D05", "Hf-Nd" + NL + "terrane" + NL + "mapping"),
    ]),
    ("E", "Mantle dynamics +" + NL + "dynamic topography", "#A569BD", [
        ("E01", "REVEAL" + NL + "tomography" + NL + "slices"),
        ("E02", "REVEAL" + NL + "plume" + NL + "cross-sect."),
        ("E03", "Mantle" + NL + "transect" + NL + "deep time"),
        ("E04", "DT cluster" + NL + "histories"),
        ("E05", "DT vs" + NL + "sediment"),
        ("E06", "DT change" + NL + "deep time"),
        ("E07", "Mantle→" + NL + "plate frame" + NL + "conversion"),
    ]),
    ("F", "Paleomagnetism", "#E74C3C", [
        ("F01", "Paleomag." + NL + "reference" + NL + "frame"),
        ("F02", "Frame" + NL + "comparison"),
        ("F03", "Plate/mantle" + NL + "frame" + NL + "uncertainty"),
        ("F04", "Continent" + NL + "reconstr." + NL + "(gplately)"),
        ("F05", "APWP vs" + NL + "gplately" + NL + "site"),
        ("F06", "Osler" + NL + "1.1 Ga"),
        ("F07", "Phaner." + NL + "APWP on" + NL + "Laurentia"),
        ("F08", "SVEI" + NL + "shallowing"),
        ("F09", "TPW" + NL + "decomp."),
        ("F10", "Paleolat." + NL + "reverse" + NL + "reconstr."),
    ]),
    ("G", "Paleo-geography +" + NL + "paleo-topography", "#16A085", [
        ("G01", "Geochem-" + NL + "corrected" + NL + "paleo-elev"),
        ("G02", "Macrostrat" + NL + "lithology" + NL + "styling"),
        ("G03", "Macrostrat" + NL + "Great" + NL + "Unconf."),
        ("G04", "Highland" + NL + "footprints"),
        ("G05", "C. Asia" + NL + "thermo-" + NL + "chron."),
        ("G06", "Cooling ×" + NL + "Earth-" + NL + "system"),
        ("G07", "Cooling ×" + NL + "kinematics" + NL + "× faults"),
        ("G08", "Cooling-" + NL + "rate" + NL + "correl."),
        ("G09", "N. America" + NL + "thermo-" + NL + "chron."),
        ("G10", "Ophiolite" + NL + "paleo-map"),
    ]),
    ("H", "Sedimentary basins", "#8E44AD", [
        ("H01", "Global" + NL + "basins" + NL + "inventory"),
        ("H02", "Crustal" + NL + "stretching" + NL + "factor β"),
        ("H03", "Individual" + NL + "rift" + NL + "analysis"),
    ]),
    ("I", "Paleobiogeography", "#F39C12", [
        ("I01", "PBDB ×" + NL + "Macrostrat" + NL + "paleo-litho"),
        ("I02", "Reef" + NL + "builders" + NL + "paleolat"),
        ("I03", "Kimmer." + NL + "dinos"),
        ("I04", "Cenozoic" + NL + "forams"),
        ("I05", "PBDB" + NL + "paleobio-" + NL + "geography"),
        ("I06", "H3 bio-" + NL + "regional-" + NL + "isation"),
    ]),
    ("J", "Paleoclimate", "#2980B9", [
        ("J01", "Boucot" + NL + "climate" + NL + "lithos"),
        ("J02", "Plant-fossil" + NL + "paleoclim." + NL + "(Xu/Mills)"),
        ("J03", "Deep-time" + NL + "paleoclim." + NL + "snapshots"),
        ("J04", "cGENIE" + NL + "SST vs" + NL + "proxies"),
        ("J05", "PLASIM" + NL + "CO2" + NL + "sensitivity"),
        ("J06", "pySCION" + NL + "Phanerozoic"),
        ("J07", "Ref-frame" + NL + "paleoclim."),
        ("J08", "Devonian" + NL + "paleogeog." + NL + "+ climate"),
        ("J09", "PhanSST" + NL + "SST" + NL + "proxies"),
        ("J10", "Cenozoic" + NL + "ocean" + NL + "gateways"),
        ("J11", "Carbonate" + NL + "platform" + NL + "degassing"),
    ]),
    ("K", "Mineral exploration", "#7D6608", [
        ("K01", "SW-Pacific" + NL + "porphyries"),
        ("K02", "Global" + NL + "porphyry" + NL + "envelope"),
        ("K03", "Seafloor" + NL + "anomalies"),
        ("K04", "Sediment-" + NL + "hosted Cu"),
        ("K05", "Porphyry-Cu" + NL + "deep-time" + NL + "trajectories"),
        ("K06", "Continent" + NL + "prospectivity" + NL + "maps"),
        ("K07", "Manganese" + NL + "1.8 Ga" + NL + "paleogeo"),
        ("K08", "Craton" + NL + "boundary" + NL + "framework"),
    ]),
]

# ----- Tile + cluster geometry — boxes sized so 3-line labels fit -----
BOX_W, BOX_H       = 1.40, 1.60
TILE_GAP           = 0.10
CLUSTER_PAD_INNER  = 0.35
CLUSTER_PAD_X      = 0.80

FS_TN     = 14.0
FS_LABEL  = 9.8
FS_HEADER = 15.0

# 9 rows for 11 clusters — less material per row so boxes/text can be bigger.
# Cluster sizes: A(7), B(9), C(4), D(5), E(7), F(10), G(10), H(3), I(6), J(11), K(8)
ROWS = [
    ["A"],               # A(7) alone
    ["B"],               # B(9) alone
    ["C", "D"],          # C(4) + D(5) = 9 tiles
    ["E"],               # E(7) alone
    ["F"],               # F(11) alone
    ["G"],               # G(9) alone
    ["H", "I"],          # H(3) + I(6) = 9 tiles
    ["J"],               # J(11) alone
    ["K"],               # K(8) alone
]


def cluster_width(c_tiles):
    return (len(c_tiles) * BOX_W
            + (len(c_tiles) - 1) * TILE_GAP
            + 2 * CLUSTER_PAD_INNER)


def build():
    fig, ax = plt.subplots(figsize=(18.0, 30.5), dpi=300)
    fig.patch.set_facecolor("white")

    by_letter = {c[0]: c for c in CLUSTERS}

    y_top              = 34.0
    row_h              = 3.75
    header_above_tile  = 1.00
    tile_band_pad      = 0.75

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

    # Widen x/y-range generously; bbox_inches="tight" crops the final PNG/PDF
    # to actual content, so extra margin here is harmless.
    ax.set_xlim(-10.5, 10.5)
    ax.set_ylim(-1.5, 34.5)
    ax.set_aspect("equal")
    ax.axis("off")

    out_png = HERE / "fig1_suite_ladder.png"
    out_pdf = HERE / "fig1_suite_ladder.pdf"
    fig.savefig(out_png, dpi=300, bbox_inches="tight", facecolor="white")
    fig.savefig(out_pdf, bbox_inches="tight", facecolor="white")
    print(f"wrote {out_png}")
    print(f"wrote {out_pdf}")

    # Sanity check — did we cover all 80 notebooks, fully contiguous?
    all_tiles = [tn for _, _, _, tiles in CLUSTERS for tn, _ in tiles]
    assert len(all_tiles) == len(set(all_tiles)), "duplicate notebook IDs"
    for letter, _, _, tiles in CLUSTERS:
        idx = sorted(int(tn[1:]) for tn, _ in tiles)
        assert all(tn[0] == letter for tn, _ in tiles), f"tile outside cluster {letter}"
        assert idx == list(range(1, len(idx) + 1)), f"cluster {letter} not contiguous: {idx}"
    assert len(all_tiles) == 80, f"expected 80 notebooks, got {len(all_tiles)}"
    print("  ✓ all 80 notebooks covered (each cluster contiguous)")


if __name__ == "__main__":
    build()
