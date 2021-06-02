#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 20:13:54 2021

@author: auropritbhanjadeo
"""


def bubbleSort(a):
    
    while True:
        
        swapped=False
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                swapped = True
                
        if swapped == False:
            break
                
            



a = [6,5,3,1,8,7,2,4]
bubbleSort(a)

print(a)