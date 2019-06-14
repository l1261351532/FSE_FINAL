# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:55:35 2019

@author: 12613
"""
def trans(n,m,trans):
    from_fee=[]
    to_fee=[]
    for i in range(m):
        if trans[i][0]==1:
            from_fee.append(trans[i][2])
        if trans[i][1]==n:
            to_fee.append(trans[i][2])
            n=trans[i][0]
def main():
    n,m=input().split()
    a = []
    for i in range(int(n)):
        a.append(list(map(int, input().rstrip().split())))
    trans(int(n),int(m),a)

main()