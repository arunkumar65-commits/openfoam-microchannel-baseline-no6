
#===============================================================#
# Automation for Benchmark No.6 Geometry
# Reynolds Number Study Only
# Fixed Mesh
#===============================================================#

import shutil
import subprocess

# ===============================================================
# Fluid Properties
# ===============================================================

Tk = 293
Tc = Tk - 273.15

mu = 2.414e-5 * 10**(247.8 / (Tk - 140))

Dh = 1.3333e-4

rho = (
    999.84
    + 18.225 * Tc
    - 7.92e-3 * (Tc**2)
    - 5.545e-5 * (Tc**3)
    + 1.498e-7 * (Tc**4)
    - 3.933e-10 * (Tc**5)
) / (1 + 1.816e-2 * Tc)



Re_list = [
    190, 244, 298, 352, 406, 460, 514,
    568, 622, 676, 730, 784, 838
]



commands = [
    "blockMesh > log.blockMesh 2>&1",
    "topoSet > log.topoSet 2>&1",
    "splitMeshRegions -cellZones -overwrite > log.splitMesh 2>&1",
    "checkMesh > log.checkMesh 2>&1",
    "foamMultiRun > log.cht 2>&1"
]



simulationFailed = False

for Re in Re_list:

    caseName = f"Case_Re{Re}"

    print(f"\nCreating {caseName}")

    
    shutil.copytree("hihRevar", caseName)     ## "hihRever" a floder that stores templete files  

   

    U = (Re * mu) / (rho * Dh)

    print(f"Re = {Re}")
    print(f"U  = {U:.6f} m/s")



    U_path = f"{caseName}/0/fluidZone/U"

    with open(U_path, "r") as Ufile:
        lines = Ufile.readlines()

    insideInlet = False
    inletValueFound = False

    for i, line in enumerate(lines):

        if line.strip() == "fluidInlet":
            insideInlet = True

        elif insideInlet and line.strip().startswith("value"):
            lines[i] = f"        value   uniform ({U:.10f} 0 0);\n"
            inletValueFound = True
            break

        elif insideInlet and line.strip() == "}":
            insideInlet = False

    if not inletValueFound:
        print(f"ERROR: Could not find inlet velocity in {U_path}")
        simulationFailed = True
        break

    with open(U_path, "w") as Ufile:
        Ufile.writelines(lines)

  

    for command in commands:

        print(f"\nRunning: {command}")
        print(f"Case: {caseName}")

        result = subprocess.run(
            command,
            shell=True,
            cwd=caseName
        )

        if result.returncode == 0:
            print(f"SUCCESS: {command}")

        else:
            print(f"FAILED: {command}")
            simulationFailed = True
            break

    if simulationFailed:
        print(f"\nStopping automation at {caseName}")
        break

print("\nAutomation Finished")
