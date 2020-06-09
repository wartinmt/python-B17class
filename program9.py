# Martin June3,2020
# program 9 - decision structures

#   if(condition):
#       action1
#   else:
#       action2
#       action3

# TRUE and FALSE are boolean operators
# in a condition, we do comparisons
# comparison operators are ==, !=, <, >, <=, >=

# let`s assume we work 40 hours a week. Pay rate = 25 Yuan
# if you work more than 40 hours, you get Overtime.
# Overtime pay = 1.5 * regular pay

# variables
# hoursWorked, standardHours = 40, standardPay = 25.00
# overtimeHours, overtimePay, totalPay

# Define the main function
def main():
    # define the constants
    standardHours = 40
    standardPay = 25.0

    overtimePay = standardPay * 1.5

    # get user input
    hoursWorked = float(input("Enter number of hours worked:"))

    # compute total pay
    if (hoursWorked <= standardHours):
        totalPay = hoursWorked * standardPay
    else:  # hoursWorked > 40
        overtimeHours = hoursWorked - standardHours
        totalPay = standardHours * standardPay + overtimeHours * overtimePay

    # display result
    print("Weekly pay is", format(totalPay, '.2f'))


main()
