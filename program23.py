#victor June 5,2020
#Program 23

#write a program that asks the user to enter a series of positive
#numbers. The user should enter a negative number to signal the end of the series.
#After all the positive nmber are entered , the program should display the sum of the numbers

#define main
def main():

    #initalies the accumulator = running total
    totalScore = 0
    #get input
    numbers = float(input("Enter the positive number. Negetive to stop. :"))

    while(numbers >= 0):
        totalScore += numbers
        numbers = float(input("Enter the positive number. Negetive to stop. :"))

    print("The sum of the number is:",totalScore)

#call main
main()

