# -*- coding: utf-8 -*-
"""
Spyder Editor

Implementation of Insertion sort in python

"""

def insertionsort(a):
    
    for i in range(1,len(a)):
        key = a[i]
        j=i-1
    
        while(j>=0 and a[j]>key):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
        
# test insertion sort

a = [6,5,3,1,8,7,2,4]
insertionsort(a)

print(a)        

        

