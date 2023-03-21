#!/usr/bin/python3
# making pascal triangle
"""Pascal's triangle"""

def pascal_triangle(n):
    """ pascal function """
    list = [1]
    if n <= 0:
        return []
    else:

    	for i in range (n)
	    print(list)
	    oglist = []
	    oglist.append(list[0])
	    for i in range(len(list)-1):
	        oglist.append(list[i]+list[i+1])
	        oglist.append(list[-1])
	    list = oglist
    return list
