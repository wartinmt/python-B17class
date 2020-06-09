# Martin June1,2020
# program6 - some math module functions

# math.sqrt(x) = square root function
# math.ceil(x) = ceiling function = smallest integer greater than equal
# to x
# math.floor(x) = floor function = largest integer smaller than or
# equal to x
# math.pow(x,n) = exponentiation function = x^n
# math.hypot(x,y) = returns the hypotenuse that extends from
# (0,0) to (x,y)

# Quadratic Formula
# Given ax^2 + bx+ c = 0, find roots x1 and x2
# Let`s hold of on this problem until Wednesday.

# Let`s find the hypotenuse of a right angled triangle

import math


# Define the main function
def main():
    # get the 2 legs from the user as input
    leg1 = float(input("Enter value of leg 1 of the triangle: "))
    leg2 = float(input("Enter value of leg 2 of the triangle: "))

    # Compute the hypotenuse using math.hypot
    hypot1 = math.hypot(leg1, leg2)

    # Compute the hypotenuse using Pythagorean Theorem
    legSQ = math.pow(leg1, 2) + math.pow(leg2, 2)
    hypot2 = math.sqrt(legSQ)

    # display result
    print("Hypotenuse using math.hypot() function = ", format(hypot1, '.1f'))
    print("Hypotenuse using Pythagorean Theorem = ", format(hypot2, '.1f'))


# Call the main function
main()
