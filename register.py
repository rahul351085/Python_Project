import bcrypt
from login_page import *
class registration:
    def __init__(self,Username=None, Password1=None, Password2=None):
        self.Username = Username
        self.Password1=Password1
        self.Password2=Password2
    def welcome(self):
        print("Welcome to your dashboard")

    def register(self):
        Username = input("Enter a username:")
        Password1 = input("Create password:")
        Password2 = input("Confirm Password:")
        db = open("database.txt", "r")
        d = []
        for i in db:
            a, b = i.split(",")
            b = b.strip()
            c = a, b
            d.append(a)
        if not len(Password1) <= 5:
            db = open("database.txt", "r")
            if not Username == None:
                if len(Username) < 1:
                    print("Please provide a username")
                    call = registration()
                    call.register()
                elif Username in d:
                    print("Username exists")
                    call = registration()
                    call.register()
                else:
                    if Password1 == Password2:
                        Password1 = Password1.encode('utf-8')
                        Password1 = bcrypt.hashpw(Password1, bcrypt.gensalt())

                        db = open("database.txt", "a")
                        db.write(Username + ", " + str(Password1) + "\n")
                        print("User created successfully!")
                        print("Please login to proceed:")
                        exit()





                    # print(texts)
                    else:
                        print("Passwords do not match")
                        call = registration()
                        call.register()
        else:
            print("Password too short")


