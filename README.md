# esgvoc-integration

Testing of esgvoc full integration

## Installation

### Python environment

#### via UV

```
uv sync
```

#### via pip

```
python3 -m venv venv
source venv/bin/activate
# or windows equivalent of the above
pip install -r requirements-locked.txt
```

### esgvoc

```
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

```
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
uv run esgvoc drsvalid cmip7 directory MIP-DRS7/CMIP7/CMIP/IPSL/DEMO/piControl/r1i1p1f1/global/mon/tas/tavg-h2m-hxy-u/g99/20251031 --verbose

# Validate a filename against the DRS
uv run esgvoc drsvalid cmip7 filename tas_tavg-h2m-hxy-u_mon_global_g99_DEMO_historical_r1i1p1f1_185001-202112.nc --verbose
```

### Python script

```
# Show how DRS can be parsed to get the member terms
uv run python drs-parsing.py
```

```
# Print entries in a number of relevant collections
uv run python print-collections.py
```
