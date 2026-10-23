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

The OpenFOAM simulation reproduces the overall trend in the Nusselt number (Nu) reported in the benchmark study, with a deviation of 4.4% for the evaluated case. This indicates good agreement with the reference result for this parameter. Further verification and comparison across the Reynolds number range are ongoing.

## Repository Contents

The repository will contain the essential OpenFOAM case configuration, selected post-processing data, comparison plots and documentation.

Large generated simulation files and unnecessary intermediate results will be excluded.


## Automation

The baseline Reynolds-number study is automated using `autocase.py`, written in Python.

The script generates 13 cases for Reynolds numbers ranging from 190 to 838, using a common smooth microchannel geometry and varying the inlet velocity.

### Automation procedure

1. Calculate the water density and dynamic viscosity at 293 K.
2. Calculate the inlet velocity corresponding to each Reynolds number using the hydraulic diameter.
3. Copy the baseline case template into a separate directory for each Reynolds number.
4. Update the fluid inlet velocity boundary condition.
5. Execute the mesh-generation, region-separation, mesh-checking, and multi-region CHT solver commands.
6. Stop the automation if a command fails or the inlet velocity entry cannot be located.

### Scope and limitations

The script automates case generation and solver execution. Post-processing, extraction of heat-transfer quantities, and quantitative comparison with the benchmark are separate tasks.

The mesh-generation commands are executed for each case, using the same template and mesh settings.

The initial Nusselt-number comparison shows a reported deviation of 4.4% for the evaluated case. Further quantitative validation across the Reynolds-number range is ongoing.

## Reproducibility

- OpenFOAM version: Foundation v13
- Geometry: Smooth microchannel heat sink, benchmark No. 6
- Validation: Initial results show approximate agreement with the benchmark; further quantitative comparison is ongoing.


## Current Progress

- [x] Create the GitHub repository
- [x] Upload the OpenFOAM baseline case configuration
- [x] Add the automation script for the 13 velocity cases
- [x] Document the benchmark reference and computational setup
- [ ] Document mesh generation and simulation execution
- [ ] Quantitatively compare Nusselt number and pressure drop with the benchmark
- [ ] Investigate numerical discrepancies and improve agreement
- [ ] Complete the validation across the Reynolds number range
- [ ] Extend the study to offset-rib geometries

## Notes

This is an ongoing engineering research project. Results and documentation will be updated as the benchmark reproduction is refined.
