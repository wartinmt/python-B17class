# Martin June1,2020
# homework1 - average

def main():
    number1 = float(input("Enter the first scores:"))
    number2 = float(input("Enter the second scores:"))
    number3 = float(input("Enter the third scores:"))
    number4 = float(input("Enter the fourth scores:"))
    answer = number1 / 4 + number2 / 4 + number3 / 4 + number4 / 4
    print("The average of these scores is:", format(answer, '.1f'))


main()
