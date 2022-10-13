import random
import string


class Payment():

    def __init__(self):
        self.amount = input("Enter Payment amount: ")
        self.confirm = "Book your Jeans Iteams"
        self.T_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(15)])
        self.p_status = "successful"

    def get_details(self):
        print("\n", "Welcome to Payment Page".center(60, '*'), "\n")
        print("Payment Amount: ", self.amount)
        # print(self.confirm ,"by clicking here")
        # print("\n","After Payment click Here","\n")
        print("Transaction ID: ", self.T_id)
        print("Transaction Status: ", self.p_status)





