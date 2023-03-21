#!/usr/bin/python3
import math
"""
Pascal's triangle
"""

list = [1]
def pascal_triangle(n):
    for i in range (n)
	print(list)
	oglist = []
	oglist.append(list[0])
	for i in range(len(list)-1):
	    oglist.append(list[i]+list[i+1])
	oglist.append(list[-1])
	list = oglist
	return list
