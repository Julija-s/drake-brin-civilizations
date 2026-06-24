# A General Probabilistic Computational Framework Applied on Drake--Fermi--Brin Models of Technological Civilizations

This repository contains code for generating, analyzing, and visualizing basic population models and supermodels, including PCA-based clustering analysis and importance-grid calculations.

## Environment Setup

Before running the code, enable LaTeX rendering and PDF figure export:

```powershell
$env:CIV_USE_TEX="1"
$env:CIV_SAVE_PDF="1"
```

---

## Generate Data and Plots

### Basic Models + Supermodels

Generate Monte Carlo samples, create plots, and build supermodels:

```bash
python main.py clean generate plot super
```

### Basic Models Only

Generate and plot only the basic models:

```bash
python main.py clean generate plot
```

---

## Importance Grid Analysis

Compute the importance grid for the selected distributions:

```bash
python importance_grid.py --out outputs --dist lognormal --super-dist mixed
```

You may change the distribution options as needed.

---

## PCA Analysis

Run PCA-based clustering analysis on the generated samples:

```bash
python main.py pca
```

---

## Complete Workflow

Generate basic models, build supermodels, create plots, and run PCA analysis in a single command:

```bash
python main.py clean generate plot super pca
```

---

## Distribution Comparison Figure

To generate the figure comparing the different sampling distributions, run:

```bash
python distributions.py
```

---

## Output

Generated data, plots, PCA results, and analysis products are written to the `outputs/` directory.

Typical output categories include:

* Monte Carlo samples
* Density surfaces and heatmaps
* Lifetime and abundance distributions
* Supermodel visualizations
* PCA projections (2D and 3D)
* Cluster summaries and centroids
* Importance grids


