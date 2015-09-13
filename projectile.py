__author__ = 'zpiao1'
import math

# Input from user
angle = 45  # angle in degrees
u = 100  # initial velocity in m/s

# Time step in second
dt = 0.2

# Initial condition
t = x = y = 0.0
ra = math.radians(angle)
ux = u * math.cos(ra)
uy = u * math.sin(ra)
g = -9.8

# The main loop using sentinel-controlled loop with while
while y >= 0:
    # report result
    print(x, " ", y)

    # update t
    t += dt

    # update x
    x = ux * t

    # update y
    y = uy * t + 0.5 * g * t * t