# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:27:59 2019

@author: 12613
"""
def count_sum(n,num_ary):
    count=0
    temp1=[]
    temp2=[]
    for i in range(n):
        for j in range(n):
            temp1.append(int(num_ary[i][0])+int(num_ary[j][1]))
    for i in range(n):
        for j in range(n):
            temp2.append(int(num_ary[i][2])+int(num_ary[j][3]))
    for i in range(n*n):
        for j in range(n*n):
            if temp1[i]==-1*temp2[j]:
                count+=1
    print(count)

def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))
    count_sum(n,a)
    
main()
    
