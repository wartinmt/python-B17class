#victor June 5,2020
#Program 21

#HH:MM:SS
#12:45:32

#timer should start at 0:0:0 and go all the way to 23:59:59

#define main
def main():

    #nested loop = loop within a loop
    for hours in range(24):
        for minutes in range(60):
            for seconds in range(60):
                print(hours,":",minutes,":",seconds)

#call main
main()