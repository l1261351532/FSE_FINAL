# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 19:11:55 2019

@author: 12613
"""

def numplus(num1,num2):
    a=num1[::-1]
    b=num2[::-1]
    ans=[]
    j=0
    flag=0
    if len(a)>len(b):
        for i in range(len(a)-len(b)):
            b=b+'0'
    if len(b)>len(a):
        for i in range(len(b)-len(a)):
            a=a+'0'
    for i in range(max(len(a),len(b))):
        if int(a[i])+int(b[i])+flag>=10:
            ans.insert(j,str(int(a[i])+int(b[i])+flag-10))
            flag=1
        else:
            ans.insert(j,str(int(a[i])+int(b[i])+flag))
            flag=0
    if flag==1:
        ans.insert(0,'1')
    answer="".join(ans)
    print(answer)
numplus('112233445566778899','998877665544332211')