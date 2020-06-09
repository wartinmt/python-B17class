#Martin June 1, 2020
#Program3 - getting user input

#Define the main function
def main():
    #get input from user
    #get input value from user, convert to float data type
    #and assign it to the variable
    pantsCost = float(input("Enter the cost of the pants:"))
    shirtCost = float(input("Enter the cost of the shirt:"))

    #compute total purchase amount
    purchaseAmount = pantsCost +shirtCost

    #display result
    print("The cost of the pruchase is", format(purchaseAmount, '.2f'))

#Call the main function
main()