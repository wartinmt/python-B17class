# Martin June8,2020
# program27 - String operations

# Define the main function
def main():
    # sample string
    name = "Smith"

    # find the length of the string
    # length = number of characters in the string
    nameLength = len(name)
    print("The length of the string is", nameLength)

    # index gives the position of the character in the string
    # index value starts from 0 and goes to n-1, where n = len(string)

    # display the character at index 2
    print("The char at index 2 is", name[2])

    for ch in name:
        print(ch)

    name2 = "I love Computer SciEnce"

    count = 0
    for ch in name2:
        if ch == 'e' or ch == 'E':
            count += 1
    print(count)

    print("The original string is", name2)

    # convert to all lower case
    name3 = name2.lower()
    print("The string in all lower case is", name3)
    name4 = name2.upper()
    print("The string in all upper case is:", name4)

    num1 = name2.find("love")
    print(num1)

    num2 = name2.find("monkey")
    print(num2)
    # replace one substring with another substring
    name5 = name2.replace("love", "baozi")
    print(name5)

    name6 = name2[3:12]
    print("Substring from index 3 to 11 is: ", name6)
    name7 = name2[3:12:2]
    print("Substring from index 3 to 11 in steps of 2 is: ", name7)
    name8 = name2[3:]
    print("Substring starting at index 3 is:", name8)
    name9 = name2[:12]
    print("Substring up to index 11 is:", name9)

    # find length of the name2
    print("name2 length is", len(name2))

    # if I use 25 as the ending index
    print("Substring up to index 24 is: ", name2[:23])

    # if I use a start index before the begining of the string, Python uses 0
    print("The substring from index 5 to index 2 is: ", name2[5:2])

    # string testing methods / functions
    n1 = name2.islower()  # is this all lower case?
    print("Is name2 all lower-case? Answer is", n1)

    n2 = name3.islower()
    print("Is name3 all lower-case? Answer is", n2)

    n3 = name4.isupper()
    print("Is name4 all upper-case? Answer is", n3)

    name11 = "123234456"
    n4 = name11.isdigit()
    print("Is name11 all digit? Answer is", n4)

    # name2.isalnum() = are all char letters or digits?
    # name2.isalpha() = are all char letters only?
    # name2.isspace() = are all char just spaces,\t,\n?

    name12 = "---I do Python.---"
    print("The original string is", name12)

    name13 = name12.lstrip('-')
    # remove (strip) off the characters before the string starts
    # these are called leading characters
    print("String with leading char removed is: ", name13)

    name14 = name12.rstrip('-')
    print("String with trailing char removed is: ", name14)

    name15 = name12.strip('-')
    print("String with both leading and trailing char removed is: ", name15)

    # splitting a string
    dateString = "2020/06/08"

    dateList = dateString.split('/')

    # display the 3 parts
    print("Year:", dateList[0])
    print("Month:", dateList[1])
    print("Day:", dateList[2])

    # If I have to split the string based on a space, then I will write nameString.split()
    # If I have to split  the string based on any other char, then I have to specify the char as nameString.split('*')


# Call the main function
main()
