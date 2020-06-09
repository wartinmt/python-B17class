# Martin June8,2020
# program28

# create a username for a student
# ask the student to give first name, last name (surname), and the University ID.
# get the first 3 characters of the first name(if first name is less than 3 char, use full first name)
# get the first 3 characters of the last name(if last name is less than 3 char, use full last name)
# get the last 3 characters of the student ID
# join all these strings to get the user name
# joining = concatenation

# define the main function
def main():
    # get user input
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    studentID = input("Enter your student ID: ")

    # extract the substrings
    n1 = firstName[0:3]
    n2 = lastName[0:3]
    n3 = studentID[-3:]  # gives the last 3 characters

    # Concatenate (join) the substrings
    userName = n1 + n2 + n3

    # print out the user name
    print("Hello", firstName)
    print("Your username is", userName)


main()
