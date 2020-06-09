# Martin June8,2020
# program29

# Write a program that asks the user to enter his/her full name, consisting of the first name, middle name and last
# name. Then the program should display the first, middle and last initials only. For example, John William Smith
# should display J.W.S

def main():
    name = input("Enter your first name, middle name and last name: ")
    # split the name into 3 parts
    nameList = name.split()
    print("Hello", nameList[0][0], nameList[1][0], nameList[2][0], sep='.')


main()
