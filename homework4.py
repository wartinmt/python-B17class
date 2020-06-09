# Martin June3,2020
# homework4 - page176,problem13 Shipping Charges
def main():
    weight = float(input("Enter the weight fo your package:"))
    if (weight <= 0):
        print("You enter a wrong data!")
    elif ((weight > 0) and (weight <= 2)):
        charges = weight * 1.5
        print("Your ship-ping charges are:$", format(charges, '.2f'))
    elif ((weight > 2) and (weight <= 6)):
        charges = weight * 3
        print("Your ship-ping charges are:$", format(charges, '.2f'))
    elif ((weight > 6) and (weight <= 10)):
        charges = weight * 4
        print("Your ship-ping charges are:$", format(charges, '.2f'))
    elif (weight > 10):
        charges = weight * 4.75
        print("Your ship-ping charges are:$", format(charges, '.2f'))


main()
