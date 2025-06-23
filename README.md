# Tracking Clusters Studies Workspace

Collection of packages for testing inner sillicon tracking digitization performance in a muon collider.

## Repository Structure
- `exts/` External packages not included with the Muon Collider framework.
- `packages/` All non-standard packages linked using git submodules.

## Setup Instructions

### Container
All commands should be run inside the `docker:gitlab-registry.cern.ch/muon-collider/mucoll-deploy/mucoll:2.9-alma9` image.

#### Singularity

```bash
apptainer shell --cleanenv -B/disk/moose docker:gitlab-registry.cern.ch/muon-collider/mucoll-deploy/mucoll:2.9-alma9
```

#### Shifter

```bash
shifter --image gitlab-registry.cern.ch/muon-collider/mucoll-deploy/mucoll:2.9-alma9 /bin/bash
```

### Build Instructions
Run the following commands from inside your container. The same commands will also work with a local installation of the ILC software, with the exception of the first line.

```bash
source /opt/setup_mucoll.sh # Setup ILC software
cmake -S . -B build 
cmake --build build
```

### Setup Script
The included `setup.sh` script is useful for defining all paths for the binaries built by the workspace. At the current stage, it setups the following:
- Muon Collider software via `setup_mucoll.sh`
- External binaries/libraries found in `exts`.
- Add all package libraries to `MARLIN_DLL`.
- Export `MYBUILD` variable with absolute path the build directory.
- Export `MYWORKSPACE` variable with absolute path the workspace directory.

Run the following at the start of every session. It has an optional argument to the build directory and is set to `build/` by default.

```bash
source setup.sh [build]
```

## Geometry information
A quick note for the MusicV2 and MAIA 10 TeV geometries.
* MusicV2; I indicated below which packages you should add to the workspace if the version in the container is too old.
    * Geometry is stored in the main branch of the lcgeo package (clone locally; branch master): `https://github.com/MuonColliderSoft/lcgeo/tree/master/MuColl/MuSIC_v2`
    * Material Map and TGeo models are now in the master branch of ACTSTracking (clone locally; branch main): `https://github.com/MuonColliderSoft/ACTSTracking/tree/main/data`
    * BIB files with this geometry are now on perlmutter here: `/global/cfs/cdirs/atlas/spgriso/MuonCollider/data/bib/10TeV-2024/MusicV2/trimmed` and then two sub-folders: `MuMinus` and `MuPlus`
    * For BIB, in the `OverlayMIX` processor set `NumberOfBackgrounds` to `6`
    * Incoherent pair production is on plermutter here: `/global/cfs/cdirs/atlas/spgriso/MuonCollider/data/bib/10TeV-2024/MusicV2/trimmed/MuPairs`
* MAIA; clone locally the repository `https://github.com/madbaron/detector-simulation/`
    * Geometry files are in this folder: `https://github.com/madbaron/detector-simulation/tree/KITP_10TeV/geometries/MAIA_v0`
    * Material Map: `/global/cfs/cdirs/atlas/spgriso/MuonCollider/data/bib/10TeV-2024/MAIA/ACTSmaps/`
    * BIB files with this geometry on perlmutter: `/global/cfs/cdirs/atlas/spgriso/MuonCollider/data/bib/10TeV-2024/MAIA`
    * For BIB, in the `OverlayMIX` processor set `NumberOfBackgrounds` to `833`

## Example Commands

