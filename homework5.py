#Martin June4,2020
#homework5 - page226,problem9 Ocean  Levels
def main():
    year = 2020
    level = 0.0
    print("Years","\t","Rising Ocean`s Level")
    for test in range(1,27,1):
        print(year,"\t",format(level,'.1f'))
        year += 1
        level += 1.6
main()

