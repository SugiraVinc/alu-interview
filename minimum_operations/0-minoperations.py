#!/usr/bin/python3
"""
Minimum ops qn interview
"""


from sys import argv


def minOperations(n):
    """
    Calculates the minimum number of operations  to form one 'H' to n 'H's
    if the only available operations are "Copy All" and "Paste"
    """

    # If n is 1 or less, no ops needed
    if n <= 1:
        return 0

    # minimum number of ops
    for i in range(2, int((n/2)+1)):
        if n % i == 0:
            return minOperations(int(n / i)) + i

    return 
