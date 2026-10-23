# openfoam-microchannel-baseline-no6
OpenFOAM Foundation v13 simulation of a smooth microchannel heat sink based on a published benchmark.
# OpenFOAM Microchannel Heat Sink — Baseline No. 6

## Project Overview

This project investigates laminar fluid flow and heat transfer in a smooth microchannel heat sink using OpenFOAM Foundation v13.

The baseline geometry corresponds to Microchannel No. 6 in the benchmark study by Chai et al. (2016), which examines microchannel heat sinks with offset ribs on the sidewalls.

The purpose of this baseline case is to reproduce the smooth-channel reference results before extending the study to offset-rib geometries.

## Reference Paper

Chai, L., Xia, G. D., & Wang, H. S. (2016). *Numerical study of laminar flow and heat transfer in microchannel heat sink with offset ribs on sidewalls.* Applied Thermal Engineering, 92, 32–41.

DOI: https://doi.org/10.1016/j.applthermaleng.2015.09.071

## Computational Setup

- **CFD software:** OpenFOAM Foundation v13
- **Computing environment:** ANGI cluster, IIST
- **Geometry:** Smooth microchannel heat sink, benchmark No. 6
- **Flow regime:** Laminar
- **Working fluid:** Water
- **Heat sink material:** Silicon
- **Study type:** Baseline numerical reproduction

The detailed numerical settings, boundary conditions, mesh information and post-processing methodology will be documented alongside the case files.

## Validation Status

The initial simulation results show approximate agreement with the benchmark results. Further quantitative comparison and verification are needed to establish the accuracy of the reproduction.

## Repository Contents

The repository will contain the essential OpenFOAM case configuration, selected post-processing data, comparison plots and documentation.

Large generated simulation files and unnecessary intermediate results will be excluded.


## Automation

The `autocase.py` script is included to support automation of the baseline velocity study.

The study consists of 13 cases using the same baseline microchannel geometry, with inlet velocity varied between cases.

The automation workflow and execution instructions will be documented alongside the script, including the required OpenFOAM environment, case-generation procedure, and simulation commands.

## Reproducibility

- OpenFOAM version: Foundation v13
- Computing environment used for the simulations: ANGI cluster, IIST
- Geometry: Smooth microchannel heat sink, benchmark No. 6
- Validation: Initial results show approximate agreement with the benchmark; further quantitative comparison is ongoing.


## Current Progress

- [x] Create the GitHub repository
- [ ] Prepare and document the OpenFOAM case
- [ ] Record mesh and solver settings
- [ ] Compare Nusselt number and pressure drop with the benchmark
- [ ] Document discrepancies and further improvements
- [ ] Extend the study to offset-rib geometries

## Notes

This is an ongoing engineering research project. Results and documentation will be updated as the benchmark reproduction is refined.
