# Martin June8,2020
# program32 use functions in circle
import circle


def main():
    radius = float(input("Enter the radius of the circle: "))
    # call the area and circumference functions of the circle module
    # call module.function(arguments)
    area = circle.area(radius)
    circumference = circle.circumference(radius)

    # display results
    print("The area of the circle is", format(area, '.1f'))
    print("The circumference of the circle is", format(circumference, '.1f'))


main()
