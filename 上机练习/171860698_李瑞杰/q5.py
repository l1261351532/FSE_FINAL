# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 00:21:29 2019

@author: 12613
"""    
import numpy as np
def find_road(sub_map):
    row = len(sub_map)
    col = len(sub_map[0])
    print(sub_map)
    begin_point=[0,0]
    end_point=[0,0]
    neighbor = np.zeros((row*col,col*row))
    for i in range(row):
        for j in range(col):
            if sub_map[i][j]==0:
                if i-1>=0:
                    neighbor[][]
                
find_road([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
