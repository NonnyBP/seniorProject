#   Jonathan Castellanos / Hanna Millares
#   File contains functions
#   TEMPORARY VARIABLE NAMES
import numpy as np
import constants as c

# Specific Impulse: Units in seconds, i_sp = T / (m_dot * g) = exhaust_velocity / gravity
# Efficiency of rocket / jet engines
def specificImpulse(thrust, massFlow, gravity):
    i_sp = thrust / (massFlow * gravity)
    return i_sp

# Rocket Equation:
def delta_V(exhaustVelocity, wetMass, dryMass):
    delta_V = exhaustVelocity * np.log(wetMass / dryMass)
    return delta_V

# Thrust Principles
# T = d/dt(m_propellant * v_exit) = m_dot_i * v_i (ion mass flow rate and ion exhaust velocity)
def massFlowRateOfIons(ionBeamCurrent, ionMass, ionCharge):
    massFlowRateOfIons = (ionBeamCurrent * ionMass) / ionCharge
    return massFlowRateOfIons

def ionExhaustVelocity(ionCharge, ionMass, netVoltageAcrossGrids):
    ionExhaustVelocity = np.sqrt((2 * ionCharge * netVoltageAcrossGrids) / ionMass)
    return ionExhaustVelocity

# Notice thrust is proportional to ion beam current * sqrt of acceleration voltage
# Also used for maximum thrust of beam 
# ASSUMPTION: UNIDIRECTIONAL SINGLE IONISED BEAM A.K.A PERFECT 
def thrustForSingleCharge(ionMass, ionCharge, ionBeamCurrent, netVoltageAcrossGrids):
    thrustForSingleCharge = np.sqrt((2 * ionMass) / ionCharge) * ionBeamCurrent * np.sqrt(netVoltageAcrossGrids)
    return thrustForSingleCharge

# Ion Optics Design Equation (FOR 3-GRID DESIGN) APERTURES MUST BE ALIGNED AND SCREEN GRID + POTENTIAL / ACCEL GRID - POTENTIAL
#Perveance: Amount of current that an ion accelerator can extract and focus into a beam for a given voltage (space charge limit)
def perveance(ionCharge, ionMass, screenGridApertureDiameter, distanceBetweenScreenAndAccel):
    perveance = ((np.pi * c.permittivityOfFreeSpace) / 9) * np.sqrt((2 * ionCharge) / ionMass) * (screenGridApertureDiameter**2 / distanceBetweenScreenAndAccel**2) # in A/V^(3/2)
    return perveance

def maxIonCurrentDensity(voltageDifferenceBetweenScreenAndAccel, distanceBetweenScreenAndAccel):
    maxIonCurrentDensity = (8.61242 * 10**-9) * ( (voltageDifferenceBetweenScreenAndAccel**(3/2)) / (distanceBetweenScreenAndAccel**2))
    return maxIonCurrentDensity

def maximumIonBeamCurrent(maxIonCurrentDensity, gridApertureArea):
    maximumIonBeamCurrent = maxIonCurrentDensity * gridApertureArea
    return maximumIonBeamCurrent

def averageBeamVoltage(screenPotentialVoltage, accelPotentialVoltage):
    averageBeamVoltage = 0.9 * (screenPotentialVoltage + (-1 * accelPotentialVoltage))
    return averageBeamVoltage



# Ion Optics Design Equations
#def accelerationlength(screenAcelGap, screenGridThickness, screenGridApertureDiameter):
#    accelerationLength = np.sqrt(screenAcelGap + screenGridThickness + (screenGridApertureDiameter**2 / 4))
#    return accelerationLength

#def gridTransparency(beamCurrentThroughGrid, totalIonCurrentGrid):
#    gridTransparency = (beamCurrentThroughGrid / totalIonCurrentGrid)
#    return gridTransparency
# Ion Optics: Normalized Perveance per Hole
#def NPH(beamCurrentPerHole, screenGridPotential, accelGridPotential, accelerationLength, screenGridApertureDiameter):
#    totalVoltageBetweenAccelAndScreenGrid = screenGridPotential - accelGridPotential
#    NPH = (beamCurrentPerHole / totalVoltageBetweenAccelAndScreenGrid**2) * (accelerationLength / screenGridApertureDiameter)**2
#    return NPH
    