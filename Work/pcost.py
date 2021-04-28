# pcost.py
#
# Exercise 1.27
purchase_prices = []
with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.rstrip("\n").split(',')
        purchase_prices.append(float(row[2])*int(row[1]))

print("Total cost ", sum(purchase_prices))