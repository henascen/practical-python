# pcost.py
#
# Exercise 1.27
from os import replace
import sys
import csv
from report import read_portfolio

def portfolio_cost(filename):
    total_cost = 0
    portfolio_data =  read_portfolio(filename)
    total_cost = sum([stock.shares*stock.price for stock in portfolio_data])
            
    return total_cost

def main(argv):
    portfolio_cost_total = portfolio_cost(argv[1])
    print(f'Total cost: {portfolio_cost_total}')
    
if __name__ == '__main__':
    import sys
    main(sys.argv)