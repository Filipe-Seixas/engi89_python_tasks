# Core:
# Write a program that prints the numbers from 1 to 100. For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz" instead of the number For numbers which are multiples of both three and five
# print "FizzBuzz".

for num in range(1, 101):  # for number starting from 1 and ranging to 100 (not counting 101)
    if num % 3 == 0:
        print(f"{num} is Fizz")
    elif num % 5 == 0:
        print(f"{num} is Buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print(f"{num} is FizzBuzz")

# Extra:
# make a new fizzbuzz file and make it functional make it so we can decide which numbers to substitute for fizz and
# buzz using functions
#
# Hint: loop, range, control flow

number = int(input("Please enter a number: "))
is_fizz = number % 3 == 0
is_buzz = number % 5 == 0
if is_fizz and is_buzz:
    print(f"{number} is FizzBuzz")
elif is_fizz:
    print(f"{number} is Fizz")
elif is_buzz:
    print(f"{number} is Buzz")
else:
    print(f"{number} is not Fizz or Buzz")
