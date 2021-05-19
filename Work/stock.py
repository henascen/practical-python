class Stock:

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'
    
    def sell(self, number):
        self.shares -= number
        return self.shares

    def cost(self):
        self.cost_number = float(self.shares*self.price)
        return self.cost_number