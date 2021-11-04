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

sql = '''
SELECT * 
FROM trades
'''

sql = '''
SELECT * 
FROM trades 
WHERE security='AAPL' 
'''

sql = '''
SELECT * 
FROM trades 
WHERE security='AAPL' 
ORDER BY trade_date 
'''

sql = '''
SELECT trade_date, quantity
FROM trades 
WHERE security='AAPL' 
ORDER BY trade_date 
'''

sql_03= '''
SELECT clients.first_name, clients.last_name, 
        trades.trade_date, trades.quantity
FROM trades 
INNER JOIN clients ON trades.client_id = clients.client_id
WHERE trades.security='AAPL' 
ORDER BY trade_date 
'''

# an aggregate function: SUM, COUNT, AVERAGE, MIN, MAX
sql = '''
SELECT SUM(quantity)
FROM trades
WHERE security='AAPL'
'''

# an example using all of our keywords
# most of these are optional, but
# when present the order of clauses is important
sql_04 = '''
SELECT clients.first_name, clients.last_name, 
        SUM(trades.quantity)
FROM trades 
INNER JOIN clients ON trades.client_id = clients.client_id
WHERE trades.security='AAPL' 
GROUP BY trades.client_id
ORDER BY 3 DESC
'''

sql_06 = '''
SELECT trades.trade_date, trades.security,trades.quantity,clients.first_name, clients.last_name,
FROM trades 
INNER JOIN clients ON trades.client_id = clients.client_id 
WHERE trades.security = 'CSCO'
GROUP BY trades.client_id
ORDER BY trades.trade_date
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
    print(pd.read_sql(sql_06, con=con))
    print()    


    
