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
        if self.check_funds(amount) is False:
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
        # NOTE THIS NEEDS TO USE THE check_funds METHOD # maybe this will satisfy the requirement b/c transfers calls on withdraw() which calls on check_funds()?
        transfer_result = False
        if self.withdraw(amount, f"Transfer to {category.category_name}") is True: # i think this may satisfy the use check_funds method for this method
            transfer_result = True
        category.deposit(amount, f"Transfer from {self.category_name}")
        return transfer_result

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
        ledger_output = ("*" * int((stars_needed / 2)))
        ledger_output = ledger_output + self.category_name
        ledger_output = ledger_output + ("*" * int((stars_needed / 2)))
        ledger_output = ledger_output.rstrip()

        # then, format the entries
        for i in self.ledger:
            # also need to provide total balance at the end of it
            description = i["description"][0:23]
            amount = i["amount"]
            if isinstance(amount, int):
                amount = str(amount) + ".00" # this seems to do the trick
            description_length = len(description)
            amount_lengh = len(str(amount))
            transaction = description + (" " * (30 - description_length - amount_lengh)) #total length of the line is 30 chars, w/ up to seven dedicated to the amt
            transaction = transaction + str(amount)
            transaction = transaction.rstrip()
            ledger_output = ledger_output + "\n" + transaction
            ledger_output = ledger_output.rstrip()
        balance = self.get_balance()
        ledger_output = ledger_output + "\n" + "Total: " + str(balance)
        ledger_output = ledger_output.rstrip()
        return ledger_output
            





def create_spend_chart(categories):
    import math
    # HEIGHT OF EACH BAR SHOULD BE ROUNDED DOWN TO NEAREST 10
    # BARS SHOULD BE BASED ON WITHDRAWALS ONLY

    # create a withdrawals list of each categories total withdrawal amt
    # calc the total withdrawals amongst all categories    
    withdrawals = []
    total_withdrawals = 0
    for i in categories:
        category_withdrawals = 0
        for item in i.ledger:
            amount = item.get("amount")
            if amount < 0:
                category_withdrawals = category_withdrawals + (amount * -1)
                total_withdrawals = total_withdrawals + (amount * -1)
        withdrawals.append(category_withdrawals)

    # next step is to take the amts, calc percentages, then create the bars
    # this will calc averages then round them down to the nearest 10
    averages = []
    for amount in withdrawals:
        percent = (amount / total_withdrawals) * 10
        percent = math.floor(percent) * 10 # not sure if i'm allowed to use libraries
        averages.append(percent)
    

    spend_chart = "Percentage spent by category" # top line
    # this builds the y-axis, and will also fill in the 'o''s 
    categories_length = len(categories)
    for i in range(100, -10, -10):
        # determine length of incoming #, then calc how many spaces are needed for formatting
        spend_chart = spend_chart + "\n" + " " * (3 - len(str(i))) + str(i) + "|"
        # now add to the other side of the line, the actual changing chart details
        spend_chart = spend_chart + " "
        for x in range(0, categories_length):
                if averages[x] >= i:
                    spend_chart = spend_chart + "o  "
                else:
                    spend_chart = spend_chart + "   " # spacing here may need tweaking

    spend_chart = spend_chart + "\n" + " " * 4
    for i in range(0, categories_length):
        spend_chart = spend_chart + "---"
    spend_chart = spend_chart + "-"
    spend_chart = spend_chart.rstrip()
    # next step is to create the descending category names
    longest_word = ""
    for word in categories: # determine the longest word
        for letter in word.category_name:
            if longest_word == "":
                longest_word = word.category_name
            elif len(word.category_name) > len(longest_word):
                longest_word = word.category_name # store the longest word in a variable so we can later get its length
    # now that the individual letters have been extracted, work on formatting and reconstructing the words vertically
    for i in range(0, len(longest_word)): # go down one line per letter in the longest word
        spend_chart = spend_chart + "\n" + " " * 5 # make the spaces need before first letter
        for word in categories:
            try:
                spend_chart = spend_chart + word.category_name[i] + "  " # for each word, add the word, plus 2 spaces afterward
            except IndexError:
                spend_chart = spend_chart + "   " # however, if there are no more letters to print, just add 3 spaces
            

    return spend_chart

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
print(create_spend_chart([food, clothing, auto]))
#create_spend_chart(food)