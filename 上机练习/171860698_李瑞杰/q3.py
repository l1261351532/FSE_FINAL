# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 20:08:50 2019

@author: 12613
"""
def stocks(stock):
    stock.append(0)
    ans=0
    i=0
    while i<len(stock)-1:
        if stock[i]<stock[i+1]:
            buy=int(stock[i])
            for j in range(i+1,len(stock)-1):
                if stock[j]>stock[j+1]:
                    sold=int(stock[j])
                    ans=ans+sold-buy
                    i=j
                    break
        i+=1
    print(ans)
stocks([7,6,4,3,1])