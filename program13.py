# Martin June3,2020
# Program13 - keeping a running total

# we ask the user if he/she got any coins every day and we keep a running total of the number of coins
# loop stops when the user does not get any coins

# while loop
# totalCoins = accumulator = running total
# days = numbers of days

# Define the main function
def main():
    # initialize variables
    totalCoins = 0
    days = 0

    # get user input
    answer = input("Do you have coins today? Press y or n.")

    # loop
    while (answer == "y"):
        days += 1
        coins = int(input("How many coins do you have today?"))

        # add these coins to totalCoins
        totalCoins += coins

        answer = input("Do you have coins today? Press y or n.")

    # print results
    print("You have a total of", totalCoins, "coins in", days, "days")


main()
