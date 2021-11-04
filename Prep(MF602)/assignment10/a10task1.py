#
# a9task1.py (Assignment 9, Problem 1)
## Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: Writing SQL Queries
# 
#



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Starter code for assignment 12.

@author: azs
"""
import sqlite3 as db
import pandas as pd


# These queries will help you discover the database schema (structure).

example_0a = '''SELECT name FROM sqlite_master'''
example_0b = '''pragma table_info(clients)'''
example_0c = '''pragma table_info(trades)'''
example_0d = '''pragma table_info(price_history)'''


# This is an example query that you can use to get started:
## QUERY 00 SHOW ALL CLIENTS IN DATABASE
sql_00 = '''
SELECT * 
FROM clients
'''

sql_01 = '''
SELECT * 
FROM price_history
WHERE date = '2020-12-31'
ORDER BY security
'''

sql_02 = '''
SELECT *
FROM trades
WHERE client_id = '4'
ORDER BY trade_date
'''

sql_03 = '''
SELECT * 
FROM trades
WHERE trade_date BETWEEN '2018-01-01' AND '2018-12-31'
ORDER BY trade_date

'''

sql_04 = '''
SELECT trades.security, COUNT(trades.quantity)
FROM trades
GROUP BY trades.security
ORDER BY security
'''

sql_05 = '''
SELECT clients.first_name, clients.last_name, COUNT(trades.quantity) as count
FROM trades 
INNER JOIN clients ON trades.client_id = clients.client_id 
GROUP BY trades.client_id
ORDER BY 3 DESC
'''

sql_06 = '''
SELECT trades.trade_date, trades.security,trades.quantity,clients.first_name, clients.last_name
FROM trades 
INNER JOIN clients ON trades.client_id = clients.client_id 
WHERE trades.security = 'CSCO'
ORDER BY trades.trade_date
'''

sql_07 = '''
SELECT trades.trade_date, clients.first_name, clients.last_name,  trades.security,trades.quantity
FROM trades 
INNER JOIN clients ON trades.client_id = clients.client_id 
WHERE trades.trade_date BETWEEN '2019-01-01' AND '2019-12-31'
ORDER BY trades.trade_date
'''

sql_08 = '''
SELECT trades.trade_date, trades.security,trades.quantity, price_history.price
FROM trades 
INNER JOIN price_history ON trades.trade_date = price_history.date AND trades.security = price_history.security
WHERE trades.client_id = '4'
ORDER BY 1 ASC
'''

sql_09 = '''
SELECT trades.security, SUM(trades.quantity) as quantity, price_history.price, SUM(trades.quantity) * price_history.price AS value
FROM trades
INNER JOIN price_history ON price_history.date = '2020-12-30' AND trades.security = price_history.security
WHERE trades.client_id = '4' 
GROUP BY trades.security
ORDER BY 4 DESC

'''


sql_10 = '''
SELECT trades.trade_date, trades.security, trades.quantity, price_history.price AS purch_price, trades.quantity * price_history.price AS cost
FROM trades
INNER JOIN price_history  ON  trades.trade_date = price_history.date AND trades.security = price_history.security

WHERE trades.client_id = '4' 
GROUP BY trades.security
ORDER BY 2 ASC


'''



################################################################################
if __name__ == '__main__':
    
    # obtain a database connection:
    con=db.connect("./portfolio.db")
    
    # set some options to display enough columns of output
    pd.set_option('display.width', 320)
    pd.set_option('display.max_columns',10)
    
    
    # Ask Pandas to run a query and return the resulting data set as a pd.DataFrame object:
    # print(pd.read_sql(example_0c, con=con))
    # print()
    
    # Ask Pandas to run a query and return the resulting data set as a pd.DataFrame object:
    print(pd.read_sql(sql_10, con=con))
    print()        