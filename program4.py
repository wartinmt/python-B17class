# Martin June1,2020
# program4 - basic math operations

# +,-,*,/,//(integer division),%(remainder /modulus)
# ** exponentiation

# Write a program to ask the user for total number of seconds,
# and then find the number of hours, minutes and seconds in that time

# 10,000 seconds = 2 hours, 46 minutes, 40 seconds

# 1 hour = 60 min = 3600 sec
# 1 min = 60 sec

# Define the main function
def main():
    # get totalSeconds as input from user
    totalSeconds = int(input("Enter total number of seconds:"))

    # comput number of hours
    hours = totalSeconds // 3600
    # integer division gives quotient only

    # compute remainder
    leftOverSeconds = totalSeconds % 3600

    # compute number of minutes
    minutes = leftOverSeconds // 60

    # compute remainder
    leftOverSeconds = leftOverSeconds % 60

    # display results
    print("Here is the breakdown:")
    print("Hours = ", hours)
    print("Minutes = ", minutes)
    print("Seconds = ", leftOverSeconds)


# Call the main function
main()

# Try 11730,21384
