"""Write a program that reads in the radius and
length of a cyclinder and computes the area
and volume using the following formula """

from math import *

def main():
    #area = pi * r^2
    #volume = area * length

    #radius of the cylinder (floating point value)
    radius = float(input())

    #length of cylinder
    length = float(input())

    if(radius <= 0.0 or length <= 0.0):
        print("Error.")
    else:
        area = pi * radius ** 2
        volume = area * length
        round(area, 2)
        round(volume, 2)

        print( format(area, "2.2f") )
        print( format(volume, "2.2f") )

main()
