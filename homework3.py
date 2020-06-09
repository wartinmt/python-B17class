# Martin June3,2020
# homework3 - page175,problem9 Roulette Wheel Colors

def main():
    number = int(input("Enter a pocket number between 1 and 36:"))
    if ((number >= 0) and (number <= 36)):
        if (number == 0):
            print("The pocket is green.")
        for red in range(1, 10, 2):
            if (number == red):
                print("The pocket is red.")
        for black in range(2, 11, 2):
            if (number == black):
                print("The pocket is black.")
        for red in range(12, 19, 2):
            if (number == red):
                print("The pocket is red.")
        for black in range(11, 19, 2):
            if (number == black):
                print("The pocket is black.")
        for red in range(19, 29, 2):
            if (number == red):
                print("The pocket is red.")
        for black in range(20, 29, 2):
            if (number == black):
                print("The pocket is black.")
        for red in range(30, 37, 2):
            if (number == red):
                print("The pocket is red.")
        for black in range(29, 27, 2):
            if (number == black):
                print("The pocket is black.")
    else:
        print("You enter a wrong data!")


main()
