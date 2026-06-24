r"""Matplotlib style helpers for MDPI/LaTeX-consistent figures.

The project LaTeX preamble uses

    \usepackage[T1]{fontenc}
    \usepackage{lmodern}

so the closest figure font is Latin Modern Roman rendered through LaTeX.

Environment switches
--------------------
CIV_USE_TEX=1   use LaTeX rendering when a latex executable is available (default)
CIV_USE_TEX=0   force Matplotlib mathtext fallback
Figures are saved as PDF only. Requested .png filenames are converted to .pdf.
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path

import matplotlib as mpl


_LATEX_PREAMBLE = r"""
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath}
\usepackage{amssymb}
"""


_CONFIGURED = False


def latex_available() -> bool:
    """Return True if a usable LaTeX executable is visible on PATH."""
    return shutil.which("latex") is not None


def configure_matplotlib_for_latex(force: bool | None = None) -> bool:
    """Configure Matplotlib to match the LaTeX article typography.

    Parameters
    ----------
    force:
        None  -> obey CIV_USE_TEX and check whether LaTeX is installed.
        True  -> request LaTeX rendering; falls back if latex is unavailable.
        False -> force Matplotlib mathtext fallback.

    Returns
    -------
    bool
        True if text.usetex is enabled, otherwise False.
    """
    global _CONFIGURED

    env_use_tex = os.environ.get("CIV_USE_TEX", "1").strip().lower()
    requested = env_use_tex not in {"0", "false", "no", "off"}
    if force is not None:
        requested = bool(force)

    use_tex = requested and latex_available()

    common = {
        "font.family": "serif",
        "font.serif": ["Latin Modern Roman", "CMU Serif", "Computer Modern Roman", "DejaVu Serif"],
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "axes.unicode_minus": False,
        "figure.dpi": 150,
        "savefig.dpi": 600,
        "savefig.bbox": "tight",
    }

    if use_tex:
        mpl.rcParams.update(common | {
            "text.usetex": True,
            "text.latex.preamble": _LATEX_PREAMBLE,
        })
    else:
        mpl.rcParams.update(common | {
            "text.usetex": False,
            "mathtext.fontset": "cm",
            "mathtext.rm": "serif",
            "mathtext.it": "serif:italic",
            "mathtext.bf": "serif:bold",
        })
        if requested:
            print(
                "[WARN] LaTeX executable not found. Falling back to Matplotlib mathtext. "
                "Install TeX Live/MiKTeX and set CIV_USE_TEX=1 for exact LaTeX rendering."
            )

    _CONFIGURED = True
    return use_tex


def savefig_publication(fig, path, *, dpi: int | None = None, bbox_inches: str = "tight", also_pdf: bool | None = None) -> None:
    """Save a publication figure as PDF only.

    The plotting code historically requested ``.png`` filenames and optionally
    saved a PDF copy next to them.  For the manuscript workflow, we now force a
    single PDF output.  If a caller passes ``foo.png``, the actual output is
    ``foo.pdf`` and no PNG is written.

    The ``dpi`` argument is still accepted because rasterized artists inside a
    PDF, such as heatmap bodies, use it.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    pdf_path = path.with_suffix(".pdf")

    if dpi is None:
        dpi = int(mpl.rcParams.get("savefig.dpi", 600))

    fig.savefig(pdf_path, dpi=dpi, bbox_inches=bbox_inches)
