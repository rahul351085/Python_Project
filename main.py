from login_page import *
from register import *
from jeans_items import *
from payment import *
from booking import *
class Home_Page():
        def home(self,option=None):
            print("Welcome, please select an option")
            option = input("1. Signup: | 2. Login:")
            if option == "1":
                call = registration()
                call.register()
            elif option == "2":
                call = login()
                call.gainAccess()
            else:
                print("Please enter a valid parameter, this is case-sensitive")

        def HomePage(self):
            check = True
            while (check):
                print("WELCOME".center(100, '='), "\n")

                print("1.Jeans Items")
                print("2.BOOKING DETAILS")
                print("3.PAYMENT")
                print("4.Logout")
                choice = int(input("Choose Any Option:"))

                if (choice == 1):
                    h = jeans_items()
                    h.upanddown()
                    h.get_details()

                elif choice == 3:
                    p = Payment()
                    p.get_details()

                elif choice == 2:
                    b = BookingDetails()
                    b.get_details()
                    p = Payment()
                    p.get_details()
                    print("\n")
                    print("Terms and conditions".center(100, '*'))
                elif choice == 4:
                    # check=False
                    exit()






call = Home_Page()
call.home()
call.HomePage()