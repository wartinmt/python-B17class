# Martin June8,2020
# program31 - void function

import math


# Define the function x^3
def xCubed(x):
    result = math.pow(x, 3)
    print("x^3 = ", result)

    # result is a variable that is defined only inside the xCubed function
    # it is called a local variable and it exists only as long as xCubed
    # function is running

    # also, xCubed() is a void function because it does not return any value.
    # It just prints out the result.


# Define the main function
def main():
    # get number from user
    number = float(input("Enter a number: "))

    # call the xCubed function
    xCubed(number)


main()
