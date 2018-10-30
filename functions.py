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
def massFlowRateOfIons(ionBeamCurrent):
    massFlowRateOfIons = (ionBeamCurrent * c.ionMass) / c.ionCharge
    return massFlowRateOfIons

def ionExhaustVelocity(netVoltageAcrossGrids):
    ionExhaustVelocity = np.sqrt((2 * c.ionCharge * netVoltageAcrossGrids) / c.ionMass)
    return ionExhaustVelocity

# Notice thrust is proportional to ion beam current * sqrt of acceleration voltage
# Also used for maximum thrust of beam 
# ASSUMPTION: UNIDIRECTIONAL SINGLE IONISED BEAM A.K.A PERFECT 
def thrustForSingleCharge(ionBeamCurrent, netVoltageAcrossGrids):
    thrustForSingleCharge = np.sqrt((2 * c.ionMass) / c.ionCharge) * ionBeamCurrent * np.sqrt(netVoltageAcrossGrids)
    return thrustForSingleCharge

# Ion Optics Design Equation (FOR 3-GRID DESIGN) APERTURES MUST BE ALIGNED AND SCREEN GRID + POTENTIAL / ACCEL GRID - POTENTIAL
#Perveance: Amount of current that an ion accelerator can extract and focus into a beam for a given voltage (space charge limit)
def perveance(screenGridApertureDiameter, distanceBetweenScreenAndAccel):
    perveance = ((np.pi * c.permittivityOfFreeSpace) / 9) * np.sqrt((2 * c.ionCharge) / c.ionMass) * (screenGridApertureDiameter**2 / distanceBetweenScreenAndAccel**2) # in A/V^(3/2)
    return perveance

def maxIonCurrentDensity(voltageDifferenceBetweenScreenAndAccel, sheathThickness):
    maxIonCurrentDensity = ((4 * c.permittivityOfFreeSpace) / 9) * np.sqrt((2* c.ionCharge) / c.ionMass) * ( (voltageDifferenceBetweenScreenAndAccel**(3/2)) / (sheathThickness**2))
    return maxIonCurrentDensity

def sheathThickness():
    x = (c.distanceBetweenScreenAndAccel + c.screenGridThickness)**2 + ((c.screenGridApertureDiameter**2) / 4)
    y = np.sqrt(x)
    return y

def maximumIonBeamCurrent(maxIonCurrentDensity, gridApertureArea):
    maximumIonBeamCurrent = maxIonCurrentDensity * gridApertureArea
    return maximumIonBeamCurrent

def averageBeamVoltage(screenPotentialVoltage, accelPotentialVoltage):
    averageBeamVoltage = 0.9 * (screenPotentialVoltage + (-1 * accelPotentialVoltage))
    return averageBeamVoltage

def apetureArea(avgBeamVoltage, thrust, singleIonBeamCurrent):
    apetureArea = thrust / ((np.sqrt( (2 * c.ionMass) / c.ionCharge) ) * np.sqrt(avgBeamVoltage) * singleIonBeamCurrent)
    return apetureArea    