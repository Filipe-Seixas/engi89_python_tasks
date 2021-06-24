# This file is part of the functional_calculator_oop.py Task
# Create a class called Calculator
class Calculator:

    def Add(self, num1, num2):
        return num1 + num2

    def Subtract(self, num1, num2):
        return num1 - num2

    def Multiply(self, num1, num2):
        return num1 * num2

    def Divide(self, num1, num2):
        return num1 / num2


# We need this conditional check so that the code doesn't run automatically when we import it on another file
if __name__ == "__main__":
    # Create calculator object
    calc = Calculator()
    # Use object to call methods
    print(calc.Add(1, 2))
    print(calc.Subtract(1, 2))
    print(calc.Multiply(1, 2))
    print(calc.Divide(1, 2))

# Here we can see that __name__ is main when ran from here directly, but calculator_oop when imported on another file
# print(__name__)
