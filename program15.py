# Martin June3,2020
# program15 - use for loop

# Let`s assume that the tuition for a full-time student is $8000 semester. Tuition will increase every year by 3% for
# the next 5 years. Write  a program that displays the year and projected tuition amount for the next 5 years.

# Define the main function
def main():
    print("Projected Semester Tuition Amounts")
    print("Year\tTuition Amount")

    tuition = 8000

    print(0, "\t", format(tuition, '.2f'))
    # loop
    for year in range(1, 6):
        tuition = tuition * 1.03
        print(year, "\t", format(tuition, '.2f'))


main()
