# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    '''Opens a given portfolio and reads it into a list of tuples'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio_dict = { 
                'name': holding[0],
                'shares': holding[1],
                'price': holding[2],
            }
            portfolio.append(portfolio_dict)
    return portfolio

def read_prices(filename):
    '''Opens the prices file reads it as a dictionary'''
    prices_dict = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                if row:
                    prices_dict[row[0]] = float(row[1])
            except:
                print("Empty row")
    return prices_dict

def compute_change(filename_portfolio, filename_prices):
    portfolio_info = read_portfolio(filename_portfolio)
    prices_info = read_prices(filename_prices)

    for stock in portfolio_info:
        stock_name = stock["name"]
        stock["new_price"] = prices_info[stock_name]
        change = stock["new_price"] - stock["price"]
        stock["change"] = change
    
    return portfolio_info

def make_report(portfolio_info):
    report = []
    for stock in portfolio_info:
        report.append((stock['name'], stock['shares'], stock['new_price'], stock['change']))
    return report

def visualize_change(report):

    print(f'      Name     Shares      Price     Change')
    print(f'---------- ---------- ---------- ----------') 

    for name, shares, price, change in report:
        price = '$' + f'{price:.2f}'
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')