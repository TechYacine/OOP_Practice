
class Bank_account : 
    def __init__(self, num_account, sold, sign_in_day, name):
        self.num_account = num_account
        self.sold = sold
        self.sign_in_day = sign_in_day
        self.name = name

    def payment(self, pay):
        self.sold += pay
        print(f"You're total sold is {self.sold}$ ")

    def withdrawal(self, amount):
        if amount > self.sold or amount < 0:
            print("You can't withdrew this amount ,You have not enough money ")
        else :
            self.sold -= amount 
            print(f"You have withdrew {amount}$ , you have now {self.sold}$ remaining ")

    def verify_balance(self):
        print(f"verification : of {self.name} bank account")
        print(f"number of the acount : {self.num_account}")
        print(f"signed in {self.sign_in_day}")
        print(f"Your total amount is {self.sold} $")


account = Bank_account(1334, 34000, "12-4-2020", "Dragon")
account1 = Bank_account(1343, 35000, "12-4-2021", "Dragon1")
account2 = Bank_account(1356, 36000, "12-4-2022", "Dragon2")

account.payment(2300)
account.withdrawal(5600)
account.verify_balance()

print("--------------") 

account1.payment(200)
account1.withdrawal(560000)
account1.verify_balance()

print("--------------------")

account2.payment(210000)
account2.withdrawal(31230)
account2.verify_balance()