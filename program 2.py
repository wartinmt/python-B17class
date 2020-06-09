# Martin June 1,2020
# Program2 - variables, basic expressions

# Write a program to compute the cost of a purchase
# I want to buy a shirt for 99.99 Yuan and a pair of pants for 149.99

# Define the main function
def main():

    #create variables to hold values
    #variables should always start with a letter
    #then have letters, digits, or the underscore _
    #UPPER Case and lower case letters are different
    #Price and price are 2 different variables

    #declare given data - assignment of values to variables
    shirtCost = 99.99 #data type is float = =decimal value
    pantsCost = 149.99

    #find total cost of the purchase
    purchaseAmount = shirtCost + pantsCost

    #display the result
    print("The purchase amount is",format(purchaseAmount,'.2f'))

    #Call the main function
main()
