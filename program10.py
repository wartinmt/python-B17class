# Martin June 3,2020
# Program 10 - if-elif-else statement

# nested if = if within another if or within an else statement
# I have multiple conditions and I test them one at a time

# if(condition1):
#   action1
# elif(condition2):
#   action2
# elif(condition3):
#   action3
# .........
# else:
#   actionN

# In the homework, you computed the average score
# if average >=90, you get A grade
# else if average >= 80, you get B grade
# if average >= 70, you get C grade
# if average >= 60, you get D grade
# if it is less than 60, you get F grade

# Define the main function
def main():
    test1 = float(input("Enter score for Test1:"))
    test2 = float(input("Enter score for Test2:"))
    test3 = float(input("Enter score for Test3:"))
    test4 = float(input("Enter score for Test4:"))

    # compute average
    average = (test1 + test2 + test3 + test4) / 4.0
    print("Your average score is", average)

    # if statement
    if (average >= 90):
        print("You scored an A")
    elif (average >= 80):
        print("You scored an B")
    elif (average >= 70):
        print("You scored an C")
    elif (average >= 60):
        print("You scored an D")
    else:
        print("You scored an F")


main()
