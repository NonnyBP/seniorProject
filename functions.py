#   Jonathan Castellanos / Hanna Millares
#   File contains functions
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
