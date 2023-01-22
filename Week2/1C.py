"""Write a programme that prompts the user to enter the radius of a circle,
        - display the area of that circle
        - Hint: The area of a circle with radius "r" is π * r2,
        - where π (Pi) can be approximated very roughly as 22 divided by 7
"""
# Gives access to the underlying C library functions
import math
Radius = float(input("Hi User, Can you input the Radius of a Circle? "))
print(f"You entered... {Radius}")

# Formula Circle Area =  math.pi * to the power of inputted {Radius}
Area = math.pi * Radius**Radius
print("Area of the circle is :", Area)

