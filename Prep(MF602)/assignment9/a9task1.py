#
# a9task1.py (Assignment 9, Problem 1)
## Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: Backtesting a Trading Strategy
# 
#
import pandas as pd

# function 1
def create_bollinger_bands(df, window =21, no_of_std = 1,column_name= ''):
    """The function returns a pandas.DataFrame with the same index as the parameter df, containing the columns: ['Observations', 'RollingMean', 'LowerBound', 'UpperBound']
    """
    # df.index = pd.to_datetime(df['Date']) 
    # y = df.index
  

    # index = pd.date_range(start=y[0], end = y[-1])

    # df2 = pd.DataFrame(index = index)
    index = df.index
    df2 = pd.DataFrame(index = index, columns = ['Observations','RollingMean','UpperBound','LowerBound'])

    if column_name == '':
        column_name_list = df.iloc[:,0]
    
    else:
        column_name_list = df[column_name]

    df2['Observations'] = column_name_list
     

    rolling_std = df2['Observations'].rolling(window).std()
    rolling_mean =df2['Observations'].rolling(window).mean()
    
    df2['RollingMean'] = df2['Observations'].rolling(window).mean()
    df2['UpperBound'] = rolling_mean + (rolling_std * no_of_std)
    df2['LowerBound'] = rolling_mean - (rolling_std * no_of_std)
    
    return df2
    
    

# function 2

def create_long_short_position(df):
    """The function will return a new pandas.DataFrame object with the same index as the parameter df, containing a column Position.
    """
    # df.index = pd.to_datetime(df['Date']) 
    index = df.index
    df2 = pd.DataFrame(index = index, columns = ['Position'])
    
    Position = pd.Series(index = df2.index, data = 0)
    
    for i in range(0,len(df2)):
    
        if df['Observations'].iloc[i] > df['UpperBound'].iloc[i]:
            Position[i] = 1           # BUY
        elif df['Observations'].iloc[i] < df['LowerBound'].iloc[i]:
            Position[i] = -1  
        else:
            Position[i] = Position[i-1]
    
    df2['Position'] = Position
    
    return df2



# function 3
def calculate_long_short_returns(df,position,column_name = ''):
    """returns a pandas.DataFrame object containing the columns ['Market Return', 'Strategy Return', and 'Abnormal Return']
    """
    index = df.index
    df2 = pd.DataFrame(index = index, columns = ['Market Return', 'Strategy Return', 'Abnormal Return'])

    if column_name == '':
        column_name_list = df.iloc[:,1]
    
    else:
        column_name_list = df[column_name]
    
    mrt = column_name_list / column_name_list.shift(1) - 1

    Position = position['Position'] 
    sr = mrt * Position

    df2['Market Return'] = mrt
    df2['Strategy Return'] =  sr
    df2['Abnormal Return'] = df2['Strategy Return'] - df2['Market Return']
    
    return df2


# function 4
def plot_cumulative_returns(df):
    """create a plot of the cumulative return for each column in the parameter df, a pandas.DataFrame object with one or more series of returns. The function does not return any values.
    """
    # y = df.index
    # index = pd.date_range(start=y[0], end = y[-1])
    # df2 = pd.DataFrame(index = index)
    
    # cumu_mr = df.['Market Return']
    df = df.fillna(method = 'ffill')
    df[['Market Return','Strategy Return','Abnormal Return',]].cumsum().plot(title = 'Cumulative Returns')













if __name__ == '__main__':
    df = pd.read_csv('SPY.csv')
    df.index = df['Date']
    # df = pd.DataFrame(index=df.index, data = df['Close'])
    # df.index = pd.to_datetime(df['Date']) 
    df = df.loc['2017-01-01':'2017-12-31']
    df.tail()
    
    bb = create_bollinger_bands(df, window = 10, no_of_std = 2, column_name = 'Adj Close')
    position = create_long_short_position(bb)
    returns = calculate_long_short_returns(df, position, 'Adj Close')
    plot_cumulative_returns(returns)