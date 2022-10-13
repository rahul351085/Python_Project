class jeans_items():

    def __init__(self):
        self.about_us = "\n We are providing world class facilities for booking of Jeans manufactuaring.And also you will get Jeans at \nlowest price from our website.So fell free to book Jeans at lowest rate and for any query pls contact to us "
        self.price = input("Enter How much you want: ")
        self.bookingtype = input("Enter Booking Type: ")
        print("Welcome to Jeans_Items".center(100, "*"), "\n")
        print("About US".center(100, "*"), self.about_us, "\n")

    def upanddown(self):
        self.order = input("Enter your order: ")
        self.destination = input("Enter Your full location: ")
        self.items = input("Enter Items: ")
        print("================================== Receipt ==================================")
        print("Your order: ", self.order)
        print("Your Location: ", self.destination)
        print("Your Items: ",self.items)

    def get_details(self):
        print("Booking price: ", self.price)
        print("Booking Type: ", self.bookingtype)

# h = jeans_items()
# h.upanddown()
# h.get_details()
# h.printonboarding()








