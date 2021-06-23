# make a loop with a range that says hello 10 times
for x in range(10):  # for loop using range() function to loop through a sequence of numbers, in this case 10
    print("Hello")

# create another loop with a range that asks for names and appends to list names
names = []  # create empty list
for x in range(3):
    name = input("Tell me your name:  ")  # ask for name
    names.append(name)  # add name to list

# make a loop that iterated over each name in list_name and format's it into lowercase in a new variable called
# list_names_lower
list_names_lower = []  # create new empty list
for name in names:  # for each name inside the names list
    lower_name = name.lower()  # turn each name into lower case
    list_names_lower.append(lower_name)  # add name into list

# Iterate over the list of values to find if they are even
for name in names:
    if len(name) % 2 == 0:  # if the remainder of the characters in the string is zero, that means it is even
        print(f"{name} is even.")
    else:
        print(f"{name} is odd.")