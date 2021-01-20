class Category:
    # some stuff here

    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        # append the transaction to the ledger list
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        # check to see if funds are avail, if yes, then append to ledger as negative int, if no, return false
        # fix needed; instead of doing its own check balance return true/false, it needs to use the check_funds() to do that
        balance = self.get_balance()
        if (balance - amount) < 0:
            return False
        else:
            amount = amount * -1
            self.ledger.append({"amount": amount, "description": description})
            return True

    def get_balance(self):
        # returns current balance in ledger
        balance = 0 
        for i in self.ledger:
            balance = balance + i["amount"]
        return balance

    def transfer(self, amount, category):
        # NOTE THIS NEEDS TO USE THE check_funds METHOD
        self.withdraw(amount, f"Transfer to {category.category_name}") # i think this may satisfy the use check_funds method for this method
        category.deposit(amount, f"Transfer from {self.category_name}") # i have no idea if this works like this or not, just kinda guessing

    def check_funds(self, amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        else:
            return True

    def __str__(self):
        # use this to return the formatted ledger?
        # first, format the header
        category_length = len(self.category_name)
        stars_needed = 30 - category_length
        ledger = ("*" * int((stars_needed / 2)))
        ledger = ledger + self.category_name
        ledger = ledger + ("*" * int((stars_needed / 2)))
        ledger = ledger.rstrip()

        # then, format the entries
        for i in self.ledger:
            description = i["description"]
            amount = i["amount"]
            description_length = len(description)
            amount_lengh = len(str(amount))
            transaction = description + (" " * (30 - description_length - amount_lengh)) #total length of the line is 30 chars, w/ up to seven dedicated to the amt
            transaction = transaction + str(amount)
            transaction = transaction.rstrip()
            ledger = ledger + "\n" + transaction
            ledger = ledger.rstrip()
            





def create_spend_chart(categories):
    # some other stuff
    # calc how many *'s need to be used w/ the category name (top line only 30 characters)
    # this code actually shouldn't go here
    # this should be in the budget class, and is printed when the budget object is printed 
    # plus more than this
    print("coming soon")

# this code down here would be used in the main.py file for the assignment
# i just placed it here so i can can more easily debug the whole class

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

# commenting this out until i write this function
# print(create_spend_chart([food, clothing, auto]))