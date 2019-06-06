# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:33:16 2019

@author: 12613
"""
def str_count(test_str):
    test_str+='@'
    ans=[]
    k=0
    i=0
    while i<len(test_str):
        num=1
        for j in range(i+1,len(test_str)):
            if test_str[i]==test_str[j]:
                num+=1
            else:
                if num>1:
                    ans+=test_str[i]
                    ans+=str(num)
                    k+=1
                    i=j-1
                else:
                    ans+=test_str[i]
                    k+=1
                    i=j-1
                break
        i+=1
    ans="".join(ans)
    print(ans)
str_count('AABBBBC')