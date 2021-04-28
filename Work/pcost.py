# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(filename):
    purchase_prices = []
    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.rstrip("\n").split(',')
            purchase_prices.append(float(row[2])*int(row[1]))
    return sum(purchase_prices)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print("Total cost ", cost)