# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:03:44 2019

@author: 12613
"""
def sortchar(a,test_str):
    for i in range(len(test_str)):
        test_str[i]=test_str[i].replace(a,'')
    test_str.sort()
    test_str.reverse()
    for word in test_str:
        print(word)


def main():
    test_ary=[]
    flag=input()
    k=0
    test_ary.append(input())
    while test_ary[k]!='@':
        k+=1
        test_ary.append(input())
    test_ary.pop()
    sortchar(flag,test_ary)

main()

    