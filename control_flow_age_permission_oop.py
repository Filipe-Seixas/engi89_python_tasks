class CheckRights:

    def __init__(self, age, dr_license):
        self.age = age
        self.license = dr_license

    def vote_drive(self):
        if self.age >= 18 and self.license == 'True':
            return "You can vote and drive."
        else:
            return "Sorry, you can't vote and drive."

    def vote(self):
        if self.age >= 18:
            return "You can vote."
        else:
            return "Sorry, you can't vote."

    def drive(self):
        if self.license == 'True':
            return "You can drive."
        else:
            return "Sorry, you can't drive."

    def drink(self):
        if self.age >= 16:
            return "You can drink."
        else:
            return "you can't legally drink but your mates/unties might have your back."

    def check_if_young(self):
        if self.age < 16:
            return "You're too young, go back to school!"
        else:
            return "You're at least 16."


while True:
    age = int(input("Tell me your age:  "))
    license_answer = input("You have a driver's license. (True/False):  ")
    chk_rights = CheckRights(age, license_answer)
    rights = int(input("Which rights do you want to check?\n"
                       "1 - Vote and Drive\n"
                       "2 - Vote\n"
                       "3 - Drive\n"
                       "4 - Drink\n"
                       "5 - Check if you're too young\n"
                       "6 - Exit\n"))
    if rights == 1:
        print(chk_rights.vote_drive())
    elif rights == 2:
        print(chk_rights.vote())
    elif rights == 3:
        print(chk_rights.drive())
    elif rights == 4:
        print(chk_rights.drink())
    elif rights == 5:
        print(chk_rights.check_if_young())
    elif rights == 6:
        break

