class Category:
    def __init__(self, description):
        self.description = description
        self.ledger = list()
        self.balance = 0.0

    def __repr__(self):
        hdr = self.description.center(30, "*") + "\n"
        ledger = ""
        for i in self.ledger:
            # Description and amount formatting
            line_description = "{:<23}".format(i["description"])
            line_amount = "{:>7.2f}".format(i["amount"])

            # Ledger description truncation
            ledger += "{}{}\n".format(line_description[:23], line_amount[:7])

        total = "Total: {:.2f}".format(self.balance)
        return hdr + ledger + total

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance = self.balance + amount

    def withdraw(self, amount, description=""):
        if self.balance - amount >= 0:
            self.ledger.append({"amount": -1 * amount, "description": description})
            self.balance = self.balance - amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category_instance):
        if self.withdraw(amount, "Transfer to {}".format(category_instance.description)):
            category_instance.deposit(amount, "Transfer from {}".format(self.description))
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False


def create_spend_chart(categories):
    amount_spent = list()

    # Total spent for each category
    for category in categories:
        spent = 0
        for i in category.ledger:
            if i["amount"] < 0:
                spent = spent + abs(i["amount"])
        amount_spent.append(round(spent, 2))

    # Calculating % --> round down to the nearest 10
    total = round(sum(amount_spent), 2)
    percentage_spent = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), amount_spent))

    # Creating the bar chart substrings
    hdr = "Percentage spent by category\n"

    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart = chart + str(value).rjust(3) + "|"
        for percent in percentage_spent:
            if percent >= value:
                chart = chart + " o "
            else:
                chart = chart + "   "
        chart = chart + " \n"

    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    descriptions = list(map(lambda category: category.description, categories))
    length_max = max(map(lambda description: len(description), descriptions))
    descriptions = list(map(lambda description: description.ljust(length_max), descriptions))
    for x in zip(*descriptions):
        footer = footer + "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (hdr + chart + footer).rstrip("\n")


# # Instantiate Category objects
# food_category = Category("Food")
# clothing_category = Category("Clothing")
# auto_category = Category("Auto")
#
# # Perform operations on the categories
# food_category.deposit(1000, "initial deposit")
# food_category.withdraw(10.15, "groceries")
# food_category.withdraw(15.89, "restaurant and more food")
# food_category.transfer(50, clothing_category)
#
# clothing_category.deposit(500, "initial deposit")
# clothing_category.withdraw(25.55, "shoes")
# clothing_category.transfer(75, auto_category)
#
# auto_category.deposit(100, "initial deposit")
# auto_category.withdraw(30, "fuel")
#
# # Print the categories
# print(food_category)
# print(clothing_category)
# print(auto_category)
#
# # Create and print the spend chart
# categories = [food_category, clothing_category, auto_category]
# spend_chart = create_spend_chart(categories)
# print(spend_chart)
#
