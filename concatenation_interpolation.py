# -- Version 1 -- #

# define a variable name, and assign a string
name = ""
# re assign the original variable with your name
name = input("What's your name?  ")
# use concatenation to print a welcome message and use methods to format the name/input (remove white spaces)
print("Hello" + " " + name.capitalize())

# -- Version 2 -- #

# define another variable full_name to a random string
full_name = ""
# re assign the variable full_name to a name
full_name = input("What's your full name?  ")
first_name = full_name.split()[0]
last_name = full_name.split()[1]
# use interpolation to print the message
print(f"Hello {first_name.capitalize()} {last_name.capitalize()}")
