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
FROM trades
'''

sql_02 = '''
SELECT * 
FROM trades
WHERE security ='AAPL'
'''

sql_03 = '''
SELECT * 
FROM trades
WHERE security ='AAPL'
ORDER BY trade_date
'''

sql_04 = '''
SELECT first_name, last_name, SUM(quantity)
FROM trades
INNER JOIN clients ON trades.client_id = clients.client_id
WHERE security ='AAPL'
ORDER BY trade_date
'''

sql_05 = '''
SELECT SUM(quantity)
FROM trades
WHERE security ='AAPL'

'''

sql_06 = '''
SELECT first_name, last_name, trades.trade_date, trades.quantity
FROM trades
INNER JOIN clients ON trades.client_id = clients.client_id
WHERE security ='AAPL'
ORDER BY trade_date
'''

sql_07 = '''
SELECT first_name, last_name, SUM(quantity)
FROM trades
INNER JOIN clients ON trades.client_id = clients.client_id
WHERE security ='AAPL'
GROUP BY trades.client_id
'''

# SUM COUNT AVERAGE.....
# ORDER MATTERS
sql_08 = '''
SELECT first_name, last_name, SUM(quantity)
FROM trades
INNER JOIN clients ON trades.client_id = clients.client_id
WHERE security ='AAPL'
GROUP BY trades.client_id
ORDER BY 3 DESC
'''
################################################################################
if __name__ == '__main__':
    
    # obtain a database connection:
    con=db.connect("./portfolio.db")
    
    # set some options to display enough columns of output
    pd.set_option('display.width', 320)
    pd.set_option('display.max_columns',10)
    
    
    # Ask Pandas to run a query and return the resulting data set as a pd.DataFrame object:
    # print(pd.read_sql(example_0d, con=con))
    # print()
    
    # Ask Pandas to run a query and return the resulting data set as a pd.DataFrame object:
    print(pd.read_sql(sql_08, con=con))
    print()        
