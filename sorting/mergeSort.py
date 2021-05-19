#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 22:48:22 2021

@author: auropritbhanjadeo
"""

"""Below merge function loops through left and right size array and sorts the
 elements and copies it to original array index. The last two while loops checks the boundary condition where
 leftover elements are copied to original array"""
 
 
def merge(reca,left,right):
    i=0
    j=0
    k=0
    
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            reca[k] = left[i]
            i+=1
        else:
            reca[k]=right[j]
            j+=1
        k+=1
    

    while i < len(left) :
        reca[k]=left[i]
        k+=1
        i+=1
        
    while j < len(right) :
        reca[k]=right[j]
        k+=1
        j+=1
        
"""Call the mergeSort function recursively to split the array into least possible size and then run backwards to merge
them. Divide and Conquer"""  
    




def mergeSort(reca):
    if len(reca)>1:
        mid = len(reca)//2
        left = reca[:mid]
        right = reca[mid:]
        mergeSort(left)
        mergeSort(right)
        merge(reca,left,right)

        
a = [1,4,7,2,3,5,6,8]
mergeSort(a)
print(a)

