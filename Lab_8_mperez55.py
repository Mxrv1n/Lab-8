''''File name: Lab_8_mperez55
Geometry Calculator
Author: Marvin Perez
Purpose: Create a menu-driven program that calculates the area and perimeter/circumference 
of circles and rectangles by importing functions from separate modules.
Date: 03/3/2026'''
from circle import area as carea
from circle import circumference 
from rectangle import area as rarea
from rectangle import perimeter
#aliases are necessary because both files a have a function named area

loop = True

while loop:
    option = int(input('''Geometry Calcuator
                       \n------------------
                       \nSelect an option:
                       \n1.-Area of a circle
                       \n2.-Circumference of a circle
                       \n3.-Area of a rectangle
                       \n4.-Perimeter of a rectangle
                       \n5.-Exit
                       \n\nEnter your choice (1-5)'''))
    if option == 1:
        radius = float(input("Please enter the radius of the circle\n"))
        while radius <=0:
            radius =float(input("Invalid radius value, please try again\nPlease enter the radius of the circle\n"))
        print(f"The area of the circle is {carea(radius)}")
        input("\nPress Enter to continue")
    if option == 2:
        radius = float(input("Please enter the radius of the circle\n"))
        while radius <=0:
            radius =float(input("Invalid radius value, please try again\nPlease enter the radius of the circle\n"))
        print(f"The circumference of the circle is {circumference(radius)}")
        input("\nPress Enter to continue")
    if option == 3:
        width = float(input("Please enter the width of the rectangle\n"))
        while width <=0:
            width =float(input("Invalid width value, please try again\nPlease enter the width of the rectangle\n"))
        height = float(input("Please enter the height of the rectangle\n"))
        while height <=0:
            height =float(input("Invalid height value, please try again\nPlease enter the height of the rectangle\n"))
        print(f"the area of the rectangle is {rarea(width, height)}")
        input("\nPress Enter to continue")
    if option == 4:
        width = float(input("Please enter the width of the rectangle\n"))
        while width <=0:
            width =float(input("Invalid width value, please try again\nPlease enter the width of the rectangle\n"))
        height = float(input("Please enter the height of the rectangle\n"))
        while height <=0:
            height =float(input("Invalid height value, please try again\nPlease enter the height of the rectangle\n"))
        print(f"the perimeter of the rectangle is {perimeter(width, height)}")
        input("\nPress Enter to continue")
    if option == 5:
        loop = False
    print("Goodbye!")