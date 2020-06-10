# Martin June10,2020
# program39


def main():
    # list of product number
    productNumber = ["B4569", "M6290", "V7345", "P0697"]

    # user wants to change the value of a specofic product number
    print("I hear that you want to change the product number of a product")
    prodNum = input("Enter the product number: ")

    # I want to see if the product number is in the list.
    # If it is there, find the index of the product number.
    # If it is not there, give a suitable message

    if prodNum in productNumber:
        print(prodNum, "was found in the list.")
        prodIndex = productNumber.index(prodNum)
        print(prodNum, "was found at index", prodIndex)
        prodNum2 = input("Give me the new product number:")
        productNumber[prodIndex] = prodNum2
        print("The new product number list is \n", productNumber)
    else:
        print(prodNum,"was nor found in the list.")


main()
