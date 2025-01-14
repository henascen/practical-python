# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv
import stock
import tableformat

def read_portfolio(filename):
    '''Opens a given portfolio and reads it into a list of tuples'''
    with open(filename) as lines:
        portdict  = parse_csv(lines, select=['name','shares','price'], types=(str, int, float))
    portfolio = [stock.Stock(d['name'], d['shares'], d['price']) for d in portdict]
    return portfolio

def read_prices(filename):
    '''Opens the prices file reads it as a dictionary'''
    prices_dict = {}
    with open(filename) as lines:
        prices_dict = dict(parse_csv(lines, types=(str, float), has_headers=False))
    return prices_dict

def compute_change(filename_portfolio, filename_prices):
    portfolio_info = read_portfolio(filename_portfolio)
    prices_info = read_prices(filename_prices)

    report = []

    for stock_unit in portfolio_info:
        stock_name = stock_unit.name
        stock_new_price = prices_info[stock_name]
        change = stock_new_price - stock_unit.price
        stock_change = change
        report.append((stock_unit.name, stock_unit.shares, stock_unit.price, stock_change))
    
    return report

def visualize_change(report, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    #print(f'      Name     Shares      Price     Change')
    #print(f'---------- ---------- ---------- ----------') 

    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)
        #price = '$' + f'{price:.2f}'
        #print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')

def portfolio_report(portfolio, prices, fmt):
    portfolio_details = compute_change(portfolio, prices)
    
    formatter = tableformat.create_formatter(fmt)
    visualize_change(portfolio_details, formatter)

def main(argv):
    print(argv)
    portfolio_report(argv[1], argv[2], argv[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)