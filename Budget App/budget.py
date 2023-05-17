class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0

        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = format(item["amount"], ".2f").rjust(7)
            items += f"{description}{amount}\n"
            total += item["amount"]

        output = title + items + f"Total: {total:.2f}"
        return output


def create_spend_chart(categories):
    category_names = list()
    spent_percentages = list()
    spent_chart = "Percentage spent by category\n"

    for category in categories:
        total_spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total_spent -= item["amount"]
        spent_percent = total_spent / category.get_balance() * 100
        spent_percentages.append(spent_percent)
        category_names.append(category.name)

    for i in range(100, -10, -10):
        spent_line = str(i).rjust(3) + "| "
        for percent in spent_percentages:
            if percent >= i:
                spent_line += "o  "
            else:
                spent_line += "   "
        spent_chart += spent_line + "\n"

    spent_chart += "    " + "-" * (3 * len(category_names) + 1) + "\n"

    max_name_length = max(len(name) for name in category_names)

    for i in range(max_name_length):
        name_line = "    "
        for name in category_names:
            if i < len(name):
                name_line += name[i] + "  "
            else:
                name_line += "   "
        spent_chart += name_line.rstrip() + " \n"

    return spent_chart
