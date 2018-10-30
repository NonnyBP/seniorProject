#   Jonathan Castellanos / Hanna Millares
#   File contains constant variables
#   TEMPORARY VARIABLE NAMES

import numpy as np

# Universal Constants
permeabilityOfFreeSpace = 4 * np.pi * 10**-7 # in H/m
permittivityOfFreeSpace = 8.8542 * 10**-12 # in F/m
velocityOfLight = 2.9979 * 10**8 # in m/s^2
impedanceOfFreeSpace = 377 # in ohms
electronMass = 9.1093822 * 10**-31 # in kg
gravity = 9.80665 # in m/s^2
ionCharge = 1.6020176487 * 10**-19 # in C
atomicMassUnit = 1.6602176487 * 10**-27 # in kg
eV = 1.602176487 * 10**-13 # in J (energy associated with 1 electron volt)

# CubeSat Constants
maxCubeSatWeight = 1.33 # in Kg for 1U
maxCubeSatVolume = .001 # in m for 1U

#Iodine Properties
iodineAtomicNumber = 53
iodineMeltingPoint = 386.9 # in K
iodineBoildingPoint = 457.6 # in K
iodineDensity = 4933.00 # in kg/m^3
iodineRelativeAtomicMass = 126.904 # in u (atomicMassUnit)
ionMass = iodineRelativeAtomicMass * atomicMassUnit
iodineStateInRoomTemp = "Solid" # room temp about 293.15 K
iodineFirstLevelIonizationEnergy = 1008.4 # in kJ/mol
iodineSecondLevelIonizationEnergy = 1845.9 # in kJ/mol
iodineThirdLevelIonizationEnergy = 3180 # in kJ/mol
iodineMinCost = 20 # in $/kg
iodineMaxCost = 27.50 # in $/kg

# Ion Optics Variables
accelPotentialVoltage = -30 # in V
screenPotentialVoltage = 30 # in V
voltageDifferenceBetweenScreenAndAccel = screenPotentialVoltage - accelPotentialVoltage
gridOuterDiameter = .03 # in m
screenGridThickness = 0.3412 / 1000 # in m (t_s)
accelGridThickness = 0.3882 / 1000 # in m (t_a)
decelGridThickness = 0.255 / 1000 # in m (t_d)
screenGridApertureDiameter = 0.9353 / 1000 # in m (d_s)
screenGridApertureArea = np.pi * screenGridApertureDiameter
accelGridApertureDiameter = 0.64 / 1000 # in m (d_a)
accelGridApertureArea = np.pi * accelGridApertureDiameter
decelGridApertureDiameter = 1.035 / 1000 # in m (d_d)
decelGridApertureArea = np.pi * decelGridApertureDiameter
distanceBetweenScreenAndAccel = 0.14765 / 1000 # in m (l_sa)
distanceBetweenAccelAndDecel = 0 # in m (l_ad)

# Propulsion Variables
designThrust = .001 # Newtons