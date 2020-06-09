# Martin June1,2020
# Program5 - area and circumference of a circle

# Area of a circle = pi * r^2
# Circumference = 2 * pi * r
# r = radius of the circle

# pi is a constant in the math module. So, we will import the math
# module and use the constant
# We will also use the pow function for power/exponentiation
# always use module.function or module.constant

import math


# Define the main function
def main():
    # get radius from the user
    radius = float(input("Enter radius of the circle:"))

    # comput area and circumference
    area = math.pi * math.pow(radius, 2)
    circ = 2 * math.pi * radius

    # display result
    print("Area = ", format(area, '.1f'))
    print("Circumference = ", format(circ, '.1f'))


# Call the main function
main()
