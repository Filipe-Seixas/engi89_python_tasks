from datetime import datetime, date

# # define the variables age and name
# age = input("Please enter your age:  ")
# name = input("Please enter your name:  ")
# # make a calculation for the year in which the person was born
# year_of_birth = 2021 - int(age)  # This isn't exact due to not accounting for months
# # print out "OMG <person>, you are <age> years old so you were born in <year>" with the correct values
# print(f"OMG {name}, you are {age} years old so you were born in {year_of_birth}")
#
# # --- Second Part --- #
#
# # prompt the user for input and re-assign the variable age and name
# age = input("Please enter your age:  ")
name = input("Please enter your name:  ")
# figure out a way to account for if the persons birthday has already happened this year or not

# We ask for the users input but we need to ensure the formatting is right and convert the string into datetime
date_of_birth = datetime.strptime(input("Please enter your date of birth (dd mm yyyy):  "), "%d %m %Y")


# Function to calculate the age based on the user's date of birth
def age_calc(dob):
    today = date.today()  # Define today
    # Calculate age by subtracting the years like in the First Part but also take into account
    # whether the dob month is bigger than today's month
    if dob.month > today.month:
        # if the birth month is bigger, that means they haven't had their birthday
        # so we need to subtract 1 to the age
        return today.year - dob.year - 1
    else:
        return today.year - dob.year


# Call function to calculate age
age = age_calc(date_of_birth)

# Output the calculated age
print(f"Hello, {name.capitalize()}. You are {age} years old.")

# Extra
# go look into the library time
# print out the amount of hour this person has lived
hours = age * int(8760) # how many hours in a year
print(f"You are {hours} hours old")
