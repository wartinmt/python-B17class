# Martin June3,2020
# program14 - for loop

# for loop = count-controlled loop - it has a fixed number of iterations /repetitions

# for i in range(1,n):
#   some job
# loop always goes from starting index to ending index-1

# for i in range(n):
#   some job
# loop goes from 0 to ending index-1 (n-1)

# for i in range(1,n,2):
#   some job
# loop goes from 1 to n-1 in steps of 2
# for i in range(1,8,2): + i will have values of 1,3,5,7
# for i in range(2,12,3): = i will have values of 2,5,8,11

# A person runs on a treadmill and burns 4.2 calories per minute.
# Write a program that uses a loop to display the number of calories burned after 10,15,20,25 and 30 minutes

# Define the main function
def main():
    # define constant
    calPerMinute = 4.2

    # Display table headers = labels
    print("Minutes\tCalories Burned")

    # loop
    for cal in range(10, 31, 5):
        print(cal, "\t", cal * calPerMinute)


main()
