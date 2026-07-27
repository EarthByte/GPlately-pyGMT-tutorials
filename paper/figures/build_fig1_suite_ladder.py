"""Build Figure 1 — the tutorial suite organised by thematic cluster.

Layout 2026-07-29: **79 notebooks across 11 clusters (A-K), fully contiguous**.
Old T31 (Subducted-slab flux inventory) was moved out of cluster E (mantle
dynamics) into cluster B (plate kinematics + tectonics) as the new T16,
directly after T15 -- it is a per-trench kinematic-flux notebook, consistent
with T08-T15's kinematic-diagnostic style, not a mantle-dynamics one. Old
T16-T30 shifted up by one to T17-T31; T32 onward is unaffected.

Run:
    cd paper/figures
    python build_fig1_suite_ladder.py

Output: fig1_suite_ladder.png + fig1_suite_ladder.pdf (this folder).

Cluster structure (2026-07-29 resequence, disk-verified):
    A : T01-T07        Getting started / core workflows
    B : T08-T16        Plate kinematics + tectonics
                              (T14 = rift obliquity; T15 = kinematic feature
                               extraction at subduction zones, contributed
                               by Ehsan Farahbakhsh; T16 = subducted-slab
                               flux inventory, reclassified from cluster E
                               2026-07-29)
    C : T17-T20        Plate-model debugging (Sculley + Cannon)
    D : T21-T25        Zircons + tectonic-setting predictors
                              (T25 = Hf-Nd terrane mapping)
    E : T26-T32        Mantle dynamics + dynamic topography
                              (T26-T27 REVEAL pair;
                               T32 = mantle-to-plate frame conversion)
    F : T33-T43        Paleomagnetism (T42 = TPW decomposition)
    G : T44-T52        Paleo-geography + paleo-topography + thermochronology
                              (T44-T50 = ThermoPlates suite;
                               T51 = North American thermochron;
                               T52 = ophiolite paleo-map)
    H : T53-T55        Sedimentary basins (Heine ICONS Atlas trio)
    I : T56-T61        Paleobiogeography
    J : T62-T71        Paleoclimate (T62-T70 = Leonard 2025 quartet + others;
                               T71 = carbonate-platform arc degassing,
                               reclassified from cluster K 2026-07-28)
    K : T72-T79        Mineral exploration
                              (T72-T77 = porphyry/Cu suite;
                               T78 = Mn 1.8 Ga; T79 = craton boundaries)
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
        ("T15", "Kinematic" + NL + "feature" + NL + "extraction"),
        ("T16", "Subducted-" + NL + "slab flux"),
    ]),
    ("C", "Plate-model debugging", "#34495E", [
        ("T17", "Div. +" + NL + "convergence" + NL + "anomalies"),
        ("T18", "MOR" + NL + "velocity" + NL + "magnitude"),
        ("T19", "Topology" + NL + "construction" + NL + "anomalies"),
        ("T20", "SZ feature" + NL + "extract-" + NL + "ability"),
    ]),
    ("D", "Zircons + tectonic-" + NL + "setting predictors", "#F4A261", [
        ("T21", "Detrital" + NL + "zircons"),
        ("T22", "Igneous" + NL + "zircons"),
        ("T23", "Meta-" + NL + "morphic" + NL + "zircons"),
        ("T24", "Dist. to" + NL + "subduction"),
        ("T25", "Hf-Nd" + NL + "terrane" + NL + "mapping"),
    ]),
    ("E", "Mantle dynamics +" + NL + "dynamic topography", "#A569BD", [
        ("T26", "REVEAL" + NL + "tomography" + NL + "slices"),
        ("T27", "REVEAL" + NL + "plume" + NL + "cross-sect."),
        ("T28", "Mantle" + NL + "transect" + NL + "deep time"),
        ("T29", "DT cluster" + NL + "histories"),
        ("T30", "DT vs" + NL + "sediment"),
        ("T31", "DT change" + NL + "deep time"),
        ("T32", "Mantle→" + NL + "plate frame" + NL + "conversion"),
    ]),
    ("F", "Paleomagnetism", "#E74C3C", [
        ("T33", "Paleomag." + NL + "reference" + NL + "frame"),
        ("T34", "Frame" + NL + "comparison"),
        ("T35", "Plate/mantle" + NL + "frame" + NL + "uncertainty"),
        ("T36", "Continent" + NL + "reconstr." + NL + "(gplately)"),
        ("T37", "APWP vs" + NL + "gplately" + NL + "site"),
        ("T38", "Osler" + NL + "1.1 Ga"),
        ("T39", "Phaner." + NL + "APWP on" + NL + "Laurentia"),
        ("T40", "SVEI" + NL + "shallowing"),
        ("T41", "Rotated" + NL + "poles"),
        ("T42", "TPW" + NL + "decomp."),
        ("T43", "Paleolat." + NL + "reverse" + NL + "reconstr."),
    ]),
    ("G", "Paleo-geography +" + NL + "paleo-topography", "#16A085", [
        ("T44", "Geochem-" + NL + "corrected" + NL + "paleo-elev"),
        ("T45", "Macrostrat" + NL + "Great" + NL + "Unconf."),
        ("T46", "Highland" + NL + "footprints"),
        ("T47", "C. Asia" + NL + "thermo-" + NL + "chron."),
        ("T48", "Cooling ×" + NL + "Earth-" + NL + "system"),
        ("T49", "Cooling ×" + NL + "kinematics" + NL + "× faults"),
        ("T50", "Cooling-" + NL + "rate" + NL + "correl."),
        ("T51", "N. America" + NL + "thermo-" + NL + "chron."),
        ("T52", "Ophiolite" + NL + "paleo-map"),
    ]),
    ("H", "Sedimentary basins", "#8E44AD", [
        ("T53", "Global" + NL + "basins" + NL + "ICONS"),
        ("T54", "Crustal" + NL + "stretching" + NL + "factor β"),
        ("T55", "Individual" + NL + "rift" + NL + "analysis"),
    ]),
    ("I", "Paleobiogeography", "#F39C12", [
        ("T56", "PBDB ×" + NL + "Macrostrat" + NL + "paleo-litho"),
        ("T57", "Reef" + NL + "builders" + NL + "paleolat"),
        ("T58", "Kimmer." + NL + "dinos"),
        ("T59", "Cenozoic" + NL + "forams"),
        ("T60", "PBDB" + NL + "paleobio-" + NL + "geography"),
        ("T61", "H3 bio-" + NL + "regional-" + NL + "isation"),
    ]),
    ("J", "Paleoclimate", "#2980B9", [
        ("T62", "Boucot" + NL + "climate" + NL + "lithos"),
        ("T63", "Deep-time" + NL + "paleoclim." + NL + "snapshots"),
        ("T64", "cGENIE" + NL + "SST vs" + NL + "proxies"),
        ("T65", "PLASIM" + NL + "CO2" + NL + "sensitivity"),
        ("T66", "pySCION" + NL + "Phanerozoic"),
        ("T67", "Ref-frame" + NL + "paleoclim."),
        ("T68", "Ocean" + NL + "gateways" + NL + "vs frame"),
        ("T69", "Multi-study" + NL + "GMST"),
        ("T70", "Proxy" + NL + "validation" + NL + "of frames"),
        ("T71", "Carbonate" + NL + "platform" + NL + "degassing"),
    ]),
    ("K", "Mineral exploration", "#7D6608", [
        ("T72", "SW-Pacific" + NL + "porphyries"),
        ("T73", "Global" + NL + "porphyry" + NL + "envelope"),
        ("T74", "Seafloor" + NL + "anomalies"),
        ("T75", "Sediment-" + NL + "hosted Cu"),
        ("T76", "Porphyry-Cu" + NL + "deep-time" + NL + "trajectories"),
        ("T77", "Continent" + NL + "prospectivity" + NL + "maps"),
        ("T78", "Manganese" + NL + "1.8 Ga" + NL + "paleogeo"),
        ("T79", "Craton" + NL + "boundary" + NL + "framework"),
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
# Cluster sizes: A(7), B(9), C(4), D(5), E(7), F(11), G(9), H(3), I(6), J(10), K(8)
ROWS = [
    ["A"],               # A(7) alone
    ["B", "C", "D"],     # B(9) + C(4) + D(5) = 18 tiles
    ["E", "F"],          # E(7) + F(11) = 18
    ["G", "H"],          # G(9) + H(3) = 12 — H pairs with G nicely
    ["I", "J"],          # I(6) + J(10) = 16
    ["K"],               # K(8) alone
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

    # Sanity check — did we cover all 79 notebooks, fully contiguous?
    all_tiles = [tn for _, _, _, tiles in CLUSTERS for tn, _ in tiles]
    assert len(all_tiles) == len(set(all_tiles)), "duplicate T-numbers"
    numbers = sorted(int(t[1:]) for t in all_tiles)
    assert numbers == list(range(1, 80)), (
        f"expected T01-T79 contiguous, got missing/extra: "
        f"{set(range(1, 80)) ^ set(numbers)}")
    print(f"  ✓ all 79 notebooks covered (T01-T79 fully contiguous)")


if __name__ == "__main__":
    build()
