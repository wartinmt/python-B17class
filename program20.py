#victor June 5,2020
#Program 20 input vaildation

#user give the test score
#min =0 max = 100

#def main
def main():

    #get input
    score = float(input("Enter your quiz score 0-100: "))

    #input vaildation
    while((score < 0) or (score >100)):
        score = float(input("Enter correct quiz score 0-100"))

    #display output
    print("Your score is", score)

#call main
main()