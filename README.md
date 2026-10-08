# Automated Gating on the Levine 32-Marker CyTOF Dataset

A learning project in automated gating of mass cytometry (CyTOF) data. 
This project works toward doing that in Python on a public bone marrow dataset.

## Dataset

The Levine 32-dimensional dataset (Levine et al., 2015, *Cell*): 265,627 healthy
human bone marrow cells from 2 donors, measured on 32 surface markers. A subset of
cells carries expert labels for 14 manually gated populations.

Download it from <https://github.com/lmweber/benchmark-data-Levine-32-dim> and place
these files in `data/` (the folder is git-ignored):

```
data/
├── Levine_32dim_notransform.fcs
└── population_names_Levine_32dim.txt
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the notebook:

```bash
jupyter lab notebooks/01_load_and_explore.ipynb
```

Run the tests from the repo root (they skip if the data file is missing):

```bash
python -m pytest
```

## Repo structure

```
.
├── data/                           # dataset files (not in the repo, see Dataset)
├── notebooks/
│   └── 01_load_and_explore.ipynb   # load the FCS file and profile each channel
├── src/
│   └── load.py                     # FCS loading and profiling functions
├── tests/
│   └── test_load.py                # loader tests
└── requirements.txt
```

## Status

- **Done:** parsing the FCS file and profiling each channel.
- **In progress:** arcsinh transform, clustering, and benchmarking against the
  14 manually gated populations.
