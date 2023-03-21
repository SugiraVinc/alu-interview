#!/usr/bin/python3
# making pascal triangle
'''Pascal's triangle'''


def pascal_triangle(n):
    """ pascal function """
    list = []
    if n <= 0:
        return []
    else:
        for i in range(1, n+1):
            x = 1
            oglist = []
            for j in range(1, i+1):
                oglist.append(x)
                x = x * (i - j) // j
            list.append(oglist)
    return list
if __name__ == "__main__":
    print(pascal_triangle(5))
