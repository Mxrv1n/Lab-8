from circle import area as carea
from circle import circumference 
from rectangle import area as rarea
from rectangle import perimeter
#aliases are necessary because both files a have a function named area

loop = True

while loop:
    option = int(input("Select an option:\n1.-Area of a circle\n2.-Circumference of a circle\n3.-Area of a rectangle\n4.-Perimeter of a rectangle\n5.-Exit\n"))
    if option == 1:
        radius = float(input("Please enter the radius of the circle\n"))
        print(f"The area of the circle is {carea(radius)}")
    if option == 2:
        radius = float(input("Please enter the radius of the circle\n"))
        print(f"The circumference of the circle is {circumference(radius)}")
    if option == 3:
        width = float(input("Please enter the width of the rectangle\n"))
        height = float(input("Please enter the height of the rectangle\n"))
        print(f"the area of the rectangle is {rarea(width, height)}")
    if option == 4:
        width = float(input("Please enter the width of the rectangle\n"))
        height = float(input("Please enter the height of the rectangle\n"))
        print(f"the perimeter of the rectangle is {perimeter(width, height)}")
    if option == 5:
        loop = False