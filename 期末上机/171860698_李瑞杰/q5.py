# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:00:25 2019

@author: 12613
"""
def function(a,b,c,x):
    return int(a*x*x+b*x+c)

def countfx(n,m,fx_ary):
    temp_ary=[]
    for i in range(n):
        x0=round(-1*fx_ary[i][1]/2*fx_ary[i][0])
        temp_ary.append(function(fx_ary[i][0],fx_ary[i][1],fx_ary[i][2],x0))
        k=1
        for j in range(m): 
            x1=round(-1*fx_ary[i][1]/2*fx_ary[i][0])+k
            x2=round(-1*fx_ary[i][1]/2*fx_ary[i][0])-k
            temp_ary.append(function(fx_ary[i][0],fx_ary[i][1],fx_ary[i][2],x1))
            temp_ary.append(function(fx_ary[i][0],fx_ary[i][1],fx_ary[i][2],x2))
            k+=1
    temp_fu=sorted(filter(lambda x:x<0,temp_ary))
    temp_zheng=sorted(filter(lambda x:x>=0, temp_ary))
    final=temp_fu+temp_zheng
    for i in range(m):
        print(final[i],end=' ')

def main():
    n,m=input().split()
    a = []
    for i in range(int(n)):
        a.append(list(map(int, input().rstrip().split())))
    countfx(int(n),int(m),a)
    
    
main()