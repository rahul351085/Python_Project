import random
from datetime import date


class BookingDetails():
    def __init__(self):
        self.B_id = random.randint(100, 201)
        self.today = date.today()
        self.Name = input("Enter your Name:")
        self.age = input("Enter your Age:")
        self.gender = input("Enter your Gender:")
        self.contact = input("Enter your Contact No:")
        self.B_status = "confirmed"

    def get_details(self):
        print("\n", "Welcome to Booking Details".center(100, "*"))
        print("Booking Date: ", self.today)
        print("Name: ", self.Name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Contact: ", self.contact)
        print("Booking id: ", self.B_id)
        print("Booking Status: ", self.B_status)


