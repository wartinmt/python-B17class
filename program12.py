# Martin June3,2020
# program12 - repetition structures (loops)

# while loop - condition-controlled loop
# while(condition):
#   repeat some tasks
# the moment the condition becomes false, the loop ends

# game of dice; roll 2 dice; if user gets 7 or 11, he/she wins;
# otherwise, he/she loses.
# The user can play any number of times
# calculate number of games, wins, losses

# variables = games, wins, looses, faceValue1, faceValue2, faceValueSum
# answer

# games = games +1 = update / increment by 1
# games += 1

import random


# Define the main function
def main():
    # get user input
    answer = input("Do you want to play the game: Press y or n.")

    # initialize the variables
    games = 0
    wins = 0
    losses = 0

    # loop
    while (answer == "y"):

        # generate the random numbers
        print("Let`s roll the dice")
        games += 1  # update games
        faceValue1 = random.randint(1, 6)
        faceValue2 = random.randint(1, 6)

        # compute the sum
        faceValueSum = faceValue1 + faceValue2

        # print
        print("You rolled", faceValue1, "and", faceValue2)
        print("The sum of the face values is", faceValueSum)

        # if
        if (faceValueSum == 7) or (faceValueSum == 11):
            print("You win")
            wins += 1  # update wins
        else:
            print("You lose")
            losses += 1

        answer = input("Do you want to continue? Press y or n.")

    # print the stats
    print("Game played =", games)
    print("Games win =", wins)
    print("Games lost =", losses)


main()
