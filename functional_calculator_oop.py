# This file is part of the calculator_oop.py Task
# import Calculator class so we can inherit from it
from calculator_oop import Calculator

import math


# Create class that inherits from Calculator
class FuncCalculator(Calculator):

    # Calculate area of circle (pi*radius^2) and round to 2 decimal points
    def area_of_circle(self, radius):
        area = math.pi * (radius ** 2)
        return round(area, 2)

    def area_of_square(self, side):
        return side ** 2

    def area_of_triangle(self, height, base):
        return (height * base) / 2


functional = FuncCalculator()
print(functional.area_of_circle(5))
print(functional.area_of_square(3))
print(functional.area_of_triangle(5, 8))
# Methods inherited from Calculator class still work, but aren't automatically ran because of __name__ on other file
print(functional.Add(1, 5))
