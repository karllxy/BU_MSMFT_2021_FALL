# 
# homework6-2.py 
# Name: Xuyang Liu
# Email address: xyangliu@bu.edu
# Description: 2.Portfolio Optimization
#              
#

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from pandas_datareader import data
from sklearn import linear_model
from sklearn.metrics import mean_squared_error as MSE
from statsmodels.tsa.ar_model import AR
import statsmodels.api as sm
from homework6 import *


#(a) Calculate the annualized returns.

def annul(df):
    return df.mean() * 252

#(b)  calculate the weights of the unconstrained mean-variance optimal portfolio.

def weights(annreturn, covmat):
    cinv = pd.DataFrame(np.linalg.inv(covmat),covmat.columns, covmat.index)
    return  0.5 * np.matmul(cinv,annreturn)
    
# (c)     
def expreturn(annreturn,sigma):
    exp = pd.DataFrame(index = annreturn.index)
    exp['exp'] = 0
    for i in range(len(annreturn)):
        z = np.random.normal()
        exp.iloc[i,0] = annreturn[i] + sigma * z
        
        
    return exp

def optimalport(weight,covmat,expreturn):
    weightT = weight.T
    return np.matmul(weightT,expreturn)- np.matmul(np.matmul(weightT,covmat),weight)



def stable(sigma,t,df,covmat):
    annreturn = annul(df)
    table = pd.DataFrame(index = annreturn.index)
    
    for i in range(t):
        exp = expreturn(annreturn,sigma)
        w = weights(exp,covmat)
        table = pd.concat([table,w],axis=1)
    
    return table.std(axis=1)
        
        
# def plotstable(sigma,t,df,covmat,):
    
#     for i in range()

# (d) (e)
def regcovmat(df,covmat,delta):
    var = df.var()
    diag = pd.DataFrame(index = annreturn.index, columns = df.columns,data=0)
    for i in range(len(var)):
        diag.iloc[i,i]=var[i]
        
    return delta * diag + (1-delta) * covmat
    

#(f)Try different values of δ between 0 and 1 and perform eigenvalue decomposition on the regularized covariance matrix.

def eigenreg(df,covmat):
    for i in np.arange(0,1,0.1):
        reg = regcovmat(df,covmat,i)
        eigenvalue, eigenvector = np.linalg.eig(reg)
        print(eigenvalue)

#(g)Repeat the exercise in (2.c) with the regularized covariance matrix for a few values of δ

def optana(annreturn,sigmalist,df):
    lst = pd.DataFrame()
    for j in sigmalist:
        
        r = []
        rindex = []
        for i in np.arange(0,1,0.1):
            reg = regcovmat(df,covmat,i)
            exp = expreturn(annreturn,j)
            w = weights(exp,reg)
            opt = optimalport(w,reg,exp)
            r += [opt[0]]
            rindex += [i]
            
            # print('Sigma ='+ str(sigma)+' Delta = '+str(i))
            # print('result=' +str(opt))
        r = pd.DataFrame(r,index=rindex)
        lst = pd.concat([lst,r],axis=1)
    lst.columns = sigmalist
    
    return lst
        
    
        
def stable2(sigma,t,df,covmat,delta):
    reg = regcovmat(df,covmat,delta)
    return stable(sigma,t,df,reg)
    








if __name__ == '__main__':
    
    stocks = ['XLB','XLE','XLF','XLI','XLK','XLP','XLU','XLV','XLY']
    source = 'yahoo'
    start_dates = '01-01-2010'
    end_dates = '07-12-2021'
    adj = collect_data(stocks, source, start_dates, end_dates)
    df = returns(adj)
    covmat = covmat(df)
    annreturn = annul(df)
    weight = weights(annreturn, covmat)
    
    # expreturn1 = expreturn(annreturn,0.005)
    # expreturn2 = expreturn(annreturn,0.01)
    # expreturn3 = expreturn(annreturn,0.05)
    # expreturn4 = expreturn(annreturn,0.1)
    # weight1 = weights(expreturn1,covmat)
    # weight2 = weights(expreturn2,covmat)
    # weight3 = weights(expreturn3,covmat)
    # weight4 = weights(expreturn4,covmat)
    # # print('the result are ' +str(weight1)+' '+str(weight2)+' '+str(weight3)+' '+str(weight4))
    # opt1 = optimalport(weight1,covmat,expreturn1)
    # opt2 = optimalport(weight2,covmat,expreturn2)
    # opt3 = optimalport(weight3,covmat,expreturn3)
    # opt4 = optimalport(weight4,covmat,expreturn4)
       
    # #(e)
    # reg = regcovmat(df,covmat,1)
    
    
    # np.linalg.eig(reg)
    # np.linalg.matrix_rank(reg)
    # eigenreg(df,covmat)
    # opte= optana(annreturn,[0.005,0.01,0.05,0.1],df)
    # a =stable(0.005,10,df,covmat)
    # b= stable2(0.005,10,df,covmat,0.1)
    # c= stable2(0.005,10,df,covmat,0.2)
    
    
    
    
