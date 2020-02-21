# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 23:56:28 2020

@author: wany105
"""

"""The script contains basic function shared by all scripts in the same folder
"""
import numpy as np

def dist(node1, node2):
    """Calculate the distance between two vertices
    """
    return np.sqrt(np.sum((node1 - node2)**2))

def sortget(A, Num, flag = 0):
    """Get the first Num minimum/maximum element in A (list)
    Firstly Sort the A; Take the first Num element and search their index
    Input: the list A, the number of Num, flag indicate whether the maximum or minimum
    """
    B = sorted(A, reverse = flag)  
    Index = []
    for b in B:
        Index.append(A.index(b))
        if(len(Index) == Num):
            break
    
    return Index
    