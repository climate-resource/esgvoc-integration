# esgvoc-integration

Testing of esgvoc full integration

## Installation

### Python environment

```
uv sync
```

### esgvoc

```
uv run esgvoc config create cmip7-playground

uv run esgvoc config switch cmip7-playground
# Remove default projects
uv run esgvoc config remove-project -f cmip6
uv run esgvoc config remove-project -f cmip6plus

# Add very custom CMIP7 setup
uv run esgvoc config add-project cmip7 --custom --repo 'https://github.com/znichollscr/CMIP7-CVs' --branch 'esgvoc-zn'
uv run esgvoc config set 'universe:github_repo=https://github.com/znichollscr/WCRP-universe' 'universe:branch=esgvoc-zn'

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
```

### Python script

```
uv run python main.py
```
