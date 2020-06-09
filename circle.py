# Martin June8,2020
# program32
# This is called a module
# A module is a set of functions that are related
# The module will be imported in another program
# and the functions can be used
import math


# Define tha area of a circle
def area(radius):
    area = math.pi * math.pow(radius, 2)
    return area


# Define the circumference of a circle
def circumference(radius):
    circ = 2 * math.pi * radius
    return circ
