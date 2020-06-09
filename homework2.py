# Martin June1,2020
# homework2 - volume and total surface area of a cylinder
import math


def main():
    radius = float(input("Enter the radius:"))
    height = float(input("Enter the height:"))
    volume = math.pi * math.pow(radius, 2) * height
    area = 2 * math.pi * math.pow(radius, 2) + 2 * math.pi * radius * height
    print("The volume of the cylinder is:", format(volume, '.1f'))
    print("The total surface area of the cylinder is:", format(area, '.1f'))


main()
