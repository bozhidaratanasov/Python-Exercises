class Account:
    def __init__(self, id, name, *args):
        self.id = id
        self.name = name
        self.balance = 0
        if args:
            self.balance = args[0]

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount > self.balance:
            return "Amount exceeded balance"
        self.balance -= amount
        return self.balance

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"