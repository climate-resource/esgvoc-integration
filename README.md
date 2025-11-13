# esgvoc-integration

Testing of esgvoc full integration

## Installation

### Python environment

#### via UV

```sh
uv sync
```

#### via pip

```sh
python3 -m venv venv
source venv/bin/activate
# or windows equivalent of the above
pip install -r requirements-locked.txt
```

### esgvoc

```sh
uv run esgvoc config create cmip7-playground

uv run esgvoc config switch cmip7-playground

# Add very custom CMIP7 setup
uv run esgvoc config set 'universe:github_repo=https://github.com/znichollscr/WCRP-universe' 'universe:branch=esgvoc-zn'
uv run esgvoc config add-project cmip7 --custom --repo 'https://github.com/znichollscr/CMIP7-CVs' --branch 'esgvoc-zn'

# Remove default projects
uv run esgvoc config remove-project -f cmip6
uv run esgvoc config remove-project -f cmip6plus

# Install everything
uv run esgvoc install
```

## Usage

### esgvoc CLI

```sh
# Get a list of everything
uv run esgvoc get ::

# Get a list of everything in the universe
uv run esgvoc get universe::

# Get a list of everything in the universe's archive collection
uv run esgvoc get universe:archive:

# Get the WCRP term from the universe's archive collection
uv run esgvoc get universe:archive:wcrp

# Get a list of everything in the universe's archive collection,
# showing only the ID
uv run esgvoc get universe:activity: --select "id"

# Get a list of everything in the universe's archive collection,
# showing only the drs_name
uv run esgvoc get universe:activity: --select "drs_name"

# Validate a path against the DRS
uv run esgvoc drsvalid cmip7 directory MIP-DRS7/CMIP7/CMIP/CCCma/CanESM6-MR/piControl/r1i1p1f1/glb/mon/tas/tavg-h2m-hxy-u/g99/20251031 --verbose

# Validate a filename against the DRS
uv run esgvoc drsvalid cmip7 filename tas_tavg-h2m-hxy-u_mon_glb_g99_CanESM6-MR_historical_r1i1p1f1_185001-202112.nc --verbose

# Export CMOR tables
uv run esgvoc cmor-export-cvs-table
# (or to a file)
uv run esgvoc cmor-export-cvs-table --out-path cmor-cvs-example.json
```

### Python script

```sh
# Show how DRS can be parsed to get the member terms
uv run python drs-parsing.py
```

```sh
# Print entries in a number of relevant collections
uv run python print-collections.py
```
