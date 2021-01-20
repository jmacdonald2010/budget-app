class Category:
    # some stuff here

    # x = 0 # not sure if this is needed
    ledger = []

    def __init__(self, category_name):
        self.category_name = category_name
    
    def deposit(self, amount, description=""):
        # function goes here
        # this might be all this needs? not yet tested 1/19/21 2200
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        # function go here
        # step one, calculate if the amt input into this method would cause the ledger amount to go negative
        # might be it? not yet tested 1/19/21 2200
        balance = self.get_balance()
        if balance < 0:
            return False
        else:
            amount = amount * -1
            self.ledger.append({"amount": amount, "description": description})
            return True

    def get_balance(self):
        # no inputs, just gets the current get_balance
        balance = 0 
        for i in self.ledger:
            balance = balance + i["amount"]
        return balance

    def transfer(self, amount, category):
        # function go here
        # NOTE THIS NEEDS TO USE THE check_funds METHOD
        self.withdraw(amount, f"Transfer to {category}") # i think this may satisfy the use check_funds method for this method
        category.deposit(amount, f"Transfer from {self.category_name}") # i have no idea if this works like this or not, just kinda guessing

    def check_funds(self, amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        else:
            return True

    def __str__(self):
        # use this to return the formatted ledger?
        pass # temporary until i write this function



def create_spend_chart(categories):
    # some other stuff
    # calc how many *'s need to be used w/ the category name (top line only 30 characters)
    # this code actually shouldn't go here
    # this should be in the budget class, and is printed when the budget object is printed 
    # plus more than this
    category_length = len(categories)
    stars_needed = 30 - category_length
    title_line = ("*" * int((stars_needed / 2)))
    title_line = title_line + categories
    title_line = title_line + ("*" * int((stars_needed / 2)))
    return title_line.rstrip()

