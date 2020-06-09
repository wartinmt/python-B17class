# Martin June8,2020
# program30 -

# why do I need to define and create functions?
# Simple functions = easy to write, easy to test
# Reuse code
# faster development of the larger program or system
# better use of teamwork

# 2 kinds of functions
# void function = does not return a value
# value-returning function = returns a value

# I want to define a function that takes in 2 values and returns the larger value

# define the function "larger" that takes in 2 values and returns the larger value
def larger(n1, n2):  # n1 and n2 are called parameters
    # parameters are placeholders for the values that come in later
    # def larger(n1,n2): is called the function header
    if (n1 >= n2):
        return n1
    else:
        return n2
    # the above is called function body


def main():
    # get user input
    number1 = int(input("Enter number 1: "))
    number2 = int(input("Enter number 2: "))

    # call the function larger with arguments number1 and number2
    # arguments are the actual values that I send to the functions

    # When I call the function
    largeNumber = larger(number1, number2)

    # print result
    print("The larger number is", largeNumber)


main()
