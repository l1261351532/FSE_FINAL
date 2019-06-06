# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 23:56:13 2019

@author: 12613
"""
import numpy as np
def judge_side(col,key):
    slide=0;
    for i in range(len(col)):
        if slide==key:
            return 1
        elif slide<key:
            slide+=col[i]
        elif slide>key:
            return 0
    return 0
def through_wall(matrix):
    total=np.sum(matrix[0])
    count=np.zeros(total,dtype=int)
    row=len(matrix)
    for i in range(1,total):
        for j in range(row):
            count[i]+=judge_side(matrix[j],i)
    ans=row-max(count)
    print(ans)
through_wall([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]])
    