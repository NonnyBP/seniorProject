#   Jonathan Castellanos / Hanna Millares
#   File contains main run
#   TEMPORARY VARIABLE NAMES
import numpy as np
from matplotlib import pyplot as plt
import functions as f
import constants as c

# __Sheath Properties__
sheathThickness = f.sheathThickness()

# __Voltage Properties__
averageBeamVoltage = f.averageBeamVoltage(c.screenPotentialVoltage, c.accelPotentialVoltage)

# __Beam Properties and Aperature Properties__
# Ion Beam for a single aperture
singleIonBeam = f.maxIonCurrentDensity(c.voltageDifferenceBetweenScreenAndAccel, sheathThickness)
# Total Area available for aperture design in m^3
apetureArea = f.apetureArea(averageBeamVoltage, c.designThrust, singleIonBeam)
# Ion Beam for sum of all aperture
totalIonBeam = singleIonBeam * apetureArea

# __Propulsion Properties__
# Single Aperture Calculated Thrust in Newtons
singleThrust = f.thrustForSingleCharge(singleIonBeam, c.voltageDifferenceBetweenScreenAndAccel)
# Total Calculated Thrust in Newtons
totalThrust = f.thrustForSingleCharge(totalIonBeam, c.voltageDifferenceBetweenScreenAndAccel)