import pandas as pd

filename = 'AMZN.csv'
df = pd.read_csv(filename)

#df.head()
#de.tail()





#df.iloc[0] #indexing by numeric index
#df.iloc[0:4]




# set the date as index

df.index = pd.to_datetime(df['Date']) 
df.loc['2020-03-02':'2020-03-06']
 

# obtain a single column

prices = df['Adj Close']
prices[0]
prices.loc['2020-03-02']
prices['2020-03-02']


rel_prices = prices / prices[0] # divide all prices by first day price
# rel_prices.plot()


# prices[1] / prices[0] - 1
# prices[2] / prices[1] - 1

returns = prices.shift(-1) / prices -1 # prices / prices.shift(1) - 1
# returns.plot()

# returns.describle()
# #count    1257.000000
# mean        0.001330
# std         0.018537
# min        -0.079221
# 25%        -0.007129
# 50%         0.001431
# 75%         0.010561
# max         0.132164
# Name: Adj Close, dtype: float64
 







##  EXTRACT A SUBSET OF THE DATE (BY DATE)
index = pd.date_range(start='2020-01-01', end = '2021-01-01')
df2 = pd.DataFrame(index = index)



##  EXTRACT ONLY ADJ CLOSE PRICE
df2['price'] = df['Adj Close']

df2 = df2.fillna(method = 'ffill') # fill with prev numeric value

##  CACULATE THE AVERAGE PRICE
df2['rm'] = df2['price'].rolling(30).mean() # rm for 'rolling mean'

##  COMPARE PRICE  VS  ROLLING AVERAGE
## Trading rule: if price cross below rollling mean :SELL
##               if price cross above rolling mean :BUY !

# +1 buy, -1 sell
signal = pd.Series(index = df2.index, data = 0)

# go thorough each day and set the signal:
# for i in range(0,len(df2)):
    
#     if df2['price'].iloc[i] > df2['rm'].iloc[i]:
#         signal[i] = 1           # BUY
#     else:
#         signal[i] = -1
        
for i in range(0,len(df2)):
    
    if df2['price'].iloc[i-1] > df2['rm'].iloc[i]:
        signal[i] = 1           # BUY
    else:
        signal[i] = -1      


# add signal into the dataframe

df2['signal'] = signal



long_returns = df2['price'] / df2['price'].shift(1) -1
df2['mkt_ret'] = long_returns

strategy_returns = long_returns * signal
df2['str_ret'] = strategy_returns

# abnormal return
df2['abn_ret'] = df2['str_ret'] - df2['mkt_ret']


df2[['mkt_ret','str_ret','abn_ret',]].cumsum().plot(title = 'Cumulative Returns')





























 