# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    '''Opens a given portfolio and reads it into a list of tuples'''
    portfolio = []
    portfolio_dict = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio_dict['name'] = holding[0]
            portfolio_dict['shares'] = holding[1]
            portfolio_dict['price'] = holding[2]
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

