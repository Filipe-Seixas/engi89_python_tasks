# While true = true, meaning the loop is always running
while True:
    # Get user input for which rating they want
    rating = input("Hello, please choose a movie rating.  ")

    # if universal
    if rating.lower() == "universal":
        print("Universal rating: Everyone can watch.")
    # else if pg
    elif rating.lower() == "pg":
        print("PG: General viewing, but some scenes may be unsuitable for young children.")
    # else if 12
    elif rating.lower() == "12":
        print("Films classified 12A and video works classified 12 contain material that is not generally suitable for "
              "children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an "
              "adult.")
    # else if 15
    elif rating.lower() == "15":
        print("No one younger than 15 may see a 15 film in a cinema.")
    # else if 18
    elif rating.lower() == "18":
        print("No one younger than 18 may see an 18 film in a cinema.")
    # else if they type 'exit', print thank you message and exit program
    elif rating.lower() == "exit":
        print("Thank you for your business.")
        exit()
    # else if user types 'help', print list of valid ratings
    elif rating.lower() == "help":
        print("Valid ratings are: universal, pg, 12, 15, 18")
    # else if user types invalid ratings, print error message with help choice
    else:
        print("Sorry, invalid choice. Type 'help' for valid choices and 'exit' to exit")
