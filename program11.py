# Martin June3,2020
# program11 - -logical operators and random numbers

# pesudo-random numbers or arandom numbers are generated using the random module

# if ((condition1) and (condition2)):
# and is a logical operator connecting 2 conditions
# if ((condition1) or(condition2)):
# or is a logical operator

# T and T == combo is T
# T and F == combo is F
# F and T == combo is F
# F and F == combo is F

# T or T == combo is T
# T or F == combo is T
# F or T == combo is T
# F or F == combo is F

# one more logical operator = not
# not FALSE = TRUE
# not TRUE = FALSE

# game of dice
# for the face value of the die, I use random number

# we roll a pair of dice. If the face values add up to 7 or 11, we win. Otherwise we lose

# random module, randint function

import random


# Define the main function
def main():
    # ask user if he/she wants to play
    answer = input("Do you want to play? Press y or n")

    if (answer == "y"):
        # roll a pair of dice = generate 2 random numbers
        faceValue1 = random.randint(1, 6)
        faceValue2 = random.randint(1, 6)

        # add the 2 numbers
        faceValueSum = faceValue1 + faceValue2

        # print the face values and the sum
        print("You rolled", faceValue1, "and", faceValue2)
        print("The sum of the face values is", faceValueSum)

        # win of lose?
        if ((faceValueSum == 7) or (faceValueSum == 11)):
            print("You win")
        else:
            print("You lose")


main()

# roll a pair of dice
