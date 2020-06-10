# Martin June10,2020
# Program38 - some operations on lists

def main():
    # A list is an object that contains multiple data items.
    # lists are mutable = changeable =contents can be changed during program execution
    # Lists are dynamic data structures = elements can be add or removed from the list
    # few basic operations on lists

    # a simple list of integers
    num = [2, 4, -6, 32, 98, -74]
    print(num)

    # print list elements one by one on different lines
    # iterating over the list
    for n in num:
        print(n)

    # list can contain items of different types
    num2 = [45, "john", 7.9, 'D']
    print(num2)

    # list of a range of values
    num3 = list(range(5))
    print(num3)

    num4 = list(range(1, 10, 2))
    print(num4)

    num5 = [0] * 5
    print(num5)

    # index of a list element = position of the element in the list
    # index starts from 0 and goes to n-1, where n = len(list)
    listLength = len(num4)
    print("Length of list num4 is", listLength)

    # print the 4th element of the list num4
    print("The 4th element of the list num4 is", num4[3])

    # print the last element of the list num4
    print(num4[-1])

    # print the second to last element of the list num4
    print(num4[-2])

    # list are mutable. Element values can change
    num4[0] = 44
    print(num4)

    # concatenate = join lists
    num6 = num3 + num4
    print("The concatenated list is", num6)

    # slicing a list = cut the list into different pieces
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # weekdays
    weekdays = days[1:6]
    print("The weekdays are: ", weekdays)

    # index values (left -> right) 0, 1, 2, 3, ..., n-1
    # (right -> left) -1, -2, -3, .....
    # do not mix and match

    # if no starting index is given, automatically starts at 0
    print(days[:6])

    # if no ending index is given, automatically it goes to end of list
    print(days[4:])

    # if no starting index and no ending index, we get the whole list
    print(days[:])

    # can use step values
    print(days[2:5:2])

    # if ending index > length of the list, no error is given, but we go to the end of the list
    print(days[2:9])

    print(days[-1])

    # if starting index < beginning of the list, then no error Python starts index at 0
    print(days[-8:4])

    # if starting index > ending index, Python returns an empty list
    print(days[6:3])


main()
